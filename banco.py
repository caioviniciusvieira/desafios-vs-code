import mysql.connector # biblioteca para conectar com o banco de dados MySQL
from decimal import Decimal
import datetime

try:
    # Conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="banco",
    )
    if conexao.is_connected():
        print("Conexão estabelecida com sucesso!")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar ao banco de dados: {erro}")


cursor = conexao.cursor(dictionary=True) # permite burcar em formato de dicionário, facilitando o acesso aos dados retornados.
while True:
    procurar_cpf = input("Digite o cpf: ")
    sql = cursor.execute("SELECT id_usuario, nome, cpf FROM usuarios WHERE cpf = %s", (procurar_cpf,))

    dados = cursor.fetchall() # retornar todos os resultados da consulta em uma lista de dicionários

    if not dados: # Verificar se a lista de dados está vazia
            print("Nenhum usuário encontrado com o cpf fornecido.")
    else:
         break

for linha in dados: # Iterar sobre cada linha retornada pela consulta
    while True:
        escolher_conta = input("Digite o número da conta que deseja acessar: ")

        cursor.execute("SELECT num_conta, saldo, tipo_conta, senha, status, id_contas FROM contas WHERE num_conta = %s AND id_usuario = %s", (escolher_conta, linha['id_usuario']))
        conta_escolhida = cursor.fetchone() # retornar o resultado da consulta em um dicion

        if not conta_escolhida:
             print("Conta não existe\nInforme um número de conta válido.")
        else:
             break
    while True:    
        senha_digitada = input("Digite a senha para verificar: ")

        if senha_digitada == conta_escolhida['senha']: # Verificar se a senha digitada é igual à senha do banco de dados
            print("Senha correta! Acesso permitido.")
            print(f"Conta escolhida: Saldo: {conta_escolhida['saldo']}, Tipo de Conta: {conta_escolhida['tipo_conta']}")

            while True:
                print("1 - Depositar")
                print("2 - Sacar")
                print("3 - Sair")
                try:
                    opcao = int(input("Insira a opção: "))
                    if opcao == 1:
                        if conta_escolhida['status'] == 'Ativa':
                            stop = True 
                            while stop == True:
                                try:
                                    deposito = float(input("Informe a quantidade para depositar: (R$)"))
                                    saldo_soma = conta_escolhida['saldo'] + Decimal(str(deposito))

                                    cursor.execute("UPDATE contas SET saldo = %s WHERE id_contas = %s", (saldo_soma, conta_escolhida['id_contas']))
                                    conexao.commit()
                                    conta_escolhida['saldo'] = saldo_soma
                                    print(f"Saldo: {conta_escolhida['saldo']}")
                                    horario = datetime.datetime.now().strftime("%H:%M:%S")
                                    dia = datetime.datetime.now().strftime("%Y-%m-%d")
                                    cursor.execute("INSERT INTO transacoes (id_conta, dia, horario, valor_transacao, tipo_transacao) VALUES "
                                    "(%s,%s,%s,%s,%s)", (conta_escolhida['id_contas'], dia, horario, saldo_soma, 'Deposito'))
                                    conexao.commit()
                                    stop = False
                                    continue

                                except ValueError:
                                    print("Informe apenas números.")
                        else:
                            print("Conta está bloqueda")
                    elif opcao == 2:
                        stop = True
                        while stop == True:
                            try:
                                sacar = float(input("Informe a quantidade para sacar: (R$)"))

                                saldo_final = conta_escolhida["saldo"] - Decimal(str(sacar)) 
                                if saldo_final < 0:
                                    print("Saldo insuficiente para realizar o saque.")
                                    print(f"Saldo: {conta_escolhida['saldo']}")
                                    

                                cursor.execute("UPDATE contas SET saldo = %s WHERE id_contas = %s", (saldo_final, conta_escolhida['id_contas']))
                                conexao.commit()
                                conta_escolhida['saldo'] = saldo_final
                                print(f"Saldo: {conta_escolhida['saldo']}, Tipo de Conta: {conta_escolhida['tipo_conta']}")

                                horario = datetime.datetime.now().strftime("%H:%M:%S")
                                dia = datetime.datetime.now().strftime("%Y-%m-%d")
                                cursor.execute("INSERT INTO transacoes (id_conta, dia, horario, valor_transacao, tipo_transacao) VALUES "
                                "(%s,%s,%s,%s,%s)", (conta_escolhida['id_contas'], dia, horario, saldo_final, 'Saque'))
                                conexao.commit()
                                stop = False
                                continue
                            except ValueError:
                                print("Informe apenas os números.")
                    elif opcao == 3:
                        print("Saiu com sucesso")
                        break
                except ValueError:
                    print("Digite uma opção válida")
            break            
        else:
            print("Senha incorreta")

cursor.close()
conexao.close()