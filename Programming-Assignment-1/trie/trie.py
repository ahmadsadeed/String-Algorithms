#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

'''
3
AT
AG
AC

Output:
0->1:A
1->4:C
1->3:G
1->2:T

Output:
0->1:A
1->4:C
1->3:G
1->2:T

Input:
3
ATAGA
ATC
GAT

Output:
0->1:A
1->2:T
2->3:A
3->4:G
4->5:A
2->6:C
0->7:G
7->8:A
8->9:T
'''