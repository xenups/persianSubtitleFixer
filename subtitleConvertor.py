import os
import threading
from pathlib import Path
import codecs


class SubtitleConvertor(threading.Thread):
    def __init__(self, cb, list_file_address):
        threading.Thread.__init__(self)
        self.files_path = list_file_address
        self.callback = cb

    def get_file_encoding(self, path):
        print(path)
        encodings = ['utf-8', 'windows-1250', 'windows-1252']
        for e in encodings:
            try:
                fh = codecs.open(path, 'r', encoding=e)
                fh.readlines()
                fh.seek(0)
            except UnicodeDecodeError:
                pass
            else:
                return e

    def ansi_to_utf8(self, path):
        with codecs.open(path, 'r', encoding='windows-1256', errors='ignore') as file:
            lines = file.read()
            # print(lines)
        # write output file
        converted_name = os.path.splitext(path)[0] + ' converted.srt'
        with codecs.open(converted_name, 'w', encoding='utf-8') as file:
            file.write(lines)

    def run(self):
        sourceFormats = ['ascii', 'iso-8859-1']
        for path in self.files_path:
            if self.get_file_encoding(path) != 'utf-8':
                self.ansi_to_utf8( path)
                self.callback(path + ' converted')
        else:
            self.callback(path + ' not converted')
