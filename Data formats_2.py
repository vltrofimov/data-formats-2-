def word_counter (list_of_words):

    for word in sorted(list_of_words):
        if len(word) < 6:
            list_of_words.remove(word)
    list_of_word_lower=[x.lower() for x in list_of_words]
    current_word = sorted(list_of_word_lower)[0]
    word_counter = 0
    word_dict = {}
    list_of_quantity = []
    for word in sorted(list_of_word_lower):
        if current_word == word:
            word_counter += 1
        else:
            word_dict[word_counter] = current_word
            current_word = word
            word_counter = 1
            list_of_quantity=[]
    for key in sorted(word_dict.keys(), reverse=True):
        list_of_quantity.append(key)
    for quantity in list_of_quantity[0:10]:
        for key in sorted(word_dict.keys(), reverse=True):
            if quantity == key:
                print(f"слово '{word_dict[key]}' встречается {key} раз")


import xml.etree.ElementTree as ET
tree = ET.parse('newsafr.xml')
news=tree.iter("description")
list_of_w=[]
for new in news:
   list_of_w+=new.text.split()
word_counter(list_of_w)