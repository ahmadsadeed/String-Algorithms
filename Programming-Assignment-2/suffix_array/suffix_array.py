# python3
import sys


def build_suffix_array(text):

    """ Build suffix array of the string text and return a list
    result of the same length as the text such that the value result[i] is
    the index (0-based) in text where the i-th lexicographically smallest
    suffix of text starts.
    SuffixArray(“panamabananas$”) = (13, 5, 3, 1, 7, 9, 11, 6, 4, 2, 8, 10, 0, 12) """

    arr = []

    for i in range(len(text)):
        arr.append((i, text[i:]))

    # sort based on second part of tuple
    arr = sorted(arr, key=lambda tup: tup[1])

    result = [arr[i][0] for i in range(len(arr))]

    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
