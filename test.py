import random
import sys

import pandas as pd


class ForeignTest:
    def __init__(self):
        self.study = pd.read_excel('./data/study.xls', header=0)

    def solution(self):
        study = self.study
        question = study.iloc[:, 0:2]
        answer = study.iloc[:, 2]
        while (True):
            rn = random.randrange(0, len(self.study) - 1)
            print(f'두 단어중 맞는 단어를 입력 하세요\n1.{question.iloc[rn][0]} 2.{question.iloc[rn][1]}')
            raw_input = sys.stdin.readline().split()[0]
            if len(raw_input) == 1:
                num_input = int(raw_input) - 1
                if num_input == 0 or num_input == 1:
                    if question.iloc[rn][num_input] == answer.iloc[rn]:
                        print('정답!\n\n')
                    else:
                        print('땡~~~~~\n\n')
                else:
                    print('땡~~~~~\n\n')

            else:
                if raw_input == answer.iloc[rn]:
                    print('정답!\n\n')
                else:
                    print('땡~~~~~\n\n')


if __name__ == '__main__':
    ForeignTest().solution()
