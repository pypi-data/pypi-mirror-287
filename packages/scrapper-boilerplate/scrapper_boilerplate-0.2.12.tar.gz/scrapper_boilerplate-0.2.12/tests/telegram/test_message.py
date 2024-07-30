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

    def test_send_message(self):
        msg = 'Teste de envio de mensagem!'
        status = self.bot.send_message(msg)
        self.assertTrue(status)

    