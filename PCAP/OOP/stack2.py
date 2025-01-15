import sys
class Stack:
    def __init__(self):
        self.size = 0
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)
        self.size += 1

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        self.size -= 1
        return val
    def __str__(self):
        for i in self.size:
            self.__stack_list[i]


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

