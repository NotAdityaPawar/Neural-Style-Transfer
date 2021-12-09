from flask import *
from flask import render_template
import os


app = Flask(__name__)


UPLOAD_FOLDER = "./static/images/uploaded"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/')
def index():
    return render_template("home.html")

@app.route('/uploader',methods = ["GET","POST"])
def uploader():
    if request.method=="POST":
        f = request.files['file']
        f.save(f.filename)

    return render_template("success.html")

if __name__=="__main__":
    app.run()


