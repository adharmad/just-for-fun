# Sequence Solver

import sys, string, math


def getOrder(seq, order):
    """
    Reduce the sequence recursively. Get the deltas between consecutive 
    terms. At the point where the deltas are all the same, we have hit
    the order
    """
    deltaSeq = []
    for i in range(len(seq)-1): 
        deltaSeq.append(seq[i+1] - seq[i])

    allEqual = all(x==deltaSeq[0] for x in deltaSeq)

    if allEqual:
        return order+1
    else:
        return getOrder(deltaSeq, order+1)

def solveSequence(seq):
    """
    Solve the integer sequence
    """
    n = getOrder(seq, 0)

if __name__ == '__main__':
    seq = sys.argv[1:]
    intSeq = list(map(lambda x: int(x), seq))

    solveSequence(intSeq)
