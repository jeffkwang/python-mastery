# pcost.py

with open("Data/portfolio.dat", mode="r") as file:
    line = file.readline()
    cost = 0.0  # initialize total cost of the stock portfolio
    while line:
        stock_data = line.split(" ")
        number_of_shares = int(stock_data[1])
        price_per_share = float(stock_data[2])
        cost += price_per_share * number_of_shares
        line = file.readline()

print(cost)
