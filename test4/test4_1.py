#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a module'

__author__ = 'admin'

import sys


def test():
    args = sys.argv
    if len(args) <= 1:
        print('hello')
    elif len(args) <= 2:
        print('hello,%s' % args[1])
    else:
        print('Too many argments!')


if __name__ == '__main__':
    test()
