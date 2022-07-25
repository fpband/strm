import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://{App_Name}.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "FarshidBand"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 3  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "🔗 لینک دانلود ⚡"
    st_link = "⁦🖥️⁩ لینک تماشای آنلاین ⚡"
    generating_link = "**⏳ در حال تولید لینک...**"
    bot_channel = "📢 کانال پشتیبانی"
    dev_channel = "⁦🛠️⁩ ادمین و سازنده ربات ⁦🛠️⁩"
    fast = "✅**لینک شما با موفقیت بروزرسانی شد 😍**"
    update_link = "⁦♻️⁩ بروزرسانی لینک به لینک پرسرعت"
    update_limited = (f"⛔ You can update just {Config.Max_Fast_Processes} link in one time, "
                      "please wait until previous update to complete")
    re_update_link = "🔄 بروز رسانی دوباره لینک"
    already_updated = "این لینک قبلا بروزرسانی شده است."
    wait_update = "<b>⏳ در حال بروزرسانی لینک...</b>"
    wait = "⏳ کمی صبر کنید..."
    progress = "🔎 نمایش پروژه بروزرسانی لینک"
    file_not_found = "⚠️ فایلی یافت نشد , لطفا فایل دیگری ارسال نمایید."
    delete_manually_button = "⚠️ آیا میخواهید لینک فایل را حذف کنید؟"
    delete_forbidden = "The bot can't delete messages older than 48 hours, you can delete this message manually"
    force_join = "<b>• کاربر گرامی برای استفاده از ربات باید در کانال زیر عضو شوید سپس /start را کلیک کنید.👇</b>"
