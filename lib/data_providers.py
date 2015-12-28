from __future__ import unicode_literals

import os
import sys


class StdInDataProvider(object):
    def __iter__(self):
        for line in sys.stdin:
            yield line


class FileDataProvider:
    def __init__(self, file_name):
        assert file_name
        assert os.path.exists(file_name)

        self.file_name = file_name

    def __iter__(self):
        with open(self.file_name, 'r') as log_file:
            for line in log_file:
                yield line
