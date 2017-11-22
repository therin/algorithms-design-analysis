# -*- coding: utf-8 -*-
import heapq
import heapq_max
'''
The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 6 lecture on hash table applications).
The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ith row of the file
specifying the ith entry of the array.
Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that
satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)
Write your numeric answer (an integer between 0 and 20001) in the space provided.
OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example, you could compare performance under the chaining
and open addressing approaches to resolving collisions.
# our two sum function which will return
# all pairs in the list that sum up to S
def twoSum(arr, S):
'''
'''
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 5 lecture on heap applications). The text file contains a list of the integers from 1 to
10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is defined as the median of the
numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)
In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)mod10000.
OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.
'''


def twoSum(numbers):
    answerCounter = 0
    searchRange = set(range(-10000, 10001))
    for i in searchRange:
        if any(i - x in numbers and 2 * x != i for x in numbers):
            answerCounter += 1
            print("found")
    return answerCounter


def medianMaintenance(numbers):
    medians = []
    minHeap = []
    maxHeap = []
    minimum = min(numbers[0], numbers[1])
    maximum = max(numbers[0], numbers[1])
    heapq_max.heappush_max(minHeap, minimum)
    heapq.heappush(maxHeap, maximum)
    medians.append(maximum)
    medians.append(minimum)
    for number in numbers[2:]:
        if number < maxHeap[0]:
            heapq_max.heappush_max(minHeap, number)
        else:
            heapq.heappush(maxHeap, number)
        while abs(len(minHeap) - len(maxHeap)) >= 2:
            if len(minHeap) > len(maxHeap):
                item = heapq_max.heappop_max(minHeap)
                heapq.heappush(maxHeap, item)
            elif len(minHeap) < len(maxHeap):
                item = heapq.heappop(maxHeap)
                heapq_max.heappush_max(minHeap, item)
        if (len(minHeap) + len(maxHeap)) % 2 != 0:
            if len(minHeap) > len(maxHeap):
                medians.append(minHeap[0])
            else:
                medians.append(maxHeap[0])
        else:
            medians.append(minHeap[0])
    print(sum(medians) % 10000)


if __name__ == '__main__':
    def generateListTwoSum():
        with open('algo1-programming_prob-2sum.txt') as file:
            return set([int(line) for line in file])

    def generateListMedian():
        with open('Median.txt') as file:
            return [int(line) for line in file]

    numbers = generateListMedian()
    medianMaintenance(numbers)
    # print(twoSum(numbers))
