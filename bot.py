import discord
from discord.ext import commands
import json
import os
import asyncio

with open('Setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!!',intents = discord.Intents().all())

@bot.event
async def on_ready():
    print("-----------------------------------------------------")
    print("loding sussess!!!!")
    print("-----------------------------------------------------")
    print("bot information:")
    print(f"bot name: {bot.user}")
    print(f"bot ID: {bot.user.id}")
    print("Made By lien")
    print("-----------------------------------------------------")
    for guild in bot.guilds:
        print('Server Connected: ' + guild.name + ' (#' + str(guild.id) + ')')
    print("-----------------------------------------------------")
    while 1 :
        activitylist=["DJ GAMER","DC:https://discord.gg/69m8zthP5E","觸發指令 !!","作者:立恩"]
        for i in  activitylist:
            game = discord.Activity(type=discord.ActivityType.watching, name=(i))
            await bot.change_presence(status=discord.Status.online, activity=game)
            await asyncio.sleep(10)
    
@bot.event
async def on_member_join(member):
    role = member.guild.get_role(863963249498128384)
    await member.add_roles(role)

@bot.command()
async def load(ctx, extension):
    adminrole = ctx.guild.get_role(jdata['administrator1'])
    if adminrole in ctx.author.roles or ctx.author.guild_permissions.manage_roles:
        bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'成功讀取{extension}.py的內容')

@bot.command()
async def unload(ctx, extension):
    adminrole = ctx.guild.get_role(jdata['administrator1'])
    if adminrole in ctx.author.roles or ctx.author.guild_permissions.manage_roles:
        bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'成功取消讀取{extension}.py的內容')

@bot.command()
async def reload(ctx, extension):
    adminrole = ctx.guild.get_role(jdata['administrator1'])
    if adminrole in ctx.author.roles or ctx.author.guild_permissions.manage_roles:
        bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'成功重新讀取{extension}.py的內容')

@bot.event
async def on_message(message):
    if message.content.startswith('轉發'):
        for channel in message.channel_mentions:
            index = message.content.find(channel.mention) + len(channel.mention)
            msg = message.content[index:]
            while msg[:1] == ' ':msg = msg[1:]
            await message.delete()
            embed = discord.Embed(title="本館公告", description= msg, color=0xff0000)
            embed.set_footer(text="重要公告 務必觀看")
            await channel.send(":mega:[ <@&863974562559295530> ]\n",embed = embed)
            break
    await bot.process_commands(message)

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])