name = "Kang"
age = 29

# Old Version : % 이용
print("Hello, %s" % name)
print("Hello, %s, I am %s" % (name, age))


# Python 2.6 : .format 이용
print("Hello, {}. I am {}".format(name, age))
print("Hello, {1}. I am {0}".format(name, age)) # 파라미터 순서 지정

person = {'name': 'Minjin', 'age': 16}
print("Hello, {name}. I am {age}.".format(name = person['name'], age = person['age'])) # 딕셔너리 출력

print("Hello, {name}. I am {age}.".format(**person)) # **를 이용하여 해당 딕셔너리(person) 안의 key


# Python 3.6 : f를 앞에 붙이고 뒤에는 변수를 그대로 사용
print(f"Hello, {name}. I am {age}.")
print(F"Hello, {name}. I am {age}.")
print(f"{name.lower()} is cool")



