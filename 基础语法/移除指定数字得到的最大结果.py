#移除指定数字得到的最大结果

def removeDigit(number: str, digit: str) -> str:
    new_list = []
    for i in range(len(number)):
        if number[i] == digit:
            new_number = number[:i] + number[i+1:]
            new_list.append(new_number)
    return max(new_list)

removeDigit('1231', '1')



