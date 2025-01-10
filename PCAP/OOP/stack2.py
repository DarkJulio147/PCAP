import sys
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def mostrar_pila(self):
        return f"Pila = {self.__stack_list}"


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.mostrar_pila())

print(stack_object.pop())
print(stack_object.mostrar_pila())

print(stack_object.pop())
print(stack_object.mostrar_pila())

print(stack_object.pop())
print(stack_object.mostrar_pila())