import pprint   # Contains the pprint.pprint function. Prettily prints stuff.

message = 'It was a 1 bright cold day in April, and the clocks were striking \
thirteen'

count = {}

for i in message:
    print("i is: "+ str(i))
    count.setdefault(i, 0)      # 'i' is assigned to a letter. If letter is not
                                # in the dictionary, it will make put it in.
                                # It will then set the count to 0 if it is not
                                # yet in the list.
                                # It then increments the count of that letter
                                # at the end of this block.
    print(count)
    count[i] = count[i] + 1

pprint.pprint(count)
