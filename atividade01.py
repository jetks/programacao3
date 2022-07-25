def resto (x, y):
    if x == y:
        return 0
    elif x < y:
        return x
    else:
        return resto (x-y, y)
    
print (resto(2, 4))
