import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    #purge command
    @commands.command(help="Purges a specified amount of messages from the chat")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, arg):
        try:
            arg = int(arg)
        except ValueError:
            await ctx.send("That's not a valid number. To use this command, please use the number of messages to purge as your argument")
        await ctx.channel.purge(limit=arg)
    
    #purge match command, only purges messages that contain a certain string
    @commands.command(help="Purges messages containing a certain string", aliases=["purge-match",])
    @commands.has_permissions(manage_messages=True)
    async def purgematch(self, ctx, limit, *, filtered):
        try:
            limit = int(limit)
        except ValueError:
            await ctx.send("That's not a valid number. To use this command, please use the number of messages to purge as yor first argument, and the filter to use as your second")
        def filter_check(message):
            return filtered in message.content
        await ctx.channel.purge(limit=limit, check=filter_check)


def setup(bot):
    bot.add_cog(Moderation(bot))