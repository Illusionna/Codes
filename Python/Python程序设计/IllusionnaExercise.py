# 1. 编写函数 twoSum( )，其功能为：给定一个元素全是整数的列表 nums 和一个整数值 target，请你在该列表中找出和为 target 的那两个整数，并返回它们的下标。
import os
os.system("cls")

def twoSum(nums:list, target:int) -> list:
    """所有满足条件的下标以元组形式存入列表"""
    L = [ ]
    for i in range(0, len(nums), 1):
        for j in range(i+1, len(nums), 1):
            if nums[i] + nums[j] == target:
                L.append((i,j))
            else:
                pass
    return L

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(*twoSum(nums,target), sep="\n")   # 列表拆包打印各元组
    print("*******")
    nums = [3, 2, 4]
    target = 6
    print(*twoSum(nums,target), sep="\n")
    print("*******")
    nums = [3, 3, 1, 5]     # 含一对以上的 target 下标元组
    target = 6
    print(*twoSum(nums,target), sep="\n")


# 2. 编写函数 addTwoNumbers( )，其功能为：给定两个非空的列表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个元素只能是一位数字。请你将两个数相加，并以相同形式返回一个表示和的列表。
import os
os.system("cls")

def addTwoNumbers(L1:list, L2:list) -> list:
    L1 = [f"{i}" for i in iter(reversed(L1))]
    L2 = [f"{i}" for i in iter(reversed(L2))]
    number1 = int("".join(L1))
    number2 = int("".join(L2))
    number = number1 + number2
    L = [int(i) for i in reversed(list(str(number)))]
    return L

if __name__ == '__main__':
    L1 = [2, 4, 3]
    L2 = [5, 6, 4]
    L3 = addTwoNumbers(L1, L2)
    print(L3)

    L1 = [0]
    L2 = [0]
    L3 = addTwoNumbers(L1, L2)
    print(L3)

    L1 = [9, 9, 9, 9, 9, 9, 9]
    L2 = [9, 9, 9, 9]
    L3 = addTwoNumbers(L1, L2)
    print(L3)


# 3. 编写函数 findMedianSortedArrays( )，其功能为：给定两个大小分别为 $m$ 和 $n$ 的正序（从小到大）列表 nums1 和 nums2。请你找出并返回这两个正序列表的中位数。
import os
import numpy
os.system("cls")

def findMedianSortedArrays(nums1:list, nums2:list) -> float:
    nums = [ ]
    nums.extend(nums1)
    nums.extend(nums2)
    nums.sort(reverse = False)
    return numpy.median(nums)

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    num = findMedianSortedArrays (nums1, nums2)
    print(num)

    nums1 = [1, 2]
    nums2 = [3, 4]
    num = findMedianSortedArrays (nums1, nums2)
    print(num)


# 4. Check if the given number is even (偶数) or not. Your function, named is_even( ), should return True if the number is even, and False if the number is odd (奇数).
import os
os.system("cls")

def is_even(num:int) -> bool:
    """位运算，计算速度更快"""
    if num & 1 == 0:
       return True
    else:
       return False

if __name__ == '__main__':
    print(is_even(2))
    print(is_even(3))


# 5. You have a number and you need to determine which digit in this number is the biggest.
import os
os.system("cls")

def max_digit(number:int) -> int:
    """寻找 int 型数中的最大数字"""
    L = [int(i) for i in list(str(number))]
    return max(L)

if __name__ == '__main__':
    print(max_digit(0))
    print(max_digit(52))
    print(max_digit(634))
    print(max_digit(1))