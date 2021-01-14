import pprint
from oxford import Word
Word.get('run')
a = Word.pronunciations()
pprint.pprint(a[0]['ipa'])