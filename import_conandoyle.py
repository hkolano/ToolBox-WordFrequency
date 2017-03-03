

import requests
import pickle

conandoyle_text = requests.get('http://www.gutenberg.org/ebooks/1661.txt.utf-8').text
f = open('conandoyle.pickle', 'wb')
pickle.dump(conandoyle_text, f)
f.close()
