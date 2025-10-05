# 校车乘客在途中有上有下
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
# 使用浅拷贝
bus2 = copy.copy(bus1)
print(bus2)
# 使用深拷贝
bus3 = copy.deepcopy(bus1)
print(bus3)