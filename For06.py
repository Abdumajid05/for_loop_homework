def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    l=[]
    for i in range(A,B+1):
        l.append(i)
    return sum(l)
print(main(3,6))