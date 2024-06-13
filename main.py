from pyrogram import Client

api_id = ''
api_hash = ''

session_name = ''

app = Client(session_name, api_id, api_hash)

def save_messages(messages, chat_name):
    with open(f'{chat_name}_messages.txt', 'a', encoding='utf-8') as f:
        for message in messages:
            if message.text:
                f.write(f'{message.date} - {message.from_user.id if message.from_user else "Unknown"}: {message.text}\n')


async def main():
    async with app:
        async for dialog in app.get_dialogs():
            print(f'Збереження повідомлень з чату: {dialog.chat.title or dialog.chat.first_name}')
            messages = [message async for message in app.get_chat_history(dialog.chat.id, limit=None)]
            save_messages(messages, dialog.chat.title or dialog.chat.first_name)


app.run(main())
