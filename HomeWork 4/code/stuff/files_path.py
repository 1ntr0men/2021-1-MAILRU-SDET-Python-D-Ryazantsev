import os


def files_path(file_name):
    return os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), file_name)


def directory_path():
    return os.path.abspath(os.path.join(__file__, os.pardir))
