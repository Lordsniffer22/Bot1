import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

# Constants for ConversationHandler states
USERNAME, PASSWORD, NUM_DAYS = range(3)

# User data dictionary to store input
user_data = {}

# Define the start command
def start(update, context):
    user_data.clear()  # Clear any previous user data
    update.message.reply_text("Welcome to the VPN account generator bot! Please enter your desired username:")
    return USERNAME

# Handle the username input
def get_username(update, context):
    user_data['username'] = update.message.text
    update.message.reply_text("Great! Now, please enter your desired password:")
    return PASSWORD

# Handle the password input
def get_password(update, context):
    user_data['password'] = update.message.text
    update.message.reply_text("Finally, please enter the number of days you want your account to last for:")
    return NUM_DAYS

# Handle the number of days input
def get_num_days(update, context):
    user_data['num_days'] = update.message.text
    
    # Generate the output message with placeholders
    output_message = f"::::HyBRid UDP CUSTOM::::\n\nUser Created Successfully\n=========================\nServer IP: cdn2.unlimitedfiles.tk\nPort Range: 1-65535.\nUsername: {user_data['username']}\nPassword: {user_data['password']}\nNumber of Days: {user_data['num_days']}\nConnection Limit: unlimited\nExpiration Date: [calculate expiry date here]\n\nConfig: cdn2.unlimitedfiles.tk:1-65535@{user_data['username']}:{user_data['password']}\n\nJoin us now @udpcustom"

    # Send the formatted message to the user
    update.message.reply_text(output_message)
    
    return ConversationHandler.END

# Define the main function
def main():
    # Replace 'YOUR_API_TOKEN' with your actual Telegram Bot API token
    updater = Updater(token='5865234656:AAH0zWkcHq8gdDaLiwm8b-99aTTL7A8vf3k', use_context=True)
    dispatcher = updater.dispatcher
    
    # Create the conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            USERNAME: [MessageHandler(Filters.text & ~Filters.command, get_username)],
            PASSWORD: [MessageHandler(Filters.text & ~Filters.command, get_password)],
            NUM_DAYS: [MessageHandler(Filters.text & ~Filters.command, get_num_days)],
        },
        fallbacks=[],
    )
    
    dispatcher.add_handler(conv_handler)
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
