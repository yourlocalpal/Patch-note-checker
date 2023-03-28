War Thunder Patch Notes Bot

This bot scrapes the War Thunder website for the latest patch notes and sends them to a Discord channel.

Requirements

This bot requires the following packages:

    discord.py
    beautifulsoup4
    requests

How to use

    Clone this repository.
    Install the required packages.
    Replace BOT_ID and CHANNEL_ID with your Discord bot ID and the ID of the channel you want to send the patch notes to.
    Run the bot with the following command: python app.py

The bot will automatically run the check_for_patch_notes() task every hour to check for new patch notes. You can also use the !patch_notes command to manually send the latest patch notes to the Discord channel.

If there are no recent patch notes, the bot will send the message "Sorry, could not find recent patch notes."
Acknowledgements

This bot was created with the Discord.py library and the Beautiful Soup library.
