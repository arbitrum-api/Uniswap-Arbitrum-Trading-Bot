import requests
import time

# Configuration
PRIVATE_KEY = '<PRIVATE_KEY>'  # Your private key in BASE58 format
TOKEN_IN = '<WETH_ADDRESS>'  # The token you are sending (e.g., WETH or ETH)
TOKEN_OUT = '<TOKEN_MINT_ADDRESS>'  # The token you want to buy or sell
AMOUNT_IN = 0.1  # Amount in ETH or WETH
SLIPPAGE = 1  # Slippage tolerance (1% or 10%)
DEADLINE = int(time.time()) + 60 * 20  # 20 minutes from current time
RECIPIENT = '<RECIPIENT_ADDRESS>'  # The address where the purchased tokens will be sent

# API Endpoints
BUY_API_URL = 'https://arbitrum-api.co/api/uniswap/buy'
SELL_API_URL = 'https://arbitrum-api.co/api/uniswap/sell'
POOL_API_URL = 'https://arbitrum-api.co/api/uniswap/pool/info/'

# Function to buy tokens from Uniswap
def buy_tokens():
    try:
        response = requests.post(BUY_API_URL, json={
            'private_key': PRIVATE_KEY,
            'token_in': TOKEN_IN,
            'token_out': TOKEN_OUT,
            'amount_in': AMOUNT_IN,
            'slippage': SLIPPAGE,
            'deadline': DEADLINE,
            'recipient': RECIPIENT
        })

        response_data = response.json()
        if response_data['status'] == 'success':
            print(f"Transaction successful: {response_data['txid']}")
        else:
            print(f"Transaction failed: {response_data['message']}, Error: {response_data['error']}")
    except Exception as e:
        print(f"Error during token purchase: {str(e)}")

# Function to sell tokens on Uniswap
def sell_tokens():
    try:
        response = requests.post(SELL_API_URL, json={
            'private_key': PRIVATE_KEY,
            'token_in': TOKEN_OUT,  # You are selling the TOKEN_OUT
            'token_out': TOKEN_IN,  # You want to receive WETH or ETH
            'amount_in': AMOUNT_IN,
            'slippage': SLIPPAGE,
            'deadline': DEADLINE,
            'recipient': RECIPIENT
        })

        response_data = response.json()
        if response_data['status'] == 'success':
            print(f"Transaction successful: {response_data['txid']}")
        else:
            print(f"Transaction failed: {response_data['message']}, Error: {response_data['error']}")
    except Exception as e:
        print(f"Error during token sale: {str(e)}")

# Function to fetch pool information for a specific token
def fetch_pool_info(token_address):
    try:
        response = requests.get(f"{POOL_API_URL}{token_address}")
        response_data = response.json()
        if response_data['status'] == 'success':
            print(f"Pool Info: {response_data['pool_data']}")
        else:
            print(f"Error fetching pool info: {response_data['message']}")
    except Exception as e:
        print(f"Error during pool info fetch: {str(e)}")

# Main execution
def main():
    # Fetch pool info
    fetch_pool_info(TOKEN_IN)

    # Execute buy or sell based on the strategy (example: buying tokens)
    buy_tokens()  # or call sell_tokens() if you want to sell tokens

# Run the bot
if __name__ == '__main__':
    main()

