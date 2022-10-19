# -*- coding: utf-8 -*-
"""
Created on Mon Mar  13 01:26:09 2022

@author: borakarakus
"""
import time
import unittest

start_time = time.time()
data = open("data.txt", "r")

def maxSumPath(data):
    """
    1. You will start from the top and move downwards to an adjacent number as in below.
    2. You are only allowed to walk downwards and diagonally.
    3. You can only walk over NON PRIME NUMBERS.
    4. You have to reach at the end of the pyramid as much as possible.
    5. You have to treat your input as pyramid.

    :return: The result according the rules above.
    """
    # reading dataset from file: dataset.txt
    readinput = data
    lines = readinput.read().splitlines()

    # populating matrix to array
    data_matrix = []
    for row in lines:
        data_matrix.append(row.split())
    # if data is invalid form.
    try:
        for list in data_matrix:
            for element in range(len(list)):
                list[element] = int(list[element])
    except ValueError as e:
        return "Your data is in a invalid form!"
    # enumerating matrix
    # if data is empty
    try:
        for i, j in enumerate(data_matrix[-1]):
            if j > 1:
                for _ in range(2, j):
                    if (j % _) == 0:
                        break
                else:
                    data_matrix[-1][i] = 0
            else:
                pass
    except IndexError as e:
        return "Your data is empty!"

    # sum up algorithm
    while len(data_matrix) > 1:
        x0 = data_matrix.pop()
        x1 = data_matrix.pop()

        for i, j in enumerate(x1):
            if j > 1:
                for _ in range(2, j):
                    if (j % _) == 0:
                        break
                else:
                    x1[i] = 0
            else:
                pass

        y = []
        for i, x in enumerate(x1):
            y.append(max(x0[i], x0[i + 1]) + x)
        data_matrix.append(y)

    # the solution of question 4
    print('Operation time : --- %s seconds ---' % (time.time() - start_time))
    return "{} {}".format("Max Sum is", data_matrix[0][0])


class TestmaxSumPath(unittest.TestCase):
    """
    Unit testing for program to find future bugs.
    """
    def test_max_sum_path(self):
        test_data = open("testData.txt", "r")
        self.assertEqual(maxSumPath(test_data),"Max Sum is 2315")

    def test_empty_data(self):
        empty_data = open("emptyData.txt", "r")
        self.assertEqual(maxSumPath(empty_data),"Your data is empty!")

    def test_invalid_data(self):
        invalid_data = open("invalidData.txt","r")
        self.assertEqual(maxSumPath(invalid_data),"Your data is in a invalid form!")


print(maxSumPath(data)) # 8219
#if __name__ == "__main__":
    #   unittest.main()