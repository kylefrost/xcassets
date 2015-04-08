import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploaded_images/'
app.config['ALLOWED_EXTENSIONS'] = set(['png'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('index.html')
    else:
        return render_template('invalid_extension.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
