import os
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

def resizeIconImages(imagename):
    resized_images_path = "resized_image_folders/" + imagename
    os.makedirs(resized_images_path)

def createiPhoneIcons(name):
    sizes = [kiPhoneSettingsIcon2x, 
             kiPhoneSettingsIcon3x,
             kiPhoneSpotlightIcon2x,
             kiPhoneSpotlightIcon3x,
             kiPhoneAppIcon2x,
             kiPhoneAppIcon3x]
  
def createiPadIcons(name):
  
def createCarPlayIcons(name):
  
def createAppleWatchIcons(name):
