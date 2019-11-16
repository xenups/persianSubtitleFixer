import os
import threading
import codecs
from named_constants import Constants


class Encoding(Constants):
    utf8 = 'utf-8'
    windows1250 = 'windows-1250'
    windows1252 = 'windows-1252'
    windows1256 = 'windows-1256'


class SubtitleConvertor(threading.Thread):
    def __init__(self, cb, list_file_address):
        threading.Thread.__init__(self)
        self.files_path = list_file_address
        self.callback = cb

    def get_file_encoding(self, path):
        print(path)
        encodings = [Encoding.windows1250, Encoding.windows1252, Encoding.windows1256]
        for e in encodings:
            try:
                fh = codecs.open(path, 'r', encoding=e)
                fh.readlines()
                fh.seek(0)
            except UnicodeDecodeError:
                pass
            else:
                return e

    def convert_format(self, path, source_encoding):
        self.callback('Trying to convert from ' + source_encoding)
        with codecs.open(path, 'r', encoding=source_encoding, errors='ignore') as file:
            lines = file.read()
            # print(lines)
        # write output file
        converted_name = os.path.splitext(path)[0] + ' converted.srt'
        with codecs.open(converted_name, 'w', encoding='utf-8') as file:
            file.write(lines)
        self.callback(path + ' converted')

    def run(self):
        for path in self.files_path:
            source_format = self.get_file_encoding(path)
            if source_format != "utf-8":
                self.convert_format(path, source_format)
