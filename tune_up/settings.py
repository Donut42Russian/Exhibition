import json

settings_original = {}
settings_original['RPI1'] = ['192.168.1.56', None]
settings_original['RPI2'] = ['192.168.1.187', None]
#settings_original['RPI3'] = ['', None]
#settings_original['RPI4'] = ['', None]



class Settings:

    def __init__(self, pathSettings: str):
        self.pathSettings = pathSettings

        self.settings = None
        self.loadSettings()

    def loadSettings(self):
        try:
            with open(self.pathSettings, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                self.settings = json.load(fh)  # загружаем из файла данные в словарь settings
        except BaseException:
            with open(self.pathSettings, 'w', encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(settings_original, ensure_ascii=False))

    def saveSettings(self):
        with open(self.pathSettings, 'w',
                  encoding='utf-8') as fh:  # открываем файл на запись
            fh.write(json.dumps(self.settings, ensure_ascii=False))

    def updateSettings(self, settings: dict):
        self.settings.update(settings)

#
