
import discord

import re
import unicodedata
import string
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in string.printable
    )

class DDClient(discord.Client):
    def getTextChannels(self):
        chans = []
        for i in self.get_all_channels():
            if str(i.type) == 'text':
                chans.append(i)
        return chans

    async def getMessagesFromUser(self, user):
        all_msg = []
        chans = self.getTextChannels()
        count = 0
        for i in chans:
            print('Working on chan: '+i.name)
            messages = await i.history(limit = 69000).flatten()
            for msg in messages:
                if msg.author == user:
                    all_msg.append(msg)
            print('Got all msgs from channel: '+i.name)
            print('Total messages from chan got: '+str(len(messages)))
            count += len(messages)
        print('Total messages: '+str(count)+'\n')
        return all_msg

    async def dirty(self, user):
        messages = await self.getMessagesFromUser(user)
        print('Got '+str(len(messages))+" messages")
        text = ' '
        dirty_list = []
        for msg in messages:
            text += msg.content+' '
        text = unicodeToAscii(text)
        text = text.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('"', ' ').replace('\'', ' ').replace('!', ' ').replace('-', ' ').replace('\r', ' ')
        #print(text)
        amount = 0
        for word in word_list:
            #word_amount = text.count(word+' ')
            word_amount = len(re.findall(re.compile(word+'\\b'), text))
            if word_amount > 0:
                amount += word_amount
                dirty_list.append([word, word_amount])
        dirty_list.sort(key=lambda l: l[1], reverse=True)
        return amount, len(messages), text.count(' '), dirty_list

    async def help(self, channel):
        await channel.send("just ask: 'how dirty am i?'")

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!\n')

    async def on_message(self, message):

        if message.author == client.user:  # ignore our own messages
            return
        print("I got a message: " + str(message.content) + " from user: " + str(message.author))  # otherwise log msg

        if message.content == 'help me daddy!':
            self.help(message.channel)
            return

        if message.content == 'how dirty am i?':
            await message.channel.send('Working on ' +str(message.author))
            bad_words, message_count, word_count, dirty_list = await self.dirty(message.author)
            response = '@'+str(message.author)+'\n'
            response += "You have said "+str(word_count)+" words in "+str(message_count)+" messages. You have used "+str(bad_words)+" bad word(s).\n"
            response += "That's "+str(round(100 * bad_words/word_count, 4))+"% of your words, or average "+str(round(100 * bad_words/message_count, 4))+"% of your messages\n"

            if bad_words > 0:
                response += "You most used naughty words are:\n"
                count = 0
                for itt in dirty_list:
                    response += itt[0] + ":\t\t" + str(itt[1]) + '\n'
                    count += 1
                    if count == 10:
                        break
            if bad_words / message_count > .075:
                response += 'You are very dirty'
            elif bad_words / message_count > .02:
                response += 'You are a little dirty'
            else:
                response += 'You are not too dirty'
            await message.channel.send(response)
            return
'''
        if message.content == 'tes':
            his = await message.channel.history(limit = 2000).flatten()
            content = ''
            for itt in his:
                content += itt.content
            await message.channel.send("#: "+str(len(his)))
            print(content)
            return

        if message.content == "msg":
            msgs = await self.getMessagesFromUser(message.author)
            await message.channel.send('#: ' + str(len(msgs)))
            return

        if message.content == "run":
            for i in range(201):
                await message.channel.send('#: '+str(i))
            return

'''
if __name__ == "__main__":
    TOKEN = "####"
    word_list = open('words.txt', 'r') .read().strip().split(',')
    client = DDClient()
    client.run(TOKEN)
