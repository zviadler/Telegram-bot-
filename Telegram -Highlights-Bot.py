 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHan>
import logging

# הגדרת הלוגים
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# פונקציה שתטפל בהודעה עם כוכביות
async def handle_message(update: Update, context) -> None:
    # מקבל את הטקסט מההודעה
    text = update.message.text

    # שימוש בביטוי רגולרי כדי למצוא טקסט מוקף בכוכביות
    matches = re.findall(r'\*(.*?)\*', text)

    # אם נמצאו טקסטים מוקפים בכוכביות
    if matches:
        # מחליפים את המילים שמוקפות בכוכביות לגרסה מודגשת
        for match in matches:
            text = text.replace(f"*{match}*", f"*{match}*")

        # שולחים את הטקסט בחזרה עם ההדגשות
        await update.message.reply_text(text, parse_mode='Markdo>
    else:
        # אם אין כוכביות, שולחים את הטקסט כמו שהוא
        await update.message.reply_text(text)

# פונקציה לטיפול בפקודת /start
async def start(update: Update, context) -> None:
    # שלח את ההודעה המותאמת עם הסבר על הבוט
    await update.message.reply_text(
        "שלום! אני בוט שמבצע הדגשות עם כוכביות.\n"
        "שלח לי טקסט עם כוכביות ואחזור אותו מודגש!\n"
        "למשל: *שלום* יוחזר כ-שלום מודגש.\n"
        "אם תשלח טקסט בלי כוכביות, אני אשלח אותו כפי שהוא."
    )

# פונקציה שתגדיר את כל הקונפיגורציה של הבוט
def main() -> None:
    # הכנס את המפתח של הבוט שלך כאן
    TOKEN = "7282123628:AAEnDpWTiTiy2U9u6on-fc_LX2y30g_AOtI"

    # יצירת application
    application = Application.builder().token(TOKEN).build()

    # הוספת פקודת /start
    application.add_handler(CommandHandler("start", start))

    # הוספת handler להודעות טקסט רגילות
    application.add_handler(MessageHandler(filters.TEXT & ~filte>

    # התחלת הבוט
    application.run_polling()

if __name__ == '__main__':
    main()
