
def triplets():
    """
    Solve Euler #9 - Three numbers that
      - Add up to 1000
      - A is less than B is less than C
      - A**2 + B**2 == C**2
    """
    for a in xrange(1, 1000):
        for b in xrange(a, 1000):
            c = 1000 - (a + b)
            if a**2 + b**2 == c**2:
                return a, b, c


def lc_triplets():
    """
    Let's try a list comprehension!
    """
    return [(a, b, 1000 - (a + b)) for a in xrange(1, 1000) for b in xrange(a, 1000) if a**2 + b**2 == (1000 - (a+b))**2][0]

print "Normal multi line function: {}".format(triplets())
print "List comprehension: {}".format(lc_triplets())
