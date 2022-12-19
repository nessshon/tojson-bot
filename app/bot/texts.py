class Text:
    strings = {
        "en": {
            "start": (
                "<b>Hi {}!</b>\n\n"
            ),
            "source": (
                "https://github.com/nessshon/to-json-bot"
            ),
        },
        "ru": {
            "start": (
                "<b>Привет {}!</b>\n\n"
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
