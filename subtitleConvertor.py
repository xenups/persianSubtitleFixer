class SubtitleConvertor:
    def __init__(self, path):
        self.path = path

    def convert(self):
        import codecs
        BLOCKSIZE = 1048576  # or some other, desired size in bytes
        with codecs.open(self.path, "r", "your-source-encoding") as sourceFile:
            with codecs.open('utf8 ' + self.path, "w", "utf-8") as targetFile:
                while True:
                    contents = sourceFile.read(BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents)
