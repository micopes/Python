question = list("batman")
lst = []
for i in range(len(question)):
    lst.append('_')
print("Here is the word")
print(lst)

num_of_try = 10
for _ in range(num_of_try):
    char = input("Guess the character?")
  
    for idx in range(len(question)):
        if char == question[idx]:
            lst[idx] = char
    print(lst)          

    if '_' not in lst:
        print("You won")
        break

if '_' in lst:
    print("You Lost")
