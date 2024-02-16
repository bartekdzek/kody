
import os
bids = {}
others = "yes"
while others == "yes":
    name = input("name: ")
    bid = input("bid: ")
    bid = int(bid)
    others = input("Are there any other bidders? Type yes or no.")
    bids[name] = bid
    os.system('cls') #to clear the console

def search_for_bid():
    max = 0
    namexd = ""
    for name in bids:
        if max < bids[name]:
            max = bids[name]
            namexd = name
    print(bids)
    print(f"The max bid is {max}$ - {namexd}")

  
search_for_bid()

