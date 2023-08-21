
import gettext

class LocalizationAccessibility:
    def __init__(self, language):
        self.language = language
        self.translator = gettext.translation('base', localedir='locales', languages=[self.language], fallback=True)

    def translate(self, msg):
        return self.translator.gettext(msg)

if __name__ == "__main__":
    la = LocalizationAccessibility('es')
    print(la.translate("Hello, World!"))
