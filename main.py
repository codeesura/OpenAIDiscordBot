import openai                       ## This imports the openai module, which allows you to use OpenAI's API.
import discord                      ## This imports the discord module, which allows you to interact with the Discord API.
from discord import app_commands    ## This imports the app_commands module from the discord module, which allows you to create commands for your Discord bot.
import os                           ## This imports the os module, which allows you to interact with the operating system.
from dotenv import load_dotenv      ## This imports the load_dotenv function from the dotenv module, which allows you to load environment variables from a .env file.

load_dotenv()  ## This function loads environment variables from a .env file.

DISCORD_API_KEY = os.getenv("DISCORD_API_KEY") ## This gets the Discord API key from the environment variables and stores it in the DISCORD_API_KEY variable.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") ## This gets the OpenAI API key from the environment variables and stores it in the OPENAI_API_KEY variable.

intents = discord.Intents.default()  ## This gets the default intents for a Discord client and stores them in the intents variable.
client = discord.Client(intents=intents) ## This creates a Discord client with the specified intents.
tree = app_commands.CommandTree(client) ## This creates a command tree for the Discord client.

openai.api_key = (OPENAI_API_KEY) ## This sets the OpenAI API key for the openai module.
guildler = []  ## Create list

URL = 'https://discord.com/api/oauth2/authorize?client_id=1052205571920625735&permissions=2147483648&scope=applications.commands%20bot'
@tree.command(name = "image", description = "Create Image ChatGPT-3") ## This is a decorator that creates a command called "image" in the command tree. The command has the description "Create Image ChatGPT-3".
@app_commands.describe(n = "Number of photos") ## This is a decorator that adds a description for the n parameter of the "image" command.
@app_commands.describe(prompt = "The image generations endpoint allows you to create an original image given a text prompt") ## This is a decorator that adds a description for the prompt parameter of the "image" command.
@app_commands.describe(sizes = "Photo sizes") ## This is a decorator that adds a description for the sizes parameter of the "image" command.
## This is a decorator that adds a list of choices for the sizes parameter of the "image" command. The choices are "sizes = 256x256", "sizes = 512x512", and "sizes = 1024x1024".
@app_commands.choices(sizes=[
  app_commands.Choice(name='sizes = 256x256', value='256x256'),
  app_commands.Choice(name='sizes = 512x512', value='512x512'),
  app_commands.Choice(name='sizes = 1024x1024', value='1024x1024')
])
async def two_command(interaction:discord.Interaction ,prompt:str ,n:app_commands.Range[int, 1,4]=2 , sizes:app_commands.Choice[str]="1024x1024"):
    if sizes != "1024x1024":
        sizes = sizes.value
    guild = interaction.guild.id
    if guild in guildler:
        ep = False
    else : 
        ep = True
    await interaction.response.defer(ephemeral=ep)
    response = openai.Image.create(
        prompt=prompt,
        n=n,
        size=sizes
    )
    b = []
    for index ,i in enumerate([x["url"] for x in response['data']]):
        globals()['embed%s' % index] = discord.Embed(title='Image 1',description=prompt,url=URL)
        globals()['embed%s' % index].set_image(url=response['data'][index]["url"])
        b.append(globals()['embed%s' % index])
    await interaction.followup.send(embeds=b,ephemeral=ep)

def is_owner(interaction:discord.Interaction):
    if interaction.user.id == interaction.guild.owner_id:
        return True
    return False

@tree.command(name="set",description="Set ephemeral messages")
@app_commands.check(is_owner)
async def three_command(interaction , ephemeral:bool):
    await interaction.response.defer(ephemeral=True)
    guild = interaction.guild.id
    if ephemeral == True :
        if guild in guildler:
            await interaction.followup.send("Set ephemeral = True")
            guildler.remove(guild)
        elif guild not in guildler :
            await interaction.followup.send("Was there any change")
    else :
        if guild in guildler:
            await interaction.followup.send("Was there any change")
        elif guild not in guildler :
            await interaction.followup.send("Set ephemeral = False")
            guildler.append(guild)
        
@client.event
async def on_ready():
    print("Name: {}".format(client.user.name))
    await tree.sync()
    print("Ready!")

client.run(DISCORD_API_KEY)
