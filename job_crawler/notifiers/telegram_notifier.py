import telegram

from job_crawler.config import telegram_token

class TelegramNotifier:
    def __init__(self):
        self.__bot = telegram.Bot(token=telegram_token)
    
    def send(self, job: str):
        # updates = self.__bot.get_updates()
        # print("All updates:")
        # for update in updates:
        #     print(update)
        # TODO: figure out how to get chats where to send notifications

        self.__bot.send_message(text=f"Found a job: {job}", chat_id=474170033)
