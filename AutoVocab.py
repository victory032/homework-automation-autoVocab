# Creator: Nathan A
# Description: Does your vocab for you
# Creation Date: 8/25/2020
# Update Date: 
from PyDictionary import PyDictionary
dic = PyDictionary()
try:
    with open('vocab.txt', 'r') as words:
        for word in words:
            print(dic.meaning(word))
except():
    print('All Done')
