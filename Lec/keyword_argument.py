def travel_to_country(country: str, name: str):
  print(f"Hello {name}!")
  print(f"You are going to travel to {country}")
  print("Are you excited?")

# Positional Argument
travel_to_country("USA", "Joon")

# Keyword Argument
travel_to_country(name="Joon", country="USA")