# 7 gives 5
# 9 gives true

items = ["a", "b", "c", "d", "e"]

if (size := len(items)) < 10 :
    print(size)

if size := len(items) < 10 : # Notice the missing parenthesis
    print(size)
