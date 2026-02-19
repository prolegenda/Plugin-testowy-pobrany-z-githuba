from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands


def get_app_commands(plugin) -> list[app_commands.Command]:
    @app_commands.command(name="p1hello", description="Test command from plugin1")
    async def p1hello(interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"plugin1 says hello from {plugin.name}",
            ephemeral=True,
        )

    return [p1hello]


def get_prefix_commands(plugin) -> list[commands.Command]:
    @commands.command(name="p1hello")
    async def p1hello_prefix(ctx: commands.Context) -> None:
        await ctx.reply(f"plugin1 prefix hello from {plugin.name}")

    return [p1hello_prefix]
