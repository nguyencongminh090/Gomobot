def pktool(move, q):
    """
    q = 0 --> PlayOK -> Piskvork \n
    q = 1 --> Piskvork -> PlayOK

    :param move: Move
    :param q: Option
    """
    lst1 = []
    lst = []
    char = ["o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
    for i in range(0, 15):
        for j in range(0, 15):
            k = j
            output = str(-(i - 14)) + ',' + str(k)
            lst1.append(output)
    for i in range(0, 15):
        for j in range(0, 15):
            k = j
            output = char[i] + str(-(k - 15))
            lst.append(output)

    def find(a, b):
        for i in range(len(b)):
            if a == b[i]:
                return i

    def returnmove(s):
        output = 0
        for i in lst:
            if s == i:
                k = find(s, lst)
                output = lst1[k]
        return output

    def returnpos(s):
        output = 0
        for i in lst1:
            if s == i:
                k = find(s, lst1)
                output = lst[k]
        return output

    if q == 0:
        out = returnmove(move)
        return out
    elif q == 1:
        out = returnpos(move)
        return out
