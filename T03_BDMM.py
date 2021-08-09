# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/8/9 16:47
software: PyCharm

Description:
    双向最大匹配: Bi-direction matching method(BDMM)
    综合MM与IMM方法，最终选择字段最少的选项
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
                piece = text[index:(index + size)]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index += size
                    break
            # if no matching is find, just increase the index value by 1
            if word is None:
                index += 1

        return result


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
    result_ = 0
    text_ = "南京市长江大桥"
    file_path = r"C:/Users/15025/Desktop/NLP/Dict02.txt"
    NLP_MM = MM(file_path)
    result_MM = NLP_MM.cut(text_)
    NLP_RMM = RMM(file_path)
    result_RMM = NLP_RMM.cut(text_)
    if len(result_MM) > len(result_RMM):
        print(result_RMM)
    else:
        print(result_MM)
