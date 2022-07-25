import psycopg2
con = psycopg2.connect (host='motty.db.elephantsql.com',
                        database='kegmoddu',
                        user='kegmoddu',
                        password='aK7cD5Amgs1VTaZvSDJYGrQwx812hTpE')
cur = con.cursor()
comando = "SELECT * FROM cliente"
resultado = cur.execute(comando)
linhas = cur.fetchall()
print(linhas)
