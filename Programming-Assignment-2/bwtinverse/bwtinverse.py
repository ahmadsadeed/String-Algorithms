# python3
import sys


def InverseBWT(txt):
    last_col = []
    for (idx, val) in enumerate(txt):
        last_col.append((val, idx))

    first_col = sorted(last_col)

    first_to_last = {}
    for first, last in zip(first_col, last_col):
        first_to_last[first] = last

    char = first_col[0]

    result = ''
    for i in range(len(txt)):
        result += char[0]
        char = first_to_last[char]

    return result[::-1]  # reversed


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))

'''
Input:
AGGGAA$

Output:
GAGAGA$

Explanation:
𝑀(Text) =
$ 𝐺 𝐴 𝐺 𝐴 𝐺 𝐴
𝐴 $ 𝐺 𝐴 𝐺 𝐴 𝐺
𝐴 𝐺 𝐴 $ 𝐺 𝐴 𝐺
𝐴 𝐺 𝐴 𝐺 𝐴 $ 𝐺
𝐺 𝐴 $ 𝐺 𝐴 𝐺 𝐴
𝐺 𝐴 𝐺 𝐴 $ 𝐺 𝐴
𝐺 𝐴 𝐺 𝐴 𝐺 𝐴 $
'''
