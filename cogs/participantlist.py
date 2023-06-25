from discord.ext import commands, tasks
import discord
from random import shuffle
import time
#----------------------------


class ParticipantList(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def list(self, ctx):
    if ctx.author.id == 526360392335753216:


      with open("database/rparticipants.txt", "r") as f:
        participantList = f.readlines()
      for p in participantList:
        part =await self.bot.fetch_user(int(p)) 
        await ctx.send(part.mention)
      
      
     

    # except Exception as e:
    #   print(e)


async def setup(bot):
  await bot.add_cog(ParticipantList(bot))
