import os
import sys


def clear_screen():
    # Clear screen for macOS/Linux
    os.system('clear')


def read_positive_int(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Please enter a positive whole number.")


def read_nonempty_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return " ".join(text.split())
        print("Input cannot be empty.")


def find_highest_bid(bids):
    if not bids:
        return 0, []
    highest_bid = max(bids.values())
    winners = [name for name, amount in bids.items() if amount == highest_bid]
    return highest_bid, winners


def main():
    print("Welcome to the Secret/Blind Auction Program!")
    bids = {}

    while True:
        name = read_nonempty_text("What is your name?: ")
        bid = read_positive_int("What is your bid?: ₹")

        # Keep highest bid per bidder
        if name in bids:
            bids[name] = max(bids[name], bid)
        else:
            bids[name] = bid

        more_bidders = input("Are there any other bidders? (yes/no): ").strip().lower()
        while more_bidders not in ("yes", "no", "y", "n"):
            more_bidders = input("Please type 'yes' or 'no': ").strip().lower()

        if more_bidders in ("yes", "y"):
            clear_screen()
        else:
            break

    highest_bid, winners = find_highest_bid(bids)
    if not winners:
        print("No valid bids were placed.")
        sys.exit()

    if len(winners) == 1:
        print(f"The winner is {winners[0]} with a bid of ₹{highest_bid}.")
    else:
        print(f"Tie detected! Winners: {', '.join(winners)} with a bid of ₹{highest_bid} each.")


if __name__ == "__main__":
    main()
