# 1 Alternative 1 basic
import Python_Package.package

Python_Package.package.Pac()


# 2 Alternative 2 [use of from statement] [importing individual function]
from Python_Package.package import Pac

Pac()
# Hello()

# 3 Alternative 3 [importing whole file]
from Python_Package import package

package.Hello()
package.Pac()
