import discord
from discord import utils
from discord.utils import get
from discord.ext import commands
import os
import pystyle
from pystyle import *

bot = commands.Bot(command_prefix= "+")  

bot.remove_command('help')





@bot.event
async def on_ready():
    print()
    print(f'                                        Connecté en tant que {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Bot de hood#1337"))

@bot.command()
async def coucou(ctx):
    print("coucou")
    await ctx.send("coucou !")


@bot.command()
async def help(ctx):
    embedVar = discord.Embed(title="Commandes", description="\n`help`\n*Sert à envoyer ce paneau d'aide*\n\n`serverinfo`\n*Sert à obtenir des informations sur le serveur*\n\n`hey`\n*Sert a combler l'ennuie*\n\n`ban`\n*Permet de banir un membre*\n\n`lock`\n*Permet de lock un chanel*\n\n`unlock`\n*Permet de unlock un chanel*\n\n`bl`\n*Permet de blacklist une personne*", color=0x336EFF)
    await ctx.send(embed=embedVar)



@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    serverName = server.name
    numberOfPerson = server.member_count
    embedVar = discord.Embed(title="ServerInfo", description=f"\n:white_check_mark:・**Le serveur a {numberOfPerson} membres** \n\n:white_check_mark:・**Le serveur a {numberOfTextChannels} salons textuels** & **{numberOfVoiceChannels} salons vocaux** ", color=0x336EFF)
    await ctx.send(embed=embedVar)

@bot.command()
async def hey(message):
    auteurcommandedieu = message.author
 
    whitelistcommandedieu = "Mon id"
 
    await message.send(message.author) #renvoie un id discord exemple fdfsfs#6516
 
    if auteurcommandedieu == whitelistcommandedieu:
        await message.send("Prosternez vous devant le **Roi des Dieux** Hood#1337!!")
    else:
        await message.send("Bonjour a toi, passe une bonne journée/soirée :)")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason = None):
  if not reason:
    await user.ban()
    await ctx.send(f"**{user}** viens de se faire **bannir** car : **pas de raison**")
  else:
    await user.ban(reason=reason)
    await ctx.send(f"**{user}** viens de se faire **bannir** car : **{reason}**")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Le channel à été **lock** avec succès')
@lock.error
async def lock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("Vous n'avez pas la permission pour utiliser cette commande")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Le channel à été **unlock** avec succès')
@lock.error
async def lock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("Vous n'avez pas la permission pour utiliser cette commande")

@bot.command()
@commands.has_permissions(ban_members=True)
async def bl(ctx, user: discord.User):
  for guild in bot.guilds:
    await guild.ban(user)
  await ctx.send(f"{user} viens d'être blacklisté")

bot.run("MTAwMDQ1MTc5MDMyOTg5Mjg3NA.GNV4xO.IdV349RmVgS1H2uV6lcUAdZKWsxBauQADhJclE")