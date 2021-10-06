import json
from tkinter import font
import PySimpleGUI as sg
import requests
from PySimpleGUI.PySimpleGUI import In, InputText, Listbox, Submit

sg.theme('DarkTanBlue')

dados = ['cep', 'logradouro', 'bairro', 'localidade', 'uf', 'ibge', 'ddd', 'siafi']

insert_column = [
    [
        sg.Text('Informe o CEP:'),
        sg.InputText(key='input_cep',text_color="black", enable_events=True,background_color="white", size=(10,1)),
        sg.Submit("Buscar", size=(5,1), button_color=("black","grey")),
    ],
    [
            sg.Text('', key='alert_tam', text_color='red'),
    ],
    [
        sg.Text('\nCEP: '),sg.Text('', key='cep'),
    ],
    [
        sg.Text('Logradouro: '),sg.Text('', key='logradouro'),
    ],
    [
        sg.Text('Bairro: '),sg.Text('', key='bairro'),
    ],
    [
        sg.Text('Localidade: '),sg.Text('', key='localidade'),
    ],
    [
        sg.Text('UF: '),sg.Text('', key='uf'),
    ],
    [
        sg.Text('IBGE: '),sg.Text('', key='ibge'),
    ],
    [
        sg.Text('DDD: '),sg.Text('', key='ddd'),
    ],
    [
        sg.Text('SIAFI: '),sg.Text('', key='siafi'),
    ],
    
]

def adquirir_Endereco(cep):
    print(cep)
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.request('GET', url)
    conteudo = resposta.content.decode('utf-8')
    resposta.close()
    endereco = json.loads(conteudo)
    try:
        for addr in dados:
            window.Element(addr).Update(endereco[addr], text_color='lime')
    except:
        window.Element('alert_tam').Update('CEP Invalido')

def validar_cep(cep):
    if len(cep) == 8:
        return True
    else:
        window.Element('alert_tam').Update('São 8 dígitos!')
        return False

def refresh():
        window.Element('input_cep').Update(values['input_cep'][:-8])
        window.Element('alert_tam').Update('')
        for addr in dados:
            window.Element(addr).Update('')

def corrigir_input(entrada):
    if len(entrada) > 0:
        if entrada[-1] not in ('0123456789.') or len(entrada)> 8:
            window.Element('input_cep').Update(values['input_cep'][:-1])


#Create the window
window = sg.Window("buscador de cep".title(), insert_column, font=("Verdana", 12))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    corrigir_input(values['input_cep'])
    if event == "Buscar" and validar_cep(values['input_cep']):
        refresh()
        adquirir_Endereco(values['input_cep'])

window.close()