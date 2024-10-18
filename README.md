# Twitter Complaint Bot

## Overview

The Twitter Complaint Bot is an automated tool designed to monitor internet speed and tweet complaints to your internet service provider if the speed falls below a specified threshold. The bot uses Selenium to interact with web pages and the Twitter API to post tweets.

## Features

- **Internet Speed Monitoring**: Uses Speedtest.net to measure download and upload speeds.
- **VPN Activation**: Activates Browsec VPN extension.
- **Automated Tweeting**: Logs into Twitter and posts a complaint tweet if the internet speed is below the promised rate.

## Technologies Used

- **Python**: Main programming language.
- **Selenium**: For web automation.
- **ChromeDriver**: To control Chrome browser.
- **dotenv**: For managing environment variables.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/Twitter-Complaint-Bot.git
    cd Twitter-Complaint-Bot
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```dotenv
    TWITTER_USERNAME="your_twitter_username"
    TWITTER_EMAIL="your_twitter_email"
    TWITTER_PASSWORD="your_twitter_password"
    ```

4. **Run the bot**:
    ```sh
    python run.py
    ```

## Usage

- **Internet Speed Test**: The bot will automatically test your internet speed.
- **VPN Activation**: The bot will activate the Browsec VPN extension.
- **Tweeting**: If the internet speed is below the promised rate, the bot will log into Twitter and post a complaint tweet.

## File Structure

- `run.py`: Main script to run the bot.
- `scripts/net_speed_complain.py`: Contains the `InternetSpeedTwitterBot` class.
- `scripts/constants.py`: Contains constants and environment variable loading.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.