# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:42:13 2024

@author: jlk
"""
#第一题
def get_min_number(source, target):
    def is_subsequence(src, tgt):
        it = iter(src)
        return all(c in it for c in tgt)

    count = 0
    i = 0

    while i < len(target):
        subseq = ""
        for source_char in source:
            if i < len(target) and target[i] == source_char:
                subseq += target[i]
                i += 1
            if subseq and not is_subsequence(source, subseq):
                break
        if not subseq:
            return -1
        count += 1
    
    return count

def main():
    # 读取源字符串source和目标字符串target
    # source = "abc"
    # target = "abcbc"
    source = input().strip()
    target = input().strip()
    result = get_min_number(source, target)
    print(result)

if __name__ == "__main__":
    main()