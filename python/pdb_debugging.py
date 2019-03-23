def multiplication(x, y):
    import pdb; pdb.set_trace()
    x = x * y
    y = y * x
    x = x * x
    y = y * y
    x = x * y - y * x
    return x

print(multiplication(5, 7))