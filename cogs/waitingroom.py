import discord
from discord.ext import commands
from discord.utils import get

class WaitingRoom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        message = f'''Welcome to the server, {member.mention}! Before you can access the rest of the server, please read through {get(member.guild.text_channels, name='rules').mention} and {get(member.guild.text_channels, name='faqs').mention} , and state what year you're currently in.

If an {get(member.guild.roles, name='Assistant').mention} does not come to assist you with entering the server, please ping one (if none are present ping a mod).'''
        channel = member.guild.system_channel
        await channel.send(message)

    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def y9(self, ctx, member: discord.Member):
        '''Verifies a Y9.
Staff role needed.'''
        role = get(member.guild.roles, name='Y9')
        await member.add_roles(role)
        role = get(member.guild.roles, name='Members')
        await member.add_roles(role)
        await ctx.send('<@{}> has been verified!'.format(member.id))
        await get(member.guild.text_channels, name='general').send(f'Welcome {member.mention} to the server :wave: This new member is year 9 so expect ~~retardation~~ fun')


    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def y10(self, ctx, member: discord.Member):
        '''Verifies a Y10.
Staff role needed.'''
        role = get(member.guild.roles, name='Y10')
        await member.add_roles(role)
        role = get(member.guild.roles, name='Members')
        await member.add_roles(role)
        await ctx.send('<@{}> has been verified!'.format(member.id))
        await get(member.guild.text_channels, name='general').send(f'Welcome {member.mention} to the server :wave:')

    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def y11(self, ctx, member: discord.Member):
        '''Verifies a Y11.
Staff role needed.'''
        role = get(member.guild.roles, name='Y11')
        await member.add_roles(role)
        role = get(member.guild.roles, name='Members')
        await member.add_roles(role)
        await ctx.send('<@{}> has been verified!'.format(member.id))
        await get(member.guild.text_channels, name='general').send(f'Welcome {member.mention} to the server :wave:')

    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def postgcse(self, ctx, member: discord.Member):
        '''Verifies a Post-GCSE.
Staff role needed.'''
        role = get(member.guild.roles, name='Post-GCSE')
        await member.add_roles(role)
        role = get(member.guild.roles, name='Members')
        await member.add_roles(role)
        await ctx.send(f'{member.mention} has been verified!')
        await get(member.guild.text_channels, name='general').send(f'Welcome {member.mention} to the server :wave:')

    @commands.command(aliases=['lurker'])
    @commands.has_role('Staff')
    async def lurkers(self, ctx):
        members = [x.mention for x in ctx.guild.members if len(x.roles) <= 1]
        message = ', '.join(members) + ' please tell us your year to be verified into the server!'
        await ctx.send(message)

def setup(bot):
    bot.add_cog(WaitingRoom(bot))
