# Uniswap Arbitrum Trading Bot

This repository contains a Python-based trading bot that interacts with the Uniswap liquidity pools on the Arbitrum network. The bot enables the automated buying and selling of tokens, leveraging the liquidity of Uniswap to execute trades efficiently. It features a flexible slippage tolerance, deadline management, and a simple way to track liquidity pool information.
Features

    Buy tokens from Uniswap liquidity pools on the Arbitrum network.
    Sell tokens back to the pool with customizable slippage tolerance.
    Fetch liquidity pool information including pool address, available liquidity, and token price.
    Simple API integration with Uniswap's trading functionality.
    Customizable parameters such as private key, transaction amount, slippage, and recipient address.

https://medium.com/@landonscott03/how-to-buy-tokens-via-uniswap-on-arbitrum-using-api-7e346beccc46

Prerequisites

    Python 3.7 or later.
    requests library for making HTTP requests.

To install the required dependencies, run:

pip install requests

Setup
1. Configuration

Before running the bot, make sure to update the following parameters in the script:

    PRIVATE_KEY: Your private key (in BASE58 format) to authorize transactions.
    TOKEN_IN: The token you wish to send (e.g., WETH, ETH).
    TOKEN_OUT: The token you want to buy or sell.
    AMOUNT_IN: The amount of the token to swap (e.g., 0.1 ETH).
    SLIPPAGE: The acceptable slippage percentage (e.g., 1% or 10%).
    RECIPIENT: The address where the purchased/sold tokens will be sent.

Example configuration:

PRIVATE_KEY = '<PRIVATE_KEY>'
TOKEN_IN = '<WETH_ADDRESS>'
TOKEN_OUT = '<TOKEN_MINT_ADDRESS>'
AMOUNT_IN = 0.1
SLIPPAGE = 1
DEADLINE = int(time.time()) + 60 * 20  # 20 minutes from the current time
RECIPIENT = '<RECIPIENT_ADDRESS>'

2. API Endpoints

The bot interacts with the following Uniswap API endpoints:

    Buy Tokens: https://arbitrum-api.co/api/uniswap/buy
    Sell Tokens: https://arbitrum-api.co/api/uniswap/sell
    Get Pool Info: https://arbitrum-api.co/api/uniswap/pool/info/

Main Functions

    buy_tokens(): Sends a POST request to Uniswap’s buy API to purchase tokens from liquidity pools.
    sell_tokens(): Sends a POST request to Uniswap’s sell API to sell tokens back to liquidity pools.
    fetch_pool_info(token_address): Fetches detailed information about the liquidity pool for a given token address.

Example Usage

    Update the configuration with your details.
    Run the script using:

python uniswap_arbitrum_trading_bot.py

The bot will:

    Fetch the current liquidity pool information.
    Execute a buy or sell order based on your configuration.
    Print the transaction status and transaction ID.

Example Responses
Successful Response (Buy or Sell)

{
  "status": "success",
  "txid": "0x3d97fd5f5c24990b395f6a6b989bfb4d5fd0c3b9c620b687e3203d0fda05939d"
}

Error Response (Insufficient Liquidity)

{
  "status": "failed",
  "message": "Transaction failed",
  "error": "Insufficient liquidity in the pool"
}
