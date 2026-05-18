# ============================================================
#                        LANGUAGE BUTTONS
# ============================================================

LANG_BUTTONS = [
    ("O'zbekcha 🇺🇿", "lang_uz"),
    ("Русский 🇷🇺",   "lang_ru"),
    ("English 🇬🇧",   "lang_en"),
]


# ============================================================
#                        MAIN MENU
# ============================================================

MAIN_MENU_BUTTONS = {
    "uz": [
        ["Taxi chaqirish 🚕", "Mening buyurtmalarim 🗒"],
        ["Tariflar 📁", "Yordam 🤝"],
        ["Sozlamalar ⚙️"]
    ],
    "ru": [
        ["Вызвать такси 🚕", "Мои заказы 🗒"],
        ["Тарифы 📁", "Помощь 🤝"],
        ["Настройки ⚙️"]
    ],
    "en": [
        ["Call a taxi 🚕", "My orders 🗒"],
        ["Tariffs 📁", "Help 🤝"],
        ["Settings ⚙️"]
    ],
}


# ============================================================
#                        SHARE BUTTONS
# ============================================================

SHARE_BUTTONS = {
    "phone": {
        "uz": "Raqamni yuborish 📱",
        "ru": "Отправить номер 📱",
        "en": "Share number 📱"
    },
}

SHARE_LOCATION_BTN = {
    "uz": "Joylashuvimni yuborish 📍",
    "ru": "Отправить геолокацию 📍",
    "en": "Share my location 📍"
}


# ============================================================
#                        SETTINGS
# ============================================================

SETTINGS_BUTTONS = {
    "uz": [
        ["Ismni tahrirlash 🖊", "Telefon raqamni tahrirlash 📞"],
        ["Tilni o'zgartirish 🌐"],
        ["Orqaga qaytish ⬅️"]
    ],
    "ru": [
        ["Изменить имя 🖊", "Изменить номер телефона 📞"],
        ["Изменить язык 🌐"],
        ["Назад ⬅️"]
    ],
    "en": [
        ["Edit name 🖊", "Edit phone number 📞"],
        ["Change language 🌐"],
        ["Go back ⬅️"]
    ],
}


# ============================================================
#                        ADMIN MENU
# ============================================================

ADMIN_MENU_BUTTONS = {
    "uz": [
        ["👤 Haydovchilar", "🚖 Tariflar"],
        ["📋 Buyurtmalar", "📊 Statistika"],
        ["📢 Xabar yuborish"],
        ["🚪 Chiqish"]
    ],
    "ru": [
        ["👤 Водители", "🚖 Тарифы"],
        ["📋 Заказы", "📊 Статистика"],
        ["📢 Рассылка"],
        ["🚪 Выход"]
    ],
    "en": [
        ["👤 Drivers", "🚖 Tariffs"],
        ["📋 Orders", "📊 Statistics"],
        ["📢 Broadcast"],
        ["🚪 Exit"]
    ],
}


# ============================================================
#                        TAXI DRIVERS
# ============================================================

ADMIN_DRIVERS_BUTTONS = {
    "uz": [
        ["📋 Haydovchilar ro'yxati", "➕ Haydovchi qo'shish"],
        ["🔍 Haydovchini qidirish", "🚖 Tarif biriktirish"],
        ["✏️ Tarifini o'zgartirish", "🗑 Haydovchini o'chirish"],
        ["🚫 Bloklash / Ochish"],
        ["⬅️ Orqaga"]
    ],
    "ru": [
        ["📋 Список водителей", "➕ Добавить водителя"],
        ["🔍 Найти водителя", "🚖 Привязать тариф"],
        ["✏️ Изменить тариф", "🗑 Удалить водителя"],
        ["🚫 Блок / Разблок"],
        ["⬅️ Назад"]
    ],
    "en": [
        ["📋 Drivers list", "➕ Add driver"],
        ["🔍 Search driver", "🚖 Assign tariff"],
        ["✏️ Change tariff", "🗑 Delete driver"],
        ["🚫 Block / Unblock"],
        ["⬅️ Back"]
    ],
}

ADMIN_TARIFFS_BUTTONS = {
    "uz": [
        ["📋 Tariflar ro'yxati", "➕ Tarif qo'shish"],
        ["✏️ Tariflarni tahrirlash", "🗑 Tariflarni o'chirish"],
        ["⬅️ Orqaga"]
    ],
    "ru": [
        ["📋 Список тарифов", "➕ Добавить тариф"],
        ["✏️ Редактировать тарифы", "🗑 Удалить тариф"],
        ["⬅️ Назад"]
    ],
    "en": [
        ["📋 Tariffs list", "➕ Add tariff"],
        ["✏️ Edit tariffs", "🗑 Delete tariff"],
        ["⬅️ Back"]
    ],
}


ADMIN_ORDERS_BUTTONS = {
    "uz": [
        ["📋 Buyurtmalar ro'yxati", "🔍 Buyurtma qidirish"],
        ["⬅️ Orqaga"]
    ],
    "ru": [
        ["📋 Список заказов", "🔍 Найти заказ"],
        ["⬅️ Назад"]
    ],
    "en": [
        ["📋 Orders list", "🔍 Search order"],
        ["⬅️ Back"]
    ],
}

ADMIN_ORDERS_FILTER_BUTTONS = {
    "uz": [
        ("⏳ Kutilmoqda", "filter_pending"),
        ("✅ Yakunlangan", "filter_finished"),
        ("❌ Bekor qilingan", "filter_cancelled"),
        ("📋 Barchasi", "filter_all"),
    ],
    "ru": [
        ("⏳ Ожидает", "filter_pending"),
        ("✅ Завершён", "filter_finished"),
        ("❌ Отменён", "filter_cancelled"),
        ("📋 Все", "filter_all"),
    ],
    "en": [
        ("⏳ Pending", "filter_pending"),
        ("✅ Finished", "filter_finished"),
        ("❌ Cancelled", "filter_cancelled"),
        ("📋 All", "filter_all"),
    ],
}


# ============================================================
#                        ORDER STATUSES
# ============================================================

ORDER_STATUSES = {
    "pending":   {"uz": "⏳ Kutilmoqda",      "ru": "⏳ Ожидает",       "en": "⏳ Pending"},
    "accepted":  {"uz": "✅ Qabul qilindi",    "ru": "✅ Принят",        "en": "✅ Accepted"},
    "picked_up": {"uz": "🚗 Yo'lovchi olindi", "ru": "🚗 Пассажир взят", "en": "🚗 Picked up"},
    "finished":  {"uz": "🏁 Yakunlandi",       "ru": "🏁 Завершён",      "en": "🏁 Finished"},
    "cancelled": {"uz": "❌ Bekor qilindi",    "ru": "❌ Отменён",       "en": "❌ Cancelled"},
}

DRIVER_MENU_BUTTONS = {
    "uz": [
        ["🟢 Online", "🔴 Offline"],
        ["📋 Mening buyurtmalarim", "💰 Daromadim"],
        ["⚙️ Sozlamalar"],
        ["🚪 Chiqish"]
    ],
    "ru": [
        ["🟢 Online", "🔴 Offline"],
        ["📋 Мои заказы", "💰 Мой доход"],
        ["⚙️ Настройки"],
        ["🚪 Выход"]
    ],
    "en": [
        ["🟢 Online", "🔴 Offline"],
        ["📋 My orders", "💰 My earnings"],
        ["⚙️ Settings"],
        ["🚪 Exit"]
    ],
}

DRIVER_SETTINGS_BUTTONS = {
    "uz": [
        ["🔐 Login/Parol o'zgartirish", "📞 Telefon raqamni o'zgartirish"],
        ["⬅️ Orqaga"]
    ],
    "ru": [
        ["🔐 Изменить логин/пароль", "📞 Изменить номер телефона"],
        ["⬅️ Назад"]
    ],
    "en": [
        ["🔐 Change login/password", "📞 Change phone number"],
        ["⬅️ Back"]
    ],
}

DRIVER_TARIFF_BUTTONS = {
    "uz": [
        ["🚗 Standart", "🚙 Comfort"],
        ["👑 Business"],
    ],
    "ru": [
        ["🚗 Стандарт", "🚙 Комфорт"],
        ["👑 Бизнес"],
    ],
    "en": [
        ["🚗 Standard", "🚙 Comfort"],
        ["👑 Business"],
    ],
}


# ============================================================
#                        TEXTS
# ============================================================

TEXTS = {

    # --- Ro'yxatdan o'tish ---
    "choose_language": {
        "uz": "Tilni tanlang 🌐",
        "ru": "Выберите язык 🌐",
        "en": "Choose a language 🌐"
    },
    "enter_name": {
        "uz": "Ism familiyangizni kiriting 📝",
        "ru": "Введите ваше имя и фамилию 📝",
        "en": "Enter your full name 📝"
    },
    "enter_phone": {
        "uz": "Telefon raqamingizni kiriting ☎️",
        "ru": "Введите ваш номер телефона ☎️",
        "en": "Enter your phone number ☎️"
    },
    "registered_success": {
        "uz": "Ro'yxatdan muvaffaqiyatli o'tdingiz ✅",
        "ru": "Вы успешно зарегистрировались ✅",
        "en": "You have successfully registered ✅"
    },

    # --- Asosiy menyu ---
    "main_menu": {
        "uz": "Asosiy menyu 🏠",
        "ru": "Главное меню 🏠",
        "en": "Main menu 🏠"
    },

    # --- Taxi chaqirish ---
    "no_tariffs": {
        "uz": "Hozircha tariflar mavjud emas 🚫",
        "ru": "Тарифы пока недоступны 🚫",
        "en": "No tariffs available yet 🚫"
    },
    "choose_tariff": {
        "uz": "Tarifni tanlang 👇",
        "ru": "Выберите тариф 👇",
        "en": "Choose a tariff 👇",
    },
    "ask_from": {
        "uz": "Qayerda turibsiz? 📍\n\nJoylashuvingizni yuboring yoki to'liq manzilingizni yozing:\n\nMasalan: Chilonzor 3-mavze, 12-uy",
        "ru": "Где вы находитесь? 📍\n\nОтправьте геолокацию или напишите полный адрес:\n\nНапример: Чиланзар 3-й массив, дом 12",
        "en": "Where are you located? 📍\n\nSend your location or type your full address:\n\nExample: Chilonzor 3rd district, house 12"
    },
    "ask_to": {
        "uz": "Qayerga bormoqchisiz? 🏁\n\nBoradigan manzilingizni to'liq yozing:\n\nMasalan: Yunusobod 1-mavze, 5-uy",
        "ru": "Куда вы хотите поехать? 🏁\n\nНапишите полный адрес назначения:\n\nНапример: Юнусабад 1-й массив, дом 5",
        "en": "Where do you want to go? 🏁\n\nType your full destination address:\n\nExample: Yunusobod 1st district, house 5"
    },
    "location_not_found": {
        "uz": "Manzil topilmadi ❌\n\nIltimos aniqroq yozing:\nMasalan: 'Chilonzor 3-mavze, 12-uy'",
        "ru": "Адрес не найден ❌\n\nНапишите точнее:\nНапример: 'Чиланзар 3-й массив, дом 12'",
        "en": "Address not found ❌\n\nPlease be more specific:\nExample: 'Chilonzor 3rd district, house 12'"
    },

    # --- Buyurtma tasdiqlash ---
    "order_confirm": {
        "uz": "Buyurtma ma'lumotlari 📋\n\nTarif: {tariff} 🚖\nQayerdan: {from_loc} 📍\nQayerga: {to_loc} 🏁\nMaxofa: {distance} km 📏\nTaxminiy narx: {price} so'm 💰\n\nTasdiqlaysizmi?",
        "ru": "Данные заказа 📋\n\nТариф: {tariff} 🚖\nОткуда: {from_loc} 📍\nКуда: {to_loc} 🏁\nРасстояние: {distance} км 📏\nПримерная цена: {price} сум 💰\n\nПодтверждаете?",
        "en": "Order details 📋\n\nTariff: {tariff} 🚖\nFrom: {from_loc} 📍\nTo: {to_loc} 🏁\nDistance: {distance} km 📏\nEstimated price: {price} sum 💰\n\nConfirm?"
    },
    "confirm_btn": {
        "uz": "Tasdiqlash ✅",
        "ru": "Подтвердить ✅",
        "en": "Confirm ✅"
    },
    "cancel_btn": {
        "uz": "Bekor qilish ❌",
        "ru": "Отмена ❌",
        "en": "Cancel ❌"
    },

    # --- To'lov ---
    "choose_payment": {
        "uz": "To'lov usulini tanlang 💳",
        "ru": "Выберите способ оплаты 💳",
        "en": "Choose payment method 💳"
    },
    "cash_btn": {
        "uz": "Naqd pul 💵",
        "ru": "Наличные 💵",
        "en": "Cash 💵"
    },
    "card_btn": {
        "uz": "Karta (Click) 💳",
        "ru": "Карта (Click) 💳",
        "en": "Card (Click) 💳"
    },
    "cash_order_sent": {
        "uz": "Buyurtmangiz yuborildi ✅\n\nHaydovchi kelgach naqd pul to'lang 💵",
        "ru": "Заказ отправлен ✅\n\nОплатите наличными при прибытии водителя 💵",
        "en": "Order sent ✅\n\nPay cash when the driver arrives 💵"
    },
    "invoice_title": {
        "uz": "Yo'l haqi",
        "ru": "Стоимость поездки",
        "en": "Trip fare"
    },
    "invoice_desc": {
        "uz": "Taxi xizmati uchun to'lov",
        "ru": "Оплата за услугу такси",
        "en": "Payment for taxi service"
    },
    "tariff_label": {
        "uz": "Yo'l haqi",
        "ru": "Стоимость поездки",
        "en": "Trip fare"
    },
    "payment_success": {
        "uz": "To'lov muvaffaqiyatli amalga oshdi ✅\n\nHaydovchi qidirilmoqda, biroz kuting...",
        "ru": "Оплата прошла успешно ✅\n\nИщем водителя, подождите немного...",
        "en": "Payment successful ✅\n\nLooking for a driver, please wait..."
    },
    "order_cancelled": {
        "uz": "Buyurtma bekor qilindi ❌",
        "ru": "Заказ отменён ❌",
        "en": "Order cancelled ❌"
    },

    # --- Buyurtma holatlari ---
    "order_sent": {
        "uz": "Buyurtmangiz yuborildi ✅\n\nHaydovchi qidirilmoqda, biroz kuting...",
        "ru": "Ваш заказ отправлен ✅\n\nИщем водителя, подождите немного...",
        "en": "Your order has been sent ✅\n\nLooking for a driver, please wait..."
    },
    "driver_coming": {
        "uz": "Haydovchi buyurtmangizni qabul qildi 🚗\nYaqin orada yetib keladi, tayyor bo'ling!",
        "ru": "Водитель принял ваш заказ 🚗\nСкоро прибудет, будьте готовы!",
        "en": "Driver accepted your order 🚗\nGet ready, coming soon!"
    },
    "driver_picked_up": {
        "uz": "Taxi keldi 🚕\n\nYoqimli sayohat tilaymiz 😊",
        "ru": "Такси прибыло 🚕\n\nЖелаем приятной поездки 😊",
        "en": "Taxi has arrived 🚕\n\nHave a pleasant journey 😊"
    },
    "trip_finished": {
        "uz": "Manzilga yetib keldingiz ✅\n\nBizdan foydalanganingiz uchun rahmat 🙏",
        "ru": "Вы прибыли на место ✅\n\nСпасибо, что воспользовались нашим сервисом 🙏",
        "en": "You have arrived ✅\n\nThank you for using our service 🙏"
    },
    "order_already_taken": {
        "uz": "Bu buyurtma allaqachon qabul qilingan ⚠️",
        "ru": "Этот заказ уже принят ⚠️",
        "en": "This order has already been taken ⚠️"
    },

    # --- Mening buyurtmalarim ---
    "no_orders": {
        "uz": "Sizda hali buyurtmalar yo'q 🤷‍♂️",
        "ru": "У вас пока нет заказов 🤷‍♂️",
        "en": "You have no orders yet 🤷‍♂️"
    },
    "my_orders_title": {
        "uz": "📋 Buyurtmalar tarixi:\n\n",
        "ru": "📋 История заказов:\n\n",
        "en": "📋 Order history:\n\n"
    },
    "order_statuses": {
        "uz": {
            "pending":   "⏳ Kutilmoqda",
            "accepted":  "✅ Qabul qilindi",
            "picked_up": "🚗 Yo'lovchi olindi",
            "finished":  "🏁 Yakunlandi",
            "cancelled": "❌ Bekor qilindi"
        },
        "ru": {
            "pending":   "⏳ Ожидает",
            "accepted":  "✅ Принят",
            "picked_up": "🚗 Пассажир взят",
            "finished":  "🏁 Завершён",
            "cancelled": "❌ Отменён"
        },
        "en": {
            "pending":   "⏳ Pending",
            "accepted":  "✅ Accepted",
            "picked_up": "🚗 Picked up",
            "finished":  "🏁 Finished",
            "cancelled": "❌ Cancelled"
        }
    },
    "order_detail_title": {
        "uz": "📦 Buyurtma #",
        "ru": "📦 Заказ #",
        "en": "📦 Order #"
    },
    "order_tariff": {
        "uz": "🚖 Tarif",
        "ru": "🚖 Тариф",
        "en": "🚖 Tariff"
    },
    "order_from": {
        "uz": "📍 Qayerdan",
        "ru": "📍 Откуда",
        "en": "📍 From"
    },
    "order_to": {
        "uz": "🏁 Qayerga",
        "ru": "🏁 Куда",
        "en": "🏁 To"
    },
    "order_distance": {
        "uz": "📏 Masofa",
        "ru": "📏 Расстояние",
        "en": "📏 Distance"
    },
    "order_price": {
        "uz": "💰 Narx",
        "ru": "💰 Цена",
        "en": "💰 Price"
    },
    "order_date": {
        "uz": "📅 Sana",
        "ru": "📅 Дата",
        "en": "📅 Date"
    },
    "order_status": {
        "uz": "⏳ Holat",
        "ru": "⏳ Статус",
        "en": "⏳ Status"
    },

    # --- Navigatsiya tugmalari ---
    "btn_prev": {
        "uz": "◀️ Oldingi",
        "ru": "◀️ Назад",
        "en": "◀️ Previous"
    },
    "btn_next": {
        "uz": "Keyingi ▶️",
        "ru": "Вперёд ▶️",
        "en": "Next ▶️"
    },
    "btn_back": {
        "uz": "⬅️ Orqaga",
        "ru": "⬅️ Назад",
        "en": "⬅️ Back"
    },

    # --- Yordam ---
    "help_ask": {
        "uz": "🤝 Yordam\n\nMuammo yoki shikoyatingizni yuboring, adminlarimiz tez orada so'rovingizni ko'rib chiqib siz bilan bog'lanishadi 👇",
        "ru": "🤝 Помощь\n\nОпишите вашу проблему или жалобу, наши администраторы скоро рассмотрят ваш запрос и свяжутся с вами 👇",
        "en": "🤝 Help\n\nSend your problem or complaint, our admins will review your request and contact you shortly 👇"
    },
    "help_cancel": {
        "uz": "Bekor qilish ❌",
        "ru": "Отмена ❌",
        "en": "Cancel ❌"
    },
    "help_admin_msg": {
        "uz": "📨 Yangi yordam so'rovi!\n\n👤 Ism: {name}\n📞 Tel: {phone}\n💬 Xabar: {message}",
        "ru": "📨 Новый запрос помощи!\n\n👤 Имя: {name}\n📞 Тел: {phone}\n💬 Сообщение: {message}",
        "en": "📨 New help request!\n\n👤 Name: {name}\n📞 Phone: {phone}\n💬 Message: {message}"
    },
    "help_sent": {
        "uz": "✅ So'rovingiz yuborildi! Adminlarimiz tez orada siz bilan bog'lanishadi.",
        "ru": "✅ Ваш запрос отправлен! Наши администраторы скоро свяжутся с вами.",
        "en": "✅ Your request has been sent! Our admins will contact you shortly."
    },

    # --- Tariflar ---
    "tariff_base_price": {
        "uz": "Boshlang'ich narx: {price} so'm 🚀",
        "ru": "Начальная цена: {price} сум 🚀",
        "en": "Base price: {price} sum 🚀",
    },
    "tariff_per_km": {
        "uz": "Km narxi: {price} so'm 📍",
        "ru": "Цена за км: {price} сум 📍",
        "en": "Price per km: {price} sum 📍",
    },
    "tariff_back": {
        "uz": "Orqaga ⬅️",
        "ru": "Назад ⬅️",
        "en": "Back ⬅️",
    },

    # --- Sozlamalar ---
    "settings_menu": {
        "uz": "Ma'lumotlarni tahrirlash ✏️",
        "ru": "Редактировать данные ✏️",
        "en": "Edit your information ✏️"
    },
    "enter_new_name": {
        "uz": "Yangi ism familiyangizni kiriting ✍️",
        "ru": "Введите новое имя и фамилию ✍️",
        "en": "Enter your new full name ✍️"
    },
    "enter_new_phone": {
        "uz": "Yangi raqamingizni kiriting ✍️",
        "ru": "Введите новый номер телефона ✍️",
        "en": "Enter your new phone number ✍️"
    },
    "name_updated": {
        "uz": "Ism familiyangiz muvaffaqiyatli o'zgartirildi ✅",
        "ru": "Имя и фамилия успешно изменены ✅",
        "en": "Your full name has been successfully updated ✅"
    },
    "phone_updated": {
        "uz": "Telefon raqamingiz muvaffaqiyatli o'zgartirildi ✅",
        "ru": "Номер телефона успешно изменён ✅",
        "en": "Your phone number has been successfully updated ✅"
    },

    # --- Admin panel ---
    "not_admin": {
        "uz": "⛔️ Siz admin emassiz! Admin panelga kira olmaysiz.",
        "ru": "⛔️ Вы не являетесь администратором! Доступ к панели администратора запрещён.",
        "en": "⛔️ You are not an admin! You cannot access the admin panel."
    },
    "admin_panel": {
        "uz": "Assalomu aleykum, hurmatli admin! ⚙️\nAdmin panelga xush kelibsiz 👋",
        "ru": "Здравствуйте, уважаемый администратор! ⚙️\nДобро пожаловать в панель управления 👋",
        "en": "Hello, dear admin! ⚙️\nWelcome to the admin panel 👋"
    },
    "admin_exit": {
        "uz": "🚪 Chiqish",
        "ru": "🚪 Выход",
        "en": "🚪 Exit"
    },

    # --- Admin: Haydovchilar ---
    "admin_drivers_menu_title": {
        "uz": "👤 Haydovchilar bo'limi bilan qanaqa amal bajaramiz?",
        "ru": "👤 Какое действие выполнить с водителями?",
        "en": "👤 What action would you like to perform with drivers?"
    },
    "admin_no_drivers": {
        "uz": "Hozircha haydovchilar yo'q 🤷‍♂️",
        "ru": "Водителей пока нет 🤷‍♂️",
        "en": "No drivers yet 🤷‍♂️"
    },
    "admin_drivers_title": {
        "uz": "👤 Haydovchilar ro'yxati:\n\n",
        "ru": "👤 Список водителей:\n\n",
        "en": "👤 Drivers list:\n\n"
    },
    "driver_status_active": {
        "uz": "🟢 Faol",
        "ru": "🟢 Активен",
        "en": "🟢 Active"
    },
    "driver_status_inactive": {
        "uz": "🔴 Nofaol",
        "ru": "🔴 Неактивен",
        "en": "🔴 Inactive"
    },
    "admin_driver_info": {
        "uz": "👤 Haydovchi ma'lumotlari:\n\n👤 Ism: {name}\n🔑 Login: {login}\n🔐 Parol: {password}\n📞 Tel: {phone}\n🚗 Mashina: {car_model}\n🔢 Raqam: {car_number}\n🚖 Tarif: {tariff}\n📊 Holat: {status}",
        "ru": "👤 Данные водителя:\n\n👤 Имя: {name}\n🔑 Логин: {login}\n🔐 Пароль: {password}\n📞 Тел: {phone}\n🚗 Машина: {car_model}\n🔢 Номер: {car_number}\n🚖 Тариф: {tariff}\n📊 Статус: {status}",
        "en": "👤 Driver info:\n\n👤 Name: {name}\n🔑 Login: {login}\n🔐 Password: {password}\n📞 Phone: {phone}\n🚗 Car: {car_model}\n🔢 Plate: {car_number}\n🚖 Tariff: {tariff}\n📊 Status: {status}"
    },

    # --- Haydovchi: Ro'yxatdan o'tish ---
    "admin_driver_add_tg_id": {
        "uz": "Haydovchining Telegram ID sini kiriting 🔢\n\nMasalan: 123456789",
        "ru": "Введите Telegram ID водителя 🔢\n\nНапример: 123456789",
        "en": "Enter driver's Telegram ID 🔢\n\nExample: 123456789"
    },
    "driver_enter_name": {
        "uz": "Haydovchi ismingizni kiriting 📝",
        "ru": "Введите ваше имя (водитель) 📝",
        "en": "Enter your driver name 📝"
    },
    "driver_enter_phone": {
        "uz": "Telefon raqamingizni kiriting ☎️",
        "ru": "Введите ваш номер телефона ☎️",
        "en": "Enter your phone number ☎️"
    },
    "driver_enter_car_model": {
        "uz": "Avtomobil rusumini kiriting 🚗\n\nMasalan: Cobalt, Nexia 3",
        "ru": "Введите модель автомобиля 🚗\n\nНапример: Cobalt, Nexia 3",
        "en": "Enter your car model 🚗\n\nExample: Cobalt, Nexia 3"
    },
    "driver_enter_car_number": {
        "uz": "Avtomobil raqamini kiriting 🔢\n\nMasalan: 01A123BC",
        "ru": "Введите номер автомобиля 🔢\n\nНапример: 01A123BC",
        "en": "Enter your car plate number 🔢\n\nExample: 01A123BC"
    },
    "driver_choose_tariff": {
        "uz": "Qaysi tarifda ishlaysiz? 🚖",
        "ru": "В каком тарифе вы работаете? 🚖",
        "en": "Which tariff do you work in? 🚖"
    },
    "driver_registered": {
        "uz": "✅ Siz haydovchi sifatida ro'yxatdan o'tdingiz!\n\nOnline bo'lish uchun tugmani bosing 🟢",
        "ru": "✅ Вы зарегистрированы как водитель!\n\nНажмите кнопку, чтобы выйти онлайн 🟢",
        "en": "✅ You are registered as a driver!\n\nPress the button to go online 🟢"
    },
    "driver_pending": {
        "uz": "⏳ Siz allaqachon ro'yxatdan o'tgansiz. Admin tasdiqlashini kuting.",
        "ru": "⏳ Вы уже зарегистрированы. Ожидайте подтверждения администратора.",
        "en": "⏳ You are already registered. Wait for admin confirmation."
    },
    "driver_not_approved": {
        "uz": "⛔️ Sizning hisobingiz admin tomonidan tasdiqlanmagan.",
        "ru": "⛔️ Ваш аккаунт не подтверждён администратором.",
        "en": "⛔️ Your account has not been approved by admin."
    },
    "admin_driver_approve_btn": {
        "uz": "✅ Tasdiqlash",
        "ru": "✅ Подтвердить",
        "en": "✅ Approve"
    },
    "admin_driver_approved": {
        "uz": "✅ Haydovchi tasdiqlandi!",
        "ru": "✅ Водитель подтверждён!",
        "en": "✅ Driver approved!"
    },
    "driver_added_notify": {
        "uz": "✅ Tabriklaymiz! Siz haydovchilar ro'yxatiga qo'shildingiz!\n\n👤 Ism: {name}\n🚗 Mashina: {car_model}\n🔢 Raqam: {car_number}\n\n📢 Buyurtmalar kanali: {channel_link}",
        "ru": "✅ Поздравляем! Вы добавлены в список водителей!\n\n👤 Имя: {name}\n🚗 Машина: {car_model}\n🔢 Номер: {car_number}\n\n📢 Канал заказов: {channel_link}",
        "en": "✅ Congratulations! You have been added to the drivers list!\n\n👤 Name: {name}\n🚗 Car: {car_model}\n🔢 Plate: {car_number}\n\n📢 Orders channel: {channel_link}"
    },
    "driver_temp_credentials": {
        "uz": "🔐 Vaqtinchalik login va parolingiz:\n\n👤 Login: `{login}`\n🔑 Parol: `{password}`\n\n⚠️ Tizimga kirgach parolingizni o'zgartiring!",
        "ru": "🔐 Ваши временные данные для входа:\n\n👤 Логин: `{login}`\n🔑 Пароль: `{password}`\n\n⚠️ После входа не забудьте сменить пароль!",
        "en": "🔐 Your temporary login credentials:\n\n👤 Login: `{login}`\n🔑 Password: `{password}`\n\n⚠️ Please change your password after logging in!"
    },
    "admin_new_driver_notify": {
        "uz": "🆕 Yangi haydovchi ro'yxatdan o'tdi!\n\n👤 Ism: {name}\n📞 Tel: {phone}\n🚗 Mashina: {car_model}\n🔢 Raqam: {car_number}\n🚖 Tarif: {tariff}",
        "ru": "🆕 Новый водитель зарегистрировался!\n\n👤 Имя: {name}\n📞 Тел: {phone}\n🚗 Машина: {car_model}\n🔢 Номер: {car_number}\n🚖 Тариф: {tariff}",
        "en": "🆕 New driver registered!\n\n👤 Name: {name}\n📞 Phone: {phone}\n🚗 Car: {car_model}\n🔢 Plate: {car_number}\n🚖 Tariff: {tariff}"
    },
    "driver_approved_notify": {
        "uz": "✅ Tabriklaymiz! Hisobingiz admin tomonidan tasdiqlandi.\nIsh boshlash uchun /start bosing.",
        "ru": "✅ Поздравляем! Ваш аккаунт подтверждён администратором.\nНажмите /start чтобы начать работу.",
        "en": "✅ Congratulations! Your account has been approved by admin.\nPress /start to begin working."
    },
    "admin_driver_search": {
        "uz": "🔍 Qidirmoqchi bo'lgan haydovchiningizning Telegram ID si, ismi yoki mashina raqamini kiriting:",
        "ru": "🔍 Введите Telegram ID, имя или номер автомобиля водителя, которого хотите найти:",
        "en": "🔍 Enter the Telegram ID, name or car plate number of the driver you want to find:"
    },
    "admin_driver_not_found": {
        "uz": "❌ Kiritgan parametrlaringiz bo'yicha haydovchi topilmadi!",
        "ru": "❌ Водитель по введённым параметрам не найден!",
        "en": "❌ No driver found matching your search parameters!"
    },
    "admin_driver_search_result": {
        "uz": "✅ Siz kiritgan parametr bo'yicha topilgan haydovchi:\n\n👤 {name} | 🔢 {car_number}",
        "ru": "✅ Найденный водитель по введённому параметру:\n\n👤 {name} | 🔢 {car_number}",
        "en": "✅ Driver found matching your search parameter:\n\n👤 {name} | 🔢 {car_number}"
    },
    "admin_driver_info_btn": {
        "uz": "👤 Haydovchi ma'lumotlari",
        "ru": "👤 Данные водителя",
        "en": "👤 Driver info"
    },
    "admin_assign_tariff_search": {
        "uz": "🔍 Qaysi haydovchiga tarif biriktirmoqchisiz?\n\nHaydovchining Telegram ID si, ismi yoki mashina raqamini kiriting:",
        "ru": "🔍 Какому водителю хотите привязать тариф?\n\nВведите Telegram ID, имя или номер автомобиля водителя:",
        "en": "🔍 Which driver would you like to assign a tariff to?\n\nEnter the driver's Telegram ID, name or car plate number:"
    },
    "admin_assign_tariff_not_found": {
        "uz": "❌ Kiritgan parametrlaringiz bo'yicha haydovchi topilmadi!",
        "ru": "❌ Водитель по введённым параметрам не найден!",
        "en": "❌ No driver found matching your search parameters!"
    },
    "admin_assign_tariff_found": {
        "uz": "✅ Topilgan haydovchi:\n\n👤 {name} | 🔢 {car_number}",
        "ru": "✅ Найденный водитель:\n\n👤 {name} | 🔢 {car_number}",
        "en": "✅ Driver found:\n\n👤 {name} | 🔢 {car_number}"
    },
    "admin_assign_tariff_btn": {
        "uz": "🚖 Tarif biriktirish",
        "ru": "🚖 Привязать тариф",
        "en": "🚖 Assign tariff"
    },
    "admin_assign_tariff_choose": {
        "uz": "🚖 Biriktirmoqchi bo'lgan tarifni tanlang:",
        "ru": "🚖 Выберите тариф для привязки:",
        "en": "🚖 Select a tariff to assign:"
    },
    "admin_assign_tariff_yes": {
        "uz": "✅ Ha",
        "ru": "✅ Да",
        "en": "✅ Yes"
    },
    "admin_assign_tariff_no": {
        "uz": "❌ Yo'q",
        "ru": "❌ Нет",
        "en": "❌ No"
    },
    "admin_assign_tariff_success": {
        "uz": "✅ Tarif muvaffaqiyatli biriktirildi!\n\n➕ Yana tarif biriktirasizmi?",
        "ru": "✅ Тариф успешно привязан!\n\n➕ Хотите привязать ещё один тариф?",
        "en": "✅ Tariff successfully assigned!\n\n➕ Would you like to assign another tariff?"
    },
    "admin_change_tariff_search": {
        "uz": "✏️ Qaysi haydovchining tarifini o'zgartirmoqchisiz?\n\nHaydovchining Telegram ID si, ismi yoki mashina raqamini kiriting:",
        "ru": "✏️ У какого водителя хотите изменить тариф?\n\nВведите Telegram ID, имя или номер автомобиля водителя:",
        "en": "✏️ Which driver's tariff would you like to change?\n\nEnter the driver's Telegram ID, name or car plate number:"
    },
    "admin_remove_tariff_btn": {
        "uz": "🗑 Tarifni olib tashlash",
        "ru": "🗑 Убрать тариф",
        "en": "🗑 Remove tariff"
    },
    "admin_driver_no_tariff": {
        "uz": "⚠️ Bu haydovchiga hali tarif biriktirilmagan!",
        "ru": "⚠️ К этому водителю ещё не привязан тариф!",
        "en": "⚠️ No tariff has been assigned to this driver yet!"
    },
    "admin_driver_select_remove_tariff": {
        "uz": "🗑 Haydovchidan olib tashlamoqchi bo'lgan tarifingizni tanlang:",
        "ru": "🗑 Выберите тариф, который хотите убрать у водителя:",
        "en": "🗑 Select the tariff you want to remove from the driver:"
    },
    "admin_driver_tariff_removed": {
        "uz": "✅ Haydovchidan tarif muvaffaqiyatli olib tashlandi!",
        "ru": "✅ Тариф успешно убран у водителя!",
        "en": "✅ Tariff successfully removed from the driver!"
    },
    "admin_driver_delete_search": {
        "uz": "🗑 Haydovchilar ro'yxatidan o'chirmoqchi bo'lgan haydovchingizning Telegram ID si, ismi yoki mashina raqamini kiriting:",
        "ru": "🗑 Введите Telegram ID, имя или номер автомобиля водителя, которого хотите удалить из списка:",
        "en": "🗑 Enter the Telegram ID, name or car plate number of the driver you want to delete from the list:"
    },
    "admin_driver_delete_btn": {
        "uz": "🗑 Haydovchini o'chirish",
        "ru": "🗑 Удалить водителя",
        "en": "🗑 Delete driver"
    },
    "admin_driver_delete_confirm": {
        "uz": "⚠️ Rostan ham haydovchini ro'yxatdan o'chirmoqchimisiz?\n\n❗️ Agar haydovchini ro'yxatdan o'chirsangiz unga tegishli barcha ma'lumotlar o'chirib tashlanadi va bundan keyin buyurtma qabul qila olmaydi!",
        "ru": "⚠️ Вы действительно хотите удалить водителя из списка?\n\n❗️ Если вы удалите водителя, все связанные с ним данные будут удалены и он больше не сможет принимать заказы!",
        "en": "⚠️ Are you sure you want to delete this driver from the list?\n\n❗️ If you delete the driver, all related data will be removed and they will no longer be able to accept orders!"
    },
    "admin_driver_deleted": {
        "uz": "✅ Haydovchi ro'yxatdan muvaffaqiyatli o'chirildi!",
        "ru": "✅ Водитель успешно удалён из списка!",
        "en": "✅ Driver successfully deleted from the list!"
    },
    "admin_driver_delete_cancelled": {
        "uz": "❌ Haydovchini ro'yxatdan o'chirish bekor qilindi!",
        "ru": "❌ Удаление водителя из списка отменено!",
        "en": "❌ Driver deletion cancelled!"
    },
    "admin_driver_block_search": {
        "uz": "🚫 Bloklamoqchi yoki blokdan chiqarmoqchi bo'lgan haydovchingizning Telegram ID si, ismi yoki mashina raqamini kiriting:",
        "ru": "🚫 Введите Telegram ID, имя или номер автомобиля водителя, которого хотите заблокировать или разблокировать:",
        "en": "🚫 Enter the Telegram ID, name or car plate number of the driver you want to block or unblock:"
    },
    "admin_driver_block_btn": {
        "uz": "🔒 Haydovchini bloklash",
        "ru": "🔒 Заблокировать водителя",
        "en": "🔒 Block driver"
    },
    "admin_driver_unblock_btn": {
        "uz": "🔓 Haydovchini blokdan chiqarish",
        "ru": "🔓 Разблокировать водителя",
        "en": "🔓 Unblock driver"
    },
    "admin_driver_already_blocked": {
        "uz": "⚠️ Bu haydovchi allaqachon bloklangan!",
        "ru": "⚠️ Этот водитель уже заблокирован!",
        "en": "⚠️ This driver is already blocked!"
    },
    "admin_driver_block_confirm": {
        "uz": "⚠️ Rostdan ham ushbu haydovchini bloklamoqchimisiz?\n\n❗️ Agar haydovchini bloklasangiz uni blokdan chiqarmaguningizcha buyurtma qabul qila olmaydi!",
        "ru": "⚠️ Вы действительно хотите заблокировать этого водителя?\n\n❗️ Если вы заблокируете водителя, он не сможет принимать заказы, пока вы его не разблокируете!",
        "en": "⚠️ Are you sure you want to block this driver?\n\n❗️ If you block the driver, they will not be able to accept orders until you unblock them!"
    },
    "admin_driver_blocked": {
        "uz": "🔒 Haydovchi muvaffaqiyatli bloklandi!",
        "ru": "🔒 Водитель успешно заблокирован!",
        "en": "🔒 Driver successfully blocked!"
    },
    "driver_unblocked_notify": {
        "uz": "🔓 Hisobingiz admin tomonidan blokdan chiqarildi!",
        "ru": "🔓 Ваш аккаунт разблокирован администратором!",
        "en": "🔓 Your account has been unblocked by the admin!"
    },
    "driver_blocked_notify": {
        "uz": "🔒 Hisobingiz admin tomonidan bloklandi!",
        "ru": "🔒 Ваш аккаунт заблокирован администратором!",
        "en": "🔒 Your account has been blocked by the admin!"
    },
    "admin_driver_block_cancelled": {
        "uz": "❌ Haydovchini bloklash bekor qilindi!",
        "ru": "❌ Блокировка водителя отменена!",
        "en": "❌ Driver blocking cancelled!"
    },

    # --- Haydovchi: Online / Offline ---
    "driver_now_online": {
        "uz": "🟢 Siz online holatdasiz!\nBuyurtmalar kela boshlaydi...",
        "ru": "🟢 Вы в сети!\nЗаказы начнут поступать...",
        "en": "🟢 You are now online!\nOrders will start coming in..."
    },
    "driver_now_offline": {
        "uz": "🔴 Siz offline holatga o'tdingiz.",
        "ru": "🔴 Вы перешли в офлайн режим.",
        "en": "🔴 You are now offline."
    },
    "driver_send_location": {
        "uz": "📍 Buyurtmalar olish uchun jonli joylashuvingizni yuboring!\n\n1. Qo'shimcha (📎) tugmasini bosing\n2. Joylashuv (Location) tanlang\n3. Jonli joylashuvni yuboring",
        "ru": "📍 Отправьте live местоположение для получения заказов!\n\n1. Нажмите кнопку (+)\n2. Выберите Местоположение\n3. Отправьте Live Location",
        "en": "📍 Send your live location to receive orders!\n\n1. Press the (+) button\n2. Select Location\n3. Send Live Location"
    },
    "driver_already_online": {
        "uz": "⚠️ Siz allaqachon online holatdasiz.",
        "ru": "⚠️ Вы уже онлайн.",
        "en": "⚠️ You are already online."
    },
    "driver_already_offline": {
        "uz": "⚠️ Siz allaqachon offline holatdasiz.",
        "ru": "⚠️ Вы уже офлайн.",
        "en": "⚠️ You are already offline."
    },

    # --- Haydovchi: Yangi buyurtma ---
    "driver_new_order": {
        "uz": "🚕 Yangi buyurtma!\n\n🚖 Tarif: {tariff}\n📍 Qayerdan: {from_loc}\n🏁 Qayerga: {to_loc}\n📏 Masofa: {distance} km\n💰 Narx: {price} so'm\n💳 To'lov: {payment}",
        "ru": "🚕 Новый заказ!\n\n🚖 Тариф: {tariff}\n📍 Откуда: {from_loc}\n🏁 Куда: {to_loc}\n📏 Расстояние: {distance} км\n💰 Цена: {price} сум\n💳 Оплата: {payment}",
        "en": "🚕 New order!\n\n🚖 Tariff: {tariff}\n📍 From: {from_loc}\n🏁 To: {to_loc}\n📏 Distance: {distance} km\n💰 Price: {price} sum\n💳 Payment: {payment}"
    },
    "driver_accept_btn": {
        "uz": "✅ Qabul qilish",
        "ru": "✅ Принять",
        "en": "✅ Accept"
    },
    "driver_reject_btn": {
        "uz": "❌ Rad etish",
        "ru": "❌ Отклонить",
        "en": "❌ Reject"
    },
    "driver_order_accepted": {
        "uz": "✅ Buyurtma qabul qilindi!\n\nYo'lovchi joylashuviga boring 📍",
        "ru": "✅ Заказ принят!\n\nЕдьте к местоположению пассажира 📍",
        "en": "✅ Order accepted!\n\nHead to the passenger location 📍"
    },
    "driver_order_rejected": {
        "uz": "❌ Buyurtma rad etildi.",
        "ru": "❌ Заказ отклонён.",
        "en": "❌ Order rejected."
    },
    "driver_order_taken": {
        "uz": "⚠️ Bu buyurtmani boshqa haydovchi qabul qilib oldi.",
        "ru": "⚠️ Этот заказ уже принят другим водителем.",
        "en": "⚠️ This order has already been taken by another driver."
    },

    # --- Haydovchi: Buyurtma jarayoni ---
    "driver_picked_up_btn": {
        "uz": "🚗 Yo'lovchini oldim",
        "ru": "🚗 Пассажир взят",
        "en": "🚗 Passenger picked up"
    },
    "driver_finished_btn": {
        "uz": "🏁 Yetkazib berdim",
        "ru": "🏁 Доставлен",
        "en": "🏁 Delivered"
    },
    "driver_picked_up_confirm": {
        "uz": "🚗 Yo'lovchi olinganligi tasdiqlandi.\nManzilga yuring!",
        "ru": "🚗 Посадка пассажира подтверждена.\nЕдьте к месту назначения!",
        "en": "🚗 Passenger pickup confirmed.\nHead to the destination!"
    },
    "driver_trip_finished": {
        "uz": "🏁 Sayohat yakunlandi!\n\nNavbatdagi buyurtmani kutmoqdasiz...",
        "ru": "🏁 Поездка завершена!\n\nОжидаете следующий заказ...",
        "en": "🏁 Trip finished!\n\nWaiting for the next order..."
    },

    # --- Haydovchi: Daromad ---
    "driver_earnings_title": {
        "uz": "💰 Daromadingiz:\n\n",
        "ru": "💰 Ваш доход:\n\n",
        "en": "💰 Your earnings:\n\n"
    },
    "driver_earnings_today": {
        "uz": "📅 Bugun: {amount} so'm",
        "ru": "📅 Сегодня: {amount} сум",
        "en": "📅 Today: {amount} sum"
    },
    "driver_earnings_total": {
        "uz": "📊 Jami: {amount} so'm",
        "ru": "📊 Всего: {amount} сум",
        "en": "📊 Total: {amount} sum"
    },
    "driver_earnings_trips": {
        "uz": "🚕 Jami sayohatlar: {count} ta",
        "ru": "🚕 Всего поездок: {count}",
        "en": "🚕 Total trips: {count}"
    },
    "driver_no_earnings": {
        "uz": "Hali daromad yo'q 🤷‍♂️",
        "ru": "Доходов пока нет 🤷‍♂️",
        "en": "No earnings yet 🤷‍♂️"
    },

    # --- Admin: Tariflar ---
    "admin_tariffs_menu_title": {
        "uz": "🚖 Tariflar bo'yicha qanday amal bajarmoqchisiz?",
        "ru": "🚖 Какое действие вы хотите выполнить с тарифами?",
        "en": "🚖 What action would you like to perform with tariffs?"
    },
    "admin_no_tariffs": {
        "uz": "Hozircha tariflar mavjud emas. Yangi tarif qo'shing ➕",
        "ru": "Тарифов пока нет. Добавьте новый тариф ➕",
        "en": "No tariffs yet. Add a new tariff ➕"
    },
    "admin_tariffs_list_title": {
        "uz": "📋 Tariflar ro'yxati:\n\n",
        "ru": "📋 Список тарифов:\n\n",
        "en": "📋 Tariffs list:\n\n"
    },
    "admin_tariff_add_name": {
        "uz": "Tarif nomini kiriting (o'zbekcha):",
        "ru": "Введите название тарифа (на узбекском):",
        "en": "Enter tariff name (in Uzbek):"
    },
    "admin_tariff_add_name_ru": {
        "uz": "Tarif nomini kiriting (ruscha):",
        "ru": "Введите название тарифа (на русском):",
        "en": "Enter tariff name (in Russian):"
    },
    "admin_tariff_add_name_en": {
        "uz": "Tarif nomini kiriting (inglizcha):",
        "ru": "Введите название тарифа (на английском):",
        "en": "Enter tariff name (in English):"
    },
    "admin_tariff_add_desc": {
        "uz": "Tarif tavsifini kiriting (o'zbekcha):",
        "ru": "Введите описание тарифа (на узбекском):",
        "en": "Enter tariff description (in Uzbek):"
    },
    "admin_tariff_add_desc_ru": {
        "uz": "Tarif tavsifini kiriting (ruscha):",
        "ru": "Введите описание тарифа (на русском):",
        "en": "Enter tariff description (in Russian):"
    },
    "admin_tariff_add_desc_en": {
        "uz": "Tarif tavsifini kiriting (inglizcha):",
        "ru": "Введите описание тарифа (на английском):",
        "en": "Enter tariff description (in English):"
    },
    "admin_tariff_add_base_price": {
        "uz": "Boshlang'ich narxni kiriting (so'mda):\n\nMasalan: 5000",
        "ru": "Введите начальную цену (в сумах):\n\nНапример: 5000",
        "en": "Enter base price (in UZS):\n\nExample: 5000"
    },
    "admin_tariff_add_per_km": {
        "uz": "1 km narxini kiriting (so'mda):\n\nMasalan: 800",
        "ru": "Введите цену за 1 км (в сумах):\n\nНапример: 800",
        "en": "Enter price per km (in UZS):\n\nExample: 800"
    },
    "admin_tariff_saved": {
        "uz": "✅ Tarif muvaffaqiyatli qo'shildi!",
        "ru": "✅ Тариф успешно добавлен!",
        "en": "✅ Tariff successfully added!"
    },
    "admin_tariff_edit_choose": {
        "uz": "✏️ O'zgartirmoqchi bo'lgan tarifingizni tanlang:",
        "ru": "✏️ Выберите тариф, который хотите изменить:",
        "en": "✏️ Choose the tariff you want to edit:"
    },
    "admin_edit_base_btn": {
        "uz": "💰 Boshlang'ich narx",
        "ru": "💰 Начальная цена",
        "en": "💰 Base price"
    },
    "admin_edit_per_km_btn": {
        "uz": "📍 Km narxi",
        "ru": "📍 Цена за км",
        "en": "📍 Price per km"
    },
    "admin_tariff_updated": {
        "uz": "✅ Tarif muvaffaqiyatli yangilandi!",
        "ru": "✅ Тариф успешно обновлён!",
        "en": "✅ Tariff successfully updated!"
    },
    "admin_tariff_del_choose": {
        "uz": "🗑 Qaysi tarifni o'chirmoqchisiz?",
        "ru": "🗑 Какой тариф вы хотите удалить?",
        "en": "🗑 Which tariff do you want to delete?"
    },
    "admin_tariff_del_yes": {
        "uz": "✅ Ha, o'chirish",
        "ru": "✅ Да, удалить",
        "en": "✅ Yes, delete"
    },
    "admin_tariff_del_no": {
        "uz": "❌ Yo'q, bekor qilish",
        "ru": "❌ Нет, отмена",
        "en": "❌ No, cancel"
    },
    "admin_tariff_del_confirm": {
        "uz": "⚠️ Rostdan ham ushbu tarifni o'chirmoqchimisiz?\n\n❗️ Agar tarifni o'chirsangiz, tarifga biriktirilgan haydovchilar ushbu tarifdan chiqarib yuboriladi!",
        "ru": "⚠️ Вы действительно хотите удалить этот тариф?\n\n❗️ Если вы удалите тариф, все водители, привязанные к этому тарифу, будут от него отключены!",
        "en": "⚠️ Are you sure you want to delete this tariff?\n\n❗️ If you delete this tariff, all drivers assigned to it will be removed from it!"
    },
    "admin_tariff_deleted": {
        "uz": "🗑 Tarif muvaffaqiyatli o'chirildi!",
        "ru": "🗑 Тариф успешно удалён!",
        "en": "🗑 Tariff successfully deleted!"
    },
    "admin_tariff_del_cancelled": {
        "uz": "❌ O'chirish bekor qilindi!",
        "ru": "❌ Удаление отменено!",
        "en": "❌ Deletion cancelled!"
    },

    # --- Admin: Buyurtmalar ---
    "admin_orders_menu_title": {
        "uz": "📋 Buyurtmalar bo'limi bilan qanaqa amal bajaramiz?",
        "ru": "📋 Какое действие выполнить с заказами?",
        "en": "📋 What action would you like to perform with orders?"
    },
    "admin_no_orders": {
        "uz": "Hozircha buyurtmalar mavjud emas 🤷‍♂️",
        "ru": "Заказов пока нет 🤷‍♂️",
        "en": "No orders yet 🤷‍♂️"
    },
    "admin_orders_list_title": {
        "uz": "📋 Buyurtmalar ro'yxati:\n\n",
        "ru": "📋 Список заказов:\n\n",
        "en": "📋 Orders list:\n\n"
    },
    "admin_orders_filter": {
        "uz": "📋 Qaysi statusdagi buyurtmalarni qarayabsiz?",
        "ru": "📋 Заказы какого статуса вы хотите просмотреть?",
        "en": "📋 Which status orders would you like to view?"
    },
    "admin_order_detail_title": {
        "uz": "📦 Buyurtma #{order_id}\n\n👤 Foydalanuvchi: {user}\n📞 Tel: {phone}\n🚖 Tarif: {tariff}\n📍 Qayerdan: {from_loc}\n🏁 Qayerga: {to_loc}\n📏 Masofa: {distance} km\n💰 Narx: {price} so'm\n💳 To'lov: {payment}\n📅 Sana: {date}\n⏳ Holat: {status}",
        "ru": "📦 Заказ #{order_id}\n\n👤 Пользователь: {user}\n📞 Тел: {phone}\n🚖 Тариф: {tariff}\n📍 Откуда: {from_loc}\n🏁 Куда: {to_loc}\n📏 Расстояние: {distance} км\n💰 Цена: {price} сум\n💳 Оплата: {payment}\n📅 Дата: {date}\n⏳ Статус: {status}",
        "en": "📦 Order #{order_id}\n\n👤 User: {user}\n📞 Phone: {phone}\n🚖 Tariff: {tariff}\n📍 From: {from_loc}\n🏁 To: {to_loc}\n📏 Distance: {distance} km\n💰 Price: {price} sum\n💳 Payment: {payment}\n📅 Date: {date}\n⏳ Status: {status}"
    },
    "admin_order_search": {
        "uz": "🔍 Qidirmoqchi bo'lgan buyurtmangizning ID sini kiriting:\n\nMasalan: 5",
        "ru": "🔍 Введите ID заказа, который хотите найти:\n\nНапример: 5",
        "en": "🔍 Enter the ID of the order you want to find:\n\nExample: 5"
    },
    "admin_order_not_found": {
        "uz": "❌ Kiritgan ID bo'yicha buyurtma topilmadi!",
        "ru": "❌ Заказ по введённому ID не найден!",
        "en": "❌ No order found with the entered ID!"
    },

    # --- Admin: Statistika ---
    "admin_stats_title": {
        "uz": "📊 Statistika\n\n",
        "ru": "📊 Статистика\n\n",
        "en": "📊 Statistics\n\n"
    },
    "admin_stats_orders": {
        "uz": "📋 Buyurtmalar:\n🗓 Kunlik: {daily}\n📅 Oylik: {monthly}\n✅ Yakunlangan: {finished}\n❌ Bekor qilingan: {cancelled}\n\n",
        "ru": "📋 Заказы:\n🗓 Суточные: {daily}\n📅 Месячные: {monthly}\n✅ Завершённые: {finished}\n❌ Отменённые: {cancelled}\n\n",
        "en": "📋 Orders:\n🗓 Daily: {daily}\n📅 Monthly: {monthly}\n✅ Finished: {finished}\n❌ Cancelled: {cancelled}\n\n"
    },
    "admin_stats_payment": {
        "uz": "💳 To'lovlar:\n💵 Naqd: {cash} ta\n💳 Karta: {card} ta\n\n",
        "ru": "💳 Оплаты:\n💵 Наличные: {cash}\n💳 Карта: {card}\n\n",
        "en": "💳 Payments:\n💵 Cash: {cash}\n💳 Card: {card}\n\n"
    },
    "admin_stats_income": {
        "uz": "💰 Daromad:\n📅 O'tgan oy: {last_month} so'm\n📅 Shu oy: {this_month} so'm\n\n",
        "ru": "💰 Доход:\n📅 Прошлый месяц: {last_month} сум\n📅 Этот месяц: {this_month} сум\n\n",
        "en": "💰 Income:\n📅 Last month: {last_month} sum\n📅 This month: {this_month} sum\n\n"
    },
    "admin_stats_top_driver_last": {
        "uz": "🏆 O'tgan oyda eng faol haydovchi:\n👤 Ism: {name}\n🆔 TG ID: {tg_id}\n🔢 Mashina: {car_number}\n🚕 Buyurtmalar: {count} ta\n\n",
        "ru": "🏆 Самый активный водитель прошлого месяца:\n👤 Имя: {name}\n🆔 TG ID: {tg_id}\n🔢 Номер: {car_number}\n🚕 Заказов: {count}\n\n",
        "en": "🏆 Top driver last month:\n👤 Name: {name}\n🆔 TG ID: {tg_id}\n🔢 Plate: {car_number}\n🚕 Orders: {count}\n\n"
    },
    "admin_stats_top_driver_this": {
        "uz": "🏆 Shu oyda eng faol haydovchi:\n👤 Ism: {name}\n🆔 TG ID: {tg_id}\n🔢 Mashina: {car_number}\n🚕 Buyurtmalar: {count} ta\n\n",
        "ru": "🏆 Самый активный водитель этого месяца:\n👤 Имя: {name}\n🆔 TG ID: {tg_id}\n🔢 Номер: {car_number}\n🚕 Заказов: {count}\n\n",
        "en": "🏆 Top driver this month:\n👤 Name: {name}\n🆔 TG ID: {tg_id}\n🔢 Plate: {car_number}\n🚕 Orders: {count}\n\n"
    },
    "admin_stats_no_top_driver": {
        "uz": "🏆 Hali ma'lumot yo'q\n\n",
        "ru": "🏆 Данных пока нет\n\n",
        "en": "🏆 No data yet\n\n"
    },
    "admin_stats_tariffs": {
        "uz": "🚖 Tariflar bo'yicha:\n{tariffs}\n",
        "ru": "🚖 По тарифам:\n{tariffs}\n",
        "en": "🚖 By tariffs:\n{tariffs}\n"
    },
    "admin_stats_users": {
        "uz": "👤 Foydalanuvchilar:\n🗓 Kunlik: {daily} ta\n📅 Oylik: {monthly} ta\n🚗 Haydovchilar: {drivers} ta",
        "ru": "👤 Пользователи:\n🗓 Суточные: {daily}\n📅 Месячные: {monthly}\n🚗 Водители: {drivers}",
        "en": "👤 Users:\n🗓 Daily: {daily}\n📅 Monthly: {monthly}\n🚗 Drivers: {drivers}"
    },

    # --- Admin: Xabar yuborish ---
    "admin_broadcast_menu": {
        "uz": "📢 Kimga xabar yubormoqchisiz?",
        "ru": "📢 Кому хотите отправить сообщение?",
        "en": "📢 Who would you like to send a message to?"
    },
    "admin_broadcast_users_btn": {
        "uz": "👤 Foydalanuvchilar",
        "ru": "👤 Пользователи",
        "en": "👤 Users"
    },
    "admin_broadcast_drivers_btn": {
        "uz": "🚗 Haydovchilar",
        "ru": "🚗 Водители",
        "en": "🚗 Drivers"
    },
    "admin_broadcast_all_btn": {
        "uz": "👥 Barchaga",
        "ru": "👥 Всем",
        "en": "👥 Everyone"
    },
    "admin_broadcast_ask": {
        "uz": "📝 Xabarni yuboring (matn, rasm, video yoki audio):",
        "ru": "📝 Отправьте сообщение (текст, фото, видео или аудио):",
        "en": "📝 Send your message (text, photo, video or audio):"
    },
    "admin_broadcast_success": {
        "uz": "✅ Xabar {count} ta foydalanuvchiga yuborildi!",
        "ru": "✅ Сообщение отправлено {count} пользователям!",
        "en": "✅ Message sent to {count} users!"
    },
    "admin_broadcast_failed": {
        "uz": "⚠️ {count} ta foydalanuvchiga xabar yuborishda xatolik yuz berdi!",
        "ru": "⚠️ Не удалось отправить сообщение {count} пользователям!",
        "en": "⚠️ Failed to send message to {count} users!"
    },

    "driver_login_wrong": {
        "uz": "❌ Login yoki parol noto'g'ri! Qaytadan urinib ko'ring.\n\nFormat: login parol\nMasalan: ali_karimov_123 Abc12345",
        "ru": "❌ Неверный логин или пароль! Попробуйте снова.\n\nФормат: логин пароль\nНапример: ali_karimov_123 Abc12345",
        "en": "❌ Wrong login or password! Please try again.\n\nFormat: login password\nExample: ali_karimov_123 Abc12345"
    },
    "driver_not_found": {
        "uz": "⛔️ Siz haydovchi emassiz, shuning uchun haydovchi paneliga kira olmaysiz!",
        "ru": "⛔️ Вы не являетесь водителем, поэтому не можете войти в панель водителя!",
        "en": "⛔️ You are not a driver, so you cannot access the driver panel!"
    },
    "driver_login_ask": {
        "uz": "🔐 Login va parolingizni kiriting:\n\nFormat: login parol",
        "ru": "🔐 Введите логин и пароль:\n\nФормат: логин пароль",
        "en": "🔐 Enter your login and password:\n\nFormat: login password"
    },
    "driver_login_blocked": {
        "uz": "🚫 Sizning hisobingiz bloklangan. Admin bilan bog'laning.",
        "ru": "🚫 Ваш аккаунт заблокирован. Свяжитесь с администратором.",
        "en": "🚫 Your account is blocked. Please contact the admin."
    },
    "driver_not_active": {
        "uz": "⚠️ Hisobingizga hali tarif biriktirilmagan. Admin bilan bog'laning.",
        "ru": "⚠️ К вашему аккаунту ещё не привязан тариф. Свяжитесь с администратором.",
        "en": "⚠️ No tariff has been assigned to your account yet. Please contact the admin."
    },
    "driver_menu": {
        "uz": "Haydovchi menyusi 🚗",
        "ru": "Меню водителя 🚗",
        "en": "Driver menu 🚗"
    },
    "driver_change_password_ask": {
        "uz": "🔐 Vaqtinchalik parol bilan kirdingiz!\n\n⚠️ Login parolingizni o'zgartirishni unutmang!",
        "ru": "🔐 Вы вошли с временным паролем!\n\n⚠️ Не забудьте изменить логин и пароль!",
        "en": "🔐 You logged in with a temporary password!\n\n⚠️ Don't forget to change your login and password!"
    },
    "driver_password_changed": {
        "uz": "✅ Login va parolingiz muvaffaqiyatli o'zgartirildi!\n\n👤 Login: {login}\n🔑 Parol: {password}\n\n⚠️ Bu ma'lumotlarni eslab qoling!",
        "ru": "✅ Ваш логин и пароль успешно изменены!\n\n👤 Логин: {login}\n🔑 Пароль: {password}\n\n⚠️ Запомните эти данные!",
        "en": "✅ Your login and password have been successfully changed!\n\n👤 Login: {login}\n🔑 Password: {password}\n\n⚠️ Please remember these credentials!"
    },
    "driver_login_success": {
        "uz": "✅ Tizimga muvaffaqiyatli kirdingiz!\n\nXush kelibsiz, {name}! 👋",
        "ru": "✅ Вы успешно вошли в систему!\n\nДобро пожаловать, {name}! 👋",
        "en": "✅ Successfully logged in!\n\nWelcome, {name}! 👋"
    },
    "driver_orders_title": {
        "uz": "📋 Mening buyurtmalarim:\n\n",
        "ru": "📋 Мои заказы:\n\n",
        "en": "📋 My orders:\n\n"
    },
    "driver_no_orders": {
        "uz": "Sizda hali buyurtmalar yo'q 🤷‍♂️",
        "ru": "У вас пока нет заказов 🤷‍♂️",
        "en": "You have no orders yet 🤷‍♂️"
    },
    "driver_order_detail": {
        "uz": "📦 Buyurtma #{order_id}\n\n👤 Yo'lovchi: {user}\n📞 Tel: {phone}\n🚖 Tarif: {tariff}\n📍 Qayerdan: {from_loc}\n🏁 Qayerga: {to_loc}\n📏 Masofa: {distance} km\n💰 Narx: {price} so'm\n📅 Sana: {date}\n⏳ Holat: {status}",
        "ru": "📦 Заказ #{order_id}\n\n👤 Пассажир: {user}\n📞 Тел: {phone}\n🚖 Тариф: {tariff}\n📍 Откуда: {from_loc}\n🏁 Куда: {to_loc}\n📏 Расстояние: {distance} км\n💰 Цена: {price} сум\n📅 Дата: {date}\n⏳ Статус: {status}",
        "en": "📦 Order #{order_id}\n\n👤 Passenger: {user}\n📞 Phone: {phone}\n🚖 Tariff: {tariff}\n📍 From: {from_loc}\n🏁 To: {to_loc}\n📏 Distance: {distance} km\n💰 Price: {price} sum\n📅 Date: {date}\n⏳ Status: {status}"
    },
    "driver_settings_menu": {
        "uz": "⚙️ Sozlamalar",
        "ru": "⚙️ Настройки",
        "en": "⚙️ Settings"
    },
    "driver_change_login_password_ask": {
        "uz": "🔐 Yangi login va parolingizni kiriting:\n\nFormat: login parol",
        "ru": "🔐 Введите новый логин и пароль:\n\nФормат: логин пароль",
        "en": "🔐 Enter your new login and password:\n\nFormat: login password"
    },
    "driver_change_login_password_wrong": {
        "uz": "❌ Siz login va parolni login parol formatida kiritishingiz kerak!\n\nMasalan: ali_karimov Abc12345\n\n⚠️ Muhim: Login yoki parol tarkibida ochiq joy qoldirish mumkin emas! Ochiq joy o'rniga pastki chiziqdan ( _ ) foydalaning. Login va parol orasi ochiq joy bilan ajratilishi shart.",
        "ru": "❌ Вы должны ввести логин и пароль в формате логин пароль!\n\nНапример: ali_karimov Abc12345\n\n⚠️ Важно: В логине и пароле нельзя использовать пробелы! Вместо пробела используйте нижнее подчёркивание ( _ ). Логин и пароль должны быть разделены пробелом.",
        "en": "❌ You must enter login and password in the format login password!\n\nExample: ali_karimov Abc12345\n\n⚠️ Important: Login and password cannot contain spaces! Use underscore ( _ ) instead of space. Login and password must be separated by a space."
    },
    "driver_login_already_exists": {
        "uz": "❌ Bu login allaqachon band! Boshqa login tanlang.",
        "ru": "❌ Этот логин уже занят! Выберите другой логин.",
        "en": "❌ This login is already taken! Please choose another login."
    },
    "user_driver_info": {
        "uz": "🚗 Haydovchi buyurtmangizni qabul qildi!\n\n👤 Ism: {name}\n📞 Tel: {phone}\n🚗 Mashina: {car_model}\n🔢 Raqam: {car_number}\n⭐ Reyting: {rating}",
        "ru": "🚗 Водитель принял ваш заказ!\n\n👤 Имя: {name}\n📞 Тел: {phone}\n🚗 Машина: {car_model}\n🔢 Номер: {car_number}\n⭐ Рейтинг: {rating}",
        "en": "🚗 Driver accepted your order!\n\n👤 Name: {name}\n📞 Phone: {phone}\n🚗 Car: {car_model}\n🔢 Plate: {car_number}\n⭐ Rating: {rating}"
    },
    "driver_rating_ask": {
        "uz": "⭐ Agar haydovchi xizmatidan qoniqqan bo'lsangiz uni baholang!\n\n💬 Safar bo'yicha shikoyatingiz bo'lsa yordam bo'limi orqali administratorlarga jo'nating.",
        "ru": "⭐ Если вы довольны услугой водителя, оцените его!\n\n💬 Если у вас есть жалоба по поездке, отправьте её администраторам через раздел помощи.",
        "en": "⭐ If you are satisfied with the driver's service, please rate them!\n\n💬 If you have a complaint about the trip, send it to the administrators via the help section."
    },
    "driver_rated": {
        "uz": "✅ Bahoyingiz uchun rahmat!",
        "ru": "✅ Спасибо за вашу оценку!",
        "en": "✅ Thank you for your rating!"
    },
    "no_drivers_found": {
        "uz": "❌ Hozirda mos haydovchi topilmadi. Keyinroq urinib ko'ring.",
        "ru": "❌ Подходящий водитель не найден. Попробуйте позже.",
        "en": "❌ No suitable driver found. Please try again later."
    },
}