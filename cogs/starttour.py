from discord.ext import commands, tasks
import discord
from random import shuffle
import time
#----------------------------


class Draw(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def draw(self, ctx):
    if ctx.author.id == 526360392335753216:

      with open("database/participants.txt", "r") as f:
        participantList = f.readlines()
      shuffle(participantList)
      partNumber = len(participantList)
      with open("database/matches.txt", "w+") as m:

        if partNumber % 2 == 1:
          part = await self.bot.fetch_user(participantList[0])

          await ctx.send(f"**{part.mention} Qualify Directly**")
          m.write(f"{part.name.rstrip()} Qualify Directly\n")
          participantList = participantList[1::]
          partNumber = len(participantList)
        categoryName = "ChessTour"

        category = discord.utils.get(ctx.guild.categories, name=categoryName)

        tableCounter = 1

        for i in range(0, len(participantList) - 1, 2):
          part1 = await self.bot.fetch_user(participantList[i])
          part2 = await self.bot.fetch_user(participantList[i + 1])

          await ctx.send(f"**{part1.mention} vs {part2.mention}**")
          m.write(f"{part1.name} vs {part2.name}\n")
          room = await ctx.guild.create_text_channel(f'table-{tableCounter}',
                                                     category=category)

          tableCounter += 1
          everyone = ctx.guild.default_role
          await room.set_permissions(everyone, read_messages=False)

          await room.set_permissions(part1,
                                     read_messages=True,
                                     send_messages=True)

          await room.set_permissions(part2,
                                     read_messages=True,
                                     send_messages=True)
          await room.send(f"""
            Hello {part1.mention} and {part2.mention} You will play against each others !\n
{part1.mention} will Play with **The White Pieces**\n 
{part2.mention} will Play with **The Black Pieces**\n 
{part1.mention} go to lichess.org and create a **blitz match 5+0 ** and choose **White pieces** and send the link **Here** \n
after the match send a **Screenshot** of **the Winner** 🏆 !  \n
Good Luck and **HAVE FUN**\n""")

          time.sleep(0.5)

    # except Exception as e:
    #   print(e)


async def setup(bot):
  await bot.add_cog(Draw(bot))
