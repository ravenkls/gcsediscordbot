﻿import discord
from discord import Embed, Colour
from discord.ext import commands
from discord.utils import get
import os
import psycopg2

class Private(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gdrive_link = os.environ['GDRIVE']
        self.classroom_link = os.environ['CLASSROOM']
        
        key = os.environ.get('DATABASE_URL')
        self.conn = psycopg2.connect(key, sslmode='require')
        self.cur = self.conn.cursor()

    def in_private_server(ctx):
        return (ctx.guild.id == 593788906646929439) or (ctx.author.id == 394978551985602571) #in priv server or is adam

    def is_adam(ctx):
        return (ctx.author.id == 394978551985602571)

    @commands.command()
    @commands.check(in_private_server)
    async def spamping(self, ctx, amount, user: discord.Member, *message):
        '''For annoying certain people'''
        await ctx.message.delete()
        
        try:
            iterations = int(amount)
        except Exception as e:
            await ctx.send(f"Please use a number for the amount, not {amount}")
            return
        
        if ctx.guild.id == 593788906646929439:
            msg = ' '.join(message) + " " + user.mention
            for i in range(iterations):
                await ctx.send(msg)
        else:
            await ctx.send("Insufficient permission to use this command in this server.")

    @commands.command()
    @commands.check(in_private_server)
    async def csnotes(self, ctx, section = None):
        embed = Embed(title="**MV16 Computer Science 2019-2021**", description="Class code: 7vhujps", color=Colour.blue())

        if section == "all":
            self.cur.execute("SELECT * FROM classroom")
            temp = self.cur.fetchall()
            notes_ids = sorted(temp, key = lambda x:x[0])
            for item in notes_ids:
                embed.add_field(name=f"**Section {item[0]} ({item[2]}) notes**", value=f"    [Click here!](https://docs.google.com/document/d/{item[1]})")

        elif section != None:
            self.cur.execute("SELECT * FROM classroom WHERE section = %s", (section,))
            notes = self.cur.fetchall()[0]
            embed.add_field(name=f"**Section {section} ({notes[2]}) notes**", value=f"    [Click here!](https://docs.google.com/document/d/{notes[1]})")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.check(is_adam)
    async def csnotesadd(self, ctx, section = None, id = None, *name):
        if not section or not id or not name:
            await ctx.send("'```-csnotesadd <section_number> <GDriveID> <name>```'")
            return
        self.cur.execute("INSERT INTO classroom (section, gid, name) VALUES (%s, %s, %s)", (section, id, ' '.join(name)))
        self.conn.commit()
        await ctx.send(":ok_hand: Done!")

    @commands.command()
    @commands.check(is_adam)
    async def csnotesdelete(self, ctx, section = None):
        if not section:
            await ctx.send("'```-csnotesdelete <section_number>```'")
            return
        self.cur.execute("DELETE FROM classroom WHERE section = %s", (section,))
        self.conn.commit()
        await ctx.send(":ok_hand: Done!")

def setup(bot):
    bot.add_cog(Private(bot))
