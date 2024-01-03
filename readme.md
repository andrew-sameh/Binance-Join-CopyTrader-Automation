# Binance Copy-Trading Automation Script

## Overview
This Python script automates the process of joining and managing copy-trading profiles on Binance. It is designed for users who wish to follow multiple traders and automatically join their trading strategies when slots become available. The script includes features such as custom investment settings per trader, sound notifications, and automatic joining based on predefined criteria.

## Tip
If you find the script to be useful and you managed to join your favourite traders. A tip would be highly appreciated.
**My Binance ID: 307397287**

## Features
- **Automated Joining**: Automatically joins trading profiles based on predefined settings.
- **Sound Notifications**: Alerts the user with a sound notification when a slot is available.
- **Custom Investment Settings**: Allows setting individual investment parameters for each trader.
- **Continuous Monitoring**: Runs in a loop, continuously checking for available slots.

## Requirements
- Python 3.x
- `simpleaudio` library
- Binance account

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries:
   ```bash
   pip install requests simpleaudio
   ```
3. Download the script to your local machine.

## Configuration
Before running the script, you need to configure the following:

- **API Headers**: Set your Binance API headers (`csrftoken`, `bncuuid`, `fvideoid`, `fvideotoken`, `cookie`) in the script.
- **Trader Profiles**: Add the required profiles to your Binance **Favorites list** and define the trader profiles you want to follow in `PROFILES_SETTINGS`. Include their `leadPortfolioId` and your desired investment settings.
- **Sound File**: Place a `.wav` sound file in the same directory as the script or update the `sound_file` variable with the path to your sound file.

## Trader Profile Settings
The script allows you to define custom settings for each trader you wish to follow. These settings are specified in the `PROFILES_SETTINGS` dictionary. Here's a breakdown of each setting:
- `leadPortfolioId`: The unique identifier of the trader's portfolio on Binance. This is a mandatory field.
- `investAmount`: The amount of capital you wish to allocate to copying this trader.
- `copyModel`: Determines how the copy trading will be executed. Options are `"FIXED_RATIO"` and `"FIXED_AMT"`. `"FIXED_RATIO"` maintains a fixed ratio of your funds to the trader's moves, while `"FIXED_AMT"` uses a fixed amount for each order.
- `costPerOrder`: Relevant only if `copyModel` is set to `"FIXED_AMT"`. It specifies the fixed amount per order.
- `investAsset`: The asset you are investing, typically `"USDT"`.
- `marginMode`: Can be `"FOLLOW_LEAD"`, `"CROSS"`, or `"ISOLATED"`, indicating the type of margin mode to be used.
- `leverageMode`: Can be `"FOLLOW_LEAD"` or `"FIX_LEVERAGE"`. `"FOLLOW_LEAD"` will mimic the trader's leverage, while `"FIX_LEVERAGE"` allows you to set a fixed leverage level.
- `totalStopLossRate`: An optional setting to specify the total stop loss rate.
- `leverageValue`: Required if `leverageMode` is `"FIX_LEVERAGE"`. It specifies the leverage level.
- `takeProfitRate`: An optional setting to specify the take profit rate.
- `stopLostRate`: An optional setting to specify the stop loss rate.
- `maxPositionPerSymbolRate`: An optional setting to limit the maximum position per symbol.

## Obtaining Headers via Inspect Network Tab
To run the script, you need to set your Binance API headers. Here's how to obtain them:
1. **Log in to Binance**: Open your web browser, go to the Binance website, and log into your account.
2. **Open Developer Tools**: Right-click on the webpage and select "Inspect" or use the keyboard shortcut (usually `F12` or `Ctrl+Shift+I` on Windows, `Cmd+Option+I` on Mac).
3. **Go to the Network Tab**: In the developer tools, navigate to the "Network" tab.
4. **Interact with the Site**: Perform an action related to copy-trading (like visiting the copy-trading page). This will generate network activity.
5. **Find the Relevant Request**: Look for a network request that corresponds to the copy-trading action. Click on it to view details.
6. **Copy Headers**: In the request details, find the "Headers" section. Here, you will see various headers like `csrftoken`, `bncuuid`, `fvideoid`, `fvideotoken`, and `cookie`.
7. **Update the Script**: Copy these header values and paste them into the corresponding variables in the script.
You can also copy the request as cURL and paste it somewhere to be able to copy all the `cookie` string

### Important Notes:
- The headers are tied to your session and may expire, requiring you to fetch new ones periodically.
- Be cautious with your headers and API keys. They provide access to your Binance account and should be kept secure.

## Usage
Run the script using Python:
```bash
python Binance_Join_CopyTrader_Automation.py
```
The script will start and continuously monitor for available slots in your favorite traders' profiles. When a slot is available, it will attempt to join using your predefined settings.

## Advanced Settings
You can customize the following advanced settings for each trader:
- `copyModel`: "FIXED_RATIO" or "FIXED_AMT"
- `marginMode`: "FOLLOW_LEAD", "CROSS", "ISOLATED"
- `leverageMode`: "FOLLOW_LEAD", "FIX_LEVERAGE"
- `totalStopLossRate`, `leverageValue`, `takeProfitRate`, `stopLostRate`, `maxPositionPerSymbolRate`: Various risk management and leverage settings.

## Disclaimer
This script is provided as-is without any guarantees or warranty. Automated trading involves significant risk. Use at your own risk.

## Contributing
The script is still in the testing phase, and contributions are welcome. If you have suggestions for improvements or bug fixes, please feel free to submit a pull request.
