from discord.ext import commands, tasks
import discord

#----------------------------


class Deleter(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def deleter(self, ctx, number):
    if ctx.author.id == 526360392335753216:
      number = int(number) + 1
      for i in range(1, number):
        channel = discord.utils.get(ctx.guild.channels, name=f"table-{i}")
        await channel.delete()
  

async def setup(bot):
  await bot.add_cog(Deleter(bot))
