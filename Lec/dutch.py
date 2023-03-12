num_of_ppl = 3
food_prices = [10, 20, 15, 17, 50]

def going_dutch(prices, num_ppl):
  total_prices = sum(prices)
  print(f"Your total is {total_prices}")
  return round(total_prices / num_ppl, 3)

print(going_dutch(prices = food_prices, num_ppl = num_of_ppl))