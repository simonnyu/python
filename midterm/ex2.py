#!usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import (LoggingEventHandler, FileSystemEventHandler)

class TestEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print("event noticed: " + event.event_type +
                     " on file " + event.src_path + " at " + time.asctime())

    def __init__(self, pattern='*'):
        self.pattern = pattern

    def on_moved(self, event):
        print ("moved src path:"+ event.src_path)
        print ("moved dest path:"+ event.dest_path)

    def on_created(self, event):
        print ("created path:"+ event.src_path)

    def on_deleted(self, event):
        print ("deleted path:"+ event.src_path)

    def should_reload(self, event):
        if isinstance(event, FileSystemMovedEvent):
            return True
        return False

    def on_modified(self, event):
        print ("modified path:"+ event.src_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    #event_handler = LoggingEventHandler()
    event_handler = TestEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

