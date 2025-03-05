import streamlit as st
import math
from scipy import stats

def calculate_black_scholes(S, K, T, r, sigma):
    try:
        # Calculate d1 and d2
        d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        
        # Calculate call option price
        call_price = S * stats.norm.cdf(d1) - K * math.exp(-r * T) * stats.norm.cdf(d2)
        
        return call_price, d1, d2
    except Exception as e:
        return None, None, None, str(e)

def main():
    # Set page title and configuration
    st.set_page_config(page_title="Black-Scholes Calculator", page_icon="📈")
    
    # Title and description
    st.title("Black-Scholes Call Option Calculator")
    st.write("Enter the parameters below to calculate the call option price using the Black-Scholes model.")
    
    # Create input fields in the sidebar
    with st.sidebar:
        st.header("Input Parameters")
        S = st.number_input("Spot Price (S)", min_value=0.01, value=100.0, step=0.1)
        K = st.number_input("Strike Price (K)", min_value=0.01, value=95.0, step=0.1)
        T = st.number_input("Time to Expiration (years)", min_value=0.01, value=1.0, step=0.01)
        r = st.number_input("Risk-free Rate (decimal)", min_value=0.0, value=0.05, step=0.01)
        sigma = st.number_input("Volatility (decimal)", min_value=0.01, value=0.2, step=0.01)
    
    # Calculate button
    if st.button("Calculate"):
        call_price, d1, d2, error = calculate_black_scholes(S, K, T, r, sigma)
        
        # Display results
        st.subheader("Results")
        if call_price is not None:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Call Option Price", f"${call_price:.2f}")
                st.write(f"d1: {d1:.4f}")
            with col2:
                st.write(f"d2: {d2:.4f}")
            
            # Display input parameters used
            with st.expander("Input Parameters Used"):
                st.write(f"Spot Price (S): {S}")
                st.write(f"Strike Price (K): {K}")
                st.write(f"Time to Expiration (T): {T} years")
                st.write(f"Risk-free Rate (r): {r}")
                st.write(f"Volatility (σ): {sigma}")
        else:
            st.error(f"Error in calculation: {error}")
    
    # Add some information about Black-Scholes
    with st.expander("About Black-Scholes Model"):
        st.write("""
        The Black-Scholes model is a mathematical model for pricing options contracts.
        The formula used is:
        C = S * N(d1) - K * e^(-rT) * N(d2)
        
        Where:
        - C = Call option price
        - S = Spot price
        - K = Strike price
        - T = Time to expiration
        - r = Risk-free rate
        - σ = Volatility
        - N() = Cumulative distribution function of standard normal distribution
        - d1 = [ln(S/K) + (r + σ²/2)T] / (σ√T)
        - d2 = d1 - σ√T
        """)

if __name__ == "__main__":
    main()
