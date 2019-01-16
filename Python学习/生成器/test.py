#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import story

def towNum(nums, target):

    for x in range(len(nums)):
        for j in range(x+1, len(nums)):
            if(nums[x] + nums[j] == target):
                return [x, j]


class Solution:
    def reverse(self, x):
        text = str(x)
        l = len(text)

        if (l == 1):
            return True

        for i in range(l):
            j = l - 1 - i
            if (text[i] != text[j]):
                return False

        return True

    def longestCommonPrefix(self, strs):

        l = len(strs)
        if l == 0:
            return ""
        if l == 1:
            return strs[0]

        result = ""
        firstWord = strs[0]

        for i in range(len(firstWord)):
            char = firstWord[i]
            ll = range(1, l)

            for j in ll:
                otherWord = strs[j]

                if i > len(otherWord)-1:
                    return result

                otherChar = otherWord[i]

                if char == otherChar:
                    if j == len(ll):
                        result += char

                    continue
                else:
                    return result

        return result


    def removeDuplicates(self, nums):

        if nums == []:
            return 0

        index = 1
        last = nums[0]
        for x in nums:
            if x != last:
                nums[index] = x
                index += 1
            last = x
        return index


    def removeElement(self, nums, val):

        index = 0
        count = 0
        l = len(nums)
        for i in range(l):
            if count == l-1:
                break
            value = nums[i]
            if val == value:
                nums.pop(i)
                nums.append(val)
                index += 1
            count += 1
        return l-index

    def searchInsert(self, nums, target):

        if target in nums:
            return nums.index(target)

        newIndex = 0
        for i in range(len(nums)):

            if target < nums[i]:
                newIndex = i
                break
            else:
                newIndex = i+1

        return newIndex




def main():
    # nums = [1, 2, 7, 11]
    # target = 9
    # li = towNum(nums, target)
    # print(li)

    # num = int(input("输入数字:"))
    # Solution().reverse(num)

    nums = [1,3,5,6]
    val = 2
    index = Solution().searchInsert(nums, val)
    print("%d" % index)


if __name__ == "__main__":
    # main()

    story.requestPage();