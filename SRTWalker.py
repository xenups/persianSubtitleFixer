import os
import logging
import threading


class SubFinderThread(threading.Thread):
    def __init__(self, cb, path):
        threading.Thread.__init__(self)
        self.callback = cb
        self.path = path

    def run(self):
        files_list = []
        logging.info("Thread %s: starting", 'started')
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".srt"):
                    files_list.append(os.path.join(root, file))
                    self.callback(os.path.join(root, file))
