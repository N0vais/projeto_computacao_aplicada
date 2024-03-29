# IMPORTAR E INSTALAR O KIVY PARA DESENHAR A TELA DO APP 
import pyrebase

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

from funcoes import volta_painel, voltarLogin

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

class Tela_registro(Screen):

    firebase_url = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/Usuario/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def voltarLogin(self, *args):
        voltarLogin(self, *args)
    
    def chamar_login(self, nome, cpf, senha):
        from funcoes import get_post
        get_post( self, nome, cpf, senha)

class Tela_logar(Screen):

    bancoDados = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/Usuario/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def volta_painel(self, *args):
        volta_painel(self, *args)

    def logando(self, cpf, senha):
        from funcoes import criando_post
        criando_post(self, cpf, senha)

class EsqueceuSenha(Screen):
    firebase_url = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def perdeuSenha(self, cpf, senha):
        from funcoes import refazerSenha
        refazerSenha(self, cpf, senha)

#FAZENDO AUTENTICAÇAO DO USUARIO, CRIANDO A CLASSE QUE VAI AUTENTICAR   
class PainelInicial(Screen):
    def entrar(self):
        nome = list(open("autenticado.txt", "r"))
        nome = nome[0]
        self.ids.lbdashboard.text = "Bem vindo(a), " + str(nome)

class SobreUsuario(Screen):
    firebase_url = "https://autocuidado-a-ansiedade-default-rtdb.firebaseio.com/.json"
    auto_key = "AIzaSyBD_N15hbNLArph_6wblwxjCFe8P6Z74gw"

    def on_enter(self):
        from funcoes import entrar
        entrar(self)

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
        from funcoes import salvar
        salvar(self, instance, value, data_range)

    def cancelar(self, instance, value):
        from funcoes import cancelar
        cancelar(self, instance, value)

    def data(self):
        from funcoes import seletorDados
        seletorDados(self)  



class AppAnsiedade(MDApp):

    def build(self):
        tela = Builder.load_file ("Screen.kv")   
        apresentarTela =tela 
        return apresentarTela

AppAnsiedade().run()