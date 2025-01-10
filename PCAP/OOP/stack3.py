class Stack:
    def __init__(self):
        self.size = 0
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from an empty stack")
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        self.size -= 1
        return val

    def __str__(self):
        return f"Pila = {self.__stack_list}"


class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        super().push(val)

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from an empty stack")
        val = super().pop()
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)

print(stack_object)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())