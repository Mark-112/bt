import telebot
from telebot import types
import json
import time


def get_user_file_way(id):
    return 'D:/yulia_bot/' + id + '.json'

def user_to_json(user):

    user_id = user['user_id']
    way = get_user_file_way(user_id)
    
    with open(way, 'w', encoding='utf-8') as file:
        json.dump(user, file, ensure_ascii=False, indent=3)

    return None

def user_from_json(id):

    way = get_user_file_way(id)

    with open(way, encoding='utf-8') as file:
            user = json.load(file)

    return user

def users():

    lst = []
    with open('D:/yulia_bot/users.txt', 'r', encoding='utf-8') as file:
        for line in file:
            lst.append(line.strip())

    return lst

def create_user(id, username):

    with open('D:/yulia_bot/users.txt', 'a', encoding='utf-8') as file:
        file.write(id)
        file.write('\n')

    way = get_user_file_way(id)
    user = {'user_id' : id, 'username': username, 'intresting_products': [0], 'filled_form': False, 'initial_information_received': False, 'viewed_products': [], 'form': {}}
    user_to_json(user)

    return None
 
def interesting_products(id):

    user = user_from_json(id)

    products = user['intresting_products']
    if products[0] == 0:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        button_1 = types.KeyboardButton("Управление персоналом")
        button_2 = types.KeyboardButton("Все о продажах")
        button_3 = types.KeyboardButton("Развитие бизнеса")
        button_4 = types.KeyboardButton("Личностное развитие (карьера) и выбор пути")
        button_5 = types.KeyboardButton("Баланс!")
        button_6 = types.KeyboardButton("Все интересно")
        button_7 = types.KeyboardButton("Больше ничего не интересно")

        if products == [0]:
            flag = 1
        else:
            flag = 0

        if 'Управление персоналом' not in products:
            keyboard.add(button_1)
        if 'Все о продажах' not in products:
            keyboard.add(button_2)
        if 'Развитие бизнеса' not in products:
            keyboard.add(button_3)
        if 'Личностное развитие (карьера) и выбор пути' not in products:
            keyboard.add(button_4)
        if 'Баланс!' not in products:
            keyboard.add(button_5)

        keyboard.add(button_6, button_7)
        bot.send_message(id, ['Может что-то еще?', 'Выбери, что тебе интересно'][flag],  reply_markup=keyboard)

    return None

def add_user_intresting_product(id, product):

    user = user_from_json(id)

    if product not in user['intresting_products']:
        user['intresting_products'].append(product)
        user['viewed_products'].append(product)

    user_to_json(user)

    return None

def all_intresting(id):

    user = user_from_json(id)

    user['intresting_products'] = ['Управление персоналом', 'Все о продажах', 'Развитие бизнеса', 'Личностное развитие (карьера) и выбор пути', 'Баланс!']

    user_to_json(user)

    return None


def no_more_intresting(id):
    user = user_from_json(id)

    user['intresting_products'] = user['intresting_products'][1:]

    user_to_json(user)

    return None

def del_keyboard(id):

    void_keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(id, 'Спасибо!', reply_markup=void_keyboard)

    return None

def selected_products(id):

    user = user_from_json(id)

    if user['intresting_products'][0] == 0:
        return False
    
    return True

def send_description_otp(id):

    user = user_from_json(id)
    if len(user['intresting_products']) == 1 and user['intresting_products'][0] != 'Иное':
        for product in user['intresting_products']:
            if product == 'Управление персоналом':
                text =  '\U00002049' + '''Тебе нужна эффективная команда?
или
''' + '\U00002049' + '''Твои сотрудники работают в пол силы?
или
''' + '\U00002049' + '''Все приходится делать самому, никому доверять нельзя, все сделают не то и не так!

Если у тебя один из этих или схожий запрос - Получишь ответы и решения в программе «Управление персоналом»
''' + '\U00002705' + '''Подбор персонала
''' + '\U00002705' + '''Командообразование
''' + '\U00002705' + '''Делегирование
''' + '\U00002705' + '''Мотивация
''' + '\U00002705' + '''Лояльность сотрудников
''' + '\U00002705' + '''Обучение персонала
''' + '\U00002705' + '''многое другое в т.ч. вопросы личностного развития…

Результат ''' + '\U0001F4B0' + ''' – эффективная команда, работающая на результат. И для Вас лично – работа в удовольствие!
'''
                bot.send_message(id, text)
            if product == 'Все о продажах':
                text = '''На продажах зиждится бизнес! 
Грамотные и качественные продажи приносят доход компании. Если ты заинтересован в увеличении своего дохода, то прокачивай себя или свою команду в продажах!

''' + '\U00002705' + '''Анализ рынка  
''' + '\U00002705' + '''Планирование 
''' + '\U00002705' + '''(Воронка продаж?) 
''' + '\U00002705' + '''Тайм-менеджмент 
''' + '\U00002705' + '''Этапы продаж 
''' + '\U00002705' + '''ПЕРЕГОВОРЫ 
''' + '\U00002705' + '''Клиентоориентированность 
''' + '\U00002705' '''и многое другое в т.ч. вопросы личностного развития… 

Твой результат ''' + '\U0001F4B0' + ''' – увеличение дохода! Успешность и уверенность в завтрашнем дне.
'''
                bot.send_message(id, text)
            if product == 'Развитие бизнеса':
                text = '''В твоем бизнесе уже все происходит по накатанной, бизнес приносит постоянный ровный доход, и нет необходимости его развивать? Это тревожные звоночки стагнации и дальнейшего регресса.  
Чтобы твой бизнес процветал и приносил доход Х2 –Х5-Х10 и более  - Пора покорять новые бизнес вершины и достигать новые цели! 
''' + '\U00002705' + '''Аудит текущей ситуации 
''' + '\U00002705' + '''Новые цели и стратегии 
''' + '\U00002705' + '''Саморазвитие 
''' + '\U00002705' + '''Масштабирование 
''' + '\U00002705' + '''Лидерство и баланс 
И многое другое вы получите в программе «Развитие бизнеса». 
'''
                bot.send_message(id, text)
            if product == 'Личностное развитие (карьера) и выбор пути':
                text = '''« … И тогда я  зажмурилась, вынула из кармана воображаемый ножик и стала нарезать туман на аккуратные кирпичики и складывать стены своего будущего. Мысленно я раскрашивала их в разные цвета, так что будущее получалось ярким и радужным. Я очень старалась! 
А когда я открыла глаза… Туман отступил, а передо мной стоял прекрасный дворец с арками и цветами – все, как придумывалось. Да, такое будущее вызывало только радость и желание к нему стремиться.  
Пусть это была всего лишь модель, но я сумею воплотить ее в жизнь!» 
Вышел ежик из тумана (Сказки Эльфики (Ирина Семина)) 

В этой программе как в сказке происходит волшебство – преображение.  
Теперь ты: 
''' + '\U00002705' + '''Видишь истинные цели 
''' + '\U00002705' + '''Работаешь с мышлением 
''' + '\U00002705' + '''Работаешь с денежным мышлением 
''' + '\U00002705' + '''Получаешь свои ресурсы 
''' + '\U00002705' + '''Знакомишься с Лидерством и Балансом! 
''' + '\U00002705' + '''Уверенно движешься к цели и достигаешь её! 
'''
                bot.send_message(id, text)
            if product == 'Баланс!':
                text = '''Баланс — система показателей, которые характеризуют соотношение или равновесие в каком-либо постоянно изменяющемся явлении.  
Мы перекладываем эту формулировку на нашу настоящую жизнь. И хотим, чтобы все аспекты нашей жизни были уравновешенны. 
'''
                bot.send_message(id, text)
                img = open('D:/yulia_bot/scale_1200.jpeg', 'rb')
                bot.send_photo(id, img)
                time.sleep(1)
                text = '''А ты этого хочешь? Хочешь, чтобы твоя жизнь была гармоничной и сбалансированной? Чтобы было время заниматься любимыми делами? Чтобы работа не занимала 24/7? Семья, Отношения, Карьера – не стояло выбора, что приоритетно?
                '''
                bot.send_message(id, text)

    user['initial_information_received'] = True

    user_to_json(user)
 
    return None

def initial_information_received(id):

    user = user_from_json(id)

    return user['initial_information_received']

def offer_a_survey(id):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = types.KeyboardButton("Заполнить анкету")
    keyboard.add(button)
    text = '\U0001F447' + 'Расскажи немного о себе' + '\U0001F447'
    bot.send_message(id, text,  reply_markup=keyboard)

    return None

def filled_form(id):

    user = user_from_json(id)

    return user['filled_form']

def survey(id, text):

    user = user_from_json(id)

    if 'Имя' not in user['form']:
        user['form']['Имя'] = text

        bot.send_message(id, "Тел.")

    elif 'Телефон' not in user['form']:
        user['form']['Телефон'] = text

        void_keyboard = telebot.types.ReplyKeyboardRemove()

        bot.send_message(id, "e-mail", reply_markup=void_keyboard)

    elif 'e-mail' not in user['form']:
        user['form']['e-mail'] = text
        
        keyboard = types.ReplyKeyboardMarkup()

        button_1 = types.KeyboardButton("до 18")
        button_2 = types.KeyboardButton("18-23")
        button_3 = types.KeyboardButton("24-29")
        button_4 = types.KeyboardButton("30-35")
        button_5 = types.KeyboardButton("36-45")
        button_6 = types.KeyboardButton("46-55")
        button_7 = types.KeyboardButton("56+")

        keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)

        bot.send_message(id, "Выберите ваш возраст", reply_markup=keyboard)

    elif 'Возраст' not in user['form']:
        user['form']['Возраст'] = text

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

        button_1 = types.KeyboardButton("Санкт-Петербург")
        button_2 = types.KeyboardButton('Москва')

        keyboard.add(button_1, button_2)

        bot.send_message(id, 'Введите ваш город, или выберете из предложенных', reply_markup=keyboard)

    elif 'Город' not in user['form']:
        user['form']['Город'] = text

        keyboard = types.ReplyKeyboardMarkup()

        button_1 = types.KeyboardButton("Предприниматель/свой бизнес")
        button_2 = types.KeyboardButton("Фрилансер")
        button_3 = types.KeyboardButton("Менеджер по продажам")
        button_4 = types.KeyboardButton("Гос. структура")

        keyboard.add(button_1, button_2, button_3, button_4)

        bot.send_message(id, "Введите сферу деятельности или выберите из предложенных", reply_markup=keyboard)

    elif 'Сфера деятельности' not in user['form']:
        user['form']['Сфера деятельности'] = text

        keyboard = types.ReplyKeyboardMarkup()

        button_1 = types.KeyboardButton("Упал")
        button_2 = types.KeyboardButton("Вырос")
        button_3 = types.KeyboardButton("Остался прежним")
        button_4 = types.KeyboardButton("Другое")

        keyboard.add(button_1, button_2, button_3, button_4)

        bot.send_message(id, "За последние полгода ваш уровень дохода", reply_markup=keyboard)

    elif 'Уровень дохода за последние полгода' not in user['form']:
        user['form']['Уровень дохода за последние полгода'] = text

        void_keyboard = telebot.types.ReplyKeyboardRemove()

        bot.send_message(id, "Что в вашей работе вас не устраивает/утомляет?", reply_markup=void_keyboard)

    elif 'Что не устраивает' not in user['form']:
        user['form']['Что не устраивает'] = text

        void_keyboard = telebot.types.ReplyKeyboardRemove()
        bot.send_message(id, 'Какой вопрос вы хотели бы обсудить?', reply_markup=void_keyboard)

    elif 'Какой вопрос вы хотели бы обсудить?' not in user['form']:
        user['form']['Какой вопрос вы хотели бы обсудить?'] = text

        keyboard = types.ReplyKeyboardMarkup()

        button_1 = types.KeyboardButton("Неделю")
        button_2 = types.KeyboardButton("2 недели")
        button_3 = types.KeyboardButton("2 недели + 2 недели сопровождения")
        button_4 = types.KeyboardButton("4 недели")
        button_5 = types.KeyboardButton("Более 1 месяца")
        button_6 = types.KeyboardButton("Более 2 месяцев")
        button_7 = types.KeyboardButton('Более 6 месяцев')

        keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)

        bot.send_message(id, "Сколько времени готовы уделить приобретению новых возможностей по вашему запросу?", reply_markup=keyboard)

    elif 'Длительность курса' not in user['form']:
        user['form']['Длительность курса'] = text

        keyboard = types.ReplyKeyboardMarkup()

        button_1 = types.KeyboardButton("Да")
        button_2 = types.KeyboardButton("Нет")

        keyboard.add(button_1, button_2)

        bot.send_message(id, 'Работали ли вы ранее с консультантами, менторами, наставниками', reply_markup=keyboard)

    elif 'Работали ли вы ранее с консультантами, менторами, наставниками' not in user['form']:
        user['form']['Работали ли вы ранее с консультантами, менторами, наставниками'] = text

        if text == 'Да':

            void_keyboard = telebot.types.ReplyKeyboardRemove()
            bot.send_message(id, 'Что вам понравилось в работе?', reply_markup=void_keyboard)

        else:

            void_keyboard = telebot.types.ReplyKeyboardRemove()
            bot.send_message(id, 'Отправь мне в личку @YuliyaSamorukova "' + '\U0001F91D' +'" и я свяжусь с тобой, чтобы ответить на твои вопросы в удобное время.\n' + 'Благодарю за ответы!', reply_markup=void_keyboard)
            bot.send_message(id, 'Мой канал https://t.me/consulting_personal_development.\nПрисоединяйся!' + '\U0001F44B')
            user['filled_form'] = True
            other_products(id)

            with open('D:/yulia_bot/new_forms.txt', 'a', encoding='utf-8') as file:
                file.write(user['username'] + ' ')
                file.write(user['user_id'])
                file.write('\n')

        bot.send_message(get_admin_id(), 'Пользователь ' + user['username'] + ', id: ' + user['user_id'] + ' заполнил(а) анкету')
    
    elif ('Что понравилось' not in user['form']) and (user['form']['Работали ли вы ранее с консультантами, менторами, наставниками'] == 'Да'):
        user['form']['Что понравилось'] = text

        void_keyboard = telebot.types.ReplyKeyboardRemove()
        bot.send_message(id, 'Что не понравилось, было непонятно?', reply_markup=void_keyboard)

    elif ('Что не понравилось' not in user['form']) and (user['form']['Работали ли вы ранее с консультантами, менторами, наставниками'] == 'Да'):
        user['form']['Что не понравилось'] = text

        bot.send_message(id, 'Отправь мне в личку @YuliyaSamorukova "' + '\U0001F91D' + '" и я свяжусь с тобой, чтобы ответить на твои вопросы в удобное время.\n' + 'Благодарю за ответы!')
        bot.send_message(id, 'Мой канал https://t.me/consulting_personal_development.\nПрисоединяйся!' + '\U0001F44B')
        

        user['filled_form'] = True
        other_products(id)


        with open('D:/yulia_bot/new_forms.txt', 'a', encoding='utf-8') as file:
            file.write(user['username'] + ' ')
            file.write(user['user_id'])
            file.write('\n')

        bot.send_message(get_admin_id(), 'Пользователь ' + user['username'] + ', id: ' + user['user_id'] + ' заполнил(а) анкету')
        

    user_to_json(user)

    return None


def other_products(id):
    
    user = user_from_json(id)

    keyboard = types.ReplyKeyboardMarkup()

    button_1 = types.KeyboardButton('Личностное развитие (карьера) и выбор пути')
    button_2 = types.KeyboardButton('Баланс!')
    button_3 = types.KeyboardButton('Все о продажах')
    button_4 = types.KeyboardButton('Управление персоналом')
    button_5 = types.KeyboardButton('Развитие бизнеса')

    if 'Личностное развитие (карьера) и выбор пути' not in user['viewed_products']:
        keyboard.add(button_1)
    if 'Баланс!' not in user['viewed_products']:
        keyboard.add(button_2)
    if 'Все о продажах' not in user['viewed_products']:
        keyboard.add(button_3)
    if 'Управление персоналом' not in user['viewed_products']:
        keyboard.add(button_4)
    if 'Развитие бизнеса' not in user['viewed_products']:
        keyboard.add(button_5)

    bot.send_message(id, 'Узнать о других программах', reply_markup=keyboard)



def get_admin_id():
    return  '1374518685'
    #return '1259111272'



bot = telebot.TeleBot('5906307857:AAG5I_l7VKetrNZDbdEIaVpPZ_WP3rSeBTg')


@bot.message_handler(commands=["start"])
def start(message, res=False):

    user_id = str(message.chat.id)
    username = message.from_user.username

    first_name = message.from_user.first_name

    text = first_name + ''', здравствуйте и добро пожаловать в чат бот! В этом чат боте мы поближе познакомимся

Меня зовут Юлия Саморукова - Я Наставник, Ментор, Консультант по бизнесу и личностному росту. Оказываю Консалтинговые услуги в сфере продаж.

Имею опыт работы более 20 лет в разных сферах бизнеса.''' + '''\U0001F4C8
''' + '''\nС 2010г. занимаюсь продажами, управлением и развитием персонала. 
За это время многие региональные филиалы компаний вывела на уверенное развитие и рост, увеличив их выручку х3-х10!''' + '''\U0001F4B0
''' + '''\nПрименяю индивидуальные подходы к решению задач.''' + '''\U0000221A
''' + '''\nСказкотерапевт.''' + '\U0001F4D6'

    bot.send_message(message.chat.id, text)

    if user_id not in users():
        create_user(user_id, username)

    interesting_products(user_id)
 
 
@bot.message_handler(content_types=["text"])
def handle_text(message):

    user_id = str(message.from_user.id)
    username = message.from_user.username
    user_text = message.text.strip()

    if user_id != get_admin_id():
        pass

    else:

        if not selected_products(user_id):

            if user_text in ['Управление персоналом', 'Все о продажах', 'Развитие бизнеса', 'Личностное развитие и выбор пути', 'Баланс!']:     
                add_user_intresting_product(user_id, user_text)

            if user_text == 'Все интересно':
                all_intresting(user_id)
                del_keyboard(user_id)

            if user_text == 'Больше ничего не интересно':
                no_more_intresting(user_id)
                del_keyboard(user_id)

            interesting_products(user_id)

        if selected_products(user_id):

            if not initial_information_received(user_id):
                send_description_otp(user_id)
                offer_a_survey(user_id)

            if not filled_form(user_id):
                if user_text != 'Больше ничего не интересно' and user_text != 'Все интересно':
                    if user_text != 'Заполнить анкету':
                        survey(user_id, user_text)
                    else:
                        void_keyboard = telebot.types.ReplyKeyboardRemove()
                        bot.send_message(user_id, 'Введите имя', reply_markup=void_keyboard)
            else:
                
                user = user_from_json(user_id)

                if user_text == 'Личностное развитие (карьера) и выбор пути':
                    user['viewed_products'].append('Личностное развитие (карьера) и выбор пути')
                    text = '''« … И тогда я  зажмурилась, вынула из кармана воображаемый ножик и стала нарезать туман на аккуратные кирпичики и складывать стены своего будущего. Мысленно я раскрашивала их в разные цвета, так что будущее получалось ярким и радужным. Я очень старалась! 
А когда я открыла глаза… Туман отступил, а передо мной стоял прекрасный дворец с арками и цветами – все, как придумывалось. Да, такое будущее вызывало только радость и желание к нему стремиться.  
Пусть это была всего лишь модель, но я сумею воплотить ее в жизнь!» 
Вышел ежик из тумана (Сказки Эльфики (Ирина Семина)) 

В этой программе как в сказке происходит волшебство – преображение.  
Теперь ты: 
''' + '\U00002705' + '''Видишь истинные цели 
''' + '\U00002705' + '''Работаешь с мышлением 
''' + '\U00002705' + '''Работаешь с денежным мышлением 
''' + '\U00002705' + '''Получаешь свои ресурсы 
''' + '\U00002705' + '''Знакомишься с Лидерством и Балансом! 
''' + '\U00002705' + '''Уверенно движешься к цели и достигаешь её! 
'''
                    bot.send_message(user_id, text)

                elif user_text == 'Баланс!':
                    user['viewed_products'].append('Баланс!')
                    text = '''Баланс — система показателей, которые характеризуют соотношение или равновесие в каком-либо постоянно изменяющемся явлении.  
Мы перекладываем эту формулировку на нашу настоящую жизнь. И хотим, чтобы все аспекты нашей жизни были уравновешенны. 
'''
                    bot.send_message(user_id, text)
                    img = open('D:/yulia_bot/scale_1200.jpeg', 'rb')
                    bot.send_photo(user_id, img)
                    time.sleep(1)
                    text = '''А ты этого хочешь? Хочешь, чтобы твоя жизнь была гармоничной и сбалансированной? Чтобы было время заниматься любимыми делами? Чтобы работа не занимала 24/7? Семья, Отношения, Карьера – не стояло выбора, что приоритетно?
                    '''
                    bot.send_message(user_id, text)

                elif user_text == 'Все о продажах':
                    user['viewed_products'].append('Все о продажах')

                    text = '''На продажах зиждится бизнес! 
Грамотные и качественные продажи приносят доход компании. Если ты заинтересован в увеличении своего дохода, то прокачивай себя или свою команду в продажах!

''' + '\U00002705' + '''Анализ рынка  
''' + '\U00002705' + '''Планирование 
''' + '\U00002705' + '''(Воронка продаж?) 
''' + '\U00002705' + '''Тайм-менеджмент 
''' + '\U00002705' + '''Этапы продаж 
''' + '\U00002705' + '''ПЕРЕГОВОРЫ 
''' + '\U00002705' + '''Клиентоориентированность 
''' + '\U00002705' '''и многое другое в т.ч. вопросы личностного развития… 

Твой результат ''' + '\U0001F4B0' + ''' – увеличение дохода! Успешность и уверенность в завтрашнем дне.
'''
                    bot.send_message(user_id, text)

                elif user_text == 'Управление персоналом':
                    user['viewed_products'].append('Управление персоналом')

                    text =  '\U00002049' + '''Тебе нужна эффективная команда?
или
''' + '\U00002049' + '''Твои сотрудники работают в пол силы?
или
''' + '\U00002049' + '''Все приходится делать самому, никому доверять нельзя, все сделают не то и не так!

Если у тебя один из этих или схожий запрос - Получишь ответы и решения в программе «Управление персоналом»
''' + '\U00002705' + '''Подбор персонала
''' + '\U00002705' + '''Командообразование
''' + '\U00002705' + '''Делегирование
''' + '\U00002705' + '''Мотивация
''' + '\U00002705' + '''Лояльность сотрудников
''' + '\U00002705' + '''Обучение персонала
''' + '\U00002705' + '''многое другое в т.ч. вопросы личностного развития…

Результат ''' + '\U0001F4B0' + ''' – эффективная команда, работающая на результат. И для Вас лично – работа в удовольствие!
'''
                    bot.send_message(user_id, text)

                elif user_text == 'Развитие бизнеса':
                    user['viewed_products'].append('Развитие бизнеса')
                    text = '''В твоем бизнесе уже все происходит по накатанной, бизнес приносит постоянный ровный доход, и нет необходимости его развивать? Это тревожные звоночки стагнации и дальнейшего регресса.  
Чтобы твой бизнес процветал и приносил доход Х2 –Х5-Х10 и более  - Пора покорять новые бизнес вершины и достигать новые цели! 
''' + '\U00002705' + '''Аудит текущей ситуации 
''' + '\U00002705' + '''Новые цели и стратегии 
''' + '\U00002705' + '''Саморазвитие 
''' + '\U00002705' + '''Масштабирование 
''' + '\U00002705' + '''Лидерство и баланс 
И многое другое вы получите в программе «Развитие бизнеса». 
'''
                    bot.send_message(user_id, text)

                user_to_json(user)

                keyboard = types.ReplyKeyboardMarkup()

                button_1 = types.KeyboardButton('Личностное развитие (карьера) и выбор пути')
                button_2 = types.KeyboardButton('Баланс!')
                button_3 = types.KeyboardButton('Все о продажах')
                button_4 = types.KeyboardButton('Управление персоналом')
                button_5 = types.KeyboardButton('Развитие бизнеса')

                if len(user['viewed_products']) == 5:

                    void_keyboard = telebot.types.ReplyKeyboardRemove()

                    bot.send_message(user_id, "Спасибо за проявленый интерес", reply_markup=void_keyboard)
                else:

                    if 'Личностное развитие (карьера) и выбор пути' not in user['viewed_products']:
                        keyboard.add(button_1)
                    if 'Баланс!' not in user['viewed_products']:
                        keyboard.add(button_2)
                    if 'Все о продажах' not in user['viewed_products']:
                        keyboard.add(button_3)
                    if 'Управление персоналом' not in user['viewed_products']:
                        keyboard.add(button_4)
                    if 'Развитие бизнеса' not in user['viewed_products']:
                        keyboard.add(button_5)

                    bot.send_message(user_id, 'Что-то еще?', reply_markup=keyboard)

 
bot.polling(none_stop=True, interval=0)