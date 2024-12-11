# **BanOnExit Telegram Bot** 🚀

Welcome to **BanOnExit** – the Telegram bot that automatically bans users who join your group or channel and leave shortly after! Perfect for combating spam, trolls, and malicious users, this bot is **lightweight**, **fully configurable**, and deployable on platforms like **Koyeb**, **Heroku**, or **Render**.

---

## **Why BanOnExit?**

Have you experienced users joining your Telegram groups or channels, spamming, trolling, or simply leaving minutes later? **BanOnExit** eliminates these problems by banning users who leave within a specified time threshold. Tailor the settings, and let the bot manage your chat's safety effortlessly.

---

## **Key Features** 🎯

- 🚫 **Auto-Ban System**: Automatically bans users who leave shortly after joining (configurable time threshold).
- ⚙️ **Customizable Settings**: Adjust bot behavior using environment variables to fit your specific needs.
- 🧑‍🤝‍🧑 **Group and Channel Support**: Compatible with both Telegram group chats and channels.
- 🚀 **Simple Deployment**: Easily set up on popular platforms like **Koyeb**, **Heroku**, **Render**, or any python-compatible environment.
- 🔄 **Always-On Functionality**: Configurable ping intervals ensure the bot stays alive and operational.

---

Keep your Telegram groups and channels secure with **BanOnExit Bot**! 💪

## Easy Installation 🛠️

Ready to get started? Here’s how to deploy **BanOnExit** in no time!

### 1. Clone the Repository

Clone the **BanOnExit** repo to your local machine or VPS:

```sh
git clone https://github.com/BotMaven/BanOnExit
cd BanOnExit
```

### 2. Set Up a Python Virtual Environment

Create a virtual environment to manage dependencies:

```sh
python3 -m venv ./venv
. ./venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies using pip:

```sh
pip3 install -r requirements.txt
```

### 4. Run the Bot Locally

Start the bot by running the following command:

```sh
python3 -m BanOnExit
```

The bot will now monitor your configured chats and auto-ban users who leave too quickly.

## Configuration ⚙️

The bot is configured through environment variables for flexibility. You can either set them in your system or use a `.env` file.

Here’s a list of configurable options:

```python
API_ID = 123456  # Your Telegram API ID from https://my.telegram.org/auth
API_HASH = "qwertyuiolkjhgfdsazxcvbnm"  # Your Telegram API Hash from https://my.telegram.org/auth
BOT_TOKEN = "8069236538:qwertyuiolbv...."  # Your bot token from BotFather
PING_INTERVAL = 300  # 5-minute ping interval to keep the bot alive on services like Render/Heroku
URL = "https://deployment.example.com"  # Your deployed bot URL
CHATS = "-1002289906416,-1002486513383"  # Comma-separated list of chat IDs (supergroups or channels)
OWNER_ID = 6646387248  # Your Telegram user ID
KEEP_ALIVE = True  # Whether the bot should stay alive continuously
BAN_THRESHOLD = 60  # Time threshold (in seconds) for banning users who join and leave quickly
```

To load environment variables from a `.env` file, use `python-dotenv`:

```sh
pip3 install python-dotenv
```

Then, create a `.env` file and add your configuration settings.

## Starting the Bot 🚀

Once your environment variables are configured, you can start the bot either locally or on a VPS.

### Start Locally:

```sh
python3 -m BanOnExit
```

### On a VPS with `tmux` (recommended):

```sh
sudo apt install tmux -y  # Install tmux
tmux  # Start a new tmux session
python3 -m BanOnExit  # Run the bot in the tmux session
```

The bot will run continuously in the background, even if you disconnect.

## **Developer Information** 👨‍💻

This bot was developed by **[BotMaven](https://t.me/BotMaven)**

Feel free to reach out with suggestions, feature requests, or bug reports! 🚀

## License 📝

This bot is open-source and licensed under the **MIT License**. Feel free to use, modify, and distribute it, as long as you retain the copyright and license notice.
