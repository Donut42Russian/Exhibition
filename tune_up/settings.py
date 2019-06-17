import json

settings_original = {
    "RPI": {
        #"RPI1": ['', None],
        "RPI2": ['192.168.1.56', None],
        "RPI3": ['192.168.1.171', None], #192.168.1.187,
        #"RPI4": ['', None],
    }
}

class Settings:

    def __init__(self, pathSettings: str):
        self.pathSettings = pathSettings
        self.settings = None
        self.loadSettings()


    def loadSettings(self):
        try:
            with open(self.pathSettings, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                self.settings = json.load(fh)  # загружаем из файла данные в словарь data
        except BaseException:
            with open(self.pathSettings, 'w',
                      encoding='utf-8') as fh:  # открываем файл на запись
                fh.write(json.dumps(settings_original, ensure_ascii=False))


    def saveSettings(self):
        with open(self.pathSettings, 'w',
                  encoding='utf-8') as fh:  # открываем файл на запись
            fh.write(json.dumps(self.settings, ensure_ascii=False))

    def updateSettings(self, settings: dict):
        self.settings.update(settings)



if __name__ == '__main__':
    pathSettings = r'settings'
    testSettings = Settings(pathSettings)
    #testSettings.loadSettings()
    print(testSettings.settings['president'])


    # updateS = {
    #     "president": {
    #         "name": "11111",
    #         "species": "dfsdfsdfdsf"
    #     }
    # }
    # testSettings.updateSettings(updateS)
    # print(testSettings.settings)
    # testSettings.saveSettings()
