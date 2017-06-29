# -*- coding: utf-8 -*-
import codecs
import json
import os

from keyword_parser import KeywordParser


def file_and_path_recursive(root_dir='.'):
    for root, sub_dirs, files in os.walk(root_dir):
        abspath = os.path.abspath(root)
        for filename in files:
            yield filename, abspath


class BookFile(object):
    def __init__(self, name, path):
        self.filename = name
        self.name, self.ext = os.path.splitext(name)
        self.path = path
        self.__keywords = []

    @property
    def keywords(self):
        if len(self.__keywords) is 0:
            self.__keywords = list(KeywordParser.extract(self.name))
        return self.__keywords

    def dump(self):

        with codecs.open('books_json/%s.json' % self.name, 'w+b', 'utf-8') as wf:
            json.dump(self.json(), wf)
        pass

    def json(self):
        print('dumpling: ', self.name)
        return {
            'filename': self.filename,
            'name': self.filename,
            'ext': self.ext,
            'path': self.path,
            'keywords': self.keywords,
        }

    def __repr__(self):
        return 'File[{}] in {}'.format(self.name, self.path)
