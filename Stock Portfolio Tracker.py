import yfinance as yf

# Portfolio structure
portfolio = {}

def add_stock(symbol, shares, buy_price):
    symbol = symbol.upper()
    portfolio[symbol] = {
        'shares': shares,
        'buy_price': buy_price
    }
    print(f"✅ Added {shares} shares of {symbol} at ${buy_price}.")

def remove_stock(symbol):
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"🗑️ Removed {symbol} from portfolio.")
    else:
        print(f"⚠️ Stock {symbol} not found in portfolio.")

def get_current_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        return stock.info['regularMarketPrice']
    except:
        return None

def show_portfolio():
    total_value = 0
    total_cost = 0
    print("\n📈 Your Portfolio:\n")
    print(f"{'Symbol':<8} {'Shares':<8} {'Buy Price':<12} {'Current Price':<15} {'P/L ($)':<10}")
    print("-" * 60)
    
    for symbol, data in portfolio.items():
        current_price = get_current_price(symbol)
        if current_price is None:
            print(f"{symbol:<8} {'-':<8} {'-':<12} {'Error':<15} {'-':<10}")
            continue
        shares = data['shares']
        buy_price = data['buy_price']
        market_value = current_price * shares
        cost = buy_price * shares
        profit = market_value - cost
        total_value += market_value
        total_cost += cost

        print(f"{symbol:<8} {shares:<8} ${buy_price:<11.2f} ${current_price:<14.2f} ${profit:<10.2f}")

    print("-" * 60)
    print(f"💼 Total Portfolio Value: ${total_value:.2f}")
    print(f"📉 Total Investment Cost: ${total_cost:.2f}")
    print(f"📊 Net Profit/Loss: ${total_value - total_cost:.2f}\n")

# Example interaction loop
def main():
    print("📊 Welcome to the Stock Portfolio Tracker")
    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            buy_price = float(input("Enter buy price: "))
            add_stock(symbol, shares, buy_price)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ")
            remove_stock(symbol)
        elif choice == '3':
            show_portfolio()
        elif choice == '4':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == '__main__':
    main()