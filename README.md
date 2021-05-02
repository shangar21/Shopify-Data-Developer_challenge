# Shopify Data Developer Challenge

## Installing Requirements
To run this you will need python 3.8 along with pip. 
To install requirements run:
```bash
pip3 install -r requirements.txt
```
If the above does not work, with a default python install the only extra packages needed are flask, flask_sqlalchemy, and werkzeug with the following:

```bash
pip3 install flask
pip3 install flask_sqlalchemy
pip3 instal werkzeug
```


## Running the Program
in terminal change directories into the Shopify-Data-Developer-Challenge directory and enter:
```bash
python3 app.py
```
After running a dialogue will come up underneath as such:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
use the link that follows the "Running on" part at the end of the dialogue and app will run on browser. 

## Using the app
The homepage will have a few dummy photos to begin with (images left after testing the delete all function (after uploading numerous images), URL upload, multiple local file upload, delete multiple). All photos that are added will be seen on this homepage. The top navbar contains 3 options, upload, delete and search. 

### Upload

Clicking browse lets you pick multiple files from your PC, once all have been selected and uploaded, cliking the upload button uploads the images to the database. 

The next option is to add via URL. This option also requires the user to set a name for the file as well as the extension the file will use (this was placed since many images online have random numbers as the name which makes it hard to identify). This only takes one URL at a time. Clicking upload, uploads the images to the database.

### Delete

There are checkboxes to select multiple images at once, or if one wants to delete all images that is also an option present at the very bottom on a button labelled "Delete All". 

### Search 

This is a substring search. One can search via substring of the name of the image (For example, if an image is labelled dog_1.jpg, searching 'dog' will return that image). One can also search via extension and the query will return all images with said file extension. 

## How it works and what it uses

This app uses Flask back end and a simple HTML front end. The database used is an sqlite database with the SQLAlchemy library from flask. 

## What features can be added in the future

I can add a select all option so that if someone wants to delete many images without deleting all they can select all and deselect the ones they want to keep. I can add images from multiple URLs instead of one at a time. I can add search from similar image.
