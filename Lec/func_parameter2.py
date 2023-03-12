def get_name(first_name: str = "No first name", last_name: str = "No last name"):
  return f"{first_name}, {last_name}"

return_value = get_name(
  first_name = input("Your first name?"),
  last_name = input("Your last name?")
)

return_value2 = get_name()

print(return_value)
print(return_value2)