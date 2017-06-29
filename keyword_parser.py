# -*- coding: utf-8 -*-
import re
import jieba

PATTERN_TO_REMOVE = re.compile('[\s+.!/\[\]_\-,$%^*(\"\']+|[+—！《》【】，。？、~：@#￥%…&*（）]+')

class KeywordParser(object):
    __shared_state = {}
    __parser = jieba

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    @staticmethod
    def extract(target):
        linted_target = re.sub(PATTERN_TO_REMOVE, '', target)
        return KeywordParser.__parser.cut(linted_target)

    def __repr__(self):
        return 'KeywordParser[{}]'.format(self.state)

KeywordParser()
