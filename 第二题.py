# -*- coding: utf-8 -*-
# 第二题
'''
样例输入：
bge)))))))))
((IIII))))))
()()()()(uuu
))))UUUU((()

'''

def check_and_print(string):
    # 读取字符串
    string = string.strip()
    stack = []
    check = []
    for i, char in enumerate(string):
        if char == "(":
            stack.append(i)
            check += " "
        elif char == ")":
            if stack:
                stack.pop()
                check += " "
            else:
                check += "x"
        else:
            check += " "
    if stack:
        for i in stack:
            check[i] = "?"
    print(string)
    ck = ""
    for i in check:
        ck += i
    print(ck)


def main():
    strings = [] 
    while True:
        line = input()  
        if not line: 
            break
        strings.append(line)
        # print(line) 
    for string in strings:
        check_and_print(string)

if __name__ == "__main__":
    main()
