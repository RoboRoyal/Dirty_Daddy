


word_list = open('words.txt', 'r').read().strip().split(',')



messages = ['asd','asd',' ass ','asd']
text = ' '
dirty_list = []
for msg in messages:
    text += msg.lower()

amount = 0
for word in word_list:
    word_amount = text.count(word)
    if word_amount > 0:
        amount += word_amount
        dirty_list.append([word, word_amount])

print(amount)
print(len(messages))
print(text.count(' ')+len(messages))
print(dirty_list)

m = ' hello hello dirty dirty dirty dirty a ahole b dirty dirty ahole dirty dirty a_s_s  a2m  a54  a55  a55hole  acrotomophilia dirty a_s_s dirty 1 2 3 4 5 dirty dirty dirty dirty dirty dirty dirty dirty dirty dirty 5h1t dirty 5h1t dirty dirty dirty msg chan chan chan chan tes tes tes tes tes tes tes tes help me daddy   dirty hello hello hello me? dirty dirty dirty dirty dirty 2g1c 2g1c 2g1c 2g1c dirty dirty dirty dirty dirty dirty dirty dink dink dink dirty dirty dirty dirty dirty dirty ass ass ass ass ass dirty msg msg msg msg msg msg msg msg tes tes run'
import re
word = 'ass'
word = '\\b'+word+'\\b'
#word = r'\bass\b'
word = re.compile(word)
print(word)
print(len(re.findall(word, m)))
