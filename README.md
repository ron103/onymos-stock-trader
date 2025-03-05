# Stock Trading Engine Simulation

This project is a simple simulation of a real-time stock trading engine implemented in Python. It demonstrates the basics of order book management, order matching, and concurrent processing using multiple threads.

## Overview

- **Order Book Management:**  
  The simulation maintains an order book for 1024 different tickers. Each ticker has two lists—one for buy orders and one for sell orders. Orders are stored as `[quantity, price]`.

- **Order Matching:**  
  The engine continuously checks for matching orders by comparing buy orders against the lowest sell orders. A trade is executed when a buy order's price meets or exceeds the lowest sell price.

- **Concurrency:**  
  The simulation uses multithreading to mimic a live market environment:
  - **Order Generators:** Threads that randomly generate buy or sell orders for random tickers.
  - **Order Matchers:** Threads that continuously check and match orders based on the defined criteria.

## Features

- **Scalable Order Book:** Supports up to 1024 ticker symbols.
- **Real-Time Simulation:** Constant order generation and matching create a dynamic trading simulation.
- **Multithreaded Processing:** Utilizes Python's threading to simulate concurrent market activity.
- **Simple, Extensible Design:** The code is structured for clarity and can be expanded for more complex simulations.

## Code Structure

- **`ticker_index(ticker)`**  
  Converts a ticker string (e.g., "TICKER5") to its corresponding index in the order book.

- **`addOrder(order_type, ticker, quantity, price)`**  
  Adds a new buy or sell order to the appropriate ticker's order book.

- **`matchOrder(ticker)`**  
  Checks the order book for a given ticker and matches buy orders with sell orders if the buy price is greater than or equal to the lowest sell price. Executes a trade for the minimum available quantity and updates the order book.

- **`order_generator()`**  
  Continuously generates random orders (both buy and sell) for random tickers, simulating real market activity.

- **`order_matcher()`**  
  Continuously attempts to match orders for randomly selected tickers, ensuring trades are executed when conditions are met.

- **`main_simulation()`**  
  Launches multiple threads for order generation and matching, running the simulation for a set period.

## Getting Started

### Requirements

- Python 3.x
- Standard libraries: `threading`, `random`, `time`

### Running the Simulation

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>

2.	Run the Simulation:

python stock-trader.py

The simulation will run for 5 seconds, generating and matching orders, with trade details printed to the console.


Author

Rohan Waghmare
Email: rwaghmare@binghamton.edu
Portfolio: http://rohanwaghmare.com/

