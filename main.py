# -*- coding: utf-8 -*-

from book_file import BookFile, file_and_path_recursive

for bf in (BookFile(filename, path) for filename, path in file_and_path_recursive(r'.\books')):
    bf.dump()

