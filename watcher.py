from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
import constants

import pathlib
from glob import glob

import cv2
import json
import os

PATH_TO_WATCH_FOLDER =  "E:/HT"

def handle_data():
    try:

        for fn in glob(PATH_TO_WATCH_FOLDER + '/*.csv'):
            print (fn)

    except Exception as inst:
        print ("error:", inst)
        

        #upload_to_dropbox

class Watcher:
    DIRECTORY_TO_WATCH = PATH_TO_WATCH_FOLDER

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        handle_data()


if __name__ == '__main__':


     w = Watcher()
     w.run()



	

	   


