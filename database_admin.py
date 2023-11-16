import asyncpg

USER = ''
PSWD = ''
DB = ''
HOST = ''

async def sql_admins_start():
    """Создание бд на старте бота"""
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    if conn:
        print('DB connected')
    await conn.execute('CREATE TABLE IF NOT EXISTS admins(username CHAR(60))')
    await conn.close()


async def get_admins():
    """Получение юзера по юзернейму и возвращение списка данных из бд(сначала производится приведение списка к нормальному виду)"""
    conn = await asyncpg.connect(user=USER,password=PSWD,database=DB,host=HOST)
    row = await conn.fetch('SELECT * FROM admins')
    rows = []
    for i in row:
        if i != None:
            b=i[0]
            b=b.strip()
            rows.append(b)
    await conn.close()
    return rows

async def update_admins(username):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    await conn.execute(f'''INSERT INTO admins (username) VALUES ($1)''',username)
    await conn.close()

async def add_new_user(username):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    await conn.execute(f'''INSERT INTO users (username) VALUES ($1)''',username)
    await conn.close()

async def new_user_region(username,region):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    await conn.execute(f'''UPDATE users SET region = $1 WHERE username = $2''',region, username)
    await conn.close()


async def export_to_csv():
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    data = await conn.fetch('SELECT * FROM users')
    with open('out.csv', 'w') as f:
        for i in data:
            f.write(",".join([str(cell).strip() for cell in i])+"\n")
    print("Table exported to CSV!")
    print(data)
    del data
    await conn.close()
    return open('out.csv', mode='rb')

async def export_to_json():
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    data = await conn.fetch('SELECT * FROM users')
    await conn.close()
    print(data)
    with open('out.json', 'w') as f:
        for row in data:
            f.write("{\n\t\"id\":" f"{row['id']},\n"
                 "\t\"username\": " f"\"{str(row['username']).strip()}\",\n"
                 "\t\"region\": " f"\"{str(row['region']).strip()}\",\n"
                 "\t\"activity\": " f"\"{str(row['activity']).strip()}\",\n"
                 "\t\"track\": " f"\"{str(row['track']).strip()}\"\n"
                    "},\n")
    return open('out.json', mode='rb')