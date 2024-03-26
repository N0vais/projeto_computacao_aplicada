#IMPORTAR E INSTALAR O KIVY PARA DESENHAR A TELA DO APP 
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

# DEFINI O TAMANHO DA TELA 
Window.size = (350, 580)

#gerencia as chamado para apresentar na tela
apresentarTela = ScreenManager()

#FAZ A CHAMADA DO APP EM LOOP

class Tela_Abertura(Screen):
    pass

class Apresentacao(Screen):
    pass

class Tela_logar(Screen):
    pass

class Tela_registro(Screen):
    pass

class AppAnsiedade(MDApp):

    def build(self):
        tela = Builder.load_file ("Screen.kv")   
        apresentarTela =tela 
        return apresentarTela
    
    
        

AppAnsiedade().run()