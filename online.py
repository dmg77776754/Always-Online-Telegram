import asyncio
from telethon import TelegramClient, events

api_id = 'Введите свои значения'
api_hash = 'Введите свои значения'
phone_number = 'Введите свои значения'

device_model = 'iPhone'
system_version = '14.5'
app_version = '8.0.1'
lang_code = 'en'
system_lang_code = 'en'

client = TelegramClient('session_name', api_id, api_hash,
                        device_model=device_model,
                        system_version=system_version,
                        app_version=app_version,
                        lang_code=lang_code,
                        system_lang_code=system_lang_code)

@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.raw_text == 'бе':
        await client.delete_messages('me', [event.message])

async def main():
    await client.start()

    confirmation_code = input('Введите код подтверждения: ')
    await client.sign_in(phone_number, confirmation_code)

    await client.get_dialogs()

    while True:
        try:
            # Отправка сообщения "бе"
            message = await client.send_message('me', 'бе')

            # Удаление отправленного сообщения "бе"
            await client.delete_messages('me', [message])

            await asyncio.sleep(10)
        except Exception as e:
            print(f'Ошибка: {e}')
            await client.start()
            continue

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
