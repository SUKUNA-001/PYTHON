cost_price = int(input("enter the cost price:"))
sell_price = int(input("enter the sell price:"))

# if sp is more than cp
if cost_price < sell_price:
    profit = sell_price - cost_price
    print("we have made profit:", profit)
 

else: sell_price < cost_price
loss = cost_price - sell_price
print("we are in loss")