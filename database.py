import asyncpg

USER = ''
PSWD = ''
DB = ''
HOST = ''

async def sql_start():
    """Создание бд на старте бота"""
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    if conn:
        print('DB connected')
    await conn.execute('CREATE TABLE IF NOT EXISTS users(id SERIAL NOT NULL PRIMARY KEY, username CHAR(60), region CHAR(70), activity CHAR(100), track CHAR(90))')
    await conn.close()

async def add_user_by_region(region, username):
    """Добавление юзера в БД на этапе региона, остальные поля пустые"""
    print(region+'jsdkj')
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    await conn.execute('INSERT INTO users(username,region)VALUES($1,$2)', username,region)
    row = await conn.fetchrow('SELECT region FROM users WHERE username = $1',username)
    print(row['region'])
    await conn.close()


async def update_user_region(region,username):
    """UPDATE региона юзера при обновлении данных"""
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    await conn.execute('''UPDATE users SET region=$1 WHERE username=$2''', region,username)
    await conn.close()


async def add_track(username, track):
    """Добавление трэка к существующему юзеру"""
    print(track)
    print(type(track))
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    await conn.execute(f'''UPDATE users SET track = $1 WHERE username = $2''',track, username)
    await conn.close()


async def add_activity(username, activity):
    """Добавление рода деятельности к существующему юзеру"""
    print(activity)
    print(type(activity))
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    await conn.execute(f'''UPDATE users SET activity = $1 WHERE username = $2''',activity, username)
    await conn.close()

async def get_user(username):
    """Получение юзера по юзернейму и возвращение списка данных из бд(сначала производится приведение списка к нормальному виду)"""
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    row = await conn.fetchrow('SELECT * FROM users WHERE username = $1',username)
    rows = []
    row = row[1:]
    for i in row:
        if i != None:
            i = i.strip()
            rows.append(i)
        else:
            rows.append(i)
    await conn.close()
    return rows

async def check_user(username):
    """Проверка, есть ли юзер уже в базе и возврат"""
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    user = await conn.fetchrow('SELECT username FROM users WHERE username = $1',username)
    await conn.close()
    if user:
        print(True)
        return True
    else:
        print(False)
        return False


async def get_user_by_track(track,username):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    user = await conn.fetchrow('SELECT * FROM users WHERE (track = $1 AND username!=$2) ORDER BY RANDOM(); ', track,
                               username)
    rows = []
    await conn.close()
    if user:
        user = user[1:]
        for i in user:
            if i != None:
                i = i.strip()
                rows.append(i)
            else:
                rows.append(i)
        return rows
    return False


async def get_user_by_activity(activity,username):
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    user = await conn.fetchrow('SELECT * FROM users WHERE (activity = $1 AND username!=$2) ORDER BY RANDOM(); ',activity,username)
    rows = []
    await conn.close()
    if user:
        user = user[1:]
        for i in user:
            if i != None:
                i = i.strip()
                rows.append(i)
            else:
                rows.append(i)
        return rows
    return False

async def get_user_by_region(region,username):
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    user = await conn.fetchrow('SELECT * FROM users WHERE (region = $1 AND username!=$2) ORDER BY RANDOM(); ',region,username)
    rows = []
    await conn.close()
    if user:
        user = user[1:]
        for i in user:
            if i != None:
                i = i.strip()
                rows.append(i)
            else:
                rows.append(i)
        return rows
    return False

async def get_user_by_track_three(track,username):
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    users = await conn.fetch('SELECT * FROM users WHERE (track = $1 AND username!=$2) ORDER BY RANDOM() LIMIT 3',track,username)
    await conn.close()
    if users:
        rows = []
        for i in users:
            user = i[1:]
            for j in user:
                if j != None:
                    j = j.strip()
                    rows.append(j)
                else:
                    rows.append(j)
        return rows
    return False

async def get_user_by_region_three(region,username):
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    users = await conn.fetch('SELECT * FROM users WHERE (region = $1 AND username!=$2) ORDER BY RANDOM() LIMIT 3',region,username)
    await conn.close()
    if users:
        rows = []
        for i in users:
            user = i[1:]
            for j in user:
                if j != None:
                    j = j.strip()
                    rows.append(j)
                else:
                    rows.append(j)
        return rows
    return False

async def get_user_by_activ_three(activ,username):
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    users = await conn.fetch('SELECT * FROM users WHERE (activity = $1 AND username!=$2) ORDER BY RANDOM() LIMIT 3',activ,username)
    await conn.close()
    if users:
        rows = []
        for i in users:
            user = i[1:]
            for j in user:
                if j != None:
                    j = j.strip()
                    rows.append(j)
                else:
                    rows.append(j)
        return rows
    return False

async def check_bd_user_region(user_id):
    """Legacy"""
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    #Кодирование в байты
    region = 'o'.encode()
    activ = 'b'.encode()
    print(type(activ))
    #await conn.execute('''INSERT INTO users(id,region,activity) VALUES($1, $2, $3)''', user_id, region, activ)
    row = await conn.fetchrow('SELECT region FROM users WHERE id = $1',user_id)
    row2 = await conn.fetchrow('SELECT activity FROM users WHERE id = $1',user_id)
    print(row)
    print(row['region'])
    print(type(row2))
    print(type(row2['activity']))
    #Декодирование из байтов
    a = row['region'].decode()
    print(a)
    await conn.close()
    if row is None:
        return 'None'
    return row['region']

