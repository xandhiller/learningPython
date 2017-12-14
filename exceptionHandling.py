def spam(denominator):
    try:
        return (42/denominator)
    except:
        return 'Error: Invalid input ya\' dunce.'

print(spam(2), spam(12), spam(0), spam(1), sep='\n')
