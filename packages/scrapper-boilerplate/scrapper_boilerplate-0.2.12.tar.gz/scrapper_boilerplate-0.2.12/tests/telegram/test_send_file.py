import unittest
import os
from dotenv import load_dotenv
from scrapper_boilerplate.telegram import TelegramBot



class TestTelegramBot(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.TOKEN = os.getenv('TELEGRAM_TOKEN')
        self.CHAT_ID = [os.getenv('TELEGRAM_CHAT_ID')]
        self.bot = TelegramBot(self.TOKEN, self.CHAT_ID)

    def test_send_file(self):
        filename = "test.jpg"
        self.bot.send_file(filename)