for x in range(0, 20):
    print("Count is " + str(x) +" and this string section is a test")

    # Prints from 0 up to 19, doesn't print 20.

for x in range(0, 20, 5):
    print("Count is now: %d" % x)

    # Prints in steps of five, printing: 0, 5, 10 and 15 (not 20).
    # I think it doesn't print 20 because that's the upper limit and
    # subsequently a condition for exit of the loop.
