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
        tempImg = PIL.Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        width, height = tempImg.size
        if width != 1024 or  height != 1024:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('invalid_size.html', height=height, width=width)
        tempImg.close()
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
        return redirect(url_for('completed', filename=filenameNoExt))
    else:
        return render_template('invalid_extension.html', extension=file.filename.rsplit('.', 1)[1])

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

@app.route('/completed/<filename>')
def completed(filename):
    print filename
    if os.path.isfile('completed_zips/' + filename + '.zip'):
        return render_template('download.html', filename=filename)
    else:
        return render_template('notavailable.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('completed_zips/', filename)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')