"""
This program implements a simple auction system using four classes provided in the Auction.py.
It loads and saves a list of items in an auction.
It provided a simple menu to add items to an auction, and to bid for them.

"""
from Auction import Auction

def print_menu():
    """Prints the menu options."""
    print("\nMenu:")
    print("1. Insert item")
    print("2. List items in the auction")
    print("3. Bid for an item")
    print("4. View highest bid for a lot") # Additional functionality
    print("5. Exit")

def main():
    """Main function to run the auction system."""
    # Create an Auction object
    auction = Auction()

    # Load a list of items from a text file
    auction.load_items("items.txt")

    # Loop for user interaction
    while True:
        print_menu()  # Print menu options

        choice = input("Enter your choice: ")  # Get user choice

        if choice == '1':
            # Insert item
            description = input("Enter item description: ")
            auction.enter_lot(description)
            print("Item inserted into the auction.")

        elif choice == '2':
            # List items in the auction
            auction.display_lots()

        elif choice == '3':
            # Bid for an item
            lot_number = int(input("Enter lot number to bid for: "))
            bidder = input("Enter bidder name: ")
            value = int(input("Enter bid value: "))
            auction.bid_for(lot_number, bidder, value)
            
        elif choice == '4':
            # Additional functionality for this program
            # Allows you to view highest bid for a lot
            lot_number = int(input("Enter lot number to view highest bid: "))
            lot = auction.get_lot(lot_number)
            if lot:
                highest_bid = lot.get_highest_bid()
                if highest_bid:
                    print(f"Highest bid for lot {lot_number}: {highest_bid.get_value()} by {highest_bid.get_bidder()}")
                else:
                    print(f"No bids for lot {lot_number}.")
            else:
                print("Invalid lot number.")

        elif choice == '5':
            # Exit and saves details
            auction.save_items("items.txt")
            print("Items saved to file. Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

