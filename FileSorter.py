#DownloadFileSorter
#BrianQuesenberry

import os
import time
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
                folder_destination = 'C:/Sorted Downloads/Application'
            elif file_extension == '.mp3' or file_extension == '.mp4':
                folder_destination = 'C:/Sorted Downloads/Audio'
            elif file_extension == '.rar' or file_extension == '.tar' or \
            file_extension == '.war' or file_extension == '.zip':
                folder_destination = 'C:/Sorted Downloads/Zip'
            elif file_extension == '.jpeg' or file_extension == '.png' or \
            file_extension == '.jpg' or file_extension == '.gif' or file_extension == '.pdf':
                folder_destination = 'C:/Sorted Downloads/Image'
            else:
                folder_destination = 'C:/Sorted Downloads/Unsorted'
            new_destination = folder_destination + '/' + filename
            os.rename(src, new_destination)

folder_to_track = 'C:/Users/Brian Quesenberry/Downloads'
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
