# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/8/4 7:51
software: PyCharm

Description:
    逆向最大匹配: Reverse Maximum Match Method(RMM)
"""


class RMM:
    def __init__(self, dict_path):
        # define a dictionary set
        self.dictionary = set()
        # define a variable
        self.maximum = 0
        # read dictionary
        with open(dict_path, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # jump the blank row in IMM_Dict file
                if not line:
                    continue
                # add reading element in our dictionary
                self.dictionary.add(line)
                # get the maximum length of phrase in our dictionary
                if len(line) > self.maximum:
                    self.maximum = len(line)
        # print the element in dictionary
        # print(self.dictionary)

    def cut(self, text):
        # create a list to save the final result
        result = []
        index = len(text)
        # if text is not bland, start matching process
        while index > 0:
            word = None
            # start from the index of last word(self.maximum) and end at the index of first word(0)
            # use the maximum matching phrase to match
            for size in range(self.maximum, 0, -1):
                # 到最左侧的时候判断，直接跳过多余的字符匹配过程
                if index - size < 0:
                    continue
                # inverse the oder of text
                piece = text[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            # if no matching is find, just decrease the index value by 1
            if word is None:
                index -= 1

        # due to inverse matching, we need to inverse back here
        return result[::-1]


if __name__ == '__main__':
    # debug 1
    text_ = "西安市大雁塔"
    file_path = r"C:/Users/15025/Desktop/NLP/Dict01.txt"
    # debug 2
    # text_ = "南京市长江大桥"
    # file_path = r"C:/Users/15025/Desktop/NLP/Dict02.txt"
    NLP = RMM(file_path)
    print(NLP.cut(text_))

