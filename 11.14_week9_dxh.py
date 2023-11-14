class vector:
    def __init__(self, lst):
        self.lst = lst

    def print_i(self, i):
        print(self.lst[i - 1])

    def change_i(self, i, num):
        self.lst[i - 1] = num
    
    def length(self):
        return sum([x ** 2 for x in self.lst]) ** 0.5
    
    def print_length(self):
        print(self.length())

    def angle(self):
        return [x/self.length() for x in self.lst]
    
    def print_angle(self):
        print(self.angle())
    
    def dot(self, other):
        return sum([x * y for x, y in zip(self.lst, other)])
    
    def scale(self, ratio):
        return [x * ratio for x in self.lst]

    def is_orthogonal(self, x):
        return self.dot(x) == 0
    
    def __str__(self):
        return f"{self.lst}"
    

vector1 = vector([3, 4])
vector1.dot([5, 2])
vector1.print_angle()
vector1.scale(2)
vector1.is_orthogonal([-4, 3])
print(vector1)
#print(list(zip([1, 2, 3], [2, 3, 4])))