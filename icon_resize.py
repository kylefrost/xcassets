import os, time
from PIL import Image

# Set Constants for icon sizes

# iPhone
kiPhoneSettingsIcon2x = 58
kiPhoneSettingsIcon3x = 87
kiPhoneSpotlightIcon2x = 80
kiPhoneSpotlightIcon3x = 120
kiPhoneAppIcon2x = 120
kiPhoneAppIcon3x = 180

# iPad
kiPadSettingsIcon1x = 29
kiPadSettingsIcon2x = 58
kiPadSpotlightIcon1x = 40
kiPadSpotlightIcon2x = 80
kiPadAppIcon1x = 76
kiPadAppIcon2x = 152

# CarPlay
kCarPlayIcon1x = 120

# Apple Watch
kAppleWatchNotificationCenterIcon38mm = 48
kAppleWatchNotificationCenterIcon48mm = 55
kAppleWatchCompanionSettingsIcon2x = 58
kAppleWatchCompanionSettingsIcon3x = 87
kAppleWatchHomeScreenIcon2x = 80
kAppleWatchLongLookIcon42mm = 88
kAppleWatchShortLookIcon38mm = 172
kAppleWatchShortLookIcon42mm = 196

resized_images_path = ""

def Resize(imagename):
    imagename = imagename.rsplit('.', 1)[0]
    resized_images_path = "resized_image_folders/" + imagename
    os.makedirs(resized_images_path)
    createiPhoneIcons(imagename, resized_images_path)
    createiPadIcons(imagename, resized_images_path)
    createCarPlayIcons(imagename, resized_images_path)
    createAppleWatchIcons(imagename, resized_images_path)

def createiPhoneIcons(name, path):
    sizes = [kiPhoneSettingsIcon2x, 
             kiPhoneSettingsIcon3x,
             kiPhoneSpotlightIcon2x,
             kiPhoneSpotlightIcon3x,
             kiPhoneAppIcon2x,
             kiPhoneAppIcon3x]
    img = Image.open("uploaded_images/" + name + ".png")
    for size in sizes:
        sizeTuple = (size, size)
        img = img.resize(sizeTuple, Image.BILINEAR)
        saveName = addSizeSuffix("iphone", size)
        img.save(path + "/" + saveName + ".png", "PNG")
    img.close()

  
def createiPadIcons(name, path):
    sizes = [kiPadSettingsIcon1x,
             kiPadSettingsIcon2x,
             kiPadSpotlightIcon1x,
             kiPadSpotlightIcon2x,
             kiPadAppIcon1x,
             kiPadAppIcon2x]
    img = Image.open("uploaded_images/" + name + ".png")
    for size in sizes:
        sizeTuple = (size, size)
        img = img.resize(sizeTuple, Image.BILINEAR)
        saveName = addSizeSuffix("ipad", size)
        img.save(path + "/" + saveName + ".png", "PNG")
    img.close()

def createCarPlayIcons(name, path):
    sizes = [kCarPlayIcon1x]
    img = Image.open("uploaded_images/" + name + ".png")
    for size in sizes:
        sizeTuple = (size, size)
        img = img.resize(sizeTuple, Image.BILINEAR)
        saveName = addSizeSuffix("carplay", size)
        img.save(path + "/" + saveName + ".png", "PNG")
    img.close()
  
def createAppleWatchIcons(name, path):
    sizes = [kAppleWatchNotificationCenterIcon38mm,
             kAppleWatchNotificationCenterIcon48mm,
             kAppleWatchCompanionSettingsIcon2x,
             kAppleWatchCompanionSettingsIcon3x,
             kAppleWatchHomeScreenIcon2x,
             kAppleWatchLongLookIcon42mm,
             kAppleWatchShortLookIcon38mm,
             kAppleWatchShortLookIcon42mm]
    img = Image.open("uploaded_images/" + name + ".png")
    for size in sizes:
        sizeTuple = (size, size)
        img = img.resize(sizeTuple, Image.BILINEAR)
        saveName = addSizeSuffix("applewatch", size)
        img.save(path + "/" + saveName + ".png", "PNG")
    img.close()

def addSizeSuffix(filename, size):
    suffix = "_" + str(size)
    return filename + suffix
