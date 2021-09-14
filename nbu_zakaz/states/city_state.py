from telebot import types
from nbu_zakaz.config import price_chooser

from nbu_zakaz.states.base import BaseState
from nbu_zakaz.states.search_state import SearchState
from nbu_zakaz.tg_buttons import PriceStateButtons
from pprint import pprint


class CityState(BaseState):
    text = "Выбери бюджет, пожалуйста."

    def __init__(self, user_filter,  chat_id=None):
        super().__init__(chat_id)
        self.user_filter = user_filter
        self.keyboard.add(PriceStateButtons.f2t5State)
        self.keyboard.add(PriceStateButtons.f5t7State)
        self.keyboard.add(PriceStateButtons.f7t10State)
        self.list_of_prices = ['f2t5', 'f5t7', 'f7t10']

    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            for price in self.list_of_prices:
                if message.data == f'nextstate:{price}State':
                    a, b = price_chooser(price)
                    self.user_filter[self.chat_id]['min_pr'] = a
                    self.user_filter[self.chat_id]['max_pr'] = b
                    return SearchState(self.user_filter, self.chat_id)
        return self
