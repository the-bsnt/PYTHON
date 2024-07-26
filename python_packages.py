# 1 Alternative 1 basic
import Python_Package.my_module

Python_Package.my_module.Pac()


# 2 Alternative 2 [use of from statement] [importing individual function]
from Python_Package.my_module import Pac

Pac()
# Hello()

# 3 Alternative 3 [importing whole file]
from Python_Package import my_module

my_module.Hello()
my_module.Pac()
