from googletrans import Translator

def translate(word):
    translator = Translator()
    translated = translator.translate(word, src="en", dest="ja");
    print(translated)

# main処理
def main():
    word = input("英語を入れてください:")
    translate(word)
    

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
