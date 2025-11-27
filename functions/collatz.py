#function to run the collatz algorithm on a number of your choice
def collatz(x:int):
    """
    This functions take in an integer values and applies the collatz (3n+1) algorithm until
    the value of 1 is reached.  Each value is printed out.
    """
    if type(x) != int:
        print('your number must be a positive integer')
    elif (type(x) == int and x < 1):
        print('your number must be a positive integer')
    else:
        steps = 0
        while x>1:
            if x%2 == 0:
                x = x/2
                steps = steps + 1
                print(x, 'step number: ', steps)
            else:
                x = 3*x + 1
                steps = steps + 1
                print(x, 'step number: ', steps)
