# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/8/4 9:05
software: PyCharm

Description:
    正向最大匹配：Maximum Match Method(MM)
"""


class MM:
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
        # get first index of string
        index = 0
        # if text is not bland, start matching process
        while index < len(text):
            word = None
            # start from the index of first word and end at the index of first word(len(text))
            # use the maximum matching phrase to match
            for size in range(self.maximum, 0, -1):
                # if the final index exceed the len(text), keep doing loop
                if index + size > len(text):
                    continue
                # get text
                piece = text[index:(index+size)]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index += size
                    break
            # if no matching is find, just increase the index value by 1
            if word is None:
                index += 1

        return result


if __name__ == '__main__':
    # debug 1
    # text_ = "西安市大雁塔"
    # file_path = r"C:/Users/15025/Desktop/NLP/IMM_Dict.txt"
    # debug 2
    text_ = "南京市长江大桥"
    file_path = r"C:/Users/15025/Desktop/NLP/IMM_Dict_2.txt"
    NLP = MM(file_path)
    print(NLP.cut(text_))
"""
['西安市', '大雁塔']
"""