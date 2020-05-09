# -*- coding: utf-8 -*-

# @Time : 2020/5/9 12:23
# @Author : yfdai


if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.dirname(__file__))
    import pandas as pd
    from os.path import join as pjoin
    from config import fd_project
    data = pd.read_excel(pjoin(fd_project, 'data/gre.xlsx'), sheet_name='3k')
    data.dropna(subset=['meaning'], inplace=True)
    os.system('cls')
    for idx, row in data.iterrows():
        print(f"{idx + 1: >4}  {row.word}", end='')
        input()
        print(' ' * 6 + f"{row.meaning}")
        input()
        os.system('cls')
