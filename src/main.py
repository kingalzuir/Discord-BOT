from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = "299667377107238913"  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(message):
    if message.content == 'Salut tout le monde':
        await message.channel.send(f'Salut tout seul{message.author.mention}')
    else:
      await bot.process_commands(message)

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    
    await ctx.send(f'{ ctx.message.author.name }')

@bot.command()
async def d6(ctx):
    await ctx.send(f'{random.randint(1,6)}')

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member):
    await member.ban()

@bot.command(pass_context = True)
async def admin(ctx, user : discord.Member):
    role = discord.utils.get(user.guild.roles, name="Admin")
    if role is None :
        await ctx.guild.create_role(name='Admin')
        perm = discord.Permissions()
        perm.update()
        await role.edit(permission = perm)
    await user.add_roles(user, "Admin")



token = ""
bot.run(token)  # Starts the bot