# Issues
Here is where you can figure out issues

# 1. Pip Installation
## Packages
### PyWin32
As one of the python packages is PyWin32 is used. People on MacOS or Linux are unable to install it as it provides access to Windows API which MacOS and Linux dont have.
If you go into the requirement.txt and remove the pywin32 installation line, you will be able to install all packages and run the server with no problems.

## 2. OS Problems
### externally-managed-environment
If you are running Linux and are running into the externally-managed-environment error when trying to install the pip packages. All you need to do is at the end of the command, add the
```
--break-system-packages
```
flag and all should go well.