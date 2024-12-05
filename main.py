import subprocess

subprocess.call(['python', 'handlers/hooks.py'])

"""

if __name__ == '__main__':
    try:
        info("Запуск бота", "utils/interaction_commands.py")
        start_polling(dp, skip_updates=True)
    except exceptions.CantDemarshException:
        warning("Ошибка при запуске бота (CantDemarshException)")
    except exceptions.BadRequest:
        warning("Ошибка при запуске бота (BadRequest)",)
    except exceptions.NetworkError:
        warning("Ошибка при запуске бота (NetworkError)")
    except exceptions.TimedOut:
        warning("Ошибка при запуске бота (TimedOut)")
    except exceptions.TelegramAPIError:
        warning("Ошибка при запуске бота (TelegramAPIError)")
    except asyncio.CancelledError:
        warning("Бот остановлен")

"""