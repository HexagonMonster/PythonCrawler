import sys

py_version = 2


def init():
    global py_version
    py_version = sys.version_info[0]
    print('py_version', py_version)

init()
