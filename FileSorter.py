#DownloadFileSorter
#BrianQuesenberry

import os
import time
import easygui
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
#install watchdog

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            file, file_extension = os.path.splitext(filename)
            if file_extension == '.exe':
                folder_destination = fd + '/Application'
            elif file_extension == '.mp3':
                folder_destination = fd + '/Audio'
            elif file_extension == '.mp4' or file_extension == '.avi':
                folder_destination = fd + '/Video'
            elif file_extension == '.rar' or file_extension == '.tar' or \
            file_extension == '.war' or file_extension == '.zip':
                folder_destination = fd + '/Zipped'
            elif file_extension == '.jpeg' or file_extension == '.png' or \
            file_extension == '.jpg' or file_extension == '.gif' or file_extension == '.pdf':
                folder_destination = fd + '/Image'
            else:
                folder_destination = fd + '/Unsorted'
            new_destination = folder_destination + '/' + filename
            os.rename(src, new_destination)

folder_to_track = easygui.enterbox("Enter your desired folder to track: ")
fd = easygui.enterbox("Enter your folder destination: ")

try:
    path = '/Application'
    os.mkdir(fd + path)
except OSError:
    print("Creation of the directory %s failed" %path)
else:
    print("Successfully created the directory %s " %path)
try:
    path = '/Audio'
    os.mkdir(fd + path)
except OSError:
    print("Creation of the directory %s failed" %path)
else:
    print("Successfully created the directory %s " %path)
try:
    path = '/Video'
    os.mkdir(fd + path)
except OSError:
    print("Creation of the directory %s failed" %path)
else:
    print("Successfully created the directory %s " %path)
try:
    path = '/Zipped'
    os.mkdir(fd + path)
except OSError:
    print("Creation of the directory %s failed" %path)
else:
    print("Successfully created the directory %s " %path)
try:
    path = '/Image'
    os.mkdir(fd + path)
except OSError:
    print("Creation of the directory %s failed" %path)
else:
    print("Successfully created the directory %s " %path)
try:
    path = '/Unsorted'
    os.mkdir(fd + path)
except OSError:
    print("Creation of the directory %s failed" %path)
else:
    print("Successfully created the directory %s " %path)


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
