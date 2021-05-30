import re
from collections import Counter
def vogais(string):
    return Counter(re.sub('[^aeiouAEIOU]', '', string))

pal = input('Digite uma palavra: ')
print(vogais(pal))