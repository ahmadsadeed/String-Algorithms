# python3
import sys


def sort_characters(S):
    order = [0] * len(S)
    count = []
    chars = sorted(set(S))

    for ch in chars:
        count.append(S.count(ch))

    for j in range(1, len(count)):
        count[j] += count[j - 1]

    for i in reversed(range(len(S))):
        c = S[i]
        count[chars.index(c)] -= 1
        order[count[chars.index(c)]] = i

    return order


def compute_char_classes(S, order):
    classes = [0] * len(S)

    for i in range(1, len(S)):
        if S[order[i]] != S[order[i - 1]]:
            classes[order[i]] = classes[order[i - 1]] + 1
        else:
            classes[order[i]] = classes[order[i - 1]]

    return classes


def sort_doubled(S, L, order, classes):
    S_len = len(S)
    count = [0] * S_len
    new_order = [0] * S_len

    for i in range(S_len):
        count[classes[i]] += 1
    for j in range(1, S_len):
        count[j] += count[j - 1]

    for i in reversed(range(S_len)):
        start = (order[i] - L + S_len) % S_len
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start

    return new_order


def update_classes(new_order, classes, L):
    n = len(new_order)
    new_classes = [0] * n

    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = cur + L, (prev + L) % n
        if classes[cur] != classes[prev] or classes[mid] != classes[mid_prev]:
            new_classes[cur] = new_classes[prev] + 1
        else:
            new_classes[cur] = new_classes[prev]

    return new_classes


def build_suffix_array(S):
    order = sort_characters(S)
    classes = compute_char_classes(S, order)
    L = 1

    while L < len(S):
        order = sort_doubled(S, L, order, classes)
        classes = update_classes(order, classes, L)
        L = 2 * L

    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))

'''
Input:
AAA$
Output:
3 2 1 0
Explanation:
Sorted suffixes:
3 $
2 A$
1 AA$
0 AAA$

Input:
GAC$
Output:
3 1 2 0
Explanation:
Sorted suffixes:
3 $
1 AC$
2 C$
0 GAC$

Input:
GAGAGAGA$
Output:
8 7 5 3 1 6 4 2 0
Explanation:
Sorted suffixes:
8 $
7 A$
5 AGA$
3 AGAGA$
1 AGAGAGA$
6 GA$
4 GAGA$
2 GAGAGA$
0 GAGAGAGA$

Input:
r
Output:
15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5
Explanation:
Sorted suffixes:
15 $
14 A$
0 AACGATAGCGGTAGA$
1 ACGATAGCGGTAGA$
12 AGA$
6 AGCGGTAGA$
4 ATAGCGGTAGA$
2 CGATAGCGGTAGA$
8 CGGTAGA$
13 GA$
3 GATAGCGGTAGA$
7 GCGGTAGA$
9 GGTAGA$
10 GTAGA$
11 TAGA$
5 TAGCGGTAGA$
'''