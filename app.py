from flask import Flask, render_template, Response, request, g, current_app, flash, redirect, url_for, send_from_directory, flash
import urllib.request
import os
from werkzeug.utils import secure_filename
from models import Image
from db import save_from_url, db_init, db
from sqlalchemy.dialects.sqlite import insert

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.getcwd() + '/media/'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db_init(app)

IMAGE_TYPES = {".png", ".jpeg", ".jpg", ".tiff", ".tif", ".gif", ".bmp", ".ico"}



@app.route('/')
def index():
    images = Image.query.all()
    return render_template('index.html', images=images)

@app.route('/upload_images', methods=['GET', 'POST'])
def upload():
    global IMAGE_TYPES
    if request.method == 'POST':
        files = request.files.getlist("files[]")
        urls = request.form.to_dict()
        if urls:
            images = Image.query.all()
            filename = urls['img_title']+urls['extension']
            mimetype = urls['extension']
            req = urllib.request.Request(urls['img_url'], headers={'User-Agent': 'Mozilla/5.0'})
            img = Image(img=urllib.request.urlopen(req).read(), mimetype=mimetype, name=filename)
            db.session.add(img)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                flash("{} already has been uploaded".format(filename))           

        for f in files:
            images = Image.query.all()
            filename = secure_filename(f.filename)
            mimetype = f.mimetype
            img = Image(img=f.read(), mimetype=mimetype, name=filename)
            db.session.add(img)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                flash("{} already has been uploaded".format(filename))
            
    return render_template('upload.html', extensions=IMAGE_TYPES, images=Image.query.all())

@app.route('/delete_images', methods=['GET', 'POST'])
def delete():
    images = Image.query.all()
    if request.method == "POST":
        files = request.form.to_dict()
        if 'delete_all_imgs' in files:
            for i in images:
                image = Image.query.filter_by(id=i.id).first()
                db.session.delete(image)
                db.session.commit()
            images = Image.query.all()
            return render_template('delete.html', images=images)
        for i in files:
            image = Image.query.filter_by(id=int(i)).first()
            db.session.delete(image)
            db.session.commit()
        images = Image.query.all()
        return render_template('delete.html', images=images)
    return render_template('delete.html', images=images)

@app.route('/search_images', methods=["GET", "POST"])
def serach():
    query = request.args.get('query').lower()
    images = [i for i in Image.query.all() if query in i.name.lower()]
    return render_template('index.html', images=images)


@app.route('/media/<int:id>')
def media(id):
    image = Image.query.filter_by(id=id).first()
    if image:
        return Response(image.img, mimetype=image.mimetype)


if __name__ == "__main__":
    app.secret_key = 'VyC74LX3hb'
    app.run()