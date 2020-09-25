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
    return trie


def prefix_trie_matching(prefix, trie):
    i = 0
    symbol = prefix[i]
    node = trie[0]

    while 1:
        if not node:
            return True
        elif symbol in node.keys():
            # update node, i and symbol variables
            node = trie[node[symbol]]
            i = i + 1
            if i < len(prefix):
                symbol = prefix[i]
            else:
                symbol = '?'
        else:
            return False


def solve(text, patterns):
    result = []
    # write your code here
    trie = build_trie(patterns)

    for i in range(len(text)):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)
    return result


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    ans = solve(text, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')

'''
AATCGGGTTCAATCGGGGT
2
ATCG
GGGT
'''
