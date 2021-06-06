
import logging
from random import randrange
import random
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


#CHANGE YOU'R TOKEN JUST RIGHT HERE
TOKEN=''


def start(update: Update, context: CallbackContext) :
    welcome='Hello in order to use this bot only click on the button wich is marked "CLICK" ...\nYou can use /info to get more info about us ;)\n\nAlso join if youd like stay update https://t.me/erunpie'
    
    key_board=[
         [InlineKeyboardButton('CLICK', switch_inline_query_current_chat ='')],
       ] 

    update.message.reply_text(welcome,reply_markup=InlineKeyboardMarkup(key_board))
       
  

bra=[
    'https://i.etsystatic.com/5495056/r/il/2b2ca4/1004799508/il_570xN.1004799508_jrcf.jpg',
    'https://i.pinimg.com/originals/c1/39/0c/c1390cdd5e2cd252f0a086d89812a73a.jpg',
    'https://m.media-amazon.com/images/I/61Kwx7Sa0jL._AC_SL1010_.jpg',
    'https://images-na.ssl-images-amazon.com/images/I/61fjaNd8rTL._AC_SL1001_.jpg',
    'https://i.etsystatic.com/6802687/c/1062/844/168/0/il/302f7b/1983617481/il_340x270.1983617481_jwvr.jpg'
]
def sizer_cock():
    size = randrange(51)
    type= random.choice(['cm','in'])
    if size >= 15 :
        emoji =random.choice(['😏','😱','😂','😁'])
    if size <= 14 :
        emoji =random.choice(['😒','☹️','😣','🥺'])   
    text='My cock size is <b>%s'%size + type +'</b> '+ emoji
    return text
def breast_sizer():
    size= randrange(190)
    if size < 60 :
        advice ="My tits are smaller than you thought ... "
        emoji=random.choice(['😬','😑','🥴','😒','😕','😣','😖'])    
    if 86 >= size > 59 :
        advice = 'This <a href="%s"> bra </a> will make me beautiful!'%random.choice(bra)
        emoji=random.choice(['😜','🤪','😘','😗','😇','😁','😅'])
    if size >= 86 :
        advice="I have big tits and i don't need bra <b>DON'T PERV ON ME</b> 😡"
        emoji=random.choice(['😳','😢','🥺','🤩','💦','🤤'])
    text="My tits are <b>%s</b> "%size+emoji+' , '+advice
    return text
def vagina_type():
    types =[
    ('Curtains','https://s.yimg.com/ny/api/res/1.2/xDof2rM83Wu09_oQDf44iQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTk2MDtjZj13ZWJw/https://s.yimg.com/uu/api/res/1.2/6CqhO8eKQuKKQpmqrM76UA--~B/aD03MTc7dz03MTc7YXBwaWQ9eXRhY2h5b24-/http://media.zenfs.com/en-US/homerun/yourtango_760/f5d9bdc5e4370db925d8abf357c283cc'),
    ('Barbie','https://s.yimg.com/ny/api/res/1.2/HjF7L8RG572fm4jh0x8YeA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTk2MDtjZj13ZWJw/https://s.yimg.com/uu/api/res/1.2/s1BJUpHFwL5_JpQ5E7.nxw--~B/aD03MTc7dz03MTc7YXBwaWQ9eXRhY2h5b24-/http://media.zenfs.com/en-US/homerun/yourtango_760/7fbe23364335e1c61af31b0fb87bc5e0'),
    ('Puffs','https://s.yimg.com/ny/api/res/1.2/5fDprLVaC8c8oOWrr_8FLA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTk2MDtjZj13ZWJw/https://s.yimg.com/uu/api/res/1.2/0lZzmShZTK8g5YN4fmLW1A--~B/aD03MTc7dz03MTc7YXBwaWQ9eXRhY2h5b24-/http://media.zenfs.com/en-US/homerun/yourtango_760/c86f9ebd28f3448870176fa7c89d53f9'),
    ('Tulip','https://s.yimg.com/ny/api/res/1.2/C_OInaFkBzE3YmXG0l6Gbg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTk2MDtjZj13ZWJw/https://s.yimg.com/uu/api/res/1.2/ng0nC6oJ2Ni.0YxJEcjQnQ--~B/aD03MTc7dz03MTc7YXBwaWQ9eXRhY2h5b24-/http://media.zenfs.com/en-US/homerun/yourtango_760/caa6f0339501c126d4356234cc5966f9'),
    ('Horseshoe','https://s.yimg.com/ny/api/res/1.2/uA9fguQHlDisB40i0D.u4A--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTk2MDtjZj13ZWJw/https://s.yimg.com/uu/api/res/1.2/gtbr3mbdyZiGOh3jcXUypA--~B/aD03MTc7dz03MTc7YXBwaWQ9eXRhY2h5b24-/http://media.zenfs.com/en-US/homerun/yourtango_760/e596b5ef40c12efbd1017c43a470a148')
    ]
    type=random.choice(types)
    emoji=random.choice(['😳','😢','🥺','🤩','💦','🤤'])
    text='My pussy is <a href="%s">%s</a> '%(type[1],type[0])+emoji
    return text
def homo_sexual():
    percent= randrange(101)
    text= " I am <b>%s</b>"%percent+"<b>%</b>"+" homosexual (LGBT) 🏳️‍🌈"
    return text
    
def inlinequery(update: Update, _: CallbackContext) :
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="penis SIZE ",
            thumb_url='https://image.flaticon.com/icons/png/512/2688/2688326.png',
            input_message_content=InputTextMessageContent(sizer_cock(),parse_mode=ParseMode.HTML),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="breast SIZE",
            thumb_url='https://image.flaticon.com/icons/png/512/2688/2688244.png',
            input_message_content=InputTextMessageContent(breast_sizer(),parse_mode=ParseMode.HTML),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="vagina TYPES",
            thumb_url='https://image.flaticon.com/icons/png/512/392/392931.png',
            input_message_content=InputTextMessageContent(vagina_type(),parse_mode=ParseMode.HTML),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="homosexual MEASUREMENT",
            thumb_url='https://image.flaticon.com/icons/png/512/2620/2620829.png',
            input_message_content=InputTextMessageContent(homo_sexual(),parse_mode=ParseMode.HTML),
        ),
    ]

    update.inline_query.answer(results,cache_time=0)

def info(update: Update, context: CallbackContext) :
    update.message.reply_text('This is really simple bot wich is written in python by | @e_run_pie | \n If you want source code  visit : \nhttps://github.com/erunpie/inline-measurement')
def main() :
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start,run_async=True))
    dispatcher.add_handler(CommandHandler("info", info,run_async=True))
    dispatcher.add_handler(InlineQueryHandler(inlinequery,run_async=True))


    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    main()
