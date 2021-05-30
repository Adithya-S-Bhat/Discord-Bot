import discord
from discord.ext import commands, tasks

#creating intents
intents=discord.Intents.default()
intents.members=True

#creating bot
client=commands.Bot(command_prefix='.',intents=intents)

@client.event
async def on_ready():
	print("Bot is ready")
	#hi_loop.start()#comment it to avoid getting spammed by messages every 2 seconds


#in Oauth enable bot and Administrator
@client.command()
async def hello(ctx):
	#await ctx.send("Hello!")#Bot replies with hello when user sends .hello
	await ctx.send(f"Hello, {ctx.author.mention}!")

@client.command()
async def clear(ctx, amount=5):
	#Purges the channel
	#await ctx.channel.purge(limit=5)#deletes last 5 messages
	await ctx.channel.purge(limit=amount)#invoked by .clear <value>
	
@tasks.loop(seconds=2)#events
async def hi_loop():
	# Right click on channel and get its id
	await client.get_channel(815512232216494093).send("Hi")# Extract a channel and send this message "Hi"

@client.command()
async def greet(ctx, * , greeting):#after context ctx everything that it gets is greeting variable
	await ctx.send(greeting)

#Should enable member intents in discord for this to work
@client.event
async def on_member_join(member):
	#await client.get_channel(<id>).send(f"Hello, {member.mention}! Great to have you here!")#for sending in a channel
	await member.send(f"Hello, {member.mention}! Great to have you here!")#for sending a dm

#for changing nickname in a channel
#.nick @<Nickname> <newNickName>
@client.command()
async def nick(ctx, member:discord.Member, * ,newname):
	#Extract Permissions
	perms = ctx.channel.permissions_for(ctx.author)#if author has permission to change
	if perms.manage_nicknames:
		await member.edit(nick=newname)
		await ctx.send(f'Nickname was changed for {member.mention} ')
	else:
		await ctx.send("You do not have the required premissions")

@client.event
async def on_command_error():
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send("Required arguments are not given")

@client.command(aliases=['embed'])#.embed
async def embed_command(ctx):
	test = discord.Embed(title="Discord.py Bot",color=discord.Color.green())
	test.add_field(name="Hello",value="Welcome to My Discord Bot Channel",inline=False)
	test.add_field(name="Developer",value="Adithya",inline=False)
	await ctx.send(embed=test)

# Run the bot
client.run("ODQ4NTE0Nzc4ODgwMDE2NDI2.YLNu9w.e-Shmbck6udB6Ihi2nKZcGJS0G8")#get token from discord developer portal
