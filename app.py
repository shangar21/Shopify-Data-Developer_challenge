from flask import Flask, render_template,  request, g, current_app, flash, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.getcwd() + '/media/'

@app.route('/')
def index():
    names = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', path=app.config['UPLOAD_FOLDER'], names=names)

@app.route('/upload_images', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        files = request.files.getlist("files[]")
        if files:
            for f in files:
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            
    return render_template('upload.html')

@app.route('/delete_images', methods=['GET', 'POST'])
def delete():
    names = os.listdir(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        files = request.form.to_dict()
        if 'delete_all_imgs' in files:
            names = os.listdir(app.config['UPLOAD_FOLDER'])
            for n in names:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], n))
            return render_template('delete.html', names=[])
        if files:
            for f in files:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))
            return render_template('delete.html', names=os.listdir(app.config['UPLOAD_FOLDER']))
            
    return render_template('delete.html', names=names)

@app.route('/media/<filename>')
def media(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/search_images')
def search():
    res = request.args.get('query').lower()

    names = [i for i in os.listdir(app.config['UPLOAD_FOLDER']) if res in i.lower()]

    return render_template('index.html', path=app.config['UPLOAD_FOLDER'], names=names)

if __name__ == "__main__":
    app.secret_key = 'VyC74LX3hb'
    app.run(debug=True)