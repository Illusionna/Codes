# **********************************************************************************
# 1. 排序算法：
# 在上述红色区域内填写代码，完善sort函数，使其最终能够对列表从小到大排序。请分别使用选择排序法、冒泡排序法和快速排序法实现sort函数。
# **********************************************************************************
# 2. 佩奇去超市购买54元巧克力和53元果冻，货币面值有20、10、2、1元，按付款货币数量最少原则，佩奇总共需要付给超市多少数量哪种面值的货币，编写函数实现该算法。
# **********************************************************************************
# 3. 青蛙跳台阶问题：
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# **********************************************************************************

import os

def cls() -> None:
    os.system("cls")
cls()

def selectionSort(L:list) -> list:
    for i in range(0, len(L), 1):
        (L[L.index(min(L[i:]))], L[i]) = (L[i], L[L.index(min(L[i:]))])
    return L

def bubbleSort(L:list) -> list:
    for i in range(1, len(L), 1):
        for j in range(0, len(L)-i, 1):
            if L[j] > L[j+1]:
                (L[j], L[j+1]) = (L[j+1], L[j])
    return L

def quickSort(L:list) -> list:
    if len(L) <= 1:
        return L
    else:
        pivot = L[0]
        low = [i for i in L[1:] if i <= pivot]
        high = [i for i in L[1:] if i > pivot]
        return quickSort(low) + [pivot] + quickSort(high)

def payMoneyDenominationNumbers(totalMoney:int) -> any:
    """用面额字典存放钱的张数，由最大面额整除 totalMoney 再次大面额整除剩余的 totalMoney 进行循环"""
    denominations = {"20元张数：":0, "10元张数：":0, "2元张数：":0, "1元张数：":0}
    moneyType = [20, 10, 2, 1]
    pos = 0
    for i in denominations:
        numbers = totalMoney // moneyType[pos]
        denominations[i] = numbers
        totalMoney = totalMoney - moneyType[pos] * numbers
        pos = pos + 1
    print(denominations)

def frogJumpStage(n:int) -> int:
    """如果只有一个台阶，那么只有一种跳法；如果只有两个台阶，那么只有两种跳法；如果有 n(>2) 个台阶，那么有剩下的 (n-1) 和 (n-2) 个台阶可能的跳法."""
    if n <= 0:
        return False
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return frogJumpStage(n-1) + frogJumpStage(n-2)

if __name__ == '__main__':
    data = [4, 6, 2, 1, 7, 12, 25, 13, 9]
    print("起源列表:", data)
    print("选择排序:", selectionSort(data))
    print("冒泡排序:", bubbleSort(data))
    print("快速排序:", quickSort(data))

    payMoneyDenominationNumbers(54+53)

    print("一共有", frogJumpStage(12), "种跳法")