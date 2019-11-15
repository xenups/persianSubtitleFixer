import os


class SRTHandler:
    def __init__(self, path):
        self.path = path
        self.files = []

    def search_srt_files(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".srt"):
                    self.files.append(os.path.join(root, file))
        return self.files
