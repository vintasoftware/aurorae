class InvalidFileType(Exception):
    def __str__(self):
        return "The file is not an Excel document"


class InvalidFileSize(Exception):
    def __str__(self):
        return "The file is over 5 MB"


class EmptyFile(Exception):
    def __str__(self):
        return "The file does not have content"
