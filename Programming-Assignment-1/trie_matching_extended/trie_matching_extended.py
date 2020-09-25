# python3
import sys


# from trie.py file
def build_trie(patterns):
    trie = dict()
    trie[0] = dict()
    root = trie[0]
    edge = 1

    for pattern in patterns:
        curr_node = root
        for symbol in pattern:
            if symbol in curr_node.keys():
                curr_node = trie[curr_node[symbol]]
            else:
                curr_node[symbol] = edge
                trie[edge] = dict()
                curr_node = trie[edge]
                edge = edge + 1
        # add '$' to end of leaf
        curr_node['$'] = {}
    return trie


def prefix_trie_matching(prefix, trie, pos):
    i = 0
    symbol = prefix[i]
    node = trie[0]
    res = -1

    while 1:
        if (not node) or ('$' in node):
            return res

        if symbol in node.keys():
            # update node, i and symbol variables
            node = trie[node[symbol]]
            i = i + 1
            res = pos
            if i < len(prefix):
                symbol = prefix[i]
            elif '$' in node:
                return res
            else:
                symbol = '?'
                res = -1
        else:
            return res if '$' in node else -1


def solve(text, patterns):
    result = set()
    # write your code here
    trie = build_trie(patterns)

    for i in range(len(text)):
        res = prefix_trie_matching(text[i:], trie, i)
        if res != -1:
            result.add(res)
    return sorted(result)


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    ans = solve(text, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')


'''
Input:
ACATA
3
AT
A
AG
Output:
0 2 4
'''