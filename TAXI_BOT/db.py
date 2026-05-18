import sqlite3
import json

DB_NAME = "user.db"

class OrderStatus:
    PENDING   = "pending"
    ACCEPTED  = "accepted"
    PICKED_UP = "picked_up"
    FINISHED  = "finished"
    CANCELLED = "cancelled"

def connect():
     return sqlite3.connect(DB_NAME)

def create_table():
    with connect() as con:
        con.execute('''CREATE TABLE IF NOT EXISTS users (
        tg_id INTEGER PRIMARY KEY,
        full_name TEXT,
        phone_number TEXT,
        language TEXT    
        )''')

    con.execute("""CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        tariff TEXT,
        from_location TEXT,
        from_lat REAL,
        from_long REAL,
        to_location TEXT,
        to_lat REAL,
        to_long REAL,
        distance REAL,
        price INTEGER,
        status TEXT DEFAULT "pending",
        driver_id INTEGER,
        channel_msg_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    con.execute("""CREATE TABLE IF NOT EXISTS tariffs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT UNIQUE,
        name_uz TEXT,
        name_ru TEXT,
        name_en TEXT,
        desc_uz TEXT,
        desc_ru TEXT,
        desc_en TEXT,
        base_price INTEGER,
        per_km INTEGER,
        is_active INTEGER DEFAULT 1
    )""")

    con.execute("""CREATE TABLE IF NOT EXISTS DRIVERS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER UNIQUE,
        login TEXT UNIQUE,
        password TEXT,
        temp_password INTEGER DEFAULT 1,
        name TEXT,
        phone TEXT,
        car_model TEXT,
        car_number TEXT,
        tariff_key TEXT,
        is_active INTEGER DEFAULT 0,
        is_online INTEGER DEFAULT 0,
        is_blocked INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    con.execute("""CREATE TABLE IF NOT EXISTS driver_tariffs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        driver_id INTEGER,
        tariff_key TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

def migrate():
    with connect() as con:
        try:
            con.execute("ALTER TABLE orders ADD COLUMN payment_type TEXT DEFAULT 'cash'")
            con.commit()
        except:
            pass
        try:
            con.execute("ALTER TABLE DRIVERS ADD COLUMN logged INTEGER DEFAULT 0")
        except:
            pass
        try:
            con.execute("ALTER TABLE DRIVERS ADD COLUMN lat REAL")
        except:
            pass
        try:
            con.execute("ALTER TABLE DRIVERS ADD COLUMN lon REAL")
        except:
            pass
        try:
            con.execute("ALTER TABLE orders ADD COLUMN driver_messages TEXT DEFAULT '{}'")
        except:
            pass
        try:
            con.execute("ALTER TABLE DRIVERS ADD COLUMN rating REAL DEFAULT 0")
        except:
            pass
        try:
            con.execute("ALTER TABLE DRIVERS ADD COLUMN rating_count INTEGER DEFAULT 0")
        except:
            pass

def add_user(tg_id, full_name, phone_number, language):
    with connect() as con:
        con.execute("""
        INSERT OR REPLACE INTO users 
        (tg_id, full_name, phone_number, language)
        VALUES (?, ?, ?, ?)
        """,(tg_id, full_name, phone_number, language))
def get_user(tg_id):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
        SELECT * FROM users WHERE tg_id = ?
        """,(tg_id,))
        return cur.fetchone()
def update_name(tg_id, full_name):
    with connect() as con:
        con.execute("UPDATE users set full_name = ? WHERE tg_id = ?",(full_name,tg_id))

def update_phone_number(tg_id, phone_number):
    with connect() as con:
        con.execute("UPDATE users set phone_number = ? WHERE tg_id = ?",(phone_number,tg_id))
def update_language(tg_id, language):
    with connect() as con:
        con.execute("UPDATE users set language = ? WHERE tg_id = ?",(language,tg_id))

def add_order(user_id, tariff, from_location, from_lat, from_lon, to_location, to_lat, to_lon, distance, price):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO orders 
            (user_id, tariff, from_location, from_lat, from_long, to_location, to_lat, to_long, distance, price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (user_id, tariff, from_location, from_lat, from_lon, to_location, to_lat, to_lon, distance, price))
        return cur.lastrowid

def get_order(order_id):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM orders WHERE id = ?
        """, (order_id,))
        return cur.fetchone()

def get_all_orders(status=None):
    with connect() as con:
        cur = con.cursor()
        if status:
            cur.execute("""SELECT * FROM orders WHERE status = ? ORDER BY created_at DESC""",(status,))
        else:
            cur.execute("""SELECT * FROM orders ORDER BY created_at DESC""")
        return cur.fetchall()

def update_order_status(order_id, status, driver_id=None, channel_msg_id=None, payment_type=None):
    with connect() as con:
        if payment_type:
            con.execute("""
                UPDATE orders SET status=?, driver_id=?, channel_msg_id=?, payment_type=?
                WHERE id=?
            """, (status, driver_id, channel_msg_id, payment_type, order_id))
        else:
            con.execute("""
                UPDATE orders SET status=?, driver_id=?, channel_msg_id=?
                WHERE id=?
            """, (status, driver_id, channel_msg_id, order_id))
        con.commit()

def get_user_orders(user_id):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT id, tariff, from_location, to_location, distance, price, status, created_at
            FROM orders WHERE user_id = ?
            ORDER BY created_at DESC
        """, (user_id,))
        return cur.fetchall()

def get_driver_orders(driver_id):
     with connect() as con:
        cur = con.cursor()
        cur.execute("""
        SELECT * FROM orders WHERE driver_id = ? ORDER BY created_at DESC
        """, (driver_id,))
        return cur.fetchall()

def get_tariffs():
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM tariffs WHERE is_active = 1
        """)
        return cur.fetchall()

def get_tariffs_by_key(key):
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tariffs WHERE key = ?", (key,))
        return cur.fetchone()

def add_tariff(key, name_uz, name_ru, name_en, desc_uz, desc_ru, desc_en, base_price, per_km):
    with connect() as con:
        con.execute("""
            INSERT INTO tariffs (key, name_uz, name_ru, name_en, desc_uz, desc_ru, desc_en, base_price, per_km)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) 
        """, (key, name_uz, name_ru, name_en, desc_uz, desc_ru, desc_en, base_price, per_km))

def update_tariffs(tariff_id, base_price, per_km):
    with connect() as con:
        con.execute("""
            UPDATE tariffs SET base_price = ?, per_km = ? WHERE id = ?
        """, (base_price, per_km, tariff_id))

def delete_tariffs(tariff_id):
    with connect() as con:
        con.execute("""
            UPDATE tariffs SET is_active=0 WHERE id = ?
        """, (tariff_id,))

    ###### DRIVERS ######
def get_all_drivers():
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM drivers
        """)
        return cur.fetchall()

def get_driver_by_login(login):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM drivers WHERE login = ?
        """, (login,))
        return cur.fetchone()

def update_driver_location(tg_id, lat, lon):
    with connect() as con:
        con.execute("UPDATE DRIVERS SET lat = ?, lon = ? WHERE tg_id = ?", (lat, lon, tg_id))
        con.commit()

def get_online_drivers(tariff_key):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT d.* FROM DRIVERS d
            JOIN driver_tariffs dt ON d.id = dt.driver_id
            WHERE d.is_online = 1
            AND d.is_blocked = 0
            AND d.lat IS NOT NULL
            AND d.lon IS NOT NULL
            AND dt.tariff_key = ?
        """, (tariff_key,))
        return cur.fetchall()

def get_driver_by_id(driver_id):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM drivers WHERE id = ?
        """ , (driver_id,))
        return cur.fetchone()

def add_driver(tg_id, name, phone, car_model, car_number, login, password):
    with connect() as con:
        con.execute("""
            INSERT INTO drivers (tg_id, name, phone, car_model, car_number, login, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (tg_id, name, phone, car_model, car_number, login, password))
        con.commit()

def driver_update_phone_number(tg_id, phone_number):
    with connect() as con:
        con.execute("UPDATE DRIVERS set phone_number = ? WHERE tg_id = ?",(phone_number,tg_id))

def search_drivers(query):
    with connect() as con:
        cur = con.cursor()
        like = f"%{query}%"
        cur.execute("""
            SELECT * FROM drivers 
            WHERE name LIKE ?
            OR phone LIKE ?
            OR car_number LIKE ?
            OR login LIKE ?
        """ , (like, like, like, like))
        return cur.fetchall()

def change_driver_login_password(driver_id, login, password):
    with connect() as con:
        con.execute("""
            UPDATE DRIVERS SET login = ?, password = ?, temp_password = 0 WHERE id = ?
        """, (login, password, driver_id))
        con.commit()

def set_driver_tariff(driver_id, tariff_key):
    with connect() as con:
        con.execute("""
            UPDATE drivers SET tariff_key = ?, is_active=1 WHERE id = ?
        """, (tariff_key, driver_id))

def set_driver_blocked(driver_id, is_blocked:bool):
    with connect() as con:
        con.execute("""
            UPDATE drivers SET is_blocked = ? WHERE id = ?
        """, (1 if is_blocked else 0, driver_id))

def set_driver_logged(driver_id, is_logged: bool):
    with connect() as con:
        con.execute("UPDATE DRIVERS SET logged = ? WHERE id = ?", (1 if is_logged else 0, driver_id))
        con.commit()

def set_driver_online(driver_id, is_online: bool):
    with connect() as con:
        con.execute("UPDATE DRIVERS SET is_online = ? WHERE id = ?", (1 if is_online else 0, driver_id))
        con.commit()

def delete_driver(driver_id):
    with connect() as con:
        con.execute("""
            DELETE FROM drivers WHERE id = ?
        """, (driver_id,))

def add_driver_tariff(driver_id, tariff_key):
    with connect() as con:
        con.execute("""
            INSERT INTO driver_tariffs (driver_id, tariff_key) VALUES (?, ?)
        """, (driver_id, tariff_key))

def get_driver_tariffs(driver_id):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT t.id, t.key, t.name_uz, t.name_ru, t.name_en,
                   t.desc_uz, t.desc_ru, t.desc_en, t.base_price, t.per_km
            FROM tariffs t
            JOIN driver_tariffs dt ON t.key = dt.tariff_key
            WHERE dt.driver_id = ?
        """, (driver_id,))
        return cur.fetchall()

def get_driver_by_tg_id(tg_id):
    with connect() as con:
        cur = con.cursor()
        cur.execute("""
            SELECT * FROM drivers WHERE tg_id = ?
       """,(tg_id,))
        return cur.fetchone()

def del_driver_tariff(driver_id, tariff_key):
    with connect() as con:
        con.execute("""
            DELETE FROM driver_tariffs WHERE driver_id = ? AND tariff_key = ?
        """, (driver_id, tariff_key))

def get_stats():
    with connect() as con:
        cur = con.cursor()

        # Kunlik buyurtmalar
        cur.execute("SELECT COUNT(*) FROM orders WHERE DATE(created_at) = DATE('now')")
        daily_orders = cur.fetchone()[0]

        # Oylik buyurtmalar
        cur.execute("SELECT COUNT(*) FROM orders WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')")
        monthly_orders = cur.fetchone()[0]

        # Yakunlangan buyurtmalar
        cur.execute("SELECT COUNT(*) FROM orders WHERE status = 'finished'")
        finished_orders = cur.fetchone()[0]

        # Bekor qilingan buyurtmalar
        cur.execute("SELECT COUNT(*) FROM orders WHERE status = 'cancelled'")
        cancelled_orders = cur.fetchone()[0]

        # Naqd buyurtmalar
        cur.execute("SELECT COUNT(*) FROM orders WHERE payment_type = 'cash'")
        cash_orders = cur.fetchone()[0]

        # Karta buyurtmalar
        cur.execute("SELECT COUNT(*) FROM orders WHERE payment_type = 'card'")
        card_orders = cur.fetchone()[0]

        # O'tgan oyda eng ko'p buyurtma bajargan haydovchi
        cur.execute("""
            SELECT driver_id, COUNT(*) as cnt FROM orders
            WHERE status = 'finished'
            AND strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now', '-1 month')
            GROUP BY driver_id ORDER BY cnt DESC LIMIT 1
        """)
        last_month_top_driver_id = cur.fetchone()

        # Bu oyda eng ko'p buyurtma bajargan haydovchi
        cur.execute("""
            SELECT driver_id, COUNT(*) as cnt FROM orders
            WHERE status = 'finished'
            AND strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
            GROUP BY driver_id ORDER BY cnt DESC LIMIT 1
        """)
        this_month_top_driver_id = cur.fetchone()

        # O'tgan oylik daromad
        cur.execute("""
            SELECT COALESCE(SUM(price), 0) FROM orders
            WHERE status = 'finished'
            AND strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now', '-1 month')
        """)
        last_month_income = cur.fetchone()[0]

        # Bu oylik daromad
        cur.execute("""
            SELECT COALESCE(SUM(price), 0) FROM orders
            WHERE status = 'finished'
            AND strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
        """)
        this_month_income = cur.fetchone()[0]

        # Tarif chaqiruv soni
        cur.execute("""
            SELECT tariff, COUNT(*) as cnt FROM orders
            GROUP BY tariff ORDER BY cnt DESC
        """)
        tariff_stats = cur.fetchall()

        # Haydovchilar soni
        cur.execute("SELECT COUNT(*) FROM DRIVERS")
        drivers_count = cur.fetchone()[0]

        # Oylik foydalanuvchilar
        cur.execute("""
            SELECT COUNT(DISTINCT user_id) FROM orders
            WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
        """)
        monthly_users = cur.fetchone()[0]

        # Kunlik foydalanuvchilar
        cur.execute("""
            SELECT COUNT(DISTINCT user_id) FROM orders
            WHERE DATE(created_at) = DATE('now')
        """)
        daily_users = cur.fetchone()[0]

        return {
            'daily_orders': daily_orders,
            'monthly_orders': monthly_orders,
            'finished_orders': finished_orders,
            'cancelled_orders': cancelled_orders,
            'cash_orders': cash_orders,
            'card_orders': card_orders,
            'last_month_top_driver': last_month_top_driver_id,
            'this_month_top_driver': this_month_top_driver_id,
            'last_month_income': last_month_income,
            'this_month_income': this_month_income,
            'tariff_stats': tariff_stats,
            'drivers_count': drivers_count,
            'monthly_users': monthly_users,
            'daily_users': daily_users,
        }

def get_all_driver_tg_ids():
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT tg_id FROM DRIVERS WHERE tg_id IS NOT NULL AND is_blocked = 0")
        return [row[0] for row in cur.fetchall()]

def get_all_user_tg_ids():
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT tg_id FROM users")
        return [row[0] for row in cur.fetchall()]

def get_all_tg_ids():
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT tg_id FROM users")
        user_ids = {row[0] for row in cur.fetchall()}
        cur.execute("SELECT tg_id FROM DRIVERS WHERE tg_id IS NOT NULL AND is_blocked = 0")
        driver_ids = {row[0] for row in cur.fetchall()}
        return list(user_ids | driver_ids)

def get_driver_earnings(driver_id):
    with connect() as con:
        cur = con.cursor()

        # Bugungi daromad
        cur.execute("""
            SELECT COALESCE(SUM(price), 0) FROM orders
            WHERE driver_id = ? AND status = 'finished'
            AND DATE(created_at) = DATE('now')
        """, (driver_id,))
        today = cur.fetchone()[0]

        # Oylik daromad
        cur.execute("""
            SELECT COALESCE(SUM(price), 0) FROM orders
            WHERE driver_id = ? AND status = 'finished'
            AND strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
        """, (driver_id,))
        monthly = cur.fetchone()[0]

        # Jami daromad
        cur.execute("""
            SELECT COALESCE(SUM(price), 0) FROM orders
            WHERE driver_id = ? AND status = 'finished'
        """, (driver_id,))
        total = cur.fetchone()[0]

        # Jami buyurtmalar soni
        cur.execute("""
            SELECT COUNT(*) FROM orders
            WHERE driver_id = ? AND status = 'finished'
        """, (driver_id,))
        trips = cur.fetchone()[0]

        return {
            'today': today,
            'monthly': monthly,
            'total': total,
            'trips': trips,
        }

def save_driver_message(order_id, driver_tg_id, message_id):
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT driver_messages FROM orders WHERE id = ?", (order_id,))
        row = cur.fetchone()
        messages = json.loads(row[0]) if row[0] else {}
        messages[str(driver_tg_id)] = message_id
        con.execute("UPDATE orders SET driver_messages = ? WHERE id = ?",
                   (json.dumps(messages), order_id))
        con.commit()

def get_driver_messages(order_id):
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT driver_messages FROM orders WHERE id = ?", (order_id,))
        row = cur.fetchone()
        return json.loads(row[0]) if row[0] else {}


def update_driver_rating(driver_id, new_rating):
    with connect() as con:
        cur = con.cursor()
        cur.execute("SELECT rating, rating_count FROM DRIVERS WHERE id = ?", (driver_id,))
        row = cur.fetchone()
        rating = row[0] or 0
        count = row[1] or 0

        avg_rating = (rating * count + new_rating) / (count + 1)

        con.execute("""
            UPDATE DRIVERS SET rating = ?, rating_count = ? WHERE id = ?
        """, (avg_rating, count + 1, driver_id))
        con.commit()