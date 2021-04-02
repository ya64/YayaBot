import discord
from discord.ext import commands
import random

class Community(commands.Cog):
    """Commands for the community!"""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    #rats
    @commands.command(help="RATS RATS RATS RATS RATS RATS RATS RATS RATS RATS RATS RATS", aliases=["rats", "RATS", "RAT"])
    async def rat(self, ctx):
        rat = random.choice(open("rats.txt").readlines())
        await ctx.send(rat)

    #hello
    @commands.command(help="Says hello")
    async def hello(self, ctx):
        await ctx.send("Hello there")

    @commands.command(help="Gives you the number of people in the server")
    async def membercount(self, ctx):
        await ctx.send(f"There are currently {ctx.guild.member_count} members in the server")

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.type == discord.MessageType.new_member:
            await message.add_reaction("🎉")

def setup(bot):
    bot.add_cog(Community(bot))