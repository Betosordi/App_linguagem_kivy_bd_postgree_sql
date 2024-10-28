import psycopg2  # Biblioteca para conexão com PostgreSQL
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from datetime import datetime
import pandas as pd
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.image import Image as CoreImage
from io import BytesIO
import os
import sys


# Função para pegar o caminho correto no executável
def get_resource_path(relative_path):
    """ Retorna o caminho correto no executável """
    try:
        # Caso esteja rodando no executável
        base_path = sys._MEIPASS
    except Exception:
        # Caso esteja rodando normalmente (não no executável)
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Exemplo de como carregar a imagem
caminho_imagem = get_resource_path('imagem_logo.png')
#***********************************************************************************


# Configurações do banco de dados
DB_PARAMS = {
    'dbname': 'Monitoramento_Producao',
    'user': 'postgres',
    'password': 'Analista#2024',
    'host': '192.168.10.253',
    'port': '5432'
}



        
#*****************************************************************************************



# Função para acrescentar informações nas colunas
def save_to_db(nome_do_operador,data_da_inspecao,turno,maquina,inicio_primeira_parada,fim_primeira_parada,motivo_primeira_parada,
               inicio_segunda_parada,fim_segunda_parada,motivo_segunda_parada,inicio_terceira_parada,fim_terceira_parada,motivo_terceira_parada,
               inicio_quarta_parada,fim_quarta_parada,motivo_quarta_parada,inicio_quinta_parada,fim_quinta_parada,motivo_quinta_parada,
               quantidade_refugo,produto_produzido,quantidade_produzida):
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        
        # Inserir dados na tabela
        cursor.execute("""
            INSERT INTO qualidade_producao (
                nome_do_operador,
                data_da_inspecao,
                turno, 
                maquina, 
                inicio_primeira_parada, 
                fim_primeira_parada, 
                motivo_primeira_parada, 
                inicio_segunda_parada, 
                fim_segunda_parada, 
                motivo_segunda_parada, 
                inicio_terceira_parada, 
                fim_terceira_parada, 
                motivo_terceira_parada, 
                inicio_quarta_parada, 
                fim_quarta_parada, 
                motivo_quarta_parada, 
                inicio_quinta_parada, 
                fim_quinta_parada, 
                motivo_quinta_parada, 
                quantidade_refugo, 
                produto_produzido, 
                quantidade_produzida
                
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
            """,
            (nome_do_operador, data_da_inspecao, turno, maquina,
             inicio_primeira_parada, fim_primeira_parada, motivo_primeira_parada,
             inicio_segunda_parada, fim_segunda_parada, motivo_segunda_parada,
             inicio_terceira_parada, fim_terceira_parada, motivo_terceira_parada,
             inicio_quarta_parada, fim_quarta_parada, motivo_quarta_parada,
             inicio_quinta_parada, fim_quinta_parada, motivo_quinta_parada,
             quantidade_refugo, produto_produzido, quantidade_produzida)
        )

        # Confirmar as alterações
        conn.commit()
        
        # Fechar a conexão  
        cursor.close()
        conn.close()
    except:
       pass
#****************************************************************************************

today_date = datetime.now().strftime("%d/%m/%Y")


class QuestionScreen1(Screen):
    def __init__(self, **kwargs):
        super(QuestionScreen1,self).__init__(**kwargs)

    
        # Primeira Tela ********************************************************************************************************************************
        # Cria um layout FloatLayout para o conteúdo da tela
        layout = FloatLayout()
        
        # Carregar a imagem localmente
        image_path = get_resource_path('imagem_logo.png')  # Use o caminho para a imagem com a função
        img = Image(source=image_path, 
                    size_hint=(None, None), size=(300, 300), pos_hint={'x': 0.02, 'y': 0.65})
        
        layout.add_widget(img)
        
        
        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Nome do operador:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.9})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto1 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.83})
        layout.add_widget(self.answer_input_name_texto1)

        # Adiciona uma etiqueta com a segunda pergunta - Data
        question_label_date = Label(text="Data do preenchimento:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.75})
        layout.add_widget(question_label_date)

        # Adiciona uma caixa de texto para o usuário inserir a data
        self.answer_input_date_minha_data = TextInput(text= today_date, size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.68},hint_text_color=(0, 0, 0, 1),foreground_color=(0, 0, 0, 1))
        layout.add_widget(self.answer_input_date_minha_data)

        # Adiciona uma etiqueta com a terceira pergunta - Número da Máquina
        question_label_machine = Label(text="Turno:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.6})
        layout.add_widget(question_label_machine)

        # Adiciona uma caixa de texto para o usuário inserir o número da máquina
        self.answer_input_machine_texto2 = TextInput(hint_text="Digite seu turno. Ex: MANHÃ = 1, TARDE = 2 e NOITE = 3 ", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.53})
        layout.add_widget(self.answer_input_machine_texto2)

        # Adiciona uma etiqueta com a quarta pergunta - Número da Máquina
        question_label_machine = Label(text="Máquina", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.45})
        layout.add_widget(question_label_machine)

        # Adiciona uma caixa de texto para o usuário inserir o número da máquina
        self.answer_input_machine_texto3 = TextInput(hint_text="Digite o número da máquina: ", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.35})
        layout.add_widget(self.answer_input_machine_texto3)


 




# Botão que vai para a pagina de paradas de maquina
        # Adiciona um botão para prosseguir para a próxima tela
        botao_paradas = Button(
            text="Relatar paradas de máquina",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'x': 0.44, 'y': 0.15},
            background_color=(1, 0.3, 0.3, 1),  # Vermelho suave
            color=(1, 1, 1, 1)  # Texto branco
        )
        botao_paradas.bind(on_press=self.botao_paginas_paradas_maquinas)
        layout.add_widget(botao_paradas)
#------------------------------------------------------------------------------------------------------------------




        # Adiciona um botão para prosseguir para a próxima tela
        proceed_button = Button(
            text="Prosseguir", 
            size_hint=(None, None), 
            size=(200, 50), 
            pos_hint={'x': 0.44, 'y': 0.05},
            background_color=(0.3, 1, 0.3, 1), # Cor de fundo do  botão verde 
            color=(1, 1, 1, 1)  # Texto branco
        )    
        proceed_button.bind(on_press=self.go_to_next_screen)
        layout.add_widget(proceed_button)
        
        self.add_widget(layout)
    

    # Função chamada quando o botão "Prosseguir" é pressionado
    def go_to_next_screen(self, instance):
        self.manager.current = 'question2'

        # Função chamada quando o botão "Prosseguir" é pressionado
    def botao_paginas_paradas_maquinas(self, instance):
        self.manager.current = 'question3'  
#*************************************************************************************************************************

# Tela de paradas -----------------------------------------------------------------------------------
class pagina_paradas_maquina(Screen):
    def __init__(self, **kwargs):
        super(pagina_paradas_maquina, self).__init__(**kwargs)

        layout_paradas = FloatLayout()

        # Carregar a imagem localmente
        image_path = get_resource_path('imagem_logo.png')  # Use o caminho para a imagem com a função
        img = Image(source=image_path, 
                    size_hint=(None, None), size=(200, 200), pos_hint={'x': 0.02, 'y': 0.7})
        
        layout_paradas.add_widget(img)


        # Adiciona uma etiqueta
        texto_acima_da_caixa_1 = Label(text="Inicio da primeira parada:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.9})
        layout_paradas.add_widget(texto_acima_da_caixa_1)

        # Adiciona uma caixa de texto
        self.caixa_de_texto_1 = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.83})
        layout_paradas.add_widget(self.caixa_de_texto_1)

        # Adiciona uma etiqueta com a primeira pergunta
        fim_primeira_parada_texto = Label(text="Fim da primeira parada :", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.44, 'y': 0.9})
        layout_paradas.add_widget(fim_primeira_parada_texto)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.caixa_horario_primeira_parada = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.475, 'y': 0.83})
        layout_paradas.add_widget(self.caixa_horario_primeira_parada)

        # Adiciona um Spinner (caixa de seleção) para o usuário escolher entre as opções
        motivo_primeira_parada_texto = Label(text="Motivo de primeira parada da maquina:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.77, 'y': 0.9})
        layout_paradas.add_widget(motivo_primeira_parada_texto)


        # Adiciona uma caixa de texto para o usuário inserir a resposta ---------------------------------------
        self.motivo_primeira_parada = Spinner(
            text="",  # Texto padrão quando nada é 
            values=("AGUARDANDO REABASTECIMENTO", "ESPERA - MANUTENÇÃO MÁQUINA", "ESPERA - MANUTENÇÃO DE MOLDE",
                    "ESPERA - SETUP", "FALTA DE COLABORADOR", "FALTA DE ENERGIA", "FALTA DE MATERIA PRIMA", "HORÁRIO DE REFEIÇÃO",
                    "INICIO/REINICIO DE PRODUÇÃO", "MANUTENÇÃO - MÁQUINA", "MANUTENÇÃO - MOLDE", "PARADA PROGRAMADA", "PROBLEMA DE REFRIGERAÇÃO",
                    "SETUP", "TROCA DE MATERIA PRIMA(COR)"
                    ),  # Opções disponíveis
            size_hint=(None, None),  # Tamanho do Spinner
            size=(250, 40),  # Dimensão do Spinner
            pos_hint={'x': 0.75, 'y': 0.83}  # Posição
        )

        layout_paradas.add_widget(self.motivo_primeira_parada) # Adiciona o Spinner ao layout
        #******************************************************************* -----------------------------------
#******************************************************************************* PRIMEIRA COLUNA

#******************************************************************************************************************** SEGUNDA COLUNA
        # Adiciona uma etiqueta
        texto_acima_da_caixa_2 = Label(text="Inicio da segunda parada:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.75})
        layout_paradas.add_widget(texto_acima_da_caixa_2)

        # Adiciona uma caixa de texto
        self.caixa_de_texto_2 = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.68})
        layout_paradas.add_widget(self.caixa_de_texto_2)

        # Adiciona uma etiqueta com a primeira pergunta
        fim_segunda_parada_texto = Label(text="Fim da segunda parada :", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.44, 'y': 0.75})
        layout_paradas.add_widget(fim_segunda_parada_texto)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.caixa_horario_segunda_parada = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.475, 'y': 0.68})
        layout_paradas.add_widget(self.caixa_horario_segunda_parada)

        # Adiciona um Spinner (caixa de seleção) para o usuário escolher entre as opções
        motivo_segunda_parada_texto = Label(text="Motivo de segunda parada da maquina:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.77, 'y': 0.75})
        layout_paradas.add_widget(motivo_segunda_parada_texto)


        # Adiciona uma caixa de texto para o usuário inserir a resposta ---------------------------------------
        self.motivo_segunda_parada = Spinner(
            text="",  # Texto padrão quando nada é 
            values=("AGUARDANDO REABASTECIMENTO", "ESPERA - MANUTENÇÃO MÁQUINA", "ESPERA - MANUTENÇÃO DE MOLDE",
                    "ESPERA - SETUP", "FALTA DE COLABORADOR", "FALTA DE ENERGIA", "FALTA DE MATERIA PRIMA", "HORÁRIO DE REFEIÇÃO",
                    "INICIO/REINICIO DE PRODUÇÃO", "MANUTENÇÃO - MÁQUINA", "MANUTENÇÃO - MOLDE", "PARADA PROGRAMADA", "PROBLEMA DE REFRIGERAÇÃO",
                    "SETUP", "TROCA DE MATERIA PRIMA(COR)"
                    ),  # Opções disponíveis
            size_hint=(None, None),  # Tamanho do Spinner
            size=(250, 40),  # Dimensão do Spinner
            pos_hint={'x': 0.75, 'y': 0.68}  # Posição
        )

        layout_paradas.add_widget(self.motivo_segunda_parada) # Adiciona o Spinner ao layout
        #******************************************************************* -----------------------------------
#******************************************************************************* SEGUNDA COLUNA

#******************************************************************************************************************** TERCEIRA COLUNA
        # Adiciona uma etiqueta
        texto_acima_da_caixa_3 = Label(text="Inicio da terceira parada:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.6})
        layout_paradas.add_widget(texto_acima_da_caixa_3)

        # Adiciona uma caixa de texto
        self.caixa_de_texto_3 = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.53})
        layout_paradas.add_widget(self.caixa_de_texto_3)

        # Adiciona uma etiqueta com a primeira pergunta
        fim_terceira_parada_texto = Label(text="Fim da terceira parada :", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.44, 'y': 0.6})
        layout_paradas.add_widget(fim_terceira_parada_texto)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.caixa_horario_terceira_parada = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.475, 'y': 0.53})
        layout_paradas.add_widget(self.caixa_horario_terceira_parada)

        # Adiciona um Spinner (caixa de seleção) para o usuário escolher entre as opções
        motivo_terceira_parada_texto = Label(text="Motivo de terceira parada da maquina:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.77, 'y': 0.6})
        layout_paradas.add_widget(motivo_terceira_parada_texto)


        # Adiciona uma caixa de texto para o usuário inserir a resposta ---------------------------------------
        self.motivo_terceira_parada = Spinner(
            text="",  # Texto padrão quando nada é 
            values=("AGUARDANDO REABASTECIMENTO", "ESPERA - MANUTENÇÃO MÁQUINA", "ESPERA - MANUTENÇÃO DE MOLDE",
                    "ESPERA - SETUP", "FALTA DE COLABORADOR", "FALTA DE ENERGIA", "FALTA DE MATERIA PRIMA", "HORÁRIO DE REFEIÇÃO",
                    "INICIO/REINICIO DE PRODUÇÃO", "MANUTENÇÃO - MÁQUINA", "MANUTENÇÃO - MOLDE", "PARADA PROGRAMADA", "PROBLEMA DE REFRIGERAÇÃO",
                    "SETUP", "TROCA DE MATERIA PRIMA(COR)"
                    ),  # Opções disponíveis
            size_hint=(None, None),  # Tamanho do Spinner
            size=(250, 40),  # Dimensão do Spinner
            pos_hint={'x': 0.75, 'y': 0.53}  # Posição
        )

        layout_paradas.add_widget(self.motivo_terceira_parada) # Adiciona o Spinner ao layout
        #******************************************************************* -----------------------------------
#******************************************************************************* TERCEIRA COLUNA


#******************************************************************************************************************** QUARTA COLUNA
        # Adiciona uma etiqueta
        texto_acima_da_caixa_4 = Label(text="Inicio da quarta parada:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.45})
        layout_paradas.add_widget(texto_acima_da_caixa_4)

        # Adiciona uma caixa de texto
        self.caixa_de_texto_4 = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.38})
        layout_paradas.add_widget(self.caixa_de_texto_4)

        # Adiciona uma etiqueta com a primeira pergunta
        fim_quarta_parada_texto = Label(text="Fim da quarta parada :", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.44, 'y': 0.45})
        layout_paradas.add_widget(fim_quarta_parada_texto)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.caixa_horario_quarta_parada = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.475, 'y': 0.38})
        layout_paradas.add_widget(self.caixa_horario_quarta_parada)

        # Adiciona um Spinner (caixa de seleção) para o usuário escolher entre as opções
        motivo_quarta_parada_texto = Label(text="Motivo de quarta parada da maquina:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.77, 'y': 0.45})
        layout_paradas.add_widget(motivo_quarta_parada_texto)


        # Adiciona uma caixa de texto para o usuário inserir a resposta ---------------------------------------
        self.motivo_quarta_parada = Spinner(
            text="",  # Texto padrão quando nada é 
            values=("AGUARDANDO REABASTECIMENTO", "ESPERA - MANUTENÇÃO MÁQUINA", "ESPERA - MANUTENÇÃO DE MOLDE",
                    "ESPERA - SETUP", "FALTA DE COLABORADOR", "FALTA DE ENERGIA", "FALTA DE MATERIA PRIMA", "HORÁRIO DE REFEIÇÃO",
                    "INICIO/REINICIO DE PRODUÇÃO", "MANUTENÇÃO - MÁQUINA", "MANUTENÇÃO - MOLDE", "PARADA PROGRAMADA", "PROBLEMA DE REFRIGERAÇÃO",
                    "SETUP", "TROCA DE MATERIA PRIMA(COR)"
                    ),  # Opções disponíveis
            size_hint=(None, None),  # Tamanho do Spinner
            size=(250, 40),  # Dimensão do Spinner
            pos_hint={'x': 0.75, 'y': 0.38}  # Posição
        )

        layout_paradas.add_widget(self.motivo_quarta_parada) # Adiciona o Spinner ao layout
        #******************************************************************* -----------------------------------


#******************************************************************************* QUINTA COLUNA

        # Adiciona uma etiqueta
        texto_acima_da_caixa_5 = Label(text="Inicio da quinta parada:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.3})
        layout_paradas.add_widget(texto_acima_da_caixa_5)

        # Adiciona uma caixa de texto
        self.caixa_de_texto_5 = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.23})
        layout_paradas.add_widget(self.caixa_de_texto_5)

        # Adiciona uma etiqueta com a primeira pergunta
        fim_quinta_parada_texto = Label(text="Fim da quinta parada :", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.44, 'y': 0.3})
        layout_paradas.add_widget(fim_quinta_parada_texto)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.caixa_horario_quinta_parada = TextInput(hint_text="Digite o horário em formato de 24h ex:15:00", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.475, 'y': 0.23})
        layout_paradas.add_widget(self.caixa_horario_quinta_parada)

        # Adiciona um Spinner (caixa de seleção) para o usuário escolher entre as opções
        motivo_quinta_parada_texto = Label(text="Motivo de quinta parada da maquina:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.77, 'y': 0.3})
        layout_paradas.add_widget(motivo_quinta_parada_texto)


        # Adiciona uma caixa de texto para o usuário inserir a resposta ---------------------------------------
        self.motivo_quinta_parada = Spinner(
            text="",  # Texto padrão quando nada é 
            values=("AGUARDANDO REABASTECIMENTO", "ESPERA - MANUTENÇÃO MÁQUINA", "ESPERA - MANUTENÇÃO DE MOLDE",
                    "ESPERA - SETUP", "FALTA DE COLABORADOR", "FALTA DE ENERGIA", "FALTA DE MATERIA PRIMA", "HORÁRIO DE REFEIÇÃO",
                    "INICIO/REINICIO DE PRODUÇÃO", "MANUTENÇÃO - MÁQUINA", "MANUTENÇÃO - MOLDE", "PARADA PROGRAMADA", "PROBLEMA DE REFRIGERAÇÃO",
                    "SETUP", "TROCA DE MATERIA PRIMA(COR)"
                    ),  # Opções disponíveis
            size_hint=(None, None),  # Tamanho do Spinner
            size=(250, 40),  # Dimensão do Spinner
            pos_hint={'x': 0.75, 'y': 0.23}  # Posição
        )

        layout_paradas.add_widget(self.motivo_quinta_parada) # Adiciona o Spinner ao layout
        #******************************************************************* -----------------------------------
#******************************************************************************* QUINTA COLUNA


        # Adiciona um botão para prosseguir para a próxima tela
        proceed_button = Button(
            text="Prosseguir", 
            size_hint=(None, None), 
            size=(200, 50), 
            pos_hint={'x': 0.475, 'y': 0.01},
            background_color=(0.3, 1, 0.3, 1), # Cor de fundo do  botão verde 
            color=(1, 1, 1, 1)  # Texto branco
        )    
        proceed_button.bind(on_press=self.go_to_next_screen)
        layout_paradas.add_widget(proceed_button)

        # Adiciona um botão para voltar para a tela anterior
        back_button_voltar = Button(text="Voltar", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.475, 'y': 0.1})
        back_button_voltar.bind(on_press=self.botao_voltar)
        layout_paradas.add_widget(back_button_voltar)


        # Adicione o layout à tela
        self.add_widget(layout_paradas) 
#*******************************************************************************************
    # Função chamada quando o botão "Prosseguir" é pressionado
    def go_to_next_screen(self, instance):
        self.manager.current = 'question2'
    # Função chamada quando o botão "Voltar" é pressionado
    def botao_voltar(self, instance):
        self.manager.current = 'question1'


#Segunda tela *****************************************************************************************************************************************
class QuestionScreen2(Screen):
    def __init__(self, **kwargs):
        super(QuestionScreen2,self).__init__(**kwargs)
        
        

        # Cria um layout FloatLayout para o conteúdo da tela, se quero que meu conteudo fique um embaixo do outro ou um do lado do outro
        layout = FloatLayout()
        #-------------------------------------------------------


        # Carregar a imagem localmente
        image_path = get_resource_path('imagem_logo.png')  # Use o caminho para a imagem com a função
        img = Image(source=image_path, 
                    size_hint=(None, None), size=(300, 300), pos_hint={'x': 0.02, 'y': 0.65})
        
        layout.add_widget(img)


    



        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite a quantidade de refugo", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.9})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto8 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'y': 0.8})
        layout.add_widget(self.answer_input_name_texto8)
        # ---------------------------------------------------------------------------------
        # Adiciona uma etiqueta com a terceira pergunta
        question_label = Label(text="Produto produzido", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.7})
        layout.add_widget(question_label)

        # Lista de itens disponíveis
        self.lista_itens = [
            "001.BICO 1/2", "001.PORCA 1/2", "001.TORN 1/2", "002.TORN 1/2 PRE",
            "01001009", "01001010", "01001015", "01007001", "01007002", "01007003",
            "01007004", "01007005", "01007006", "01007007", "01007008", "01007009",
            "01007010", "01007011", "01007012", "01007013", "01007014", "01007015",
            "01007016", "01007017", "01007018", "01007019", "01007020", "01007021",
            "01007022", "01007023", "01007024", "01007025", "01007026", "01007027",
            "01007028", "01007029", "01007030", "01007031", "01007032", "01007033",
            "01007034", "01007035", "01007036", "01007037", "01007038", "01007039",
            "01007040", "01007041", "01007042", "01007043", "01007044", "01007045",
            "01007046", "01007047", "01007048", "01007049", "01007050", "01007051",
            "01007052", "01007053", "01007054", "01007055", "01007056", "01007057",
            "01007058", "01007059", "01007060", "01007061", "01007062", "01007063",
            "01007064", "01007065", "01007066", "01007067", "01007068", "01007069",
            "01007070", "01007071", "01007072", "01007073", "01007074", "01007075",
            "01007076", "01007077", "01007078", "01007079", "01007080", "01007081",
            "01007082", "01007083", "01007084", "01007085", "01007092", "01007093",
            "01007094", "01007095", "01007096", "01007097", "01007098", "01007099",
            "01007100", "01007101", "01007102", "01007103", "01007104", "01007105",
            "01008001", "01008002", "01008003", "01008004", "01008005", "01008006",
            "01008007", "01008008", "01008009", "01008010", "01008011", "01008012",
            "01008013", "01008014", "01008015", "01008016", "01008017", "01008018",
            "01008019", "01008020", "01008021", "01008022", "01008023", "01008024",
            "01008025", "01008026", "01008027", "01008028", "01008029", "01008030",
            "20001091", "20001092", "20001093", "20001094", "A59Z-ADAPT 1/2 AZUL",
            "A60Z-ADAP 3/4 AZUL", "AD51A-ADAP 1/2 AZ", "AD51P-ADAP 1/2 PT", "AD52A-ADAP 3/4 AZ",
            "AD52P-ADAP 3/4 PT", "AD53A-ADAP 1\" AZ", "AD53P-ADAP 1\" PT", "AD54A-ADA 3/4x1/2 AZ",
            "AD54P-ADA 3/4x1/2 PT", "AD55A-ADAP 1x3/4 AZ", "AD55P-ADAP 1x3/4 PT", "AD56A-ADAP 1.1/4 AZ",
            "AD56P-ADAP 1.1/4 PT", "AD57A-ADAP 1.1/2 AZ", "AD57P-ADAP 1.1/2 PT", "AD58A-ADAP 2\" AZ",
            "AD58P-ADAP 2\" PT", "AD59P-ADAP 1/2\" PT", "AD60P-ADAP 3/4 PRETO", "ARAN1-ARANHA 3/4\"",
            "CCH4P-COPO CHUV 4\"P", "CCH7P-COPO CHUV 7\"", "CHUCBM-MONT CAB C/RE", "CHUV1M-MONT CAN/PI",
            "CONTROLADOR DE VIBRA", "CORAB-COPO RALO RED", "CORPO REG MAQ", "FITA KRAFT 48MM X 50",
            "FITA PP 45X100", "ISLC1-ISOLAD CAST AM", "ISOL CASTANHA PRETO", "JO51A-JO 1/2\" AZ",
            "JO51P-JO 1/2\" PT", "JO52A-JO 3/4\" AZ", "JO52P-JO 3/4\" PT", "JO53A-JO 1\" AZ",
            "JO53P-JO 1\" PT", "JO54A-JO 1.1/4\" AZ", "JO54P-JO 1.1/4\" PT", "JO55A-JO 1.1/2\" AZ",
            "JO55P-JO 1.1/2\" PT", "JO56A-JO 2\" AZ", "JO56P-JO 2\" PT", "JO57A-JO DP 1/2 AZ",
            "JO57P-JO DP 1/2 PT", "JO58A-JO DP 3/4 AZ", "JO58P-JO DP 3/4 PT", "JO59A-JO DP 1\" AZ",
            "JO59P-JO DP 1\" PT", "PLV5P-PORC VA 7/8 PT", "PLVR1-PRC T LAVAT PR", "REC1B-CORP R PVC 1/2",
            "REC1M-CORP R PVC 1/2", "REC2B-CORP R PVC 3/4", "REC2M-CORP R PVC 3/4", "RF1/2Z",
            "RF1Z", "RF20M", "RF20Z", "RF25M", "RF25Z", "RF3/4Z", "RF32M", "RF32Z", "RF40M", 
            "RF40Z", "RF50M", "RF50Z", "TAMPA GR TORN/RE", "TAMPA TORN COLORIDAS", 
            "TE51A-TEE 1/2 AZ", "TE51P-TEE 1/2 PT", "TE52A-TEE 3/4 AZ", "TE52P-TEE 3/4 PT", 
            "TE53A-TEE 1\" AZ", "TE53P-TEE 1\" PT", "TE54A-TEE 1.1/4\" AZ", "TE54P-TEE 1.1/4\" PT", 
            "TE55A-TEE 1.1/2\" AZ", "TE55P-TEE 1.1/2\" PT", "TE56A-TEE 2\" AZ", "TE56P-TEE 2\" PT", 
            "TE57A-TTRIP 1/2 AZ", "TE57P-TTRIP 1/2 PT", "TE58A-TTRIP 3/4 AZ", "TE58P-TTRIP 3/4 PT", 
            "TE59A-TTRIP 1\" AZ", "TE59P-TTRIP 1\" PT", "TJ1BBN-MONT TOR JDM1", "TJ1BBX-MONT TOR JDM1", 
            "TJ1PCN-MONT TOR JDM1", "TJ1PPN-MONT TOR JDM1", "TJ2BBN-MONT TOR JDM2", "TJ2PCN-MONT TOR JDM2", 
            "TJ2PPN-MONT TOR JDM2", "TLR13-TP TOR LAV-ABS", "TLR14-TP TOR LAV-ABS", "TPVAP-TAMPA VAP", 
            "TTC1RM-MONT TPB CRT1", "TTC2R-CORP TO CT 3/4", "TTC2RM-MONT TPB CRT2", "TTL1RM-MONT TOR LEN 1"
        ]
        #***************************************************************************************************


        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_texto23 = TextInput(hint_text="Digite aqui o código do produto fabricado", size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'y': 0.6})
        layout.add_widget(self.answer_input_texto23)



#*******************************************************************************************

        # Cria um DropDown para mostrar sugestões
        self.dropdown = DropDown()



        # Define a função para abrir o dropdown quando o usuário começa a digitar
        def show_dropdown(instance, text):
            self.dropdown.clear_widgets()  # Limpa os itens anteriores
            if text:  # Se há texto digitado
                # Filtra os itens que contêm o texto digitado
                filtered_items = [item for item in self.lista_itens if text.lower() in item.lower()]
                for item in filtered_items:
                    btn = Button(text=item, size_hint_y=None, height=40)
                    btn.bind(on_release=update_text)  # Atualiza o TextInput ao selecionar
                    self.dropdown.add_widget(btn)



                if filtered_items:  # Abre o dropdown se houver itens filtrados
                    if not self.dropdown.parent:  # Verifica se o dropdown não tem um pai
                        self.dropdown.open(self.answer_input_texto23)  # Abre o dropdown
                                          
            else:
                pass



        # Atualiza o TextInput com o item selecionado
        def update_text(instance):
            self.answer_input_texto23.text = instance.text  # Define o texto diretamente
            self.dropdown.dismiss()  # Fecha o dropdown após a seleção   
        self.answer_input_texto23.bind(text=show_dropdown)

#*****************************************************************
        # Adiciona uma etiqueta com a terceira pergunta
        question_label = Label(text="Quatidade produzida", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.5})
        layout.add_widget(question_label)
        
        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_texto24 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'y': 0.4})
        layout.add_widget(self.answer_input_texto24)



       
        # Adiciona um botão para prosseguir para a próxima tela (ou voltar para a tela anterior)
        proceed_button = Button(text="Finalizar", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.1})
        proceed_button.bind(on_press=self.go_to_next_screen)
        layout.add_widget(proceed_button)
        
        # Adiciona um botão para voltar para a tela anterior
        back_button = Button(text="Voltar", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.2})
        back_button.bind(on_press=self.go_to_previous_screen)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
#*******************************************************************************************************************************************



#*******************************************************************************************************************************************  
#   # Função chamada quando o botão paradas de maquinas é pressionado


    # Função chamada quando o botão "Prosseguir" é pressionado
    def go_to_next_screen(self, instance):

        screen1 = self.manager.get_screen('question1') # Nome do operador pagina 1

        screenturno = self.manager.get_screen('question1') # Turno pagina 1

        screenmaquina = self.manager.get_screen('question1') # Maquina pagina 1

        screen_data = self.manager.get_screen('question1') # Data da inspeção pagina 1
        #---------------------------------------------------------------------        
        screen_ciclo2 = self.manager.get_screen('question2') # Quantidade de refugo ultima pagina

        screen_produto_produzido = self.manager.get_screen('question2') # Código do produto ultima pagina

        screen_quatidade_produzida = self.manager.get_screen('question2') # Quantidade produzida ultima pagina
        #***********************************

        #----------------------------- Primeira linha das paradas
        parte_1H_parada = self.manager.get_screen('question3') # hora primeira parada pagina 3
        parte_fim_1H_parada = self.manager.get_screen('question3') # hora fim primeira parada pagina 3
        parte_motivo_1_parada = self.manager.get_screen('question3') # motivo primeira parada pagina 3
        #---------------------------------------------------------------------
        #----------------------------- Segunda linha das paradas
        parte_2H_parada = self.manager.get_screen('question3') # hora segunda parada pagina 3
        parte_fim_2H_parada = self.manager.get_screen('question3') # hora fim segunda parada pagina 3
        parte_motivo_2_parada = self.manager.get_screen('question3') # motivo segunda parada pagina 3
        #---------------------------------------------------------------------

        #----------------------------- terceira linha das paradas
        parte_3H_parada = self.manager.get_screen('question3') # hora terceira parada pagina 3
        parte_fim_3H_parada = self.manager.get_screen('question3') # hora fim terceira parada pagina 3
        parte_motivo_3_parada = self.manager.get_screen('question3') # motivo terceira parada pagina 3
        #---------------------------------------------------------------------

        #----------------------------- quarta linha das paradas
        parte_4H_parada = self.manager.get_screen('question3') # hora quarta parada pagina 3
        parte_fim_4H_parada = self.manager.get_screen('question3') # hora fim quarta parada pagina 3
        parte_motivo_4_parada = self.manager.get_screen('question3') # motivo quarta parada pagina 3
        #---------------------------------------------------------------------


        #----------------------------- quinta linha das paradas
        parte_5H_parada = self.manager.get_screen('question3') # hora quinta parada pagina 3
        parte_fim_5H_parada = self.manager.get_screen('question3') # hora fim quinta parada pagina 3
        parte_motivo_5_parada = self.manager.get_screen('question3') # motivo quinta parada pagina 3
        #---------------------------------------------------------------------



        # Coletando os textos pagina de paradas  *******************************************************
        #----------------------------- Primeira linha das paradas
        inicio_primeira_parada = parte_1H_parada.caixa_de_texto_1.text # hora primeira parada pagina 3
        fim_primeira_parada = parte_fim_1H_parada.caixa_horario_primeira_parada.text # hora fim primeira parada pagina 3
        motivo_primeira_parada = parte_motivo_1_parada.motivo_primeira_parada.text # motivo primeira parada pagina 3
        #---------------------------------------------------------------------

        #----------------------------- Segunda linha das paradas
        inicio_segunda_parada = parte_2H_parada.caixa_de_texto_2.text # hora segunda parada pagina 3
        fim_segunda_parada = parte_fim_2H_parada.caixa_horario_segunda_parada.text # hora fim segunda parada pagina 3
        motivo_segunda_parada = parte_motivo_2_parada.motivo_segunda_parada.text # motivo segunda parada pagina 3
        #---------------------------------------------------------------------

        #----------------------------- Terceira linha das paradas
        inicio_terceira_parada = parte_3H_parada.caixa_de_texto_3.text # hora terceira parada pagina 3
        fim_terceira_parada = parte_fim_3H_parada.caixa_horario_terceira_parada.text # hora fim terceira parada pagina 3
        motivo_terceira_parada = parte_motivo_3_parada.motivo_terceira_parada.text # motivo terceira parada pagina 3
        #---------------------------------------------------------------------

        #----------------------------- Quarta linha das paradas
        inicio_quarta_parada = parte_4H_parada.caixa_de_texto_4.text # hora quarta parada pagina 3
        fim_quarta_parada = parte_fim_4H_parada.caixa_horario_quarta_parada.text # hora fim quarta parada pagina 3
        motivo_quarta_parada = parte_motivo_4_parada.motivo_quarta_parada.text # motivo quarta parada pagina 3
        #---------------------------------------------------------------------

        #----------------------------- Quinta linha das paradas
        inicio_quinta_parada = parte_5H_parada.caixa_de_texto_5.text # hora quinta parada pagina 3
        fim_quinta_parada = parte_fim_5H_parada.caixa_horario_quinta_parada.text # hora fim quinta parada pagina 3
        motivo_quinta_parada = parte_motivo_5_parada.motivo_quinta_parada.text # motivo quinta parada pagina 3
        #---------------------------------------------------------------------
        #*******************************************************************************Coletando os textos pagina de paradas




        nome_do_operador = screen1.answer_input_name_texto1.text # Nome do operador pagina 1

        turno = screenturno.answer_input_machine_texto2.text # Turno pagina 1
        
        maquina = screenmaquina.answer_input_machine_texto3.text

        data_da_inspecao = screen_data.answer_input_date_minha_data.text # Data da inspeção pagina 1
        
        quantidade_refugo = screen_ciclo2.answer_input_name_texto8.text # Quantidade de refugo ultima pagina

        produto_produzido = screen_produto_produzido.answer_input_texto23.text # Código do produto ultima pagina
        
        quantidade_produzida = screen_quatidade_produzida.answer_input_texto24.text # Quantidade produzida ultima pagina



        # Adicionando o Popup de confirmação
        # Criar o layout do Popup
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Deseja salvar os dados?")
        btn_sim = Button(text="Sim", size_hint_y=None, height=50)
        btn_nao = Button(text="Não", size_hint_y=None, height=50)

        layout.add_widget(label)
        layout.add_widget(btn_sim)
        layout.add_widget(btn_nao)

        popup = Popup(title='Confirmação',
                      content=layout,
                      size_hint=(0.75, 0.5))

        # Função para salvar os dados e reiniciar a aplicação
        def salvar_e_reiniciar(instance):
            
            # Chama a função de salvar dados
            save_to_db(nome_do_operador,data_da_inspecao,turno,maquina,inicio_primeira_parada,fim_primeira_parada,motivo_primeira_parada,
                       inicio_segunda_parada,fim_segunda_parada,motivo_segunda_parada,inicio_terceira_parada,fim_terceira_parada,
                       motivo_terceira_parada,inicio_quarta_parada,fim_quarta_parada,motivo_quarta_parada,inicio_quinta_parada,fim_quinta_parada,
                       motivo_quinta_parada,quantidade_refugo,produto_produzido,quantidade_produzida)
            



            # Chama a função para atualizar o tempo de parada
            
            


                
                # Limpar os campos de entrada

            parte_1H_parada.caixa_de_texto_1.text = '' # hora primeira parada pagina 3
            parte_fim_1H_parada.caixa_horario_primeira_parada.text = '' # hora fim primeira parada pagina 3
            parte_motivo_1_parada.motivo_primeira_parada.text = '' # motivo primeira parada pagina 3
        #---------------------------------------------------------------------

            #----------------------------- Segunda linha das paradas
            parte_2H_parada.caixa_de_texto_2.text = '' # hora segunda parada pagina 3
            parte_fim_2H_parada.caixa_horario_segunda_parada.text = '' # hora fim segunda parada pagina 3
            parte_motivo_2_parada.motivo_segunda_parada.text = '' # motivo segunda parada pagina 3
            #---------------------------------------------------------------------

            #----------------------------- Terceira linha das paradas
            parte_3H_parada.caixa_de_texto_3.text = '' # hora terceira parada pagina 3
            parte_fim_3H_parada.caixa_horario_terceira_parada.text = '' # hora fim terceira parada pagina 3
            parte_motivo_3_parada.motivo_terceira_parada.text = '' # motivo terceira parada pagina 3
            #---------------------------------------------------------------------

            #----------------------------- Quarta linha das paradas
            parte_4H_parada.caixa_de_texto_4.text = '' # hora quarta parada pagina 3
            parte_fim_4H_parada.caixa_horario_quarta_parada.text = '' # hora fim quarta parada pagina 3
            parte_motivo_4_parada.motivo_quarta_parada.text = '' # motivo quarta parada pagina 3
            #---------------------------------------------------------------------

            #----------------------------- Quinta linha das paradas
            parte_5H_parada.caixa_de_texto_5.text = '' # hora quinta parada pagina 3
            parte_fim_5H_parada.caixa_horario_quinta_parada.text = '' # hora fim quinta parada pagina 3
            parte_motivo_5_parada.motivo_quinta_parada.text = '' # motivo quinta parada pagina 3
            #---------------------------------------------------------------------
            #*******************************************************************************Coletando os textos pagina de paradas




            parte_1H_parada.caixa_de_texto_1.text = '' # hora primeira parada pagina 3

            screen1.answer_input_name_texto1.text = '' # Nome do operador pagina 1

            screenturno.answer_input_machine_texto2.text = '' # Turno pagina 1

            screenmaquina.answer_input_machine_texto3.text = '' # Maquina pagina 1

            screen_ciclo2.answer_input_name_texto8.text = '' # Quantidade de refugo ultima pagina

            screen_produto_produzido.answer_input_texto23.text = '' # Código do produto ultima pagina

            screen_quatidade_produzida.answer_input_texto24.text = '' # Quantidade produzida ultima pagina
            #--------------------------------------------------------------------------------------

            popup.dismiss()

            # Reiniciar o app voltando para a primeira tela
            self.manager.current = 'question1'


        # Função para apenas fechar o popup
        def nao_fazer_nada(instance):
            popup.dismiss()

        # Conectar os botões às funções
        btn_sim.bind(on_press=salvar_e_reiniciar)
        btn_nao.bind(on_press=nao_fazer_nada)

        # Exibir o popup
        popup.open()

        
    
    # Função chamada quando o botão "Voltar" é pressionado
    def go_to_previous_screen(self, instance):
        self.manager.current = 'question1'

class Qualidade(App):
    def build(self):
        sm = ScreenManager()
        # Adiciona as três telas ao gerenciador de telas
        sm.add_widget(QuestionScreen1(name='question1'))
        sm.add_widget(QuestionScreen2(name='question2'))
        sm.add_widget(pagina_paradas_maquina(name='question3'))
        
             
        return sm
    
    
    
if __name__ == "__main__":
    Qualidade().run()



