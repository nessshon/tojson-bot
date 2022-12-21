class Text:
    strings = {
        "en": {
            "start": (
                "<b>Hi {}!</b>\n\n"
                "The bot will return all sent messages as a json.\n\n"
                "<b>Send or forward a message:</b>"
            ),
            "source": (
                "https://github.com/nessshon/to-json-bot"
            ),
        },
        "ru": {
            "start": (
                "<b>Привет {}!</b>\n\n"
                "Этот Бот вернет отправленные сообщения в виде json.\n\n"
                "<b>Отправьте или перешлите сообщение:</b>"
            ),
            "source": (
                "https://github.com/nessshon/to-json-bot"
            ),
        }
    }

    def __init__(self, language: str):
        self.language = language

    def get(self, key: str) -> str:
        return self.strings[self.language][key]
