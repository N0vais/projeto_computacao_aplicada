# IMPORTAR E INSTALAR O KIVY PARA DESENHAR A TELA DO APP 
import pyrebase

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


from funcoes import voltar_Login, voltar_Registro

# DEFINI O TAMANHO DA TELA 
Window.size = (350, 580)

#gerencia as chamado para apresentar na tela
apresentarTela = ScreenManager()
firebaseConfig={
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
listaBase = []

#CRIANDO CLASSES PARA MANIPULAR O APP
class TelaAbertura(Screen):
    pass

class Apresentacao(Screen):
    pass

class Ansiedada(Screen):
    pass

class Deprecao(Screen):
    pass

class PreCrise(Screen):
    pass

class PosCrise(Screen):
    pass

class Tela_registro(Screen):

    bancoDados = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/Usuario/.json"
    bancoDados2 = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def voltar_Registro(self, *args):
        voltar_Registro(self, *args)
    
    def chamar_login(self, nome, cpf, senha):
        from funcoes import criar_Postagem
        criar_Postagem( self, nome, cpf, senha)

class Tela_logar(Screen):

    bancoDados = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/Usuario/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def voltar_Login(self, *args):
        voltar_Login(self, *args)

    def logando(self, cpf, senha):
        from funcoes import pegar_Postagem
        pegar_Postagem(self, cpf, senha)

class EsqueceuSenha(Screen):
    bancoDados = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def perdeuSenha(self, cpf, senha):
        from funcoes import refazer_Senha
        refazer_Senha(self, cpf, senha)

#FAZENDO AUTENTICAÇAO DO USUARIO, CRIANDO A CLASSE QUE VAI AUTENTICAR   
class PainelInicial(Screen):
    def entrar(self):
        nome = list(open("autenticado.txt", "r"))
        nome = nome[0]
        self.ids.lbdashboard.text = "Bem vindo(a), " + str(nome)

class SobreUsuario(Screen):
    firebase_url = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def entrar(self):
        from funcoes import entrar2
        entrar2(self)

class MudarInformacao(Screen):
    def editar_informacao(self, nome, cpf, id):
        from funcoes import editar_usuario
        editar_usuario(self, nome, cpf, id)

class chekarTela(Screen):
    bancoFirebase = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/Usuario/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def checar(self, especialidade, data, paciente):
        from funcoes import checar
        checar(self, especialidade, data, paciente) 

    def salvar(self, instance, value, data_range):
        from funcoes import salvar
        salvar(self, instance, value, data_range)

    def cancelar(self, instance, value):
        from funcoes import cancelar
        cancelar(self, instance, value)

    def data(self):
        from funcoes import seletorDados
        seletorDados(self)

class checandoTela(Screen):

    def retirada(self, med, data, paciente2):
        from funcoes import checar
        checar(self, med, data, paciente2)

    def salvar(self, instance, value, data_range):
        from funcoes import salvar2
        salvar2(self, instance, value, data_range)

    def cancelar2(self, instance, value):
        from funcoes import cancelar2
        cancelar2(self, instance, value)

    def data(self):
        from funcoes import seletorDados2
        seletorDados2(self)  

class MedicosTela(Screen):
    pass

class ComtroleMedico(Screen):
    def entradaMedicamento(self, nome_medicamento, qtd, id_medicamento):
        from funcoes import criar_postagen_medicamento
        criar_postagen_medicamento(self, nome_medicamento, qtd, id_medicamento)

    def saidaMedicamento(self,nome_medicamento, qtd, id_medicamento):
        from funcoes import criar_delete
        criar_delete(self, nome_medicamento, qtd, id_medicamento)

class VerificarMedicamentos(Screen):
    def parar(self):
        from funcoes import salvar
        salvar(self)

    def entrar(self):
        from funcoes import entrar
        entrar(self) 

    def start_second_thread(self):
        from funcoes import start_second_thread
        start_second_thread(self)
  
    def carregar_dados(self, *args):
        from funcoes import carregar_dados
        carregar_dados(self, *args)

    def dados_tabela(self, cols, values):
        from funcoes import dados_tabela
        dados_tabela(self, cols, values)

class RegistroPaciente(Screen):
    def callbackregisterpacientes(self, *args):
        from funcoes import callbackregisterpacientes
        callbackregisterpacientes(self, *args)

    def registroPacientes(self, nome2, cpf2, senha2):
        from funcoes import criar_postagen_paciente
        criar_postagen_paciente(self, nome2, cpf2, senha2)

class AppAnsiedade(MDApp):

    def build(self):
        tela = Builder.load_file ("Screen.kv")   
        apresentarTela =tela 
        return apresentarTela

AppAnsiedade().run()