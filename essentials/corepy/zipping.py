sunday  = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday  = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
tuesday = [ 2,  2,  3,  7,  9, 10, 11, 12, 10,  9,  8,  8]

for item in zip(sunday, monday):
    print(item)
for item in zip(sunday, monday, tuesday):
    print(item)


