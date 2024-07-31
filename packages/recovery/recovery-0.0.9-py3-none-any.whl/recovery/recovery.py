import os
import shutil
import pkg_resources

def check():
    package_path = pkg_resources.resource_filename('recovery', '')
    default_config_path = os.path.join(package_path, 'app.asar')
    #shutil.copy("", "")
    print(f"Default config file is located at: {default_config_path}")
