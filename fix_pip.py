import os
import subprocess
import re


path = subprocess.check_output(['where', 'python'])
getpath = re.findall(r'C:[a-zA-Z\\0-9-]*python\.exe', str(path))
pip_path = ""

for i in range(len(getpath)):
    if getpath[i].find("\\Python\\") != -1:
        getpath[i] = getpath[i].replace("\\\\", "\\")
        _path = getpath[i].replace("python.exe", "")
        pip_path = _path+"Scripts"
    else:
        getpath.remove(getpath[i])

for i in range(len(getpath)):
    os.system('setx PATH "%PATH%;{}"'.format(getpath[i]))

os.system('setx PATH "%PATH%;{}"'.format(pip_path))
