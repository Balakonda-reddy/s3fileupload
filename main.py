from flask import Flask, render_template, request
import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename
# import key_config as keys

s3 = boto3.client('s3')

BUCKET_NAME='s3-access-1391'

@app.route('/')  
def home():
    return render_template("index.html")
@app.route('/home')
def home1():
    return render_template("index.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
            filename = secure_filename(img.filename)
            img.save(filename)
            s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                # msg = "Upload Done ! "
            return render_template("/goback.html",msg="Uploaded Successfully...!")
             
            # return redirect(url_for('home'))  
            # msg = "Upload Done ! " 
            
            

    return render_template("index.html")




if __name__ == "__main__":
    
    app.run(debug=True,port=333,host='0.0.0.0')