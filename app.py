import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import requests
import asyncio

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready!')

# The last_patch_notes.txt file is populated by the check_for_patch_notes() task, which runs every hour and scrapes the War Thunder website for the latest patch notes. If there are new patch notes available, the task updates the contents of the last_patch_notes.txt file with the new patch notes.When you run the send_patch_notes() command, it reads the contents of the last_patch_notes.txt file and sends them as a message to the channel where the command was executed. If the file is empty or does not exist, the bot will send the message "Sorry, could not find recent patch notes."
# This decorator will define a task that runs every hour to check for new patch notes
@tasks.loop(hours=1)
async def check_for_patch_notes():
    url = "https://warthunder.com/en/game/changelog"

    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")
    patch_notes_element = soup.find("div", {"class": "showcase"})

    patch_notes_lines = patch_notes_element.text.strip().split('\n')
    recent_updates = []
    for line in patch_notes_lines:
        if "update" in line.lower():
            recent_updates.append(line.strip())

    # Load the last checked patch notes from a file
    with open("last_patch_notes.txt", "r") as f:
        last_patch_notes = f.read()

    # Compare the last checked patch notes with the current patch notes
    if last_patch_notes != "\n".join(recent_updates):
        # If there are new patch notes, update the file and send a message to a channel on Discord
        with open("last_patch_notes.txt", "w") as f:
            f.write("\n".join(recent_updates))

        channel = bot.get_channel(CHANNEL_ID)  # Replace with the ID of the channel to send the message to

        message = "New patch notes available!\n\n"
        message += "\n\n".join(recent_updates)
        print("Message created:", message)

        await channel.send(message)
        print("Message sent!")


@bot.command(name='test')
async def test(ctx):
    channel = bot.get_channel(CHANNEL_ID)  # Replace CHANNEL_ID with the ID of the channel to send the message to
    await channel.send("This is a test message.")


@bot.command(name='patch_notes')
async def send_patch_notes(ctx):
    print("Sending patch notes...")
    with open("last_patch_notes.txt", "r") as f:
        last_patch_notes = f.read().strip()

    if not last_patch_notes:
        await ctx.send("Sorry, could not find recent patch notes.")
        return

    url = "https://warthunder.com/en/game/changelog"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    patch_notes_element = soup.find("div", {"class": "showcase"})

    patch_notes_lines = patch_notes_element.text.strip().split('\n')
    recent_updates = []
    for line in patch_notes_lines:
        if "update" in line.lower():
            recent_updates.append(line.strip())

    print("Recent updates:", recent_updates)

    message = "Recent patch notes:\n\n"
    message += "\n\n".join(recent_updates)
    print("Message:", message)

    try:
        for chunk in [message[i:i+2000] for i in range(0, len(message), 2000)]:
            await ctx.send(chunk)
            await asyncio.sleep(1) # add a 1 second delay between sending messages
    except discord.HTTPException as e:
        print(f"Failed to send message: {e}")




async def start_check_for_patch_notes():
    await bot.wait_until_ready()
    check_for_patch_notes.start()
    print("Patch note checking task started!")


async def async_main():
    await bot.login('BOT_ID') # Replace BOT_ID with  discord API
    await bot.connect()
    await start_check_for_patch_notes()
    await bot.run()


asyncio.run(async_main())
