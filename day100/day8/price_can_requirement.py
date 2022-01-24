print(
"""
  _    _        _        _              _          
 | |  | |_ ___ | |_ __ _| |  _ __  _ __(_) ___ ___ 
/ __) | __/ _ \| __/ _` | | | '_ \| '__| |/ __/ _ \
\__ \ | || (_) | || (_| | | | |_) | |  | | (_|  __/
(   /  \__\___/ \__\__,_|_| | .__/|_|  |_|\___\___|
 |_|                        |_|                    

""")
def total_price(price,quantity):
    total = price*quantity
    print(total)
object = input("what do want to calculate: ")
price_of_a_object = int(input(f"what is the price of a single {object}: "))
how_much = int(input(f"how many {object} you want to buy: "))

print(total_price(price_of_a_object,how_much))
