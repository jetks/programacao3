import psycopg2
con = psycopg2.connect(host='motty.db.elephantsql.com',database='kegmoddu',user='kegmoddu',password='aK7cD5Amgs1VTaZvSDJYGrQwx812hTpE')
cur = con.cursor()

print("1- Inserir aluno\n2- Buscar aluno(s)\n3- Sair")

continuar = True
while continuar:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Insira um nome: ")
        cidade = input("Insira sua cidade: ")
        nasc = input("Insira seu nascimento (ano-mês-dia): ")

        comando = "INSERT INTO Aluno(Nome, Cidade, DataNasc) VALUES ('"+nome+"', '"+cidade+"','"+nasc+"')"
        cur.execute(comando)
        con.commit()
        

    elif opcao == 2:
        pesq = input("Nome da cidade: ")
        comando = "SELECT IdAluno, Nome, DataNasc FROM Aluno WHERE cidade = '"+pesq+"'"
        cur.execute(comando)
        linhas = cur.fetchall()
        for linha in linhas:
            print(linha[0], linha[1], linha[2])
    

    elif opcao == 3:
        con.close()
        continuar = False
