from discord.ext import commands, tasks
import discord
from random import shuffle
import time
import asyncio
#----------------------------


class Brodcast(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def brod(self, ctx,*,message):
    if ctx.author.id == 526360392335753216:


      with open("database/participants.txt", "r") as f:
        participantList = f.readlines()
      sentCounter=0
      notSentCounter=0
      for p in participantList:
          user =await self.bot.fetch_user(int(p)) 
 
          try:
 
            await user.create_dm()
            await user.dm_channel.send(message)
            print(f"sent to {user.name}")
            await asyncio.sleep(1)
            sentCounter += 1
          except Exception as e:
            print(e)
            notSentCounter += 1
      await ctx.send(
        f"Message sent to **{str(sentCounter)}** members and not sent to **{str(notSentCounter)}** members"
    )
      
      
     

   
async def setup(bot):
  await bot.add_cog(Brodcast(bot))
