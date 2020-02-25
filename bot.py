import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    activity = discord.Activity(name='you, from inside the Snotmobile', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("Hello there!")

@client.command(aliases=['PING', 'p'])
async def ping(ctx):
    embed = discord.Embed(color=discord.Color.blurple())

    embed.set_author(name=f'Ping Requested By: {ctx.author}', icon_url=ctx.author.avatar_url)
    embed.set_footer(text='All values are rounded to the nearest whole number!')

    embed.add_field(name='**Pong!**', value=f'{round(client.latency * 1000)}ms')

    await ctx.send(embed=embed)

@client.command(aliases=['8ball', '8'])
async def eightball(ctx, *, question, member : discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=discord.Color.blurple())
    responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]

    embed.set_author(name=f'Requested By: {ctx.author}', icon_url=ctx.author.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

    embed.add_field(name='Question:', value=f'{question}', inline=False)
    embed.add_field(name='Answer:', value=f'{random.choice(responses)}')
    await ctx.send(embed=embed)

@client.command()
async def emoji(ctx,*,iconid):
    await ctx.send(f'Emoji: {iconid}\nID: {discord.Emoji.name, discord.Emoji.id}')

@client.command(aliases=['pfp'])
async def avatar(ctx, author: discord.Member):
    show_avatar = discord.Embed(color = discord.Color.blurple())
    show_avatar.set_image(url=f'{author.avatar_url}')
    await ctx.send(embed=show_avatar)

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['no'])
async def noone(ctx):
    await ctx.send('noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked noone asked \nnoone asked noone asked noone asked noone asked noone asked ')

@client.command()
async def testembed(ctx):
    embed = discord.Embed(title='Title', description='Description', color=discord.Color.blurple(), url='https://www.fortniteburger.net')

    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_image(url='https://pbs.twimg.com/profile_images/949803901162807298/d0wy9bBX.jpg')
    embed.set_thumbnail(url='https://lh3.googleusercontent.com/proxy/ZTTutZex9iN6DkSi3KpWicj5Qppets39JcFk-fyQGMaJChNEEr9mYEjGT8ZMdz2szH7tkszjiiNohDIhNXnCJQbsQcBni4M')

    embed.add_field(name='Field 1', value='Value 1') #To be able to set a newline for the field value use "inline=False", which by default will always be true.
    embed.add_field(name='Field 2', value='Value 2')

    await ctx.send(embed=embed)

@client.command(aliases=['ui'])
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='Server nickname:', value=member.display_name)
    embed.add_field(name='ID:', value=member.id)

    embed.add_field(name='Account Created At:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p GMT'), inline=False)
    embed.add_field(name='Server Join Date:', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p GMT'))

    embed.add_field(name=f'Roles in Server: ({len(roles)})', value=' '.join([role.mention for role in roles]), inline=False)
    embed.add_field(name='Top Role:', value=member.top_role.mention)

    embed.add_field(name='Bot?:', value=member.bot, inline=False)

    await ctx.send(embed=embed)


@client.command()
async def hj(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/604609273250709506/680882078383996978/unknown.png')

@client.command()
async def say(ctx,*,usertext):
    await ctx.send(f'You told me to say: {usertext}')

client.run('NjgwNDQxMzU4NTY5NTcwMzQ5.XlV_7w.6vgCJXI-lSW5sKFXHvkMnEDrI-A')
