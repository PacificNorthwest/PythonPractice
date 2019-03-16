import pickle
class TestObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

obj = TestObject(1, 2, 3)
with open('file.bin', 'wb') as handle:
    pickle.dump(obj, handle)

with open('file.bin', 'rb') as handle:
    obj_des = pickle.load(handle)
    print(obj_des.__dict__)