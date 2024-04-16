def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    l=[]
    for i in range(N):
        if i%2==1:
            l.append(i)
    return sum(l)
print(main(12))