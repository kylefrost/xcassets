import os, time, PIL, shutil
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from icon_resize import Resize
from icon_json import CreateJSON

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploaded_images/'
app.config['ALLOWED_EXTENSIONS'] = set(['png'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = addTimeSuffix(secure_filename(file.filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        Resize(filename)
        CreateJSON(filename)
        #shutil.move('resized_image_folders/' + filename.rsplit('.', 1)[0] + '/', 'pre_zip_folders/' + 'AppIcon.appiconset/' + filename.rsplit('.', 1)[0])
        return render_template('uploaded.html', filename=filename)
    else:
        return render_template('invalid_extension.html')

def addTimeSuffix(filename):
    nameList = filename.rsplit('.', 1)
    suffix = "_" + time.strftime('%Y%m%d%H%M%S')
    return nameList[0] + suffix + "." + nameList[1]

@app.route('/download/<filename>')
def download():
    return

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
