# Pós Graduação em Ciência de dados e Big Data Analytics.
# Nome da disciplina: Linguagem Python
# Rinaldo Gama
#Prof. ANDRE LUIZ BRAGA
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

arquivo = open ('votos.db', 'wb')
for i in range (5):  # permite cadastro de 5 candidatos
    pickle.dump (i, arquivo)
arquivo.close ()
print ('Arquivo criado com sucesso')

db = {}


def show_menu():
    os.system ('cls')
    print ('Existem ' + str (len (db)) + ' Candidatos Inscritos nesta Eleição\n\n')
    print ('Escolha a opção')
    print ('1 - Candidatos')
    print ('2 - Votaçao')
    print ('3 - Sair')
    option = int (input (''))

    if (option == 1):
        incluir()
    elif (option == 2):
        votacao()
    elif (option == 3):
        print ('Encerrando a Urna')
        exit()
    else:
        print ('Opcao não disponivel, saindo do programa')
    show_menu()


def incluir(): #função para inclusão de candidatos
    candidato = {}
    npartido = input('Informe o numero da celula do candidado..: ')
    if (npartido in db.keys ()):
        print('candidato já cadastrado')
        show_menu()
    else:
        print('Tenha uma otima Eleição')
        candidato['codigo'] = npartido
        candidato['nome'] = input('Digite o nome da Candidato..: ')
        candidato['voto'] = 0
        candidato['votobranco'] = 0
        db[npartido] = candidato
        show_menu()

def listar(): #Função listar Votação
    print ('----- Resultado da Votação ------')
    for npartido in db.keys ():
        print ('Candidado: ' + db[npartido]['codigo'])
        print ('Nome: ' + db[npartido]['nome'])
        print ('Total votos Candidato:')
        print (db[npartido]['voto'])
        print ('-' * 31)

def votacao(): #função votação de votos
    branco = 0
    nulo = 0
    contagem = 0
    regiao = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}
    print ('----- Inicio da Votação ------')
    print ('0 - voto em branco')
    print ('-------------------------------')
    if len (db) > 0: #verifica se existe candidatos cadastrados
                print ('Nr Cedula    -  Candidato   ')
                for npartido in db.keys ():
                    print (db[npartido]['codigo'] + '           ' + db[npartido]['nome'])
    else:
        print ('Não existem candidatos inscritos para disputar as eleição')
        input('pressione qualquer tecla para sair da votação\n')
        show_menu()
    print ('-' * 31)
    print('Infome numero de Eleitores')
    eleitores = int (input (''))
    for i in range(eleitores):
        npartido = input ('Informe o numero da celula do candidato..:')
        if (npartido in db.keys ()):
            print ('Candidado: ' + db[npartido]['codigo'])
            print ('Nome: ' + db[npartido]['nome'])
            db[npartido]['voto']+=1


        else: ## conta numero de votos em brancos e nulos
            if (npartido=='0'):
                branco=branco+1
                print('voto em branco')
            else:
                print('voto em Nulo - candidato não existe')
                nulo=nulo+1
    contagem+=1
    vazio=branco+nulo
    listar ()
    print('Total de votos brancos/nulos..:' + str(vazio))
    print ('Total de votos região..:' + str (eleitores))
    print ('-' * 31)
    show_menu ()



show_menu()