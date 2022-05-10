import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    wordList = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    # Text in given web-page is stared under
    #the <div> tags with class <entry-content>
    for each_Text in soup.find_all('div', {'class' : 'entry-content' }):
        content = each_Text.text

        words = content.lower().split()

        for each_word in words:
            wordList.append(each_word)
        clean_wordlist(wordList)

def clean_wordlist(wordlist):
    clear_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/.,'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

            if len(word) > 0:
                clear_list.append(word)
        create_dictionary(clear_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print ("% s : %s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programing-language/?ref=leftbar")
