from aiogram.utils import executor
from handlers import client,callback,extra,callback_vetka_good,callback_vetka_bad
from config import dp


client.register_handlers_client(dp)
callback.register_handler_callback(dp)
callback_vetka_good.register_handler_callback(dp)
callback_vetka_bad.register_handler_callback(dp)
extra.register_handler_other(dp)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)