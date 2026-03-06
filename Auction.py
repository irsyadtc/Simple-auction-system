"""

This program contains definition of four classes related to a simple auction system.
The classes include Auction, Lot, Bid, and Person.
 
"""

import time


class Auction:
    """A class that simulates an auction."""

    def __init__(self):
        """Create a new auction."""
        self.lots = list()  # The list of Lots in this auction.
        self.next_lot_number = 1  # The number given to the next lot added

    def enter_lot(self, description):
        """Enter a new lot into the auction."""
        self.lots.append(Lot(self.next_lot_number, description))
        self.next_lot_number += 1

    def display_lots(self):
        """Show the full list of lots in this auction."""
        print("\nList of all lots in the auction")
        print("-" * 40)
        for lot in self.lots:
            print(lot)
        print()

    def bid_for(self, lot_number, bidder, value):
        """# Bid for a lot.

        A message indicating whether the bid is successful or not is printed.
        """
        successful = False
        selected_lot = self.get_lot(lot_number)
        if selected_lot != None:
            bid = Bid(bidder, value)
            successful = selected_lot.bid_for(bid)
            #highest_bid = selected_lot.get_highest_bid()

            if successful:
                print("The bid for lot number", lot_number, "was successful.")
            else:
                #  Report which bid is higher.
                highest_bid = selected_lot.get_highest_bid()
                print(
                    "Lot number:",
                    lot_number,
                    "already has a bid of:",
                    highest_bid.get_value(),
                    "named: ",
                    highest_bid.get_bidder()
                )
        #else syntax is in get_lot()

        return successful

    # Return the lot with the given number. Return null
    # if a lot with this number does not exist.
    def get_lot(self, lot_number):
        if (lot_number >= 1) and (lot_number < self.next_lot_number):
            return self.lots[lot_number - 1]
        else:
            print("Lot number:", lot_number, "does not exist.")
            return None
        
    
    def load_items(self, file_path):
        """Read details of auction items from a text file and add them to the auction."""
        file= open(file_path, 'r')
        for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:  # Ensure correct format of each line
                        description, reserve_value, auction_duration = parts
                        reserve_value = int(reserve_value)
                        auction_duration = int(auction_duration)
                        self.enter_lot(description)
                        self.lots[-1].reserve_value = reserve_value
                        self.lots[-1].auction_duration = auction_duration
                    else:
                        print(f"Ignoring line: {line.strip()} (Invalid format)")
            

    def save_items(self, file_path):
        """Write details of each item in the list of lots to a text file."""
        
        file = open(file_path, 'w')
        for lot in self.lots:
                    file.write(f"{lot.description},{lot.reserve_value},{lot.auction_duration}\n")
        print("Items saved successfully to:", file_path)


class Lot:
    """A class to model an item in an auction."""

    def __init__(self, number, description,reserve_value=0,auction_duration=0):
        self.number = number  # A unique identifying number
        self.description = description  # A description of the lot
        self.highest_bid = None  # The current highest bid for this lot
        self.reserve_value = reserve_value
        self.auction_duration = auction_duration
        self.timestamp = time.time()

    def bid_for(self, bid):
        """Attempt to bid for this lot.

        A successful bid must have a value higher than any existing bid, and the remaining auction time
        must be greater than zero."""
        #set no time
        current_time=time.time()
        remaining_time= self.timestamp + self.auction_duration * 24*3600 - current_time
        
        # if (self.highest_bid == None) or (bid.get_value() > self.highest_bid.get_value()) and (remaining_time>0):
        if (self.highest_bid == None) or (bid.get_value() > self.highest_bid.get_value()):
           # This bid is the best so far, and there is still time remaining for the auction.
            self.highest_bid = bid
            return True
        else:
            return False
        
    def get_remaining_time(self):
        """Calculate and return the remaining time in the auction."""
        current_time = time.time()
        remaining_time = self.timestamp + self.auction_duration * 24 * 3600 - current_time
        return max(0, remaining_time)


    def __str__(self):
        # details = f"{self.number}: {self.description} (Reserve: {self.reserve_value}, Duration: {self.auction_duration} days)"
        details = f"{self.number}: {self.description} (Reserve: {self.reserve_value}, Duration: {self.auction_duration} days)"
        if self.highest_bid:
            details += f", Bid Value: {self.highest_bid.get_value()}, Bidder: {self.highest_bid.get_bidder()}"
        else:
            details += ", (No bid)"
        return details
    
    
    def get_reserve_value(self):
        """Return the reserve value of the lot."""
        return self.reserve_value

    def get_auction_duration(self):
        """Return the auction duration of the lot."""
        return self.auction_duration

    def get_timestamp(self):
        """Return the timestamp of the lot."""
        return self.timestamp

    def get_number(self):
        return self.number

    def get_description(self):
        return self.description

    def get_highest_bid(self):
        return self.highest_bid


class Bid:
    """A class that models an auction bid.

    It contains a reference to the Person bidding and the amount bid."""

    def __init__(self, bidder, value):
        self.bidder = bidder  # The person making the bid.
        self.value = value  # The value of the bid.

    def get_bidder(self):   #name
        return self.bidder

    def get_value(self):
        return self.value


class Person:
    """Maintains details of someone who participates in an auction."""

    def __init__(self, name):
        self.name = name  # The name of this person.

    def get_name(self):
        return self.name
