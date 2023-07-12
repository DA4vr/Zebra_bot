import discord
from discord.ext import commands
import responses


async def send_message(message, user_message, is_private):
    # send_message takes the message , and the user message that the person sent
    try:
        # response returns to the user the message.
        #response =#needs to be implemented
        response = responses.get_response(user_message)
        #if private send to author private, else send on the channel
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def is_user_author(author_id):
    def check(message):
        return message.author.id == author_id

    return check

def run_discord_bot():

    TOKEN = 'MTExODgzOTc2MzQwMzgyMTE0Nw.GBGhfN.r0aift1pSOPKdjV629Js_oc7i2BzKME6hyguSw'
    #intents
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message.startswith('?'):
            #it will start from the second index.
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
