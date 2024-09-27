# Reddit Account Creator

## Overview
The **Reddit Account Creator** is a Python script designed to automate the creation of Reddit accounts using specified proxies. This tool can help you create multiple accounts quickly and efficiently.

## Prerequisites
Before you can use the script, ensure you have the following:

1. **Python**: Make sure Python (version 3.10 or higher) is installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).
2. **API Key**: Sign up at [ReddAPI](https://rapidapi.com/SeasonedCode/api/reddapi) and get your API key.

## Getting Started

### Step 1: Clone or Download the Repository
1. Clone the repository or download it as a ZIP file and extract it to your desired location on your computer.

### Step 2: Install Required Packages
1. Open a terminal or command prompt.
2. Navigate to the folder where you extracted the files.
3. Run the following command to install the necessary packages:

   ```bash
   pip install -r requirements.txt
   ``` 
### Step 3: Configure config.ini
1. Open the config.ini file in a text editor.
2. Update the API_KEY with the API key you obtained One.

### Step 4: Prepare Your Proxies
1. List your proxies in the ""proxies.txt file, one per line. For example:
   ```bash
    proxy1:port or username@password:ip:port
    proxy2:port or username@password:ip:port
    proxy3:port or username@password:ip:port
   ```
### Step 5: Run the Script
To create accounts, run the following command in your terminal or command prompt:
   ```bash
    python main.py <account_number>
   ```
Replace <account_number> with the number of accounts you wish to create. For example, to create 5 accounts, use:
   ```bash
    python main.py 5
   ```
## Output
- The account information (username, email, and password) will be saved in the accounts.txt file.
- Any errors or logs will be displayed in the terminal.

## Notes
- Ensure you have valid proxies in the proxies.txt file; otherwise, the account creation may fail.
- Be aware of Reddit's terms of service regarding account creation and usage. This script should be used responsibly.

## Troubleshooting
- If you encounter issues, ensure your API key is valid and that your proxies are working correctly.
- Check the logs for any error messages that may provide clues about what went wrong.
----

#### For Support Joing our telegram group at: https://t.me/reddapi_support
