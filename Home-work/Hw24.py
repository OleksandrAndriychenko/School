class String(str):
    def __mul__(self, other):
        return self + str(other)
    def __sub__(self, other):
        return self.replace(other, '', 1)
st_1 = String('pineapple apple pine')
st_2 = String('apple')
print(st_1 - st_2)
