import asyncio
import discord
from discord.ext import commands
import get_link
client = commands.Bot(command_prefix='.') # Sets the prefix to listen.


async def post_tasks(): # background method to send the data extracted in get_link.py
    await client.wait_until_ready()
    channel = client.get_channel(680655448042504232)  # channel ID goes here
    while not client.is_closed():
        await channel.purge(limit=100)
        get_link.get_html() # this calls get_link.py to download the webpage to get the newest information
        titel = ['None', 'None', 'Deutsch', 'English', 'Mathe', 'FBE', 'Datenbanken', 'Programmieren', 'FBIN', 'None',
                 'None', 'Politik', 'Wirtschaft', 'None', 'None'] # list with titels in it
        for section in range(2, 14): # goes through every section in get_link.py
            text = str(get_link.get_information_main(section)).replace('[', '').replace(']', '').replace("'", '') # calls get_link with section(an int), so that the script knows wich section
            if text == None:
                test = "Oh nothing found xD"
            else:
                test = "Footer :D"
            message = discord.Embed(
                titel = titel[section],
                description = text,
                colour = discord.Colour.blurple()
            )
            message.set_footer(text= test)
            await channel.send(embed=message)
            #await channel.send(str(lists[section])+'\n'+str(get_link.get_information_main(section)).replace('[', '').replace(']', '').replace("'", ''))
        await channel.send('@everyone ')
        await asyncio.sleep(86400)  # task runs every 60 seconds


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def post(): # Method to manually get the data from get_link.py
    channel = client.get_channel(680655448042504232)
    lists = ['None', 'None', 'Deutsch', 'English', 'Mathe', 'FBE', 'Datenbanken', 'Programmieren', 'FBIN', 'None',
                'None', 'Politik', 'Wirtschaft', 'None', 'None']
    for section in range(2, 14):
        await channel.send(str(lists[section])+'\n'+str(get_link.get_information_main(section))) #Not sent in an embed remember it


@client.command()
async def vertretungsplan(message): # this method will sends the link below and mentions the author of the request
    channel = client.get_channel(680655448042504232)
    await channel.send('https://webuntis.krzn.de/WebUntis/monitor?school=bk-technik-moers&monitorType'
                 '=subst&format=Schulflur' + '{0.author.mention}'.format(message))


@client.command()
async def clear(ctx): # Method to manually clear the channel
    channel = client.get_channel(680655448042504232)
    await channel.purge(limit=100)


client.loop.create_task(post_tasks())
client.run('')
