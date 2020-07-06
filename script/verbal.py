# -*- coding: utf-8 -*-

# @Time : 2020/6/4 19:31
# @Author : yfdai

import os, pandas as pd, sys
from os.path import join as pjoin
sys.path.append(pjoin(os.path.dirname(__file__), '../src'))
import config


def main():
    existing = pd.read_excel(os.path.join(config.fd_project, 'data/gre3k.xlsx')).word.to_list()
    while True:
        word = input()
        if word in existing:
            print('Exist')
            continue
        else:
            print('No')


if __name__ == '__main__':
    main()
