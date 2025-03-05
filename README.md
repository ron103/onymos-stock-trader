# Stock Trading Engine Simulation

Python simulation built for the Onymos coding challenge. It mimics a live trading environment by managing an order book for 1024 tickers, matching buy and sell orders, and using threads to simulate real-time market activity.

## What It Does

- **Order Book Management:**  
  Maintains an order book where each ticker (e.g., "TICKER5") has two lists—one for buy orders and one for sell orders (orders are represented as `[quantity, price]`).

- **Order Matching:**  
  The `matchOrder` function scans for the best match: it finds the lowest sell order and checks if any buy order meets or exceeds that price, then executes a trade for the minimum available quantity.

- **Concurrency:**  
  Uses multiple threads to:
  - **Generate Orders:** Randomly create buy/sell orders.
  - **Match Orders:** Continuously check for and execute matching orders.

## Key Functions

- **`ticker_index(ticker)`:**  
  Converts a ticker string (like "TICKER5") into its corresponding index in the order book.

- **`addOrder(order_type, ticker, quantity, price)`:**  
  Adds a buy or sell order to the proper list in the order book.

- **`matchOrder(ticker)`:**  
  Finds and processes matching orders for a given ticker.

- **`order_generator()` & `order_matcher()`:**  
  Run in separate threads to simulate ongoing order placement and matching.

## How to Run

1. **Clone the Repository & Navigate:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>

2.	Run the Simulation:

python stock-trader.py

The simulation runs for 5 seconds, with executed trades printed to the console.

Rohan Waghmare
Email: rwaghmare@binghamton.edu
Portfolio: http://rohanwaghmare.com/

