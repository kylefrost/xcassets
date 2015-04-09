import os, time, PIL, shutil, zipfile
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
        filenameNoExt = filename.rsplit('.', 1)[0]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        Resize(filename)
        CreateJSON(filename)
        to_dir = 'pre_zip_folders/' + filenameNoExt + '/AppIcon.appiconset/'
        from_dir = 'resized_image_folders/' + filenameNoExt + '/'
        source = os.listdir(from_dir)
        for img in source:
            img = from_dir + img
            shutil.copy(img, to_dir)
        makeArchive(dirEntries('pre_zip_folders/' + filenameNoExt + '/', True), filenameNoExt + '.zip', 'pre_zip_folders/')
        shutil.rmtree('pre_zip_folders/' + filenameNoExt)
        shutil.rmtree('resized_image_folders/' + filenameNoExt)
        os.remove('uploaded_images/' + filename)
        return render_template('uploaded.html', filename=filename)
    else:
        return render_template('invalid_extension.html')

def addTimeSuffix(filename):
    nameList = filename.rsplit('.', 1)
    suffix = "_" + time.strftime('%Y%m%d%H%M%S')
    return nameList[0] + suffix + "." + nameList[1]

def makeArchive(fileList, archive, root):
    a = zipfile.ZipFile('completed_zips/' + archive, 'w', zipfile.ZIP_DEFLATED)

    for f in fileList:
        print "archiving file %s" % (f)
        a.write(f, os.path.relpath(f, root))
    a.close()


def dirEntries(dir_name, subdir, *args):
    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if not args:
                fileList.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    fileList.append(dirfile)
            # recursively access file names in subdirectories
        elif os.path.isdir(dirfile) and subdir:
            print "Accessing directory:", dirfile
            fileList.extend(dirEntries(dirfile, subdir, *args))
    return fileList

@app.route('/download/<filename>')
def download():
    return

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
