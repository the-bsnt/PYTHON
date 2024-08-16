from pathlib import Path

path1 = Path("Python_Package")
# ^here, path1 is object of class Path imported from pathlib.py module
print(path1.exists())
path2 = Path("email")
path2.mkdir()
print(path2.exists())

ans = input("Do you want to delete email directory? y/n")
if ans == "y":
    path2.rmdir()
print(path2.exists())

# *path.glob() module
print(path1.glob("*"))
for file in path1.glob("*.*"):
    print(file)
