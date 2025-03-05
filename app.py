import math
from scipy import stats

def black_scholes_call():
    print("Black-Scholes Call Option Price Calculator")
    print("Please enter the following values one at a time:")
    
    # Get user inputs
    S = float(input("Spot Price of the underlying asset (S): "))
    K = float(input("Strike Price of the option (K): "))
    T = float(input("Time to expiration in years (T): "))
    r = float(input("Risk-free interest rate (r) as decimal (e.g., 0.05 for 5%): "))
    sigma = float(input("Volatility (σ) as decimal (e.g., 0.2 for 20%): "))
    
    # Calculate d1 and d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    # Calculate call option price
    call_price = S * stats.norm.cdf(d1) - K * math.exp(-r * T) * stats.norm.cdf(d2)
    
    # Display results
    print("\nResults:")
    print(f"d1: {d1:.4f}")
    print(f"d2: {d2:.4f}")
    print(f"Call Option Price: Rs:{call_price:.2f}")
    
    return call_price

def main():
    try:
        call_price = black_scholes_call()
    except ValueError:
        print("Error: Please enter valid numerical values")
    except ZeroDivisionError:
        print("Error: Time to expiration and volatility must be greater than 0")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    # Ask if user wants to calculate another option
    while True:
        again = input("\nWould you like to calculate another option? (yes/no): ").lower()
        if again == 'yes':
            print("\n" + "-"*50 + "\n")
            try:
                call_price = black_scholes_call()
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        elif again == 'no':
            print("Thank you for using the calculator!")
            break
        else:
            print("Please enter 'yes' or 'no'")

if __name__ == "__main__":
    main()
