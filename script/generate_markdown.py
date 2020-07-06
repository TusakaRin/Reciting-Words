# -*- coding: utf-8 -*-

# @Time : 2020/6/25 18:39
# @Author : yfdai

import os, pandas as pd, numpy as np

list_file = r'E:\Programing\python\recite\data\gre3k.xlsx'
output_dir = r'E:\Programing\reveal.js\examples'

wl = pd.read_excel(list_file)

a = int(input('start: '))
b = int(input('step: '))
s = bool(input('Learning?'))

head = '''<style>
    .reveal section p {
    font-size: 2.5em;
    line-height: 1.2em;
    vertical-align: top;
  }
</style>
'''

with open(os.path.join(output_dir, 'recite.md'), 'w', encoding='utf-8', newline='\n') as mdfile:
    mdfile.write(head)
    mdfile.write('\n\n')
    mdfile.write('# Reciting Words!')
    mdfile.write('\n\n\n\n')

    wl['rd'] = np.random.random(len(wl))
    if not s:
        wl.sort_values(by='rd', inplace=True)

    for idx, row in wl[(wl.list <= a + b - 1) & (wl.list >= a)].iterrows():
        mdfile.write(f'{row.word}')
        mdfile.write('\n\n')    
        mdfile.write(f'{row["mean"]} <!-- .element: class="fragment" data-fragment-index="2" -->')
        mdfile.write('\n\n\n\n')
