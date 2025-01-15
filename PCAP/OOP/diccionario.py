class ExampleClass:
    def __init__(self, val = 1, val2 =0 ):
        self.first = val1
        self.foo = val2
    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2, 10)

example_object_2.set_second(3)

example_object_3 = ExampleClass(3)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

