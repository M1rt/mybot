import telebot
from telebot import types



bot = telebot.TeleBot('6542782309:AAEPAV_AWIzV50WR-KAzsQeTLUSXps5D9co')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("/about_us")
    btn2 = types.KeyboardButton("/pay")
    btn3 = types.KeyboardButton('/help')
    markup.row(btn1, btn2, btn3)
    bot.send_message(message.chat.id, f'Привет!👋 Если ты видишь это сообщение, значит ты на правильном пути и ты готов зарабатывать и вправду хорошие деньги. Ты наверное хочешь узнать кто мы такие? Мы команда трейдеров с многолетним опытом, которые начинали осваивать эту нишу с самых низов. В этот курс вложена не только сухая теория, но и львиная доля нашего опыта, который мы приобрели через многие ошибки. В этот курс вложено все самое лучшее из других иностранных курсов, которые мы также разрабатывали вместе с китайскими, американскими, но в большинстве с итальянскими партнёрами.')
    bot.send_message(message.chat.id, f'Зачем мы сделали этот курс? Мы хотим обучить действительно талантливых людей этому ремеслу за символическую плату. Мы знаем, что если ты открыл этот бот и читаешь этот текст, то потенциал у тебя уже есть. Помни, самое главное это желание и упорство, это два основных качества, которые тебя приведут к успеху.')

@bot.message_handler(content_types=['text'])
def on_click(message):
    if message.text == '/about_us':
       bot.send_message(message.chat.id, 'Корса ди трейдинг, курсо де комерцио, candele giapoonesi итл, velas japonesas исп,Magnus cursus di trading Компания друзей👥 которые три года назад начали заниматься трейдингом, сделала курс, в который собрала все самое лучшее📈 из других курсов, которые они проходили, и опыт всех самых успешных трейдеров с которыми они имели дело, большинство которых были итальянцы🇮🇹.')
    elif message.text == '/pay':
        bot.send_message(message.chat.id,'Способы оплаты 💲1️⃣ А-bank 4323347383149140 2️⃣Monobank 5375411510335545 .После оплаты отправьте квитанцию о оплате нашему админу🧾 @vnmnk1')
    else:
        bot.send_message(message.chat.id,'❔По вопросам к нашему оператору:Вадим @vnmnk1👤')


bot.polling(none_stop=True)