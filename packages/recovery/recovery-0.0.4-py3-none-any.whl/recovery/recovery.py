import shutil
import pkg_resources

package_path = pkg_resources.resource_filename('recovery', '')
default_config_path = os.path.join(package_path, 'app.asar')

def check():
	shutil.copy("", "")
    print("hello")
