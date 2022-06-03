#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#    Script Improved by Anshusharma

from . import *
from .config import *
from .worker import *
from .devtools import *
from .FastTelethon import *
LOGS.info("Starting...")

try:
    bot.start(bot_token=BOT_TOKEN)
except Exception as er:
    LOGS.info(er)


####### GENERAL CMDS ########

@bot.on(events.NewMessage(pattern="/start"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await start(e)


@bot.on(events.NewMessage(pattern="/setcode"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await coding(e)


@bot.on(events.NewMessage(pattern="/getcode"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await getcode(e)


@bot.on(events.NewMessage(pattern="/showthumb"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await getthumb(e)


@bot.on(events.NewMessage(pattern="/logs"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await getlogs(e)


@bot.on(events.NewMessage(pattern="/cmds"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await zylern(e)


@bot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await up(e)


@bot.on(events.NewMessage(pattern="/sysinfo"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await sysinfo(e)


@bot.on(events.NewMessage(pattern="/leech"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await dl_link(e)


@bot.on(events.NewMessage(pattern="/help"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await ihelp(e)


@bot.on(events.NewMessage(pattern="/renew"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await renew(e)


@bot.on(events.NewMessage(pattern="/clear"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await clearqueue(e)


@bot.on(events.NewMessage(pattern="/speed"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
    await test(e)
    
    

########## Direct ###########

@bot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)

@bot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)


######## Callbacks #########

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile("help")))
async def _(e):
    await help(e)

########## AUTO ###########

@bot.on(events.NewMessage(incoming=True))
async def _(event):
        if str(event.sender_id) not in OWNER and event.sender_id !=DEV:
            return await event.reply_text("**සමාවන්න ඔබ බලයලත් පරිශීලකයෙක් නොවේ!**")
        if not event.photo:
            return
        os.system("rm thumb.jpg")
        await event.client.download_media(event.media, file="/bot/thumb.jpg")
        await event.reply("**සිඟිති රුව සාර්ථකව සුරකින ලදී.**")


@bot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


async def something():
    for i in itertools.count():
        try:
            if not WORKING and QUEUE:
                user = int(OWNER.split()[0])
                e = await bot.send_message(user, "** පෝලිම් ගොනු බාගනිමින්...**")
                s = dt.now()
                try:
                    if isinstance(QUEUE[list(QUEUE.keys())[0]], str):
                        dl = await fast_download(
                            e, list(QUEUE.keys())[0], QUEUE[list(QUEUE.keys())[0]]
                        )
                    else:
                        dl, file = QUEUE[list(QUEUE.keys())[0]]
                        tt = time.time()
                        dl = "downloads/" + dl
                        with open(dl, "wb") as f:
                            ok = await download_file(
                                client=bot,
                                location=file,
                                out=f,
                                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                                    progress(
                                        d,
                                        t,
                                        e,
                                        tt,
                                        f"** බාගත කරමින්**\n__{dl.replace(f'downloads/', '')}__",
                                    )
                                ),
                            )
                except Exception as r:
                    LOGS.info(r)
                    WORKING.clear()
                    QUEUE.pop(list(QUEUE.keys())[0])
                es = dt.now()
                kk = dl.split("/")[-1]
                aa = kk.split(".")[-1]
                newFile = dl.replace(f"downloads/", "").replace(f"_", " ")
                rr = "encode"
                bb = kk.replace(f".{aa}", ".mkv")
                out = f"{rr}/{bb}"
                thum = "thumb.jpg"
                dtime = ts(int((es - s).seconds) * 1000)
                hehe = f"{out};{dl};{list(QUEUE.keys())[0]}"
                wah = code(hehe)
                nn = await e.edit(
                    "**🗜 සම්පීඩනය කරමින්...**",
                    buttons=[
                        [Button.inline("දැනට පවතින තත්වය", data=f"stats{wah}")],
                        [Button.inline("අවලංගු කරන්න", data=f"skip{wah}")],
                    ],
                )
                cmd = f"""ffmpeg -i "{dl}" {ffmpegcode[0]} "{out}" -y"""
                process = await asyncio.create_subprocess_shell(
                    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                er = stderr.decode()
                try:
                    if er:
                        await e.edit(str(er) + "\n\n**දෝෂයකි**")
                        QUEUE.pop(list(QUEUE.keys())[0])
                        os.remove(dl)
                        os.remove(out)
                        continue
                except BaseException:
                    pass
                ees = dt.now()
                ttt = time.time()
                await nn.delete()
                nnn = await e.client.send_message(e.chat_id, "** උඩුගත කරමින්...**")
                with open(out, "rb") as f:
                    ok = await upload_file(
                        client=e.client,
                        file=f,
                        name=out,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(d, t, nnn, ttt, f"** උඩුගත කරමින්**\n__{out.replace(f'encode/', '')}__")
                        ),
                    )
                await nnn.delete()
                org = int(Path(dl).stat().st_size)
                com = int(Path(out).stat().st_size)
                pe = 100 - ((com / org) * 100)
                per = str(f"{pe:.2f}") + "%"
                eees = dt.now()
                x = dtime
                xx = ts(int((ees - es).seconds) * 1000)
                xxx = ts(int((eees - ees).seconds) * 1000)
                a1 = await info(dl, e)
                a2 = await info(out, e)
                dk = f"<b>ගොනු නම:</b> {newFile}\n\n<b>මුල් ගොනු ප්‍රමාණය:</b> {hbs(org)}\n<b>කේතගත ගොනු ප්‍රමාණය:</b> {hbs(com)}\n<b>කේතගත ප්‍රතිශතය:</b> {per}\n\n<b>මෙහි මාධ්‍ය තොරතුරු ලබා ගන්න:</b> <a href='{a1}'>පෙර</a>/<a href='{a2}'>පසු</a>\n\n<i>බාගත කළේ {x}\nකේතනය කළේ {xx}\nඋඩුගත කළේ {xxx}</i>"
                ds = await e.client.send_file(
                    e.chat_id, file=ok, force_document=True, caption=dk, link_preview=False, thumb=thum, parse_mode="html"
                )
                QUEUE.pop(list(QUEUE.keys())[0])
                os.remove(dl)
                os.remove(out)
            else:
                await asyncio.sleep(3)
        except Exception as err:
            LOGS.info(err)


########### Start ############

LOGS.info("බොට් ආරම්භ වී ඇත.")
with bot:
    bot.loop.run_until_complete(something())
    bot.loop.run_forever()
