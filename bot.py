from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup, 
    KeyboardButton, ReplyKeyboardMarkup, Update
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, 
    MessageHandler, ContextTypes, filters
)

# دکمه‌های شیشه‌ای
inline_keyboard = [
    [InlineKeyboardButton("💼 خدمات", callback_data='services')],
    [InlineKeyboardButton("🎓 آموزش", callback_data='education')],
    [InlineKeyboardButton("📞 تماس", url="tel:+989366641968")],
    [InlineKeyboardButton("🌐 سایت", url="https://yourwebsite.com")],
    [InlineKeyboardButton("📸 اینستاگرام", url="https://instagram.com/yourpage")]
]
inline_markup = InlineKeyboardMarkup(inline_keyboard)

# دکمه‌های reply برای دریافت شماره و لوکیشن
reply_keyboard = [
    [KeyboardButton("📱 ارسال شماره من", request_contact=True)],
    [KeyboardButton("📍 ارسال موقعیت مکانی من", request_location=True)]
]
reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

# پیام خوش‌آمدگویی
welcome_text = (
    "👋 به ربات *مهدی حسنلو* خوش آمدید!\n\n"
    "🔧 انجام کلیه خدمات *سخت‌افزاری* و *نرم‌افزاری*\n"
    "🏠 در *منزل* یا محل کار شما، فقط با یک تماس 📞\n"
    "📱 *۰۹۳۶۶۶۴۱۹۶۸*\n\n"
    "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
)

# دستور start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_markdown(welcome_text, reply_markup=inline_markup)
    await update.message.reply_text("👇 همچنین می‌تونی شماره یا لوکیشن خودتو ارسال کنی:", reply_markup=reply_markup)

# دکمه‌های شیشه‌ای (خدمات، آموزش)
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "services":
        await query.message.reply_text(
            "💼 *خدمات ما:*\n"
            "- نصب انواع *ویندوز* و *نرم‌افزارهای تخصصی*\n"
            "- *عیب‌یابی رایگان*\n"
            "- حتی در *ایام تعطیل*! 🛠️",
            parse_mode="Markdown"
        )
    elif query.data == "education":
        await query.message.reply_text(
            "🎓 دوره‌های آموزشی ما:\n"
            "- آموزش کامپیوتر مقدماتی تا پیشرفته\n"
            "- آموزش آفیس، فتوشاپ، ویندوز\n"
            "- پشتیبانی کامل و حضوری"
        )

# دریافت شماره تلفن
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    await update.message.reply_text(f"✅ شماره شما دریافت شد:\n📱 {contact.phone_number}")

# دریافت لوکیشن
async def location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = update.message.location
    await update.message.reply_text(f"📍 موقعیت شما:\nLatitude: {location.latitude}\nLongitude: {location.longitude}")

# اجرای ربات
if __name__ == '__main__':
    TOKEN = "توکن_ربات_شما"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.add_handler(MessageHandler(filters.CONTACT, contact_handler))
    app.add_handler(MessageHandler(filters.LOCATION, location_handler))

    print("🤖 ربات آماده‌ست...")
    app.run_polling()
