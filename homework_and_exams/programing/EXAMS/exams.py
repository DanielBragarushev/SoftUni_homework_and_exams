import math

one_tenis_raketa = float(input())
number_tenis_raketa = int(input())
shoes_number = int(input())

price_tenis_raketa = one_tenis_raketa * number_tenis_raketa
shoes_price = one_tenis_raketa / 6
all_shoes_price = shoes_price * shoes_number
left_equipment = (price_tenis_raketa + all_shoes_price) * 0.2
total = price_tenis_raketa + all_shoes_price + left_equipment
price_djokovic = math.floor(total / 8)
sponsor_price = math.ceil((total * 7) / 8)

print(f"Price to be paid by Djokovic {price_djokovic}")
print(f"Price to be paid by sponsors {sponsor_price}")