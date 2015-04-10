import os, json, config
from flask import jsonify

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

def CreateJSON(imagename):
    pre_zip_path = os.path.join(config.APP_ROOT_DIR, "pre_zip_folders/", imagename, "AppIcon.appiconset/")
    os.makedirs(pre_zip_path)
    device_json = createiPhoneJSON()
    device_json.extend(createiPadJSON())
    device_json.extend(createCarPlayJSON())
    device_json.extend(createAppleWatchJSON())
    total_json = {"images":device_json, "info": { "version" : 1, "author" : "xcode" } }
    with open(pre_zip_path + '/Contents.json', 'w+') as jsondump:
        jsondump.write(json.dumps(total_json, indent=2))


def createiPhoneJSON():
    json_list = [{ "size" : "29x29", "idiom" : "iphone", "filename" : "iphone_58.png", "scale" : "2x" },
                 { "size" : "29x29", "idiom" : "iphone", "filename" : "iphone_87.png", "scale" : "3x" },
                 { "size" : "40x40", "idiom" : "iphone", "filename" : "iphone_80.png", "scale" : "2x" },
                 { "size" : "40x40", "idiom" : "iphone", "filename" : "iphone_120.png", "scale" : "3x" },
                 { "size" : "60x60", "idiom" : "iphone", "filename" : "iphone_120.png", "scale" : "2x" },
                 { "size" : "60x60", "idiom" : "iphone", "filename" : "iphone_180.png", "scale" : "3x" }]
    return json_list
    

def createiPadJSON():
    json_list = [{ "size" : "29x29", "idiom" : "ipad", "filename" : "ipad_29.png", "scale" : "1x" },
                 { "size" : "29x29", "idiom" : "ipad", "filename" : "ipad_58.png", "scale" : "2x" },
                 { "size" : "40x40", "idiom" : "ipad", "filename" : "ipad_40.png", "scale" : "1x" },
                 { "size" : "40x40", "idiom" : "ipad", "filename" : "ipad_80.png", "scale" : "2x" },
                 { "size" : "76x76", "idiom" : "ipad", "filename" : "ipad_76.png", "scale" : "1x" },
                 { "size" : "76x76", "idiom" : "ipad", "filename" : "ipad_152.png", "scale" : "2x" }]
    return json_list

def createCarPlayJSON():
    json_list = [{ "size" : "120x120", "idiom" : "car", "filename" : "carplay_120.png", "scale" : "1x" }]
    return json_list

def createAppleWatchJSON():
    json_list = [{ "size" : "24x24", "idiom" : "watch", "scale" : "2x", "filename" : "applewatch_48.png", "role" : "notificationCenter", "subtype" : "38mm" },
                 { "size" : "27.5x27.5", "idiom" : "watch", "scale" : "2x", "filename" : "applewatch_55.png", "role" : "notificationCenter", "subtype" : "42mm" },
                 { "size" : "29x29", "idiom" : "watch", "filename" : "applewatch_58.png", "role" : "companionSettings", "scale" : "2x" },
                 { "size" : "29x29", "idiom" : "watch", "filename" : "applewatch_87.png", "role" : "companionSettings", "scale" : "3x" },
                 { "size" : "40x40", "idiom" : "watch", "scale" : "2x", "filename" : "applewatch_80.png", "role" : "appLauncher", "subtype" : "38mm" },
                 { "size" : "44x44", "idiom" : "watch", "scale" : "2x", "filename" : "applewatch_88.png", "role" : "longLook", "subtype" : "42mm" },
                 { "size" : "86x86", "idiom" : "watch", "scale" : "2x", "filename" : "applewatch_172.png", "role" : "quickLook", "subtype" : "38mm" },
                 { "size" : "98x98", "idiom" : "watch", "scale" : "2x", "filename" : "applewatch_196.png", "role" : "quickLook", "subtype" : "42mm" }]
    return json_list
