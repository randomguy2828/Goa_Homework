
def st(sent):
    wr = sent.split()
    first_let = []
    for wrs in wr:
        first_let.append(wrs[0].upper())
    result = "".join(first_let)
    return result
