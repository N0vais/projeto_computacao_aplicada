# IMPORTAR AS DEPENDECIAS 
import json
import pyrebase
import requests
import threading

from kivy.clock import Clock, mainthread
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.pickers import MDDatePicker

# CRIANDO A CONECÇÃO COM O BANCO FIREBASE (real time)...
firebaseConfig = {
    'apiKey': "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw",
    'authDomain': "autocuidado-a-ansiedade.firebaseapp.com",
    'databaseURL': "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com",
    'projectId': "autocuidado-a-ansiedade",
    'storageBucket': "autocuidado-a-ansiedade.appspot.com",
    'messagingSenderId': "225042815723",
    'appId': "1:225042815723:web:423468a0eb24b46e85bcae",
    'measurementId': "G-3B9PNYNH0P"
};
baseDados = pyrebase.initialize_app(firebaseConfig)
listaBase =[]

# DIRECIONA NOVAMENTE PARA TELA DE LOGIN
def voltar_Registro(self, *args):
    MDApp.get_running_app().root.current = 'logar'

# FUNCAO QUE COLOCA INFORMAÇOES DO USUARIO NO BANCO FIREBASE UTILIZANDO POST
def criar_Postagem(self, nome, cpf, senha):    
    bancoDados = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/Usuario/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    lista = []
    request = requests.get(self.bancoDados + '?auth=' + self.auto_key)
    resposta = json.dumps(request.json())

    try:        
        to_database = '{"Nome": 'f'{json.dumps(nome)}'', "CPF": 'f'{json.dumps(cpf)}'', "Senha": 'f'{json.dumps(senha)}''}'

        if nome == "":
            self.ids.lbregister.text = "Insira nome"

        elif cpf == "":
            self.ids.lbregister.text = "Insira CPF"

        elif senha == "":
            self.ids.lbregister.text = "Insira Senha"  

        elif len(cpf) < 11:
            self.ids.lbregister.text = "CPF inválido, tente novamente"

        elif len(senha) < 6:
            self.ids.lbregister.text = "Senha precisa de pelo menos 6 caracteres"   

        elif cpf in resposta:
            self.ids.lbregister.text = "CPF já cadastrado"

        else:
            requests.post(url = self.bancoDados, json = json.loads(to_database))

            self.ids.lbregister.text = "Cadastrado com sucesso! Redirecionando para a tela de login..."
            Clock.schedule_once(self.voltar_Registro, 3)

            lista.append(nome)
            lista.append(cpf)
            lista.append(senha)

            with open(f'{cpf}.txt',"w") as a:
                a.write(str(lista[0]))
                a.write("\n")
                a.write(str(lista[1]))
                a.write("\n")
                a.write(str(lista[2]))
    except ValueError:
        pass 

    lista.clear

# CHAMA O PAINEL DE ACESSO PRIMARIO
def voltar_Login(self, *args):
    MDApp.get_running_app().root.current ='painel'

# PUCHA INFORMAÇOES DO BANCO FIREBSE REAL TIME E FAZ AUTENTICAÇÃO
def pegar_Postagem(self, cpf, senha):
    request = requests.get(self.bancoDados + '?auth=' + self.auto_key)
    resposta = json.dumps(request.json())

    if (cpf != '' and senha != ''):
        if (len(cpf) == 11 and cpf in resposta) and (len(senha) >= 6 and senha in resposta):
            self.ids.lblogin.text = "Aguarde...! "               
            Clock.schedule_once(self.voltar_Login, 3)
            nome = list(open(f'{cpf}.txt', "r"))
            nome = nome[0]
            id = list(open(f'{cpf}.txt', "r"))
            id = id[2]
            with open("autenticado.txt", "w") as f:    
                f.write(str(nome))
                f.write(str(cpf))
                f.write("\n")
                f.write(str(id))  
        else: 
            self.ids.lblogin.text = "CPF ou senha inválidos, Tente novamente"   
    else: 
        if(cpf == ''):
            self.ids.lblogin.text = "Insira o CPF..."
        elif(senha == ''):
            self.ids.lblogin.text = "Insira a senha..."
        elif (cpf == '' and senha == ''):
            self.ids.lblogin.text = "Insira os dados para fazer o login..." 

# REFAZER A SENHA (esquecei a senha)...
def refazer_Senha(self, cpf, senha):
    request = requests.get(self.bancoDados + '?auth=' + self.auto_key)
    resposta = json.dumps(request.json()) 
  
    if cpf == "":
        self.ids.lbredfsenha.text = "Insira o cpf"
    elif cpf not in resposta:
        self.ids.lbredfsenha.text = "CPF não cadastrado"
    elif len(cpf) < 11:
        self.ids.lbredfsenha.text = "CPF Inválido"
    elif senha == "": 
        self.ids.lbredfsenha.text = "Insira a nova senha"
    elif len(senha) < 6:
        self.ids.lbredfsenha.text = "Senha precisa ter pelo menos 6 caracteres"
    
    else:
        db = baseDados.database()
        user = db.child("Usuario").get()
        for usuario in user.each():
            if usuario.val()["CPF"] == f'{cpf}' :
                db.child("Usuario").child(usuario.key()).update({'Senha': f'{senha}'})
                linha = open(f'{cpf}.txt', "r")
                list_lines = linha.readlines()    
                list_lines[2] = f'{senha}'
                linha = open(f'{cpf}.txt', "w")
                linha.writelines(list_lines) 
                linha.close()
    
        self.ids.lbredfsenha.text = "Senha redefinida com sucesso!"

# EDITAR INFORMAÇÕES DO USUARIO QUANDO LOGADO...
def editar_Usuario(self, nome, cpf, id):
    segundoNome = list(open("autenticado.txt", "r"))
    segundoNome = segundoNome[0]
    segundoCpf = list(open("autenticado.txt", "r"))
    segundoCpf = segundoCpf[1]
    segundoId = list(open("autenticado.txt", "r"))
    segundoId = segundoId[2]
 
    bancoDados = baseDados.database()
    usuario = bancoDados.child("Usuario").get()
    for user in usuario.each(): 
        if user.val()["Nome"] in segundoNome:
            if f'{nome}' != "":
                bancoDados.child("Usuario").child(user.key()).update({'Nome': f'{nome}'})
                linha = open("autenticado.txt", "r")
                list_lines = linha.readlines()
                list_lines[0] = f'{nome} \n\n'
                linha = open("autenticado.txt", "w")
                linha.writelines(list_lines)
                linha.close()
                
        if user.val()['CPF'] in segundoCpf:
            if f'{cpf}' != "":
                bancoDados.child("Usuario").child(user.key()).update({'CPF': f'{cpf}'})
                sc =open("autenticado.txt", "r")
                list_lines = sc.readlines()
                list_lines[1] = f'{cpf} \n\n'
                sc = open("autenticado.txt", "w")
                sc.writelines(list_lines)
                sc.close()

        if user.val()['Senha'] in segundoId:
            if f'{id}' != "":
                bancoDados.child("Usuario").child(user.key()).update({'Senha': f'{id}'})
                si =open("autenticado.txt", "r")
                list_lines = si.readlines()
                list_lines[2] = f'{cpf} \n\n'
                si = open("autenticado.txt", "w")
                si.writelines(list_lines)
                si.close()

            self.ids.lbchange.text = "Atualizaçao completa !"
            with open(f'{cpf}.txt', "w") as operacao:
                operacao.write(str(nome))
                operacao.write("\n\n")
                operacao.write(str(cpf))
                operacao.write("\n\n")
                operacao.write(str(id))

# A DATA É SALVA ATRAVES DA ESCOLHA DO USUARIO
def salvar(self, instacia, value, date_ranger):
    self.ids.data.text = str(value)

# MOSTRA UMA MENSAGEM QUANDO A DATA FOR CANCELADA 
def cancelar(self, instacia, value):
    self.ids.data.text = "Data cancelada..."

# FUNÇÃO QUE VAI CRIAR UM CALENDARIO
def seletorDados(self):
    dataDialogo = MDDatePicker(year=2024, month=3, day=28)
    dataDialogo.bind(salvar = self.salvar, cancelar = self.cancelar)
    dataDialogo.open()

# CHECAR A CONSULTA NO BANCO DE DADOS
def checar(self, especialista, data, paciente):
    baseDados = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com "    
    auto_key = 'AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw' 

    request = requests.get(self.baseDados + '?auth=' + self.auto_key) 
    resposta = json.dumps(request.json())

    if especialista == "":
        self.ids.lbcheckin.text = "Insira a especialidade..."
    elif paciente not in resposta:
        self.ids.lbcheckin.text = "Não existe esse paciente..."
    elif paciente == "":
        self.ids.lbcheckin.text = "Incira um paciente valido..."
    else:
        to_database = '{"Especialidade"}: 'f'{json.dumps(especialista)}'', "Data": 'f'{json.dumps(data)}'', "ID do paciente": 'f'{json.dumps(paciente)}'''
        bancoDados = baseDados.database()
        pacientes = bancoDados.child("Pacientes").get()
        for pacients in pacientes.each():
            if pacients.val()["ID Paciente"] == f'{paciente}':
               bancoDados.child("Pacientes").child(pacients.key()).update({"Tipo de Tratamento...": f'{especialista}'}) 
        try:
            requests.post(url = self.bancoFirebase, json = json.loads(to_database))
            self.ids.lbcheckin.text = "Consulta agendada com sucesso..."

        except ValueError:
            pass
  



def entrar(self):
    firebase_url = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com "    
    auto_key = 'AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw'  
  
    nome = list(open('autenticado.txt', 'r'))
    nome = nome[0]
    cpf = list(open('autenticado.txt', 'r'))
    cpf = cpf[1]
    id = list(open('autenticado.txt', 'r')) 
    id = id[2]
    self.ids.cpffuncionario.text = cpf    
    self.ids.nomefuncionario.text = nome
    self.ids.idfuncionario.text = id
    