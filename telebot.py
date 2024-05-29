from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes

# Define the command handler function for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! How can I assist you today?")

# Define a message handler function to respond to all messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()
    
    if message_text == "hello":
        response_text = "Hi there!"
    elif message_text == "how are you":
        response_text = "I'm just a bot, but I'm doing great! How about you?"
    elif message_text == "bye":
        response_text = "Goodbye! Have a great day!"
    else:
        response_text = f"Sorry, I don't know what you are saying: '{message_text}'"
    
    await update.message.reply_text(response_text)

# Create the application
app = ApplicationBuilder().token("6794321765:AAFVR5U-APosc7g2OQkjsiJ04GbcqxroXg0").build()

# Add the command handler to the dispatcher
app.add_handler(CommandHandler("start", start))

# Add the message handler to the dispatcher to handle all text messages
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

# Start polling
if __name__ == '__main__':
    app.run_polling()
