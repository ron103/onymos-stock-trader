# Rohan Waghmare
# Email: rwaghmare@binghamton.edu
# Portfolio: http://rohanwaghmare.com/


import threading
import random
import time

# Create a global order book array for 1024 tickers.
# Each index holds two lists: one for buy orders and one for sell orders.
# Each order is represented as a list: [quantity, price]
order_book = [[[], []] for _ in range(1024)]

# Helper: Convert a ticker string "TICKER<num>" to its integer index.
def ticker_index(ticker):
    # Expecting ticker strings like "TICKER5", "TICKER123"
    try:
        num = int(ticker[6:])
        if 0 <= num < 1024:
            return num
    except:
        pass
    return None

# addOrder: Adds an order (Buy or Sell) into the order book.
def addOrder(order_type, ticker, quantity, price):
    idx = ticker_index(ticker)
    if idx is None:
        return  # invalid ticker; do nothing
    # Buy orders go to index 0, Sell orders to index 1.
    if order_type.lower() == "buy":
        order_book[idx][0].append([quantity, price])
    elif order_type.lower() == "sell":
        order_book[idx][1].append([quantity, price])
    # Otherwise, ignore unknown order types.

# matchOrder: For a given ticker, checks if any buy order can match the lowest priced sell order.
# If found, a trade is executed for the minimum available quantity.
# This function runs in O(n) relative to the number of orders in that ticker’s book.
def matchOrder(ticker):
    idx = ticker_index(ticker)
    if idx is None:
        return
    buy_orders = order_book[idx][0]
    sell_orders = order_book[idx][1]
    if not buy_orders or not sell_orders:
        return  # No match possible if one side is empty

    # Find the sell order with the minimum price.
    min_sell_price = None
    min_sell_pos = -1
    for pos, order in enumerate(sell_orders):
        # order[1] is the sell price.
        if min_sell_price is None or order[1] < min_sell_price:
            min_sell_price = order[1]
            min_sell_pos = pos

    # Check if any buy order meets or exceeds the minimum sell price.
    for pos, b_order in enumerate(buy_orders):
        if b_order[1] >= min_sell_price:
            # Execute a trade for the lesser of the two order quantities.
            trade_qty = b_order[0] if b_order[0] < sell_orders[min_sell_pos][0] else sell_orders[min_sell_pos][0]
            print("Trade on {}: {} shares at ${}".format(ticker, trade_qty, min_sell_price))
            # Deduct traded quantity from both orders.
            b_order[0] -= trade_qty
            sell_orders[min_sell_pos][0] -= trade_qty
            # Remove orders that are fully executed.
            order_book[idx][0] = [o for o in buy_orders if o[0] > 0]
            order_book[idx][1] = [o for o in sell_orders if o[0] > 0]
            return  # Only one trade per matchOrder call

# Simulation wrapper for generating random orders.
def order_generator():
    types = ["buy", "sell"]
    while True:
        # Generate a random ticker among 1024 (e.g., "TICKER0" to "TICKER1023")
        ticker = "TICKER" + str(random.randint(0, 1023))
        otype = random.choice(types)
        qty = random.randint(1, 100)      # Quantity between 1 and 100
        prc = random.randint(10, 1000)      # Price between 10 and 1000
        addOrder(otype, ticker, qty, prc)
        time.sleep(0.01)  # Small pause to simulate realistic order frequency

# Simulation wrapper for continuously matching orders.
def order_matcher():
    while True:
        # Randomly select a ticker to attempt matching orders.
        ticker = "TICKER" + str(random.randint(0, 1023))
        matchOrder(ticker)
        time.sleep(0.01)

# Main simulation: Launch threads to simulate active market activity.
def main_simulation():
    threads = []
    # Start threads that add orders.
    for _ in range(5):
        t = threading.Thread(target=order_generator)
        t.daemon = True
        t.start()
        threads.append(t)
    # Start threads that match orders.
    for _ in range(2):
        t = threading.Thread(target=order_matcher)
        t.daemon = True
        t.start()
        threads.append(t)
    # Let the simulation run for a while.
    time.sleep(5)

if __name__ == "__main__":
    main_simulation()