print('Enter a string: ')
n = input()

print("\nLength of string is: " + str(len(n)))
print()

# Starting i at 1 because i determines the non-inclusive upper limit of string
#   truncation.
for i in range(1, len(n)+1):
    print("string[0:"+str(i)+"]: \t" + n[0:i])

print()

# Conclusions:
# The operator 'string[0:8]' will take the zeroth element up to element 7.
# The operator 'string[1:8]' will take element one (second letter) up to
#   element 7.
