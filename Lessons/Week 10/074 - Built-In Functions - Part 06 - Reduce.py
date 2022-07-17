# ------------------------------------------------------------------------------------
# --------------------------- Built-In Functions => Reduce ---------------------------
# ------------------------------------------------------------------------------------
# [1] Reduce Takes A Function + Iterator
# [2] Reduce Runs A Function On The First and The Second Element And Store The Result
# [3] Then Run The Function On Result And The Third Element
# [4] Then Run The Function On Result And The Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ------------------------------------------------------------------------------------

from functools import reduce


def sumAll(num1, num2):
    return num1 + num2


numbers = [1, 8, 2, 9, 100]
result = reduce(sumAll, numbers)
result = reduce(lambda num1, num2: num1 + num2, numbers)
print(result)  # ((((1 + 8) + 2) + 9) + 100)
