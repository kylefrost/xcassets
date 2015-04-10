from __future__ import print_function
import os, time, shutil, zipfile, sys
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from icon_resize import Resize
from icon_json import CreateJSON
from PIL import Image

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ['png']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
    except:
        print("Unexpected error:", sys.exc_info()[0], file=sys.stderr)
        raise
    if file and allowed_file(file.filename):
        try:
            filename = addTimeSuffix(secure_filename(file.filename))
            filenameNoExt = filename.rsplit('.', 1)[0]
            file.save(os.path.join(app.root_path, 'uploaded_images/', filename))
            print(os.path.join(app.root_path, "uploaded_images/", filename))
            return redirect(url_for('completed', filename=filenameNoExt))
        except:
            print("Unexpected error:", sys.exc_info()[0], file=sys.std.err)
            raise
    else:
        return render_template('invalid_extension.html', extension=file.filename.rsplit('.', 1)[1])

def addTimeSuffix(filename):
    nameList = filename.rsplit('.', 1)
    suffix = "_" + time.strftime('%Y%m%d%H%M%S')
    return nameList[0] + suffix + "." + nameList[1]

def makeArchive(fileList, archive, root):
    a = zipfile.ZipFile('completed_zips/' + archive, 'w', zipfile.ZIP_DEFLATED)

    for f in fileList:
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
            fileList.extend(dirEntries(dirfile, subdir, *args))
    return fileList

@app.route('/completed/<filename>')
def completed(filename):
    try:
        try:
            try:
                tempImg = Image.open(os.path.join(app.root_path, 'uploaded_images/', filename + '.png'))
            except:
                print("Could not: ", "Open file: " + os.path.join(app.root_path, 'uploaded_images/', filename + '.png') + " as tempImg.", file=sys.stderr)
            width, height = tempImg.size
            if width != 1024 or  height != 1024:
                os.remove(os.path.join(app.root_path, 'uploaded_images/', filename + ".png"))
                tempImg.close()
                return render_template('invalid_size.html', height=height, width=width)
        except:
            print("Could not check size of image, ", "I guess.", file=sys.stderr)
        try:
            Resize(filename + ".png")
        except:
            print("Could not: ", "Resize image with name: " + filename, file=sys.stderr)
        try:
            CreateJSON(filename)
        except:
            print("Could not: ", "Create JSON for file: " + filename, file=sys.stderr)
        try:
            to_dir = app.root_path + 'pre_zip_folders/' + filenameNoExt + '/AppIcon.appiconset/'
            from_dir = app.root_path + 'resized_image_folders/' + filenameNoExt + '/'
            source = os.listdir(from_dir)
            for img in source:
                img = from_dir + img
                shutil.copy(img, to_dir)
        except:
            print("Could not: ", "Move images to pre_zip.", file=sys.stderr)
        try:
            makeArchive(dirEntries(app.root_path + 'pre_zip_folders/' + filenameNoExt + '/', True), filenameNoExt + '.zip', 'pre_zip_folders/')
        except:
            print("Could not: ", "Make archive of images.", file=sys.stderr)
        try:
            shutil.rmtree(app.root_path + 'pre_zip_folders/' + filenameNoExt)
            shutil.rmtree(app.root_path + 'resized_image_folders/' + filenameNoExt)
            os.remove(app.root_path + 'uploaded_images/' + filename)
        except:
            print("Could not: ", "Cleanup image folders.", file=sys.stderr)
    except:
        print("Creating archive didn't work, ", "and I don't know why.", file=sys.stderr)
    if os.path.isfile('completed_zips/' + filename + '.zip'):
        return render_template('download.html', filename=filename)
    else:
        return render_template('notavailable.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    try:
        return send_from_directory('completed_zips/', filename)
    except:
        print("Could not: ", "Get URL for completed ZIP.", file=sys.stderr)
        return render_template('notavailable.html', filename=filename)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
    app.port = 80
