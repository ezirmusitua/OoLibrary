# -*- coding: utf-8 -*-
from book_file import BookFile
from keyword_parser import KeywordParser

print('test parser: ', '/'.join(KeywordParser.extract("我来到北京清华大学")))
print('test BookFile: ', BookFile('test.pdf', '.'))
