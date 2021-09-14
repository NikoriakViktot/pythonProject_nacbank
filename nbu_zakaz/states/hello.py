from telebot import types

from nbu_zakaz.states.base import BaseState
from nbu_zakaz.states.city_state import CityState
from nbu_zakaz.tg_buttons import CityStateButtons

user_filter = {}

class HelloState(BaseState):
    text = "Привет! Давай искать квартиры! Выбери город поиска, пожалуйста!"

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.keyboard.add(CityStateButtons.od_button)
        self.keyboard.add(CityStateButtons.ky_button)
        self.keyboard.add(CityStateButtons.kh_button)
        self.keyboard.add(CityStateButtons.lv_button)
        self.list_of_cities = ['Odessa', 'Kiev', 'Kharkov', 'Lvov']

    def proccess(self, message:types.Message):
        if hasattr(message, 'data'):
            for city in self.list_of_cities:
                if message.data == f'nextstate:{city}State':
                    user_filter = {self.chat_id: {}}
                    user_filter[self.chat_id] = {"city": city}
                    return CityState(user_filter, self.chat_id)
        return self
