flag = False

class Dynamic:
    if flag:
        def __init__(self):
            self.value = 5
    else:
        def __init__(self):
            self.value = 444

instance = Dynamic()
print(instance.value)