from telebot import types

from nbu_zakaz.config import bot
from nbu_zakaz.states.base import BaseState
from nbu_zakaz.tg_buttons import SearchButton
from nbu_zakaz.states.advviewer_state import AdvViewer
from nbu_zakaz import olx


class SearchState(BaseState):
    text = ""

    def __init__(self, user_filter, chat_id=None):
        super().__init__(chat_id)
        self.user_filter = user_filter
        bot.send_message(self.chat_id, f"Вы выбрали: {user_filter[chat_id]['city']}\nДиапазон цен: "
                                       f"от {user_filter[chat_id]['min_pr']} "
                                       f"до {user_filter[chat_id]['max_pr']}.",
                         reply_markup=self.keyboard.add(SearchButton.search))

    def proccess(self, message: types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:searchState':
                parcer = olx.OlxApi(self.user_filter[self.chat_id], 232145135)
                return AdvViewer(parcer.get_adv(), self.chat_id, self.user_filter)
        return self
