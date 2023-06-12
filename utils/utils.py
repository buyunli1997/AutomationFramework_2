#Constants
import inspect


def whoami():
    return inspect.stack()[1][3]


URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = 'admin'
PASSWORD = 'admin123'
