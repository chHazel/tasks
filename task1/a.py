
open_price=43.96875  
close_price=44.25000
a = [(43.96875, 44.25000), (44.21875, 44.34375), (44.40625, 44.81250)]
quantity = 0
i=0
found = 100000
for open_price, close_price in a:
        # open_price = row["Open"]
        # close_price = row["Close"]


        # if i == 0:
        #     quantity = found // close_price
        #     found = found % close_price

        # elif i == len(a)-1: 
        #     found += open_price * quantity
        # else:
        #     found += quantity * open_price
        #     quantity = found // close_price
        #     found = found % close_price
        # i+=1
        # print(found)
        quantity = found // open_price
        found = found % open_price
        found += close_price * quantity
        print(found)