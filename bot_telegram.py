from aiogram.utils import executor
from create_bot import dp
from background import keep_alive


async def on_startup(_):
    print('Бот вышел в онлайн')

from handlers import client, admin, other

client.questions_handlers_user(dp)



keep_alive()
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
