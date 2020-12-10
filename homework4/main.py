from stack import*
s =[]

print("Введите количество элементов в стеке")
n = int(input())
if n <= 0:
    print("Стек не может быть пустым")
else:
    print("Введите элементы")
    for i in range(n):
        element = int(input())
        s.append(element)
print(s.pop())
print(s)
print(isEmpty(s))



