# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *
from datetime import datetime

START_TIME = datetime.now()

async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"Ping = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"**ඔබට සම්පීඩනය කිරීමට අවශ්‍ය වීඩියෝව මට එවන්න.**\n**Uptime: {str(datetime.now() - START_TIME).split('.')[0]}**",
        buttons=[
            [Button.inline("උදව්", data="help")],
        ],
    )

async def zylern(event):
    await event.reply(
        f"""
**ලබා ගත හැකි විධාන 😉**
/start - __බොට් ක්‍රියා කරන්නේද නැද්ද යන්න__
/help - __විස්තරාත්මක උදවු ලබා ගන්න__
/setcode - __අභිරුචි FFMPEG කේතය සකසන්නe__
/getcode - __වත්මන් FFMPEG කේතය මුද්‍රණය කරන්න__
/logs - __Get Bot Logs__
/ping - __Ping පරීක්ෂා කරන්න__
/sysinfo - __පද්ධති තොරතුරු ලබා ගන්න__
/renew - __Cache හිස් කරන්න__
/clear - __Clear Queued Files__
/showthumb - __වත්මන් සිඟිති රුව පෙන්වන්න__
/cmds - __විධාන ලැයිස්තුව__
"""
    )


async def help(event):
    await event.edit(
        f"""**ffmpeg කේතය පරීක්ෂා කිරීමට ඔබට** /getcode **භාවිතා කල හැක**\n\n**පහත විධානය ක්‍රියාත්මක කිරීමෙන් ඔබට ඔබගේ ffmpeg කේතය වෙනස් කළ හැක.**\n\n`/setcode -preset faster -c:v libx265 -s 1280x720 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1`\n\n**අභිරුචි සිඟිති රුව සැකසීමට මට රූපය එවන්න.**\n\n**තවත් උදව් සඳහා /cmds කරන්න**"""
    )
    
async def ihelp(e):
    await e.reply(
        f"""**ffmpeg කේතය පරීක්ෂා කිරීමට ඔබට** /getcode **භාවිතා කල හැක**\n\n**පහත විධානය ක්‍රියාත්මක කිරීමෙන් ඔබට ඔබගේ ffmpeg කේතය වෙනස් කළ හැක.**\n\n`/setcode -preset faster -c:v libx265 -s 1280x720 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1`\n\n**අභිරුචි සිඟිති රුව සැකසීමට මට රූපය එවන්න.**\n\n**තවත් උදව් සඳහා /cmds කරන්න**"""
    )
