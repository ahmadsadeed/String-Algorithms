# python3
import sys


def BWT(txt):
    matrix = []
    for i in range(len(txt)):
        begin = txt[0:len(txt) - 1]
        end = txt[len(txt) - 1:]
        txt = end + begin
        matrix.append(txt)
    matrix.sort()

    return ''.join([matrix[i][len(txt) - 1] for i in range(len(txt))])


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
'''
Input:
AGACATA$

Output:
ATG$CAAA

Explanation:
𝑀(Text) =
$ 𝐴 𝐺 𝐴 𝐶 𝐴 𝑇 𝐴
𝐴 $ 𝐴 𝐺 𝐴 𝐶 𝐴 𝑇
𝐴 𝐶 𝐴 𝑇 𝐴 $ 𝐴 𝐺
𝐴 𝐺 𝐴 𝐶 𝐴 𝑇 𝐴 $
𝐴 𝑇 𝐴 $ 𝐴 𝐺 𝐴 𝐶
𝐶 𝐴 𝑇 𝐴 $ 𝐴 𝐺 𝐴
𝐺 𝐴 𝐶 𝐴 𝑇 𝐴 $ 𝐴
𝑇 𝐴 $ 𝐴 𝐺 𝐴 𝐶 𝐴

'''