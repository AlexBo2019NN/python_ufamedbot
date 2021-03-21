# -*- coding: utf-8 -*-
"""

@author: User
"""
import pickle  #for saving trained model
import pandas as pd
import telebot
import re
import config
import send_mail as sm

PATH_TO_DATA='d:/Python_ufa_med_bot/'  #working dir
#регулярное выражение с помощью которого будет токенизировать колонку description
TOKEN_RE = re.compile(r'[\w\d]+')  #regular expression to start with

def tokenize_text_simple_regex(txt, min_token_size=2):
    """ This func tokenize text with TOKEN_RE applied ealier """
    txt = txt.lower()
    all_tokens = TOKEN_RE.findall(txt)
    return [token for token in all_tokens if len(token) >= min_token_size]
# load the model from disk
filename=PATH_TO_DATA+'model_ufa_rf07.pickle'
model = pickle.load(open(filename, 'rb'))

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    start_message='''✌️✌️✌️✌️✌️Это бот-помошник по медицинским вопросам.\n\
                 Как записаться к врачу?\n\
                 Какие есть вакцины от короновирсуса?\n\
                 Это и много другое я уже знаю!✌️✌️✌️✌️✌️\n'''
    bot.reply_to(message,start_message)
    
    
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    token=message.text
    ask_list=[]
    ask_list.append(token)
    #let s make dict and then data frame
    dict_train={'Vopros':ask_list}
    df=pd.DataFrame.from_dict(dict_train)
    answer=model.predict(df['Vopros'])
    print('Vopros: ',token)    #we print that for debiging
    print(type(answer))
    print('Otvet: '+answer)
    sm.send_mail(str(token),
                 str(answer))

    bot.send_message(message.chat.id, answer)
if __name__ == '__main__':
    print('bot started.')
    bot.polling(none_stop=True)