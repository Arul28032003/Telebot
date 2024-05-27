from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters, ApplicationBuilder, ContextTypes

# Initialize the bot with your token
mybot = Bot("6794321765:AAFVR5U-APosc7g2OQkjsiJ04GbcqxroXg0")

# Define the command handler function for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Hey", callback_data='hey')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button below:", reply_markup=reply_markup)

# Define a callback query handler to handle button presses
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'hey':
        await query.edit_message_text(text="Sollri punda !!!")

# Define a message handler function to respond to all messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()
    if message_text == "hey":
        await update.message.reply_text("Sollri punda !!!")
    else:
        response_text = f"Sorry !! I don't know what are you saying : '{message_text}'"
        await update.message.reply_text(response_text)

# Create the application
app = ApplicationBuilder().token("6794321765:AAFVR5U-APosc7g2OQkjsiJ04GbcqxroXg0").build()

# Add the command handler to the dispatcher
app.add_handler(CommandHandler("start", start))

# Add the callback query handler to handle button presses
app.add_handler(CallbackQueryHandler(button))

# Add the message handler to the dispatcher to handle all text messages
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

# Start polling
app.run_polling()
