import os
#enter name for folder that you want to be created

def foldercreate(name):
    
    desktop_path = os.path.expanduser("~/Desktop")
    folder_path = os.path.join(desktop_path, name)
    os.mkdir(folder_path)
