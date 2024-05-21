from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes

# Initialize the bot with your token
mybot = Bot("6794321765:AAFVR5U-APosc7g2OQkjsiJ04GbcqxroXg0")

# Define the command handler function for /hi
async def cal_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi, I am your Jerry Bot")

# Define a message handler function to respond to all messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()
    if message_text == "hi":
        await update.message.reply_text("Hi how can i ")
    else:
        response_text = f"Sorry !! I don't know what are you saying : '{message_text}'"
        await update.message.reply_text(response_text)

# Create the application
app = ApplicationBuilder().token("6794321765:AAFVR5U-APosc7g2OQkjsiJ04GbcqxroXg0").build()

# Add the command handler to the dispatcher
app.add_handler(CommandHandler("hi", cal_func))

# Add the message handler to the dispatcher to handle all text messages
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

# Start polling
app.run_polling()
