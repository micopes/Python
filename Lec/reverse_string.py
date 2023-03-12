value = "Hello World"

#1 reverse
value_list = list(value)
value_list.reverse()
print("".join(value_list))

#2 reversed
print("".join(reversed(list(value))))

#3 for loop
lst = list(value)
res = ""
for i in range(len(lst)-1, -1, -1):
    res += lst[i]
print(res)

#4 while
lst = list(value)
res = ""
while lst:
  res += lst.pop()
print(res)
  