import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileModifiedEvent


class FileWatcher(PatternMatchingEventHandler):
    def __init__(self, patterns=None):
        super(FileWatcher, self).__init__(patterns=patterns)


def on_created(event):
    print(f"created - {event}")


def on_deleted(event):
    print(f"deleted - {event}")


def on_modified(event: FileModifiedEvent):
    print(f"modified - {event}")
    getmtime = os.path.getmtime(event.src_path)
    print(f"getmtime - {getmtime}")


def on_moved(event):
    print(f"moved - {event}")


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    path = r'\\r-storage.rc\song\Плей-листы'
    # path = r'z:/temp'

    event_handler = FileWatcher(patterns=["*.xml"])
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
