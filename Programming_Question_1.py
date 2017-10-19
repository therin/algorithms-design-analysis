'''
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an 
array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
The numeric answer for the given input file should be typed in the space below.
So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation
 marks. You can make up to 5 attempts, and we'll use the best one for grading.
(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric 
answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your
 best test cases to the discussion forums to help your fellow students!]
'''

import time
file = open('IntegerArray.txt')
array = file.read().splitlines()
array = [int(x) for x in array]
start_time = time.clock()

# brute force:
# 2407905288
'''
count = 0
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            count += 1
'''
print time.clock() - start_time, "seconds"


def sort_count_inversions(array):
    if len(array) == 1:
        return array, 0
    middle = len(array) / 2
    x, left_inv = sort_count_inversions(array[:middle])
    y, right_inv = sort_count_inversions(array[middle:])
    z, count = merge_sort(x, y)
    return z, (count + left_inv + right_inv)


def merge_sort(a, b):
    result = []
    count = 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            result.append(b[j])
            j += 1
            count += (len(a) - i)
        else:
            result.append(a[i])
            i += 1
    result += a[i:]
    result += b[j:]
    return result, count


print sort_count_inversions(array)[1]
print time.clock() - start_time, "seconds"
