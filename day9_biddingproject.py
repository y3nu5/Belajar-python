print("================= Day 9: Bidding Project =================")

bids ={}


bidding_finished = False

while not bidding_finished:
    nama_lengkap = str(input("What is your name?: "))
    harga_tawaran = int(input("What is your bid?: $"))
    bids[nama_lengkap] = harga_tawaran
    
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    
    if more_bidders == "no":
        max_bid = max(bids.values())
        for nama, bid_value in bids.items():
            if bid_value == max_bid:
                print(f"The winner is {nama} with a bid of ${max_bid}")
        bidding_finished = True
    else:
        print("\n" * 100)
        bidding_finished = False
