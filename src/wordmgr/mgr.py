from config import fd_project
import pandas as pd, random
from os.path import join as pjoin


class WordMgr:
    def __init__(self, auto_shuffle=True):
        # Words
        self.words = pd.read_excel(pjoin(fd_project, 'data/gre3k.xlsx')).rename(columns={'mean': 'meaning'}).drop_duplicates('word')
        self.enabled_list = set({})
        self.current_remain = []
        self.finished = []
        self.next_round = []
        self.current_word = None
        # config
        self.auto_shuffle = auto_shuffle

        self.pass_counter = 0
    
    def filter_words(self):
        self.current_remain = self.words[self.words.list.isin(self.enabled_list)].values.tolist()
        if self.auto_shuffle:
            random.shuffle(self.current_remain)

    def switch_word(self):
        if not self.current_remain:
            if self.next_round:
                self.current_remain = self.next_round[:]
                self.next_round = []
                self.current_word = self.current_remain.pop(0)
                return self.current_word, True
            else:
                return None, None
        else:
            self.current_word = self.current_remain.pop(0)
            return self.current_word, False

    def get_meaning(self):
        if not self.current_word:
            return self.current_word[4]

    def shuffle(self):
        random.shuffle(self.current_remain)
        random.shuffle(self.next_round)

    def pass_word(self, finish: bool):
        if not finish:
            self.next_round.append(self.current_word)
        else:
            self.finished.append(self.current_word)
        return self.current_word

    def reset(self):
        self.current_remain = []
        self.current_word = None
        self.next_round = []
        self.finished = []
