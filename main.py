from translate import Translator
import xml.etree.ElementTree as ET
from time import sleep
import sys
import html

translator = Translator(to_lang=sys.argv[3])
tree = ET.parse(sys.argv[1])
root = tree.getroot()
print(chr(27) + "[2J")

for item in root.iter('string'):
    try:
        if item.attrib['translatable'] == "false":
            exit
    except:
        translation = translator.translate(item.text)
        a = '{} -> {}'.format((item.text), translation)
        print(a.encode('ascii', 'xmlcharrefreplace'))

        ask = input('Is this a good translation? n[no], q[close]: ')
        if ask == "n":
            correctTranslation = input('Write the correct translation here: ')
            correctTranslation = html.unescape(correctTranslation)
            item.text = correctTranslation
        elif ask == "q":
            sys.exit(0)
        else:
            item.text = translation

        tree.write(sys.argv[2])
        sleep(1)
        print('- - -')


print("Finish!")
