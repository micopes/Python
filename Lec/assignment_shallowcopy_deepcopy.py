# Assignment Operator(=)
# 기존의 주소를 가리킴.
colors = ['red', 'blue', 'green']
b = colors
b.append('white')
print(b)
print(colors)

print()

# Shallow Copy
# 기존에 존재하는 것은 그대로이나, compound object(두 개 이상의 객체들이 합성된 것)라면 주소값을 받아오게 된다.
a = [[1, 2], [2, 4]]
b = a[:]
b.append([3, 6])
print(b)
print(a)

b[0].append(3)
print(b)
print(a)

print()

# Deep Copy
# 값을 받아오게 된다.

a = [[1, 2], [2, 4]]

import copy
b = copy.deepcopy(a)
b[0].append(4)
print(b)
print(a)

# Compound object가 아닌 경우. (내부 요소가 그냥 element인 경우)
# Shallow Copy가 Deep Copy와 동일한 동작을 한다.
a = [1, 2, 3, 4]
b = a[:]
b.append(5)
print(a)
print(b)