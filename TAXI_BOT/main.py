from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update, ReplyKeyboardRemove, LabeledPrice
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, CallbackContext, CallbackQueryHandler, \
    Updater, Filters, PreCheckoutQueryHandler
from dotenv import load_dotenv


import db
import texts
import utils
import os


load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
CHAT_ID = os.getenv('CHAT_ID')
CHAT_LINK = os.getenv('CHAT_LINK')
PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN')
ADMINS_CHAT_ID = os.getenv('ADMINS_CHAT_ID')

(
    SET_LAN,
    NAME,
    PHONE,
    MAIN_MENU,
    TARIFFS_LIST,
    SETTINGS,
    EDIT_NAME,
    EDIT_PHONE,
    TAKE_TAXI,
    TAKE_TAXI_FROM,
    TAKE_TAXI_TO,
    TAKE_TAXI_CONFIRM,
    TAKE_TAXI_PAYMENT,
    HELP
) = range(14)

(
    ADMIN_MENU,
    ADMIN_MENU_TARIFFS,
    ADMIN_TARIFF_ADD_NAME_UZ,
    ADMIN_TARIFF_ADD_NAME_RU,
    ADMIN_TARIFF_ADD_NAME_EN,
    ADMIN_TARIFF_ADD_DESC_UZ,
    ADMIN_TARIFF_ADD_DESC_RU,
    ADMIN_TARIFF_ADD_DESC_EN,
    ADMIN_TARIFF_ADD_BASE_PRICE,
    ADMIN_TARIFF_ADD_PER_KM,
    ADMIN_TARIFF_EDIT,
    ADMIN_TARIFF_EDIT_PRICE,
    ADMIN_TARIFF_DEL,
    ADMIN_TARIFF_DEL_CONFIRM,
    ADMIN_DRIVERS,
    ADMIN_DRIVER_ADD_TG_ID,
    ADMIN_DRIVER_ADD_NAME,
    ADMIN_DRIVER_ADD_PHONE,
    ADMIN_DRIVER_ADD_CAR_MODEL,
    ADMIN_DRIVER_ADD_CAR_NUM,
    ADMIN_DRIVERS_SEARCH,
    ADMIN_DRIVER_INFO,
    ADMIN_DRIVERS_ADD_TARIFF,
    ADMIN_DRIVERS_SELECT_TARIFF,
    ADMIN_DRIVERS_ASSIGN_TARIFF,
    ADMIN_DRIVERS_SELECT_MORE_TARIFF,
    ADMIN_DRIVER_DELETE_TARIFF,
    ADMIN_DRIVER_SELECT_DELETE_TARIFF,
    ADMIN_DRIVER_CHOOSE_DELETE_TARIFF,
    ADMIN_DRIVER_DELETE,
    ADMIN_DRIVER_DELETE_CONFIRM,
    ADMIN_DRIVER_DELETE_CONFIRM_FINISH,
    ADMIN_DRIVER_B_UB,
    ADMIN_DRIVER_B_UB_CHOOSE,
    ADMIN_DRIVER_B_UB_SUBMIT,
    ADMIN_ORDERS,
    ADMIN_ORDERS_FILTER,
    ADMIN_ORDER_SEARCH,
    ADMIN_BROADCAST, ADMIN_BROADCAST_SEND

) = range(15, 55)


(
    DRIVER_LOGIN,
    DRIVER_MENU,
    DRIVER_ORDERS,
    DRIVER_SETTINGS,
    DRIVER_LOG_PASSW_CHANGE,
    DRIVER_SEND_LOCATION
) = range(56, 62)


def get_lang(context: CallbackContext, tg_id=None):
    lang = context.user_data.get('language')
    if not lang and tg_id:
        user = db.get_user(tg_id)
        if user:
            lang = user[3]
    return lang or 'uz'


def start(update: Update, context: CallbackContext):
    user = db.get_user(update.effective_user.id)

    if user:
        context.user_data['language'] = user[3]
        return main_menu(update, context)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(label, callback_data=data)]
        for label, data in texts.LANG_BUTTONS
    ])
    update.message.reply_text("Tilni tanlang 🌐:", reply_markup=keyboard)
    return SET_LAN


def choose_language(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    lang_map = {"lang_uz": "uz", "lang_ru": "ru", "lang_en": "en"}
    lang = lang_map.get(query.data, "uz")
    context.user_data['language'] = lang


    if context.user_data.get('changing_lang'):
        context.user_data['changing_lang'] = False
        db.update_language(query.from_user.id, lang)
        query.edit_message_text(texts.TEXTS['choose_language'][lang])
        return main_menu_after_query(query, context, lang)


    query.edit_message_text(texts.TEXTS['enter_name'][lang])
    return NAME


def main_menu_after_query(query, context: CallbackContext, lang: str):
    query.message.reply_text(
        texts.TEXTS['main_menu'][lang],
        reply_markup=ReplyKeyboardMarkup(
            texts.MAIN_MENU_BUTTONS[lang],
            resize_keyboard=True
        )
    )
    return MAIN_MENU


def get_name(update: Update, context: CallbackContext):
    context.user_data['name'] = update.message.text
    lang = get_lang(context)

    update.message.reply_text(
        texts.TEXTS['enter_phone'][lang],
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(texts.SHARE_BUTTONS['phone'][lang], request_contact=True)]],
            resize_keyboard=True,
        )
    )
    return PHONE


def get_phone(update: Update, context: CallbackContext):
    context.user_data['phone'] = update.message.contact.phone_number
    lang = get_lang(context)
    db.add_user(
        update.effective_user.id,
        context.user_data['name'],
        context.user_data['phone'],
        lang
    )
    update.message.reply_text(texts.TEXTS['registered_success'][lang])
    return main_menu(update, context)


def main_menu(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(
        texts.TEXTS['main_menu'][lang],
        reply_markup=ReplyKeyboardMarkup(
            texts.MAIN_MENU_BUTTONS[lang],
            resize_keyboard=True
        )
    )
    return MAIN_MENU


def main_menu_select(update: Update, context: CallbackContext):
    text = update.message.text
    lang = get_lang(context, update.effective_user.id)
    buttons = texts.MAIN_MENU_BUTTONS[lang]

    taxi_btn     = buttons[0][0]
    orders_btn   = buttons[0][1]
    tariffs_btn  = buttons[1][0]
    help_btn     = buttons[1][1]
    settings_btn = buttons[2][0]

    if text == taxi_btn:
        return take_taxi(update, context)
    if text == orders_btn:
        my_orders(update, context)
    if text == tariffs_btn:
        return tariffs(update, context)
    if text == help_btn:
        return help_menu(update, context)
    if text == settings_btn:
        return setting_menu(update, context)


    return MAIN_MENU

def get_tariffs_for_lang(lang):
    tariffs_list = db.get_tariffs()
    result = []

    for t in tariffs_list:
        result.append({
            "key": t[1],
            "name": t[2] if lang == "uz" else t[3] if lang == "ru" else t[4],
            "desc": t[5] if lang == "uz" else t[6] if lang == "ru" else t[7],
            "base_price": t[8],
            "per_km": t[9],
        })
    return result


def take_taxi(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    tariffs_lang = get_tariffs_for_lang(lang)

    if not tariffs_lang:
        update.message.reply_text(texts.TEXTS['no_tariffs'][lang])
        return MAIN_MENU

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(t["name"], callback_data=f"tariff_{t['key']}")]
        for t in tariffs_lang
    ])

    update.message.reply_text(texts.TEXTS['choose_tariff'][lang], reply_markup=keyboard)
    return TAKE_TAXI

def take_taxi_select(update: Update, context: CallbackContext):
    query = update.callback_query
    lang = get_lang(context, query.from_user.id)
    query.answer()

    tariff_key = query.data.split("_", 1)[1]
    tariff = next(t for t in get_tariffs_for_lang(lang) if t["key"] == tariff_key)
    context.user_data['tariff_key'] = tariff_key
    context.user_data['tariff_name'] = tariff['name']

    query.edit_message_text(f"{tariff['name']} ✅:")
    location_btn = KeyboardButton(texts.SHARE_LOCATION_BTN[lang], request_location=True)
    markup = ReplyKeyboardMarkup([[location_btn]], resize_keyboard=True, one_time_keyboard=True)

    query.message.reply_text(texts.TEXTS['ask_from'][lang], reply_markup=markup)
    return TAKE_TAXI_FROM

def share_from(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    if update.message.location:
        lat = update.message.location.latitude
        lon = update.message.location.longitude
        context.user_data['from_lat'] = lat
        context.user_data['from_lon'] = lon
        context.user_data['from_location'] = utils.reverse_geocode(lat, lon)
    else:
        context.user_data['from_lat'] = None
        context.user_data['from_lon'] = None
        context.user_data['from_location'] = update.message.text

    update.message.reply_text(texts.TEXTS['ask_to'][lang], reply_markup=ReplyKeyboardRemove())
    return TAKE_TAXI_TO

def share_to(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    if update.message.location:
        loc = update.message.location
        context.user_data['to_lat'] = loc.latitude
        context.user_data['to_lon'] = loc.longitude
        context.user_data['to_location'] = utils.reverse_geocode(loc.latitude, loc.longitude)
    else:
        to_location = update.message.text
        result = utils.geocode(to_location)
        if not result:
            update.message.reply_text(texts.TEXTS['location_not_found'][lang])
            return TAKE_TAXI_TO
        context.user_data['to_location'] = result['address']
        context.user_data['to_lat'] = result['lat']
        context.user_data['to_lon'] = result['lon']

    distance = utils.get_distance(
        context.user_data['from_lat'],
        context.user_data['from_lon'],
        context.user_data['to_lat'],
        context.user_data['to_lon']
    )

    if distance:
        context.user_data['distance'] = distance['km']
        context.user_data['duration'] = distance['minutes']
        price = utils.calculate_price(context.user_data['tariff_key'], distance['km'])
        context.user_data['price'] = price
    else:
        context.user_data['distance'] = None
        context.user_data['duration'] = None
        context.user_data['price'] = None

    tariff_name = context.user_data['tariff_name']
    from_loc = context.user_data['from_location']
    to_loc = context.user_data['to_location']
    distance_km = context.user_data['distance']
    price = context.user_data['price']

    text = texts.TEXTS['order_confirm'][lang].format(
        tariff=tariff_name,
        from_loc=from_loc,
        to_loc=to_loc,
        distance=distance_km if distance_km else "-",
        price=f"{price:,}" if price else "-",
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['confirm_btn'][lang], callback_data='order_confirm'),
            InlineKeyboardButton(texts.TEXTS['cancel_btn'][lang], callback_data='order_cancel'),
        ]
    ])

    update.message.reply_text(text, reply_markup=keyboard)
    return TAKE_TAXI_CONFIRM

def confirm_order(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, query.from_user.id)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['cash_btn'][lang], callback_data='pay_cash'),
            InlineKeyboardButton(texts.TEXTS['card_btn'][lang], callback_data='pay_card'),
        ]
    ])

    query.edit_message_text(texts.TEXTS['choose_payment'][lang], reply_markup=keyboard)
    return TAKE_TAXI_PAYMENT

def pay_cash(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, query.from_user.id)

    query.edit_message_text(texts.TEXTS['cash_order_sent'][lang])

    order_id = db.add_order(
        user_id=update.effective_user.id,
        tariff=context.user_data.get('tariff_name'),
        from_location=context.user_data.get('from_location'),
        from_lat=context.user_data.get('from_lat'),
        from_lon=context.user_data.get('from_lon'),
        to_location=context.user_data.get('to_location'),
        to_lat=context.user_data.get('to_lat'),
        to_lon=context.user_data.get('to_lon'),
        distance=context.user_data.get('distance'),
        price=context.user_data.get('price'),
    )
    send_order_to_drivers(context, update.effective_user.id, order_id, payment_type="cash")
    return MAIN_MENU

def pay_card(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, query.from_user.id)

    price = context.user_data.get('price', 0)

    context.bot.send_invoice(
        chat_id=update.effective_chat.id,
        title=texts.TEXTS['invoice_title'][lang],
        description=texts.TEXTS['invoice_desc'][lang],
        payload='taxi_order',
        provider_token=PROVIDER_TOKEN,
        currency='UZS',
        prices=[LabeledPrice(texts.TEXTS['tariff_label'][lang], price * 100)],
        start_parameter='taxi_order'
    )
    return TAKE_TAXI_PAYMENT

def pre_checkout(update: Update, context: CallbackContext):
    query = update.pre_checkout_query
    query.answer(ok=True)

def payment_success(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['payment_success'][lang])

    order_id = db.add_order(
        user_id=update.effective_user.id,
        tariff=context.user_data.get('tariff_name'),
        from_location=context.user_data.get('from_location'),
        from_lat=context.user_data.get('from_lat'),
        from_lon=context.user_data.get('from_lon'),
        to_location=context.user_data.get('to_location'),
        to_lat=context.user_data.get('to_lat'),
        to_lon=context.user_data.get('to_lon'),
        distance=context.user_data.get('distance'),
        price=context.user_data.get('price'),
    )
    send_order_to_drivers(context, update.effective_user.id, order_id, payment_type="card")
    return MAIN_MENU

def cancel_order(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, query.from_user.id)

    query.edit_message_text(texts.TEXTS['order_cancelled'][lang])
    return ConversationHandler.END

ORDERS_PER_PAGE = 10
def my_orders(update: Update, context: CallbackContext, page=0):
    lang = get_lang(context, update.effective_user.id)
    all_orders = db.get_user_orders(update.effective_user.id)

    if not all_orders:
        update.message.reply_text(texts.TEXTS['no_orders'][lang])
        return MAIN_MENU

    total = len(all_orders)
    total_pages = (total + ORDERS_PER_PAGE - 1) // ORDERS_PER_PAGE
    start = page * ORDERS_PER_PAGE
    page_orders = all_orders[start:start + ORDERS_PER_PAGE]

    text = texts.TEXTS['my_orders_title'][lang]
    for i, order in enumerate(page_orders, start=start + 1):
        order_id, tariff, from_loc, to_loc, distance, price, status, created_at = order
        emoji = texts.TEXTS['order_statuses'][lang].get(status, "❓").split()[0]
        date = created_at[:10]
        text += f"{i}. {date} | {from_loc} → {to_loc} {emoji}\n"

    buttons = []
    row = []

    for i, order in enumerate(page_orders, start=start + 1):
        row.append(InlineKeyboardButton(str(i), callback_data=f"order_detail_{order[0]}_{page}"))
        if len(row) == 5:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_prev'][lang], callback_data=f"orders_page_{page - 1}"))
    if page < total_pages - 1:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_next'][lang], callback_data=f"orders_page_{page+1}"))
    if nav:
        buttons.append(nav)

    keyboard = InlineKeyboardMarkup(buttons)
    update.message.reply_text(text, reply_markup=keyboard, parse_mode='Markdown')
    return MAIN_MENU

def orders_page(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)
    page = int(query.data.split("_")[-1])

    all_orders = db.get_user_orders(update.effective_user.id)
    total = len(all_orders)
    total_pages = (total + ORDERS_PER_PAGE - 1) // ORDERS_PER_PAGE
    start = page * ORDERS_PER_PAGE
    page_orders = all_orders[start:start + ORDERS_PER_PAGE]

    text = texts.TEXTS['my_orders_title'][lang]
    for i, order in enumerate(page_orders, start=start+1):
        order_id, tariff, from_loc, to_loc, distance, price, status, created_at = order
        emoji = texts.TEXTS['order_statuses'][lang].get(status, "❓").split()[0]
        date = created_at[:10]
        text += f"{i}. {date} | {from_loc} → {to_loc} {emoji}\n"

    buttons = []
    row = []
    for i, order in enumerate(page_orders, start=start+1):
        row.append(InlineKeyboardButton(str(i), callback_data=f"order_detail_{order[0]}_{page}"))
        if len(row) == 5:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_prev'][lang], callback_data=f"orders_page_{page-1}"))
    if page < total_pages - 1:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_next'][lang], callback_data=f"orders_page_{page+1}"))
    if nav:
        buttons.append(nav)

    keyboard = InlineKeyboardMarkup(buttons)
    query.edit_message_text(text, reply_markup=keyboard, parse_mode='Markdown')

def order_detail(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, query.from_user.id)

    _, _, order_id, page = query.data.split("_")
    order = db.get_order(int(order_id))

    status_text = texts.TEXTS['order_statuses'][lang].get(order[11], order[11])
    text = (
        f"{texts.TEXTS['order_detail_title'][lang]}{order[0]}\n\n"
        f"{texts.TEXTS['order_tariff'][lang]}: {order[2]}\n"
        f"{texts.TEXTS['order_from'][lang]}: {order[3]}\n"
        f"{texts.TEXTS['order_to'][lang]}: {order[6]}\n"
        f"{texts.TEXTS['order_distance'][lang]}: {order[9]} km\n"
        f"{texts.TEXTS['order_price'][lang]}: {order[10]:,} so'm\n"
        f"{texts.TEXTS['order_date'][lang]}: {order[14][:16]}\n"
        f"{texts.TEXTS['order_status'][lang]}: {status_text}\n"
    )
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['btn_back'][lang], callback_data=f"orders_page_{page}")
        ]
    ])

    query.edit_message_text(text, reply_markup=keyboard, parse_mode='Markdown')

def help_menu(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['help_cancel'][lang], callback_data='help_cancel')
        ]
    ])

    update.message.reply_text(texts.TEXTS['help_ask'][lang], reply_markup=keyboard)
    return HELP

def help_receive(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    user = db.get_user(update.effective_user.id)

    msg = texts.TEXTS['help_admin_msg'][lang]
    msg = msg.replace('{name}', user[1])
    msg = msg.replace('{phone}', user[2])
    msg = msg.replace('{message}', update.message.text)

    context.bot.send_message(chat_id=ADMINS_CHAT_ID, text=msg)
    update.message.reply_text(texts.TEXTS['help_sent'][lang])
    return main_menu(update, context)

def help_cancel(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    return main_menu_after_query(query, context, get_lang(context, update.effective_user.id))

def tariffs(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    tariffs_list = get_tariffs_for_lang(lang)

    if not tariffs_list:
        update.message.reply_text(texts.TEXTS['no_tariffs'][lang])
        return MAIN_MENU

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(t["name"], callback_data=f"tariff_{i}")]
        for i, t in enumerate(tariffs_list)
    ])

    update.message.reply_text(texts.TEXTS['choose_tariff'][lang], reply_markup=keyboard)
    return TARIFFS_LIST

def tariffs_select(update: Update, context: CallbackContext):
    query = update.callback_query
    lang = get_lang(context, query.from_user.id)
    query.answer()


    if query.data == "tariff_back":
        tariffs_list = get_tariffs_for_lang(lang)
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(t["name"], callback_data=f"tariff_{i}")]
            for i, t in enumerate(tariffs_list)
        ])
        query.edit_message_text(texts.TEXTS['choose_tariff'][lang], reply_markup=keyboard)
        return TARIFFS_LIST

    index = int(query.data.split("_")[1])
    tariff = get_tariffs_for_lang(lang)[index]

    text = (
        f"{tariff['name']}\n\n"
        f"{tariff['desc']}\n\n"
        f"{texts.TEXTS['tariff_base_price'][lang].format(price=tariff['base_price'])}\n"
        f"{texts.TEXTS['tariff_per_km'][lang].format(price=tariff['per_km'])}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(texts.TEXTS['tariff_back'][lang], callback_data='tariff_back')]
    ])

    query.edit_message_text(text, reply_markup=keyboard)
    return TARIFFS_LIST


def setting_menu(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(
        texts.TEXTS['settings_menu'][lang],
        reply_markup=ReplyKeyboardMarkup(
            texts.SETTINGS_BUTTONS[lang],
            resize_keyboard=True
        )
    )
    return SETTINGS


def setting_menu_select(update: Update, context: CallbackContext):
    text = update.message.text
    lang = get_lang(context, update.effective_user.id)
    buttons = texts.SETTINGS_BUTTONS[lang]

    edit_name_btn  = buttons[0][0]
    edit_phone_btn = buttons[0][1]
    change_lang_btn = buttons[1][0]
    back_btn       = buttons[2][0]

    if text == edit_name_btn:
        update.message.reply_text(texts.TEXTS['enter_new_name'][lang])
        return EDIT_NAME
    if text == edit_phone_btn:
        update.message.reply_text(texts.TEXTS['enter_new_phone'][lang])
        return EDIT_PHONE
    if text == change_lang_btn:
        context.user_data['changing_lang'] = True
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(label, callback_data=data)]
            for label, data in texts.LANG_BUTTONS
        ])
        update.message.reply_text(texts.TEXTS['choose_language'][lang], reply_markup=keyboard)
        return SET_LAN
    if text == back_btn:
        return main_menu(update, context)

    return SETTINGS


def edit_name(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    db.update_name(update.effective_user.id, update.message.text)
    update.message.reply_text(texts.TEXTS['name_updated'][lang])
    return main_menu(update, context)


def edit_phone(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    db.update_phone_number(update.effective_user.id, update.message.text)
    update.message.reply_text(texts.TEXTS['phone_updated'][lang])
    return main_menu(update, context)

def send_order_to_drivers(context: CallbackContext, user_id: int, order_id: int, payment_type: str = "cash"):
    user = db.get_user(user_id)
    tariff_key = context.user_data.get('tariff_key')
    drivers = db.get_online_drivers(tariff_key)

    from_lat = context.user_data.get('from_lat')
    from_lon = context.user_data.get('from_lon')

    lang = user[3] if user else 'uz'
    payment_text = "💳 Karta (Click)" if payment_type == "card" else "💵 Naqd pul"
    price = context.user_data.get('price', 0)

    text = (
        f"🚕 Yangi buyurtma #{order_id}\n\n"
        f"👤 Ism: {user[1]}\n"
        f"📞 Tel: {user[2]}\n"
        f"🚖 Tarif: {context.user_data.get('tariff_name')}\n"
        f"📍 Qayerdan: {context.user_data.get('from_location')}\n"
        f"🏁 Qayerga: {context.user_data.get('to_location')}\n"
        f"📏 Masofa: {context.user_data.get('distance')} km\n"
        f"💰 Narx: {price:,} so'm\n"
        f"💳 To'lov: {payment_text}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Qabul qilish", callback_data=f"accept_{order_id}_{user_id}")]
    ])

    # Avval 1 km, topilmasa 3 km, topilmasa 5 km
    for max_distance in [1, 3, 5]:
        nearby_drivers = []
        for driver in drivers:
            if driver[15] is None or driver[16] is None:
                continue
            distance = utils.haversine(from_lat, from_lon, driver[15], driver[16])
            if distance <= max_distance:
                nearby_drivers.append((driver, distance))

        nearby_drivers.sort(key=lambda x: x[1])

        if nearby_drivers:
            for driver, dist in nearby_drivers:
                driver_tg_id = driver[1]
                if str(driver_tg_id) == str(user_id):
                    continue
                try:
                    msg = context.bot.send_message(
                        chat_id=driver_tg_id,
                        text=text,
                        reply_markup=keyboard
                    )
                    db.save_driver_message(order_id, driver_tg_id, msg.message_id)
                except:
                    pass
            db.update_order_status(order_id, db.OrderStatus.PENDING)
            return

    # Hech kim topilmasa
    context.bot.send_message(
        chat_id=user_id,
        text=texts.TEXTS['no_drivers_found'][lang],
        reply_markup=ReplyKeyboardMarkup(texts.MAIN_MENU_BUTTONS[lang], resize_keyboard=True)
    )
def admin_start(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    if str(update.effective_user.id) != str(ADMIN_ID):
        update.message.reply_text(texts.TEXTS['not_admin'][lang])
        return ConversationHandler.END

    update.message.reply_text(
        texts.TEXTS['admin_panel'][lang],
        reply_markup=ReplyKeyboardMarkup(
            texts.ADMIN_MENU_BUTTONS[lang],
            resize_keyboard=True,
        )
    )
    return ADMIN_MENU

def admin_menu(update: Update, context: CallbackContext):
    text = update.message.text
    lang = get_lang(context, update.effective_user.id)
    buttons = texts.ADMIN_MENU_BUTTONS[lang]

    tariffs_btn = buttons[0][1]
    drivers_btn = buttons[0][0]
    orders_btn = buttons[1][0]
    stats_btn = buttons[1][1]
    broadcast_btn = buttons[2][0]

    if text == drivers_btn:
        return admin_drivers(update, context)
    if text == tariffs_btn:
        return admin_tariffs(update, context)
    if text == orders_btn:
        return admin_orders(update, context)
    if text == stats_btn:
        return admin_stats(update, context)
    if text == broadcast_btn:
        return admin_broadcast(update, context)

    return ADMIN_MENU

def admin_drivers(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    button = texts.ADMIN_DRIVERS_BUTTONS[lang]
    update.message.reply_text(texts.TEXTS['admin_drivers_menu_title'][lang], reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True))
    return ADMIN_DRIVERS

def admin_drivers_select(update: Update, context: CallbackContext):
    text = update.message.text
    lang = get_lang(context, update.effective_user.id)
    keyboard = texts.ADMIN_DRIVERS_BUTTONS[lang]

    drivers_list = keyboard[0][0]
    driver_add = keyboard[0][1]
    driver_search = keyboard[1][0]
    driver_tariff = keyboard[1][1]
    driver_edit = keyboard[2][0]
    driver_del = keyboard[2][1]
    driver_block = keyboard[3][0]
    back = keyboard[4][0]

    if text == drivers_list:
        return admin_drivers_list(update, context)
    if text == driver_add:
        return admin_driver_add(update, context)
    if text == driver_search:
        return admin_driver_search(update, context)
    if text == driver_tariff:
        return admin_driver_add_tariff(update, context)
    if text == driver_edit:
        return admin_tariff_delete(update, context)
    if text == driver_del:
        return admin_driver_delete(update, context)
    if text == driver_block:
        return admin_driver_block_or_unblock(update, context)
    if text == back:
        return admin_start(update, context)
    return ADMIN_MENU

DRIVERS_PER_PAGE = 10
def admin_drivers_list(update: Update, context: CallbackContext, page=0):
    lang = get_lang(context, update.effective_user.id)
    all_drivers = db.get_all_drivers()

    if not all_drivers:
        update.message.reply_text(texts.TEXTS['admin_no_drivers'][lang])
        return ADMIN_DRIVERS

    total = len(all_drivers)
    total_pages = (total + DRIVERS_PER_PAGE - 1) // DRIVERS_PER_PAGE
    start = page * DRIVERS_PER_PAGE
    page_orders = all_drivers[start:start + DRIVERS_PER_PAGE]

    text = texts.TEXTS['admin_drivers_title'][lang]
    for i, order in enumerate(page_orders, start=start + 1):
        text += f"{i}. {order[8]} |  {order[5]}\n"
    buttons = []
    row = []

    for i, order in enumerate(page_orders, start=start + 1):
        row.append(InlineKeyboardButton(str(i), callback_data=f"drivers_list_{order[0]}_{page}"))
        if len(row) == 5:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_prev'][lang], callback_data=f"drivers_list_{page - 1}"))
    if page < total_pages - 1:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_next'][lang], callback_data=f"drivers_list_{page+1}"))
    if nav:
        buttons.append(nav)

    keyboard = InlineKeyboardMarkup(buttons)
    update.message.reply_text(text, reply_markup=keyboard, parse_mode='Markdown')
    return ADMIN_DRIVERS

def admin_drivers_list_select(update: Update, context: CallbackContext, page=0):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)
    page = int(query.data.split("_")[-1])
    all_drivers = db.get_all_drivers()

    if not all_drivers:
        update.message.reply_text(texts.TEXTS['admin_no_drivers'][lang])
        return ADMIN_DRIVERS

    total = len(all_drivers)
    total_pages = (total + DRIVERS_PER_PAGE - 1) // DRIVERS_PER_PAGE
    start = page * DRIVERS_PER_PAGE
    page_orders = all_drivers[start:start + DRIVERS_PER_PAGE]

    text = texts.TEXTS['admin_drivers_title'][lang]
    for i, order in enumerate(page_orders, start=start + 1):
        text += f"{i}. {order[8]} |  {order[5]}\n"
    buttons = []
    row = []

    for i, order in enumerate(page_orders, start=start + 1):
        row.append(InlineKeyboardButton(str(i), callback_data=f"drivers_list_{order[0]}_{page}"))
        if len(row) == 5:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_prev'][lang], callback_data=f"drivers_list_{page - 1}"))
    if page < total_pages - 1:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_next'][lang], callback_data=f"drivers_list_{page+1}"))
    if nav:
        buttons.append(nav)

    keyboard = InlineKeyboardMarkup(buttons)
    query.edit_message_text(text, reply_markup=keyboard, parse_mode='Markdown')
    return ADMIN_DRIVERS

def admin_driver_detail(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    driver_id = int(query.data.split("_")[2])
    driver = db.get_driver_by_id(driver_id)

    driver_tariffs = db.get_driver_tariffs(driver_id)
    if driver_tariffs:
        tariff_names = ", ".join(
            t[2] if lang == 'uz' else t[3] if lang == 'ru' else t[4]
            for t in driver_tariffs
        )
    else:
        tariff_names = "-"

    status = texts.TEXTS['driver_status_active'][lang] if driver[10] == 1 else texts.TEXTS['driver_status_inactive'][lang]

    text = texts.TEXTS['admin_driver_info'][lang].format(
        name=driver[5],
        login=driver[2],
        password=driver[3],
        phone=driver[6],
        car_model=driver[7],
        car_number=driver[8],
        tariff=tariff_names,
        status=status,
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(texts.TEXTS['btn_back'][lang], callback_data=f"drivers_page_0")]
    ])

    query.edit_message_text(text, reply_markup=keyboard)
    return ADMIN_DRIVERS

def admin_driver_add(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_driver_add_tg_id'][lang])
    return ADMIN_DRIVER_ADD_TG_ID

def admin_driver_add_tg_id(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    context.user_data['tg_id'] = int(update.message.text)
    update.message.reply_text(texts.TEXTS['driver_enter_name'][lang])
    return ADMIN_DRIVER_ADD_NAME

def admin_driver_add_name(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    context.user_data['name'] = update.message.text
    update.message.reply_text(texts.TEXTS['driver_enter_phone'][lang])
    return ADMIN_DRIVER_ADD_PHONE

def admin_driver_add_phone(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    context.user_data['phone'] = update.message.text
    update.message.reply_text(texts.TEXTS['driver_enter_car_model'][lang])
    return ADMIN_DRIVER_ADD_CAR_MODEL

def admin_driver_add_car_model(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    context.user_data['car_model'] = update.message.text
    update.message.reply_text(texts.TEXTS['driver_enter_car_number'][lang])
    return ADMIN_DRIVER_ADD_CAR_NUM

def admin_driver_add_car_number(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    context.user_data['car_number'] = update.message.text
    # update.message.reply_text(texts.TEXTS['admin_new_driver_notify'][lang])

    login = utils.generate_login(context.user_data['name'])
    password = utils.generate_password()


    db.add_driver(
        tg_id=context.user_data['tg_id'],
        name=context.user_data['name'],
        phone=context.user_data['phone'],
        car_model=context.user_data['car_model'],
        car_number=context.user_data['car_number'],
        login=login,
        password=password,
    )

    update.message.reply_text(texts.TEXTS['admin_driver_approved'][lang])

    context.bot.send_message(
        chat_id=context.user_data['tg_id'],
        text=texts.TEXTS['driver_added_notify'][lang].format(
            name=context.user_data['name'],
            phone=context.user_data['phone'],
            car_model=context.user_data['car_model'],
            car_number=context.user_data['car_number'],
            channel_link=CHAT_LINK),
    )

    context.bot.send_message(
        chat_id=context.user_data['tg_id'],
        text=texts.TEXTS['driver_temp_credentials'][lang].format(
            login=login,
            password=password,
        ),
        parse_mode="Markdown",
    )
    return ADMIN_DRIVERS

def admin_driver_search(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_driver_search'][lang])
    return ADMIN_DRIVERS_SEARCH

def admin_driver_find(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    result = db.search_drivers(text)


    if not result:
        update.message.reply_text(texts.TEXTS['admin_driver_not_found'][lang])
        return ADMIN_DRIVERS
    driver = result[0]

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_driver_info_btn'][lang], callback_data=f"driver_info_{driver[0]}")
        ]
    ])

    update.message.reply_text(texts.TEXTS['admin_driver_search_result'][lang].format(
        name=driver[5],
        car_number=driver[8],
    ), reply_markup=keyboard)
    return ADMIN_DRIVER_INFO

def admin_driver_info(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    query = update.callback_query
    query.answer()

    driver_id = int(query.data.split("_")[-1])
    driver = db.get_driver_by_id(driver_id)

    driver_tariffs = db.get_driver_tariffs(driver_id)
    if driver_tariffs:
        tariff_names = ", ".join(
            t[2] if lang == 'uz' else t[3] if lang == 'ru' else t[4]
            for t in driver_tariffs
        )
    else:
        tariff_names = "-"

    status = texts.TEXTS['driver_status_active'][lang] if driver[10] == 1 else texts.TEXTS['driver_status_inactive'][lang]

    text = texts.TEXTS['admin_driver_info'][lang].format(
        name=driver[5],
        login=driver[2],
        password=driver[3],
        phone=driver[6],
        car_model=driver[7],
        car_number=driver[8],
        tariff=tariff_names,
        status=status,
    )

    query.edit_message_text(text)
    return ADMIN_DRIVERS

def admin_driver_add_tariff(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_assign_tariff_search'][lang])
    return ADMIN_DRIVERS_ADD_TARIFF

def admin_driver_find_for_tariff(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    driver = db.search_drivers(text)

    if not driver:
        update.message.reply_text(texts.TEXTS['admin_assign_tariff_not_found'][lang])
        return ADMIN_DRIVERS

    driver = driver[0]
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_assign_tariff_btn'][lang], callback_data=f"assign_tariff_{driver[0]}")
        ]
    ])

    update.message.reply_text(texts.TEXTS['admin_assign_tariff_found'][lang].format(
        name=driver[5],
        car_number=driver[8],
    ), reply_markup=keyboard)
    return ADMIN_DRIVERS_SELECT_TARIFF

def admin_driver_assign_tariff(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    driver_id = int(query.data.split("_")[-1])
    context.user_data['assign_driver_id'] = driver_id

    tariffs_list = db.get_tariffs()

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                t[2] if lang == 'uz' else t[3] if lang == 'ru' else t[4],
                callback_data=f"select_tariff_{t[1]}",
            )
        ] for t in tariffs_list
    ])

    query.edit_message_text(texts.TEXTS['admin_assign_tariff_choose'][lang], reply_markup=keyboard)
    return ADMIN_DRIVERS_ASSIGN_TARIFF

def admin_driver_save_tariff(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    tariff_key = query.data.split("_")[-1]
    driver_id = context.user_data['assign_driver_id']
    db.add_driver_tariff(driver_id, tariff_key)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_assign_tariff_yes'][lang], callback_data=f"assign_tariff_more_yes"),
            InlineKeyboardButton(texts.TEXTS['admin_assign_tariff_no'][lang], callback_data=f"assign_tariff_more_no"),
        ]
    ])

    query.edit_message_text(texts.TEXTS['admin_assign_tariff_success'][lang], reply_markup=keyboard)
    return ADMIN_DRIVERS_SELECT_MORE_TARIFF

def admin_driver_select_more_tariff(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    if query.data == "assign_tariff_more_yes":
        tariffs_list = db.get_tariffs()
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                t[2] if lang == 'uz' else t[3] if lang == 'ru' else t[4],
                callback_data=f"select_tariff_{t[1]}"
            )]
            for t in tariffs_list
        ])
        query.edit_message_text(texts.TEXTS['admin_assign_tariff_choose'][lang], reply_markup=keyboard)
        return ADMIN_DRIVERS_ASSIGN_TARIFF
    else:
        query.edit_message_text(texts.TEXTS['admin_drivers_menu_title'][lang])
        return ADMIN_DRIVERS

def admin_tariff_delete(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_change_tariff_search'][lang])
    return ADMIN_DRIVER_DELETE_TARIFF

def admin_driver_tariff_del_find(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    driver = db.search_drivers(text)

    if not driver:
        update.message.reply_text(texts.TEXTS['admin_assign_tariff_not_found'][lang])
        return ADMIN_DRIVERS

    driver = driver[0]
    context.user_data['remove_driver_id'] = driver[0]

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_remove_tariff_btn'][lang], callback_data='remove_driver_tariff'),
        ]
    ])

    update.message.reply_text(texts.TEXTS['admin_assign_tariff_found'][lang].format(
        name=driver[5],
        car_number=driver[8],
    ), reply_markup=keyboard)
    return ADMIN_DRIVER_SELECT_DELETE_TARIFF

def admin_driver_select_delete_tariff(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    driver_id = context.user_data['remove_driver_id']
    tariff_key = db.get_driver_tariffs(driver_id)

    if not tariff_key:
        query.edit_message_text(texts.TEXTS['admin_driver_no_tariff'][lang])
        return ADMIN_DRIVERS

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                t[1] if lang == 'uz' else t[3] if lang == 'ru' else t[4],
                callback_data=f"del_driver_tariff_{t[1]}"
            )
        ] for t in tariff_key
    ])

    query.edit_message_text(texts.TEXTS['admin_driver_select_remove_tariff'][lang], reply_markup=keyboard)
    return ADMIN_DRIVER_CHOOSE_DELETE_TARIFF

def admin_driver_choose_delete_tariff(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    driver_id = context.user_data['remove_driver_id']
    tariff_key = query.data.split('del_driver_tariff_')[1]

    db.del_driver_tariff(driver_id, tariff_key)

    query.edit_message_text(texts.TEXTS['admin_driver_tariff_removed'][lang])
    return ADMIN_DRIVERS

def admin_driver_delete(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_driver_delete_search'][lang])
    return ADMIN_DRIVER_DELETE

def admin_driver_delete_find(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    driver = db.search_drivers(text)


    if not driver:
        update.message.reply_text(texts.TEXTS['admin_assign_tariff_not_found'][lang])
        return ADMIN_DRIVERS
    driver = driver[0]
    driver_id = context.user_data['del_driver_id'] = driver[0]

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_driver_delete_btn'][lang], callback_data='driver_delete'),
        ]
    ])

    update.message.reply_text(texts.TEXTS['admin_assign_tariff_found'][lang].format(
        name=driver[5],
        car_number=driver[8],
    ), reply_markup=keyboard)
    return ADMIN_DRIVER_DELETE_CONFIRM

def admin_driver_delete_confirm(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_assign_tariff_yes'][lang], callback_data='driver_delete_yes'),
            InlineKeyboardButton(texts.TEXTS['admin_assign_tariff_no'][lang], callback_data='driver_delete_no'),
        ]
    ])
    query.edit_message_text(texts.TEXTS['admin_driver_delete_confirm'][lang], reply_markup=keyboard)
    return ADMIN_DRIVER_DELETE_CONFIRM_FINISH

def admin_driver_delete_confirm_finish(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    driver_id = context.user_data['del_driver_id']

    if query.data == 'driver_delete_yes':
        db.delete_driver(driver_id)
        query.edit_message_text(texts.TEXTS['admin_driver_deleted'][lang])
        return ADMIN_DRIVERS
    else:
        query.edit_message_text(texts.TEXTS['admin_driver_delete_cancelled'][lang])
        return ADMIN_DRIVERS

def admin_driver_block_or_unblock(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_driver_block_search'][lang])
    return ADMIN_DRIVER_B_UB

def admin_driver_b_ub_search(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text

    driver = db.search_drivers(text)
    if not driver:
        update.message.reply_text(texts.TEXTS['admin_driver_not_found'][lang])
        return ADMIN_DRIVERS
    driver = driver[0]
    tg_id = context.user_data['driver_tg_id'] = driver[1]
    driver_id = context.user_data['b_ub_driver_id'] = driver[0]

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_driver_block_btn'][lang], callback_data='driver_b_btn'),
            InlineKeyboardButton(texts.TEXTS['admin_driver_unblock_btn'][lang], callback_data='driver_ub_btn'),
        ]
    ])

    update.message.reply_text(texts.TEXTS['admin_assign_tariff_found'][lang].format(
        name=driver[5],
        car_number=driver[8],
    ), reply_markup=keyboard)
    return ADMIN_DRIVER_B_UB_CHOOSE

def admin_driver_b_ub_choose(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    if query.data == 'driver_b_btn':
        driver_id = context.user_data['b_ub_driver_id']
        driver = db.get_driver_by_id(driver_id)
        if driver[12] == 1:
            query.edit_message_text(texts.TEXTS['admin_driver_already_blocked'][lang])
            return ADMIN_DRIVERS
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(texts.TEXTS['admin_assign_tariff_yes'][lang], callback_data='driver_b_btn_yes'),
                InlineKeyboardButton(texts.TEXTS['admin_assign_tariff_no'][lang], callback_data='driver_b_btn_no'),
            ]
        ])
        query.edit_message_text(texts.TEXTS['admin_driver_block_confirm'][lang], reply_markup=keyboard)
        return ADMIN_DRIVER_B_UB_SUBMIT
    else:
        driver_id = context.user_data['b_ub_driver_id']
        tg_id = context.user_data['driver_tg_id']
        db.set_driver_blocked(driver_id, False)
        query.edit_message_text(texts.TEXTS['admin_driver_unblock_btn'][lang])
        context.bot.send_message(
            chat_id=tg_id,
            text=texts.TEXTS['driver_unblocked_notify'][lang],
        )
        return ADMIN_DRIVERS

def admin_driver_block_submit(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    if query.data == 'driver_b_btn_yes':
        driver_id = context.user_data['b_ub_driver_id']
        tg_id = context.user_data['driver_tg_id']
        db.set_driver_blocked(driver_id, True)
        query.edit_message_text(texts.TEXTS['admin_driver_blocked'][lang])
        context.bot.send_message(
            chat_id=tg_id,
            text=texts.TEXTS['driver_blocked_notify'][lang],
        )
        return ADMIN_DRIVERS
    else:
        query.edit_message_text(texts.TEXTS['admin_driver_block_cancelled'][lang])
        return ADMIN_DRIVERS

def admin_tariffs(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    keyboard = texts.ADMIN_TARIFFS_BUTTONS[lang]

    update.message.reply_text(
        texts.TEXTS['admin_tariffs_menu_title'][lang],
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )
    return ADMIN_MENU_TARIFFS

def admin_tariffs_select(update: Update, context: CallbackContext):
    text = update.message.text
    lang = get_lang(context, update.effective_user.id)
    keyboard = texts.ADMIN_TARIFFS_BUTTONS[lang]

    list_btn = keyboard[0][0]
    add_btn = keyboard[0][1]
    edit_btn = keyboard[1][0]
    delete_btn = keyboard[1][1]
    exit_btn = keyboard[2][0]

    if text == list_btn:
        return admin_tariffs_list(update, context)
    if text == add_btn:
        return admin_tariffs_add(update, context)
    if text == edit_btn:
        return admin_tariffs_edit(update, context)
    if text == delete_btn:
        return admin_tariffs_del(update, context)
    if text == exit_btn:
        return admin_start(update, context)
    return ADMIN_MENU_TARIFFS

def admin_tariffs_list(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    tariffs_list = db.get_tariffs()

    if not tariffs_list:
        update.message.reply_text(texts.TEXTS['admin_no_tariffs'][lang])
        return ADMIN_MENU_TARIFFS

    text = texts.TEXTS['admin_tariffs_list_title'][lang]

    for t in tariffs_list:
        name = t[2] if lang == "uz" else t[3] if lang == "ru" else t[4]
        text += f"▪️ {name} | {t[8]:,} so'm + {t[9]:,} so'm/km\n"


    update.message.reply_text(text)
    return ADMIN_MENU_TARIFFS

def admin_tariffs_add(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_tariff_add_name'][lang])
    return ADMIN_TARIFF_ADD_NAME_UZ

def admin_tariff_add_name_uz(update: Update, context: CallbackContext):
    context.user_data['tariff_name_uz'] = update.message.text
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_tariff_add_name_ru'][lang])
    return ADMIN_TARIFF_ADD_NAME_RU

def admin_tariff_add_name_ru(update: Update, context: CallbackContext):
    context.user_data['tariff_name_ru'] = update.message.text
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_tariff_add_name_en'][lang])
    return ADMIN_TARIFF_ADD_NAME_EN

def admin_tariff_add_name_en(update: Update, context: CallbackContext):
    context.user_data['tariff_name_en'] = update.message.text
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_tariff_add_desc'][lang])
    return ADMIN_TARIFF_ADD_DESC_UZ

def admin_tariff_add_desc(update: Update, context: CallbackContext):
    context.user_data['tariff_desc_uz'] = update.message.text
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_tariff_add_desc_ru'][lang])
    return ADMIN_TARIFF_ADD_DESC_RU

def admin_tariff_add_desc_ru(update: Update, context: CallbackContext):
    context.user_data['tariff_desc_ru'] = update.message.text
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_tariff_add_desc_en'][lang])
    return ADMIN_TARIFF_ADD_DESC_EN

def admin_tariff_add_desc_en(update: Update, context: CallbackContext):
    context.user_data['tariff_desc_en'] = update.message.text
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_tariff_add_base_price'][lang])
    return ADMIN_TARIFF_ADD_BASE_PRICE

def admin_tariff_add_base_price(update: Update, context: CallbackContext):
    context.user_data['tariff_base_price'] = update.message.text
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_tariff_add_per_km'][lang])
    return ADMIN_TARIFF_ADD_PER_KM

def admin_tariff_add_per_km(update: Update, context: CallbackContext):
    context.user_data['tariff_per_km'] = update.message.text
    lang = get_lang(context, update.effective_user.id)
    db.add_tariff(
        key=context.user_data['tariff_name_uz'].lower().replace(" ", "_"),
        name_uz=context.user_data['tariff_name_uz'],
        name_ru=context.user_data['tariff_name_ru'],
        name_en=context.user_data['tariff_name_en'],
        desc_uz=context.user_data['tariff_desc_uz'],
        desc_ru=context.user_data['tariff_desc_ru'],
        desc_en=context.user_data['tariff_desc_en'],
        base_price=context.user_data['tariff_base_price'],
        per_km=context.user_data['tariff_per_km'],
    )
    update.message.reply_text(texts.TEXTS['admin_tariff_saved'][lang])
    return ADMIN_MENU_TARIFFS

def admin_tariffs_edit(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    tariffs_list = db.get_tariffs()

    if not tariffs_list:
        update.message.reply_text(texts.TEXTS['no_tariffs'][lang])
        return ADMIN_MENU_TARIFFS

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            t[2] if lang == 'uz' else t[3] if lang == 'ru' else t[4],
            callback_data=f"edit_tariff_{t[1]}"
         )]
        for t in tariffs_list
    ])

    update.message.reply_text(texts.TEXTS['admin_tariff_edit_choose'][lang], reply_markup=keyboard)
    return ADMIN_TARIFF_EDIT

def admin_tariffs_edit_select   (update: Update, context: CallbackContext):
    query = update.callback_query
    lang = get_lang(context, update.effective_user.id)
    query.answer()

    tariff_key = query.data.split("_", 2)[2]

    context.user_data['edit_tariff_key'] = tariff_key
    tariff = db.get_tariffs_by_key(tariff_key)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(f"{texts.TEXTS['admin_edit_base_btn'][lang]}: {tariff[8]}:", callback_data=f"edit_base_{tariff_key}"),
            InlineKeyboardButton(f"{texts.TEXTS['admin_edit_per_km_btn'][lang]}: {tariff[9]}:", callback_data=f"edit_per_km_{tariff_key}"),
        ]
    ])

    query.edit_message_text(texts.TEXTS['admin_tariff_edit_choose'][lang], reply_markup=keyboard)
    return ADMIN_TARIFF_EDIT

def admin_tariff_edit_base(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    tariff_key = query.data.split("_", 2)[2]
    context.user_data['edit_tariff_key'] = tariff_key
    context.user_data['edit_failed'] = 'base_price'

    query.edit_message_text(texts.TEXTS['admin_tariff_add_base_price'][lang])
    return ADMIN_TARIFF_EDIT_PRICE

def admin_tariff_edit_per_km(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    tariff_key = query.data.split("_", 3)[3]
    context.user_data['edit_tariff_key'] = tariff_key
    context.user_data['edit_failed'] = 'per_km'

    query.edit_message_text(texts.TEXTS['admin_tariff_add_per_km'][lang])
    return ADMIN_TARIFF_EDIT_PRICE

def admin_tariff_save_price(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    tariff_key = context.user_data['edit_tariff_key']
    failed = context.user_data['edit_failed']
    new_price = int(update.message.text)

    tariff = db.get_tariffs_by_key(tariff_key)

    if failed == 'base_price':
        db.update_tariffs(tariff[0], base_price=new_price, per_km=tariff[9])
    else:
        db.update_tariffs(tariff[0], base_price=tariff[8], per_km=new_price)
    update.message.reply_text(texts.TEXTS['admin_tariff_updated'][lang])
    return admin_tariffs(update, context)

def admin_tariffs_del(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    tariffs_list = db.get_tariffs()

    if not tariffs_list:
        update.message.reply_text(texts.TEXTS['no_tariffs'][lang])
        return ADMIN_MENU_TARIFFS

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            t[2] if lang == 'uz' else t[3] if lang =='ru' else t[4],
            callback_data=f"delete_tariff_{t[1]}"
        )]
        for t in tariffs_list
    ])

    update.message.reply_text(texts.TEXTS['admin_tariff_del_choose'][lang], reply_markup=keyboard)
    return ADMIN_TARIFF_DEL

def admin_tariffs_del_select(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    tariffs_key = query.data.split("_", 2)[2]
    context.user_data['edit_tariff_key'] = tariffs_key

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_tariff_del_yes'][lang], callback_data=f"del_confirm_yes"),
            InlineKeyboardButton(texts.TEXTS['admin_tariff_del_no'][lang], callback_data=f"del_confirm_no"),
        ]
    ])

    query.edit_message_text(texts.TEXTS['admin_tariff_del_confirm'][lang], reply_markup=keyboard)
    return ADMIN_TARIFF_DEL_CONFIRM

def admin_tariffs_del_execute(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    if query.data == "del_confirm_yes":
        tariffs_key = context.user_data['edit_tariff_key']
        tariff = db.get_tariffs_by_key(tariffs_key)
        db.delete_tariffs(tariff[0])
        query.edit_message_text(texts.TEXTS['admin_tariff_deleted'][lang])
    else:
        query.edit_message_text(texts.TEXTS['admin_tariff_del_cancelled'][lang])
    query.message.reply_text(
        texts.TEXTS['admin_tariffs_menu_title'][lang],
        reply_markup=ReplyKeyboardMarkup(
            texts.ADMIN_TARIFFS_BUTTONS[lang],
            resize_keyboard=True
        )
    )
    return ADMIN_MENU_TARIFFS

def admin_orders(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    buttons = texts.ADMIN_ORDERS_BUTTONS[lang]
    update.message.reply_text(texts.TEXTS['admin_orders_menu_title'][lang], reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
    return ADMIN_ORDERS

def admin_orders_select(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    buttons = texts.ADMIN_ORDERS_BUTTONS[lang]

    order_list = buttons[0][0]
    find_order = buttons[0][1]
    back = buttons[1][0]

    if text == order_list:
        return admin_orders_filter(update, context)
    if text == find_order:
        return admin_order_search(update, context)
    if text == back:
        return admin_start(update, context)
    return ADMIN_ORDERS

def admin_orders_filter(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(label, callback_data=data)
        ] for label, data in texts.ADMIN_ORDERS_FILTER_BUTTONS[lang]
    ])
    update.message.reply_text(texts.TEXTS['admin_orders_filter'][lang], reply_markup=markup)
    return ADMIN_ORDERS_FILTER

def admin_orders_filtered_list(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    if query.data.startswith('filter_'):
        context.user_data['orders_filter'] = query.data
        page = 0
    else:
        page = int(query.data.split("_")[-1])

    status_map = {
        'filter_all': None,
        'filter_pending': 'pending',
        'filter_finished': 'finished',
        'filter_cancelled': 'cancelled',
    }
    filter_key = context.user_data.get('orders_filter', 'filter_all')
    orders = db.get_all_orders(status=status_map[filter_key])

    if not orders:
        query.edit_message_text(texts.TEXTS['admin_no_orders'][lang])
        return ADMIN_ORDERS

    total = len(orders)
    total_pages = (total + ORDERS_PER_PAGE - 1) // ORDERS_PER_PAGE
    start = page * ORDERS_PER_PAGE
    page_orders = orders[start:start + ORDERS_PER_PAGE]

    text = texts.TEXTS['admin_orders_list_title'][lang]
    for i, order in enumerate(page_orders, start=start + 1):
        status = texts.TEXTS['order_statuses'][lang].get(order[11], "❓").split()[0]
        text += f"{i}. #{order[0]} | {order[3]} → {order[6]} {status}\n"

    buttons = []
    row = []
    for i, order in enumerate(page_orders, start=start + 1):
        row.append(InlineKeyboardButton(str(i), callback_data=f"admin_order_{order[0]}_{page}"))
        if len(row) == 5:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_prev'][lang], callback_data=f"orders_filter_page_{page - 1}"))
    if page < total_pages - 1:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_next'][lang], callback_data=f"orders_filter_page_{page + 1}"))
    if nav:
        buttons.append(nav)

    query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(buttons))
    return ADMIN_ORDERS_FILTER

def admin_order_detail(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    parts = query.data.split("_")
    order_id = int(parts[2])
    page = int(parts[3])

    order = db.get_order(order_id)
    user = db.get_user(order[1])

    status_text = texts.TEXTS['order_statuses'][lang].get(order[11], "❓")
    payment_text = "💳 Karta (Click)" if order[13] == "card" else "💵 Naqd pul"

    text = texts.TEXTS['admin_order_detail_title'][lang].format(
        order_id=order[0],
        user=user[1] if user else "-",
        phone=user[2] if user else "-",
        tariff=order[2],
        from_loc=order[3],
        to_loc=order[6],
        distance=order[9],
        price=f"{order[10]:,}",
        payment=payment_text,
        date=order[14][:16],
        status=status_text,
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(texts.TEXTS['btn_back'][lang], callback_data=f"orders_filter_page_{page}")]
    ])

    query.edit_message_text(text, reply_markup=keyboard)
    return ADMIN_ORDERS_FILTER

def admin_order_search(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    update.message.reply_text(texts.TEXTS['admin_order_search'][lang])
    return ADMIN_ORDER_SEARCH

def admin_order_find(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    order_id = update.message.text

    try:
        order = db.get_order(int(order_id))
    except:
        order = None

    if not order:
        update.message.reply_text(texts.TEXTS['admin_order_not_found'][lang])
        return ADMIN_ORDERS

    user = db.get_user(order[1])
    status_text = texts.TEXTS['order_statuses'][lang].get(order[11], "❓")
    payment_text = "💳 Karta (Click)" if order[13] == "card" else "💵 Naqd pul"

    text = texts.TEXTS['admin_order_detail_title'][lang].format(
        order_id=order[0],
        user=user[1] if user else "-",
        phone=user[2] if user else "-",
        tariff=order[2],
        from_loc=order[3],
        to_loc=order[6],
        distance=order[9],
        price=f"{order[10]:,}",
        payment=payment_text,
        date=order[14][:16],
        status=status_text,
    )

    update.message.reply_text(text)
    return ADMIN_ORDERS

def admin_stats(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    stats = db.get_stats()

    # Top driver o'tgan oy
    if stats['last_month_top_driver']:
        driver_id, count = stats['last_month_top_driver']
        driver = db.get_driver_by_id(driver_id)
        last_top = texts.TEXTS['admin_stats_top_driver_last'][lang].format(
            name=driver[5],
            tg_id=driver[1],
            car_number=driver[8],
            count=count
        )
    else:
        last_top = texts.TEXTS['admin_stats_no_top_driver'][lang]

    # Top driver shu oy
    if stats['this_month_top_driver']:
        driver_id, count = stats['this_month_top_driver']
        driver = db.get_driver_by_id(driver_id)
        this_top = texts.TEXTS['admin_stats_top_driver_this'][lang].format(
            name=driver[5],
            tg_id=driver[1],
            car_number=driver[8],
            count=count
        )
    else:
        this_top = texts.TEXTS['admin_stats_no_top_driver'][lang]

    # Tarif statistikasi
    tariff_lines = ""
    for tariff_name, count in stats['tariff_stats']:
        tariff_lines += f"▪️ {tariff_name}: {count} ta\n"

    text = (
        texts.TEXTS['admin_stats_title'][lang] +
        texts.TEXTS['admin_stats_orders'][lang].format(
            daily=stats['daily_orders'],
            monthly=stats['monthly_orders'],
            finished=stats['finished_orders'],
            cancelled=stats['cancelled_orders']
        ) +
        texts.TEXTS['admin_stats_payment'][lang].format(
            cash=stats['cash_orders'],
            card=stats['card_orders']
        ) +
        texts.TEXTS['admin_stats_income'][lang].format(
            last_month=f"{stats['last_month_income']:,}",
            this_month=f"{stats['this_month_income']:,}"
        ) +
        last_top +
        this_top +
        texts.TEXTS['admin_stats_tariffs'][lang].format(tariffs=tariff_lines) +
        texts.TEXTS['admin_stats_users'][lang].format(
            daily=stats['daily_users'],
            monthly=stats['monthly_users'],
            drivers=stats['drivers_count']
        )
    )

    update.message.reply_text(text)
    return ADMIN_MENU

def admin_broadcast(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(texts.TEXTS['admin_broadcast_users_btn'][lang], callback_data='broadcast_users'),
            InlineKeyboardButton(texts.TEXTS['admin_broadcast_drivers_btn'][lang], callback_data='broadcast_drivers'),
        ],
        [
            InlineKeyboardButton(texts.TEXTS['admin_broadcast_all_btn'][lang], callback_data='broadcast_all'),
        ]
    ])
    update.message.reply_text(texts.TEXTS['admin_broadcast_menu'][lang], reply_markup=keyboard)
    return ADMIN_BROADCAST

def admin_broadcast_choose(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    context.user_data['broadcast_target'] = query.data
    query.edit_message_text(texts.TEXTS['admin_broadcast_ask'][lang])
    return ADMIN_BROADCAST_SEND

def admin_broadcast_send(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    target = context.user_data.get('broadcast_target')

    if target == 'broadcast_users':
        tg_ids = db.get_all_user_tg_ids()
    elif target == 'broadcast_drivers':
        tg_ids = db.get_all_driver_tg_ids()
    else:
        tg_ids = db.get_all_tg_ids()

    success = 0
    failed = 0

    for tg_id in tg_ids:
        try:
            if update.message.photo:
                context.bot.send_photo(chat_id=tg_id, photo=update.message.photo[-1].file_id, caption=update.message.caption)
            elif update.message.video:
                context.bot.send_video(chat_id=tg_id, video=update.message.video.file_id, caption=update.message.caption)
            elif update.message.audio:
                context.bot.send_audio(chat_id=tg_id, audio=update.message.audio.file_id, caption=update.message.caption)
            elif update.message.voice:
                context.bot.send_voice(chat_id=tg_id, voice=update.message.voice.file_id, caption=update.message.caption)
            else:
                context.bot.send_message(chat_id=tg_id, text=update.message.text)
            success += 1
        except:
            failed += 1

    update.message.reply_text(
        texts.TEXTS['admin_broadcast_success'][lang].format(count=success)
    )
    if failed > 0:
        update.message.reply_text(
            texts.TEXTS['admin_broadcast_failed'][lang].format(count=failed)
        )
    return ADMIN_MENU

def admin_exit(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    update.message.reply_text(
        texts.TEXTS['main_menu'][lang],
        reply_markup=ReplyKeyboardMarkup(
            texts.MAIN_MENU_BUTTONS[lang],
            resize_keyboard=True,
        ),
    )
    return ConversationHandler.END

# DRIVERS DASHBOARD

def driver_start(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    driver = db.get_driver_by_tg_id(update.effective_user.id)

    if driver and driver[14] == 1:  # logged = 1
        update.message.reply_text(
            texts.TEXTS['driver_menu'][lang],
            reply_markup=ReplyKeyboardMarkup(texts.DRIVER_MENU_BUTTONS[lang], resize_keyboard=True)
        )
        return DRIVER_MENU

    update.message.reply_text(texts.TEXTS['driver_login_ask'][lang])
    return DRIVER_LOGIN

def driver_login(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.split()

    if len(text) != 2:
        update.message.reply_text(texts.TEXTS['driver_login_wrong'][lang])
        return DRIVER_LOGIN

    login, password = text
    driver = db.get_driver_by_login(login)


    if not driver or driver[3] != password:
        update.message.reply_text(texts.TEXTS['driver_login_wrong'][lang])
        return DRIVER_LOGIN

    driver_tariffs = db.get_driver_tariffs(driver[0])


    if driver[12] == 1:
        update.message.reply_text(texts.TEXTS['driver_login_blocked'][lang])
        return ConversationHandler.END

    if not driver_tariffs:
        update.message.reply_text(texts.TEXTS['driver_not_active'][lang])
        return ConversationHandler.END

    if driver[4] == 1:
        update.message.reply_text(texts.TEXTS['driver_change_password_ask'][lang])

    update.message.reply_text(
        texts.TEXTS['driver_login_success'][lang].format(name=driver[5]),
        reply_markup=ReplyKeyboardMarkup(texts.DRIVER_MENU_BUTTONS[lang], resize_keyboard=True)
    )
    db.set_driver_logged(driver[0],True)
    return DRIVER_MENU

def driver_menu(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    keyboard = texts.DRIVER_MENU_BUTTONS[lang]
    update.message.reply_text(texts.TEXTS['driver_menu'][lang], reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
    return DRIVER_MENU

def driver_menu_select(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    keyboard = texts.DRIVER_MENU_BUTTONS[lang]

    driver_online = keyboard[0][0]
    driver_offline = keyboard[0][1]
    driver_orders = keyboard[1][0]
    driver_incomes = keyboard[1][1]
    settings = keyboard[2][0]
    logout = keyboard[3][0]

    driver = db.get_driver_by_tg_id(update.effective_user.id)
    driver_id = driver[0]

    if text == driver_online:
        update.message.reply_text(texts.TEXTS['driver_send_location'][lang])
        return DRIVER_SEND_LOCATION
    if text == driver_offline:
        db.set_driver_online(driver_id, False)
        update.message.reply_text(texts.TEXTS['driver_now_offline'][lang])
        return DRIVER_MENU
    if text == driver_orders:
        return driver_my_orders(update, context)
    if text == driver_incomes:
        return driver_earnings(update, context)
    if text == settings:
        return driver_settings(update, context)
    if text == logout:
        driver = db.get_driver_by_tg_id(update.effective_user.id)
        db.set_driver_logged(driver[0], False)
        update.message.reply_text(
            texts.TEXTS['main_menu'][lang],
            reply_markup=ReplyKeyboardMarkup(texts.MAIN_MENU_BUTTONS[lang], resize_keyboard=True)
        )
        return ConversationHandler.END
    return DRIVER_MENU


def driver_location_received(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    if not update.message or not update.message.location:
        return DRIVER_SEND_LOCATION

    driver = db.get_driver_by_tg_id(update.effective_user.id)

    if update.message.location.live_period is None:
        update.message.reply_text(texts.TEXTS['driver_send_location'][lang])
        return DRIVER_SEND_LOCATION

    lat = update.message.location.latitude
    lon = update.message.location.longitude

    db.update_driver_location(update.effective_user.id, lat, lon)
    db.set_driver_online(driver[0], True)

    update.message.reply_text(
        texts.TEXTS['driver_now_online'][lang],
        reply_markup=ReplyKeyboardMarkup(texts.DRIVER_MENU_BUTTONS[lang], resize_keyboard=True)
    )
    return DRIVER_MENU

DRIVER_ORDERS_PER_PAGE = 10

def driver_my_orders(update: Update, context: CallbackContext, page=0):
    lang = get_lang(context, update.effective_user.id)
    driver = db.get_driver_by_tg_id(update.effective_user.id)
    all_orders = db.get_driver_orders(driver[0])

    if not all_orders:
        update.message.reply_text(texts.TEXTS['driver_no_orders'][lang])
        return DRIVER_MENU

    total = len(all_orders)
    total_pages = (total + DRIVER_ORDERS_PER_PAGE - 1) // DRIVER_ORDERS_PER_PAGE
    start = page * DRIVER_ORDERS_PER_PAGE
    page_orders = all_orders[start:start + DRIVER_ORDERS_PER_PAGE]

    text = texts.TEXTS['driver_orders_title'][lang]
    for i, order in enumerate(page_orders, start=start + 1):
        status = texts.TEXTS['order_statuses'][lang].get(order[11], "❓").split()[0]
        text += f"{i}. #{order[0]} | {order[3]} → {order[6]} {status}\n"

    buttons = []
    row = []
    for i, order in enumerate(page_orders, start=start + 1):
        row.append(InlineKeyboardButton(str(i), callback_data=f"driver_order_{order[0]}_{page}"))
        if len(row) == 5:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_prev'][lang], callback_data=f"driver_orders_page_{page - 1}"))
    if page < total_pages - 1:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_next'][lang], callback_data=f"driver_orders_page_{page + 1}"))
    if nav:
        buttons.append(nav)

    keyboard = InlineKeyboardMarkup(buttons)
    update.message.reply_text(text, reply_markup=keyboard)
    return DRIVER_ORDERS

def driver_orders_page(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)
    page = int(query.data.split("_")[-1])
    driver = db.get_driver_by_tg_id(update.effective_user.id)
    all_orders = db.get_driver_orders(driver[0])

    total = len(all_orders)
    total_pages = (total + DRIVER_ORDERS_PER_PAGE - 1) // DRIVER_ORDERS_PER_PAGE
    start = page * DRIVER_ORDERS_PER_PAGE
    page_orders = all_orders[start:start + DRIVER_ORDERS_PER_PAGE]

    text = texts.TEXTS['driver_orders_title'][lang]
    for i, order in enumerate(page_orders, start=start + 1):
        status = texts.TEXTS['order_statuses'][lang].get(order[11], "❓").split()[0]
        text += f"{i}. #{order[0]} | {order[3]} → {order[6]} {status}\n"

    buttons = []
    row = []
    for i, order in enumerate(page_orders, start=start + 1):
        row.append(InlineKeyboardButton(str(i), callback_data=f"driver_order_{order[0]}_{page}"))
        if len(row) == 5:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_prev'][lang], callback_data=f"driver_orders_page_{page - 1}"))
    if page < total_pages - 1:
        nav.append(InlineKeyboardButton(texts.TEXTS['btn_next'][lang], callback_data=f"driver_orders_page_{page + 1}"))
    if nav:
        buttons.append(nav)

    keyboard = InlineKeyboardMarkup(buttons)
    query.edit_message_text(text, reply_markup=keyboard)
    return DRIVER_ORDERS

def driver_order_detail(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    lang = get_lang(context, update.effective_user.id)

    parts = query.data.split("_")
    order_id = int(parts[2])
    page = int(parts[3])

    order = db.get_order(order_id)
    user = db.get_user(order[1])
    status_text = texts.TEXTS['order_statuses'][lang].get(order[11], "❓")

    text = texts.TEXTS['driver_order_detail'][lang].format(
        order_id=order[0],
        user=user[1] if user else "-",
        phone=user[2] if user else "-",
        tariff=order[2],
        from_loc=order[3],
        to_loc=order[6],
        distance=order[9],
        price=f"{order[10]:,}",
        date=order[14][:16],
        status=status_text,
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(texts.TEXTS['btn_back'][lang], callback_data=f"driver_orders_page_{page}")]
    ])

    query.edit_message_text(text, reply_markup=keyboard)
    return DRIVER_ORDERS

def driver_earnings(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    driver = db.get_driver_by_tg_id(update.effective_user.id)
    earnings = db.get_driver_earnings(driver[0])

    text = (
        texts.TEXTS['driver_earnings_title'][lang] +
        texts.TEXTS['driver_earnings_today'][lang].format(amount=f"{earnings['today']:,}") + "\n" +
        texts.TEXTS['driver_earnings_monthly'][lang].format(amount=f"{earnings['monthly']:,}") + "\n" +
        texts.TEXTS['driver_earnings_total'][lang].format(amount=f"{earnings['total']:,}") + "\n" +
        texts.TEXTS['driver_earnings_trips'][lang].format(count=earnings['trips'])
    )

    update.message.reply_text(text)
    return DRIVER_MENU

def driver_settings(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    keyboard = texts.DRIVER_SETTINGS_BUTTONS[lang]
    update.message.reply_text(texts.TEXTS['driver_settings_menu'][lang], reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
    return DRIVER_SETTINGS

def driver_settings_select(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text
    keyboard = texts.DRIVER_SETTINGS_BUTTONS[lang]

    change_l_p = keyboard[0][0]
    change_phone_num = keyboard[0][1]
    back = keyboard[1][0]

    if text == change_l_p:
        return driver_change_login_password(update, context)
    if text == change_phone_num:
        update.message.reply_text(texts.TEXTS['enter_new_phone'][lang])
        return driver_edit_phone(update, context)
    if text == back:
        return driver_menu(update, context)
    return DRIVER_SETTINGS

def driver_change_login_password(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)

    update.message.reply_text(texts.TEXTS['driver_change_login_password_ask'][lang])
    return DRIVER_LOG_PASSW_CHANGE

def driver_new_login_password(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    text = update.message.text.split()

    if len(text) != 2:
        update.message.reply_text(texts.TEXTS['driver_change_login_password_wrong'][lang])
        return DRIVER_LOG_PASSW_CHANGE

    driver = db.get_driver_by_tg_id(update.effective_user.id)
    driver_id = driver[0]
    login = text[0]
    password = text[1]
    try:
        db.change_driver_login_password(driver_id, login, password)
        update.message.reply_text(texts.TEXTS['driver_password_changed'][lang].format(
            login=login,
            password=password
        ))
        return DRIVER_SETTINGS
    except:
        update.message.reply_text(texts.TEXTS['driver_login_already_exists'][lang])
        return DRIVER_LOG_PASSW_CHANGE

def driver_edit_phone(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    db.driver_update_phone_number(update.effective_user.id, update.message.text)
    update.message.reply_text(texts.TEXTS['phone_updated'][lang])
    return DRIVER_SETTINGS

def driver_exit(update: Update, context: CallbackContext):
    lang = get_lang(context, update.effective_user.id)
    driver = db.get_driver_by_tg_id(update.effective_user.id)
    driver_id = driver[0]

    update.message.reply_text(
        texts.TEXTS['main_menu'][lang],
        reply_markup=ReplyKeyboardMarkup(
            texts.MAIN_MENU_BUTTONS[lang],
            resize_keyboard=True,
        ),
    )
    db.set_driver_logged(driver_id, False)
    return ConversationHandler.END

def accept_order(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    parts = query.data.split("_")
    order_id = int(parts[1])
    user_id = int(parts[2])

    # Haydovchi o'z buyurtmasini qabul qila olmasligini tekshirish
    if str(query.from_user.id) == str(user_id):
        query.answer("❌ Siz o'z buyurtmangizni qabul qila olmaysiz!", show_alert=True)
        return

    order = db.get_order(order_id)

    # Buyurtma allaqachon qabul qilinganmi
    if order[11] != db.OrderStatus.PENDING:
        query.edit_message_text(texts.TEXTS['order_already_taken']['uz'])
        return

    driver = db.get_driver_by_tg_id(query.from_user.id)

    # Holat yangilash
    db.update_order_status(order_id, db.OrderStatus.ACCEPTED, driver_id=driver[0])

    # Boshqa haydovchilardagi xabarni o'zgartirish
    driver_messages = db.get_driver_messages(order_id)
    for tg_id, msg_id in driver_messages.items():
        if str(tg_id) != str(query.from_user.id):
            try:
                context.bot.edit_message_text(
                    chat_id=int(tg_id),
                    message_id=msg_id,
                    text=texts.TEXTS['order_already_taken']['uz']
                )
            except:
                pass

    # Haydovchiga yo'lovchi manzili va lokatsiyasi yuborish
    query.edit_message_text(texts.TEXTS['driver_order_accepted']['uz'])

    context.bot.send_message(
        chat_id=query.from_user.id,
        text=f"📍 Yo'lovchi manzili:\n{order[3]}"
    )

    if order[4] and order[5]:
        context.bot.send_location(
            chat_id=query.from_user.id,
            latitude=order[4],
            longitude=order[5]
        )

    # Haydovchiga yo'lovchini oldim tugmasi
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚗 Yo'lovchini oldim", callback_data=f"picked_up_{order_id}_{user_id}")]
    ])
    context.bot.send_message(
        chat_id=query.from_user.id,
        text="Yo'lovchi oldingizga yetib borgach tugmani bosing:",
        reply_markup=keyboard
    )

    # Yo'lovchiga haydovchi ma'lumotlari yuborish
    rating = f"{driver[17]:.1f} ⭐ ({driver[18]} ta baho)" if driver[18] > 0 else "Hali baho yo'q"
    context.bot.send_message(
        chat_id=user_id,
        text=texts.TEXTS['user_driver_info']['uz'].format(
            name=driver[5],
            phone=driver[6],
            car_model=driver[7],
            car_number=driver[8],
            rating=rating
        )
    )

def driver_picked_up(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    parts = query.data.split("_")
    order_id = int(parts[2])
    user_id = int(parts[3])

    driver = db.get_driver_by_tg_id(query.from_user.id)
    order = db.get_order(order_id)

    # Holat yangilash
    db.update_order_status(order_id, db.OrderStatus.PICKED_UP, driver_id=driver[0])

    # Haydovchiga borilish manzili va lokatsiyasi yuborish
    query.edit_message_text("🚗 Yo'lovchi olindi! Manzilga yuring.")

    context.bot.send_message(
        chat_id=query.from_user.id,
        text=f"🏁 Borilishi kerak bo'lgan manzil:\n{order[6]}"
    )

    if order[7] and order[8]:  # to_lat, to_lon
        context.bot.send_location(
            chat_id=query.from_user.id,
            latitude=order[7],
            longitude=order[8]
        )

    # Haydovchiga safarni tugatish tugmasi
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🏁 Safarni tugatish", callback_data=f"finish_{order_id}_{user_id}")]
    ])
    context.bot.send_message(
        chat_id=query.from_user.id,
        text="Manzilga yetib borgach tugmani bosing:",
        reply_markup=keyboard
    )

    # Yo'lovchiga xabar
    context.bot.send_message(
        chat_id=user_id,
        text=texts.TEXTS['driver_picked_up']['uz']
    )


def driver_finish_trip(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    parts = query.data.split("_")
    order_id = int(parts[1])
    user_id = int(parts[2])

    driver = db.get_driver_by_tg_id(query.from_user.id)

    # Holat yangilash
    db.update_order_status(order_id, db.OrderStatus.FINISHED, driver_id=driver[0])

    # Haydovchiga xabar
    query.edit_message_text(texts.TEXTS['driver_trip_finished']['uz'])

    # Yo'lovchiga xabar + baho berish
    user = db.get_user(user_id)
    lang = user[3] if user else 'uz'

    context.bot.send_message(
        chat_id=user_id,
        text=texts.TEXTS['trip_finished'][lang],
        reply_markup=ReplyKeyboardMarkup(texts.MAIN_MENU_BUTTONS[lang], resize_keyboard=True)
    )

    # Baho berish tugmalari
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("1⭐", callback_data=f"rate_{order_id}_1"),
            InlineKeyboardButton("2⭐", callback_data=f"rate_{order_id}_2"),
            InlineKeyboardButton("3⭐", callback_data=f"rate_{order_id}_3"),
            InlineKeyboardButton("4⭐", callback_data=f"rate_{order_id}_4"),
            InlineKeyboardButton("5⭐", callback_data=f"rate_{order_id}_5"),
        ]
    ])
    context.bot.send_message(
        chat_id=user_id,
        text="⭐ Agar haydovchi xizmatidan qoniqqan bo'lsangiz uni baholang!\n\n💬 Safar bo'yicha shikoyatingiz bo'lsa yordam bo'limi orqali administratorlarga jo'nating.",
        reply_markup=keyboard
    )
def rate_driver(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    parts = query.data.split("_")
    order_id = int(parts[1])
    rating = int(parts[2])

    order = db.get_order(order_id)
    driver = db.get_driver_by_id(order[12])

    db.update_driver_rating(driver[0], rating)

    query.edit_message_text(texts.TEXTS['driver_rated']['uz'])

def main():
    exit_buttons = [
        texts.ADMIN_MENU_BUTTONS["uz"][-1][0],
        texts.ADMIN_MENU_BUTTONS["ru"][-1][0],
        texts.ADMIN_MENU_BUTTONS["en"][-1][0],
    ]

    db.create_table()
    db.migrate()

    updater = Updater(TOKEN)
    dp = updater.dispatcher

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SET_LAN:   [CallbackQueryHandler(choose_language, pattern='^lang_')],
            NAME:      [MessageHandler(Filters.text & ~Filters.command, get_name)],
            PHONE:     [MessageHandler(Filters.contact, get_phone)],
            MAIN_MENU: [MessageHandler(Filters.text & ~Filters.command, main_menu_select),
                        CallbackQueryHandler(orders_page, pattern=r'^orders_page_\d+$'),
                        CallbackQueryHandler(order_detail, pattern=r'^order_detail_\d+_\d+$'),
                        CommandHandler("admin", admin_start)
                        ],
            TAKE_TAXI: [CallbackQueryHandler(take_taxi_select, pattern='^tariff_'),
                        MessageHandler(Filters.text & ~Filters.command, main_menu_select)],
            TAKE_TAXI_TO: [
                MessageHandler(Filters.location, share_to),
                MessageHandler(Filters.text & ~Filters.command, share_to),
            ],
            TAKE_TAXI_FROM: [MessageHandler(Filters.location, share_from),
                             MessageHandler(Filters.text & ~Filters.command, share_from)],
            TAKE_TAXI_CONFIRM: [CallbackQueryHandler(confirm_order, pattern='^order_confirm$'),
                                CallbackQueryHandler(cancel_order, pattern='^order_cancel$')],
            TAKE_TAXI_PAYMENT: [CallbackQueryHandler(pay_cash, pattern='^pay_cash$'),
                                CallbackQueryHandler(pay_card, pattern='^pay_card$')],
            HELP: [
                MessageHandler(Filters.text & ~Filters.command, help_receive),
                CallbackQueryHandler(help_cancel, pattern='^help_cancel$'),
            ],
            TARIFFS_LIST: [CallbackQueryHandler(tariffs_select, pattern="^tariff_"),
                           MessageHandler(Filters.text & ~Filters.command, main_menu_select)],
            SETTINGS:  [MessageHandler(Filters.text & ~Filters.command, setting_menu_select)],
            EDIT_NAME: [MessageHandler(Filters.text & ~Filters.command, edit_name)],
            EDIT_PHONE:[MessageHandler(Filters.text & ~Filters.command, edit_phone)],
        },
        fallbacks=[CommandHandler("admin", admin_start)],
        per_message=False
    )

    admin_conv = ConversationHandler(
        entry_points=[CommandHandler("admin", admin_start)],
        states={
            ADMIN_MENU: [MessageHandler(Filters.text & ~Filters.command, admin_menu),
                         MessageHandler(Filters.text(exit_buttons), admin_exit)],
            ADMIN_MENU_TARIFFS: [MessageHandler(Filters.text & ~Filters.command, admin_tariffs_select)],
            ADMIN_TARIFF_ADD_NAME_UZ: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_add_name_uz)],
            ADMIN_TARIFF_ADD_NAME_RU: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_add_name_ru)],
            ADMIN_TARIFF_ADD_NAME_EN: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_add_name_en)],
            ADMIN_TARIFF_ADD_DESC_UZ: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_add_desc)],
            ADMIN_TARIFF_ADD_DESC_RU: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_add_desc_ru)],
            ADMIN_TARIFF_ADD_DESC_EN: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_add_desc_en)],
            ADMIN_TARIFF_ADD_BASE_PRICE: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_add_base_price)],
            ADMIN_TARIFF_ADD_PER_KM: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_add_per_km)],
            ADMIN_TARIFF_EDIT: [CallbackQueryHandler(admin_tariffs_edit_select, pattern=r'^edit_tariff_'),
                                CallbackQueryHandler(admin_tariff_edit_base, pattern=r'^edit_base_'),
                                CallbackQueryHandler(admin_tariff_edit_per_km, pattern=r'^edit_perkm_')],
            ADMIN_TARIFF_EDIT_PRICE: [MessageHandler(Filters.text & ~Filters.command, admin_tariff_save_price)],
            ADMIN_TARIFF_DEL: [CallbackQueryHandler(admin_tariffs_del_select, pattern=r'^delete_tariff_')],
            ADMIN_TARIFF_DEL_CONFIRM: [CallbackQueryHandler(admin_tariffs_del_execute, pattern=r'^del_confirm_')],
            ADMIN_DRIVERS: [
                MessageHandler(Filters.text & ~Filters.command, admin_drivers_select),
                CallbackQueryHandler(admin_drivers_list_select, pattern=r'^drivers_page_\d+$'),
                CallbackQueryHandler(admin_driver_detail, pattern=r'^drivers_list_\d+_\d+$'),
            ],
            ADMIN_DRIVER_ADD_TG_ID: [MessageHandler(Filters.text & ~Filters.command, admin_driver_add_tg_id)],
            ADMIN_DRIVER_ADD_NAME: [MessageHandler(Filters.text & ~Filters.command, admin_driver_add_name)],
            ADMIN_DRIVER_ADD_PHONE: [MessageHandler(Filters.text & ~Filters.command, admin_driver_add_phone)],
            ADMIN_DRIVER_ADD_CAR_MODEL: [MessageHandler(Filters.text & ~Filters.command, admin_driver_add_car_model)],
            ADMIN_DRIVER_ADD_CAR_NUM: [MessageHandler(Filters.text & ~Filters.command, admin_driver_add_car_number)],
            ADMIN_DRIVERS_SEARCH: [MessageHandler(Filters.text & ~Filters.command, admin_driver_find)],
            ADMIN_DRIVER_INFO: [CallbackQueryHandler(admin_driver_info, pattern=r"^driver_info_\d+$")],
            ADMIN_DRIVERS_ADD_TARIFF: [MessageHandler(Filters.text & ~Filters.command, admin_driver_find_for_tariff)],
            ADMIN_DRIVERS_SELECT_TARIFF: [CallbackQueryHandler(admin_driver_assign_tariff, pattern=r"^assign_tariff_\d+$")],
            ADMIN_DRIVERS_ASSIGN_TARIFF: [CallbackQueryHandler(admin_driver_save_tariff, pattern=r"^select_tariff_\w+$")],
            ADMIN_DRIVERS_SELECT_MORE_TARIFF: [CallbackQueryHandler(admin_driver_select_more_tariff, pattern=r"^assign_tariff_more_")],
            ADMIN_DRIVER_DELETE_TARIFF: [MessageHandler(Filters.text & ~Filters.command, admin_driver_tariff_del_find)],
            ADMIN_DRIVER_SELECT_DELETE_TARIFF: [CallbackQueryHandler(admin_driver_select_delete_tariff, pattern=r"^remove_driver_tariff$")],
            ADMIN_DRIVER_CHOOSE_DELETE_TARIFF: [CallbackQueryHandler(admin_driver_choose_delete_tariff, pattern=r"^del_driver_tariff_\w+$")],
            ADMIN_DRIVER_DELETE: [MessageHandler(Filters.text & ~Filters.command, admin_driver_delete_find)],
            ADMIN_DRIVER_DELETE_CONFIRM: [CallbackQueryHandler(admin_driver_delete_confirm, pattern=r"^driver_delete$")],
            ADMIN_DRIVER_DELETE_CONFIRM_FINISH: [CallbackQueryHandler(admin_driver_delete_confirm_finish, pattern=r"^driver_delete_")],
            ADMIN_DRIVER_B_UB: [MessageHandler(Filters.text & ~Filters.command, admin_driver_b_ub_search)],
            ADMIN_DRIVER_B_UB_CHOOSE: [CallbackQueryHandler(admin_driver_b_ub_choose, pattern=r"^driver_b_btn$|^driver_ub_btn$")],
            ADMIN_DRIVER_B_UB_SUBMIT: [CallbackQueryHandler(admin_driver_block_submit, pattern=r"^driver_b_btn_")],
            ADMIN_ORDERS: [
                MessageHandler(Filters.text & ~Filters.command, admin_orders_select),
                CallbackQueryHandler(admin_orders_filtered_list, pattern=r"^filter_"),
                CallbackQueryHandler(admin_orders_filtered_list, pattern=r"^orders_filter_page_\d+$"),
                CallbackQueryHandler(admin_order_detail, pattern=r"^admin_order_\d+_\d+$"),
            ],
            ADMIN_ORDERS_FILTER: [
                MessageHandler(Filters.text & ~Filters.command, admin_orders_select),
                CallbackQueryHandler(admin_orders_filtered_list, pattern=r"^filter_"),
                CallbackQueryHandler(admin_orders_filtered_list, pattern=r"^orders_filter_page_\d+$"),
                CallbackQueryHandler(admin_order_detail, pattern=r"^admin_order_\d+_\d+$"),
            ],
            ADMIN_ORDER_SEARCH: [MessageHandler(Filters.text & ~Filters.command, admin_order_find)],
            ADMIN_BROADCAST: [CallbackQueryHandler(admin_broadcast_choose, pattern=r"^broadcast_")],
            ADMIN_BROADCAST_SEND: [
                MessageHandler(Filters.text & ~Filters.command, admin_broadcast_send),
                MessageHandler(Filters.photo, admin_broadcast_send),
                MessageHandler(Filters.video, admin_broadcast_send),
                MessageHandler(Filters.audio, admin_broadcast_send),
                MessageHandler(Filters.voice, admin_broadcast_send),
            ],
        },
        fallbacks=[MessageHandler(Filters.text(exit_buttons), admin_exit)],
        per_message=False
    )
    driver_conv = ConversationHandler(
        entry_points=[CommandHandler("driver", driver_start)],
        states={
            DRIVER_LOGIN: [MessageHandler(Filters.text & ~Filters.command, driver_login)],
            DRIVER_MENU: [MessageHandler(Filters.text & ~Filters.command, driver_menu_select)],
            DRIVER_ORDERS: [
                MessageHandler(Filters.text & ~Filters.command, driver_menu_select),
                CallbackQueryHandler(driver_orders_page, pattern=r"^driver_orders_page_\d+$"),
                CallbackQueryHandler(driver_order_detail, pattern=r"^driver_order_\d+_\d+$"),
            ],
            DRIVER_SETTINGS: [MessageHandler(Filters.text & ~Filters.command, driver_settings_select)],
            DRIVER_LOG_PASSW_CHANGE: [MessageHandler(Filters.text & ~Filters.command, driver_new_login_password)],
            DRIVER_SEND_LOCATION: [
                MessageHandler(Filters.location, driver_location_received),
                MessageHandler(Filters.text & ~Filters.command, driver_menu_select),
            ],
        },
        fallbacks=[MessageHandler(Filters.text(exit_buttons), driver_exit)],
        per_message=False
    )

    dp.add_handler(conv)
    dp.add_handler(admin_conv)
    dp.add_handler(driver_conv)
    dp.add_handler(PreCheckoutQueryHandler(pre_checkout))
    dp.add_handler(MessageHandler(Filters.successful_payment, payment_success))
    dp.add_handler(CallbackQueryHandler(accept_order, pattern=r"^accept_\d+_\d+$"))
    dp.add_handler(CallbackQueryHandler(driver_picked_up, pattern=r"^picked_up_\d+_\d+$"))
    dp.add_handler(CallbackQueryHandler(driver_finish_trip, pattern=r"^finish_\d+_\d+$"))
    dp.add_handler(CallbackQueryHandler(rate_driver, pattern=r"^rate_\d+_\d+$"))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()