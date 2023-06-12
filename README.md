Discord Bot with Patch Notes Update

This is a Discord bot written in Python using the discord library. The bot scrapes the War Thunder website for the latest patch notes and sends them to a Discord channel. It also includes a command to manually send the patch notes.
Prerequisites

Before running the bot, make sure you have the following prerequisites installed:

    Python 3.x
    discord library (pip install discord.py)
    bs4 library (pip install beautifulsoup4)

Getting Started

To get started with the bot, follow these steps:

    Clone the repository or download the code:
        git clone <repository_url>

    Install the required dependencies:

        pip install -r requirements.txt

    Replace the placeholders in the code:

    Replace BOT_ID with your Discord bot token. You can obtain a bot token by creating a new bot in the Discord Developer Portal.

    Replace CHANNEL_ID with the ID of the channel where you want to send the patch notes. You can get the channel ID by enabling Developer      Mode in your Discord client and right-clicking on the desired channel, then selecting "Copy ID".

Run the bot:



    python bot.py

Features
Automatic Patch Notes Update

The bot includes a task check_for_patch_notes() that runs every hour to check for new patch notes on the War Thunder website. If there are new patch notes available, it updates the last_patch_notes.txt file with the new patch notes and sends them as a message to the specified Discord channel.
Manual Patch Notes Update

You can manually trigger the patch notes update by using the !patch_notes command. The bot reads the contents of the last_patch_notes.txt file and sends them as a message to the channel where the command was executed.
Test Command

The bot also includes a !test command that sends a test message to the specified channel. This command can be used to verify if the bot is functioning correctly.
Contributing

If you'd like to contribute to this project, feel free to submit a pull request. Any contributions are welcome!
License

This project is licensed under the MIT License. Feel free to use and modify the code according to your needs.
Acknowledgments

    Discord.py Documentation
    Beautiful Soup Documentation
