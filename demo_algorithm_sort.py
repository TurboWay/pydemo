#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/9 17:14
# @Author : way
# @Site : 
# @Describe: 排序算法

# 快速排序
def quicksort(seq):
    if len(seq) < 2:
        return seq
    else:
        base = seq[0]
        left = [i for i in seq[1:] if i < base]
        right = [i for i in seq[1:] if i >= base]
        return quicksort(left) + [base] + quicksort(right)


# 冒泡排序
def bubblesort(seq):
    for i in range(len(seq) - 1):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq

# 归并算法
def mergesort(seq):
    def merge(left, right):
        """
        入参数组都是有序的，此处将两个有序数组合并成一个大的有序数组
        """
        # 两个数组的起始下标
        l, r = 0, 0

        new_list = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                new_list.append(left[l])
                l += 1
            else:
                new_list.append(right[r])
                r += 1
        new_list += left[l:]
        new_list += right[r:]
        return new_list

    if len(seq) < 2:
        return seq
    else:
        middle = len(seq) // 2
        left = mergesort(seq[:middle])
        right = mergesort(seq[middle:])
        return merge(left, right)



test = [5, 4, 2, 5, 8, 19, 7]
# print(quicksort(test))
# print(bubblesort(test))
print(mergesort(test))