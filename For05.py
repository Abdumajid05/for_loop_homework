def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(A,B+1):
        l.append(i)
    return l[::-1]
print(main(5,9))