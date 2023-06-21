import requests
from kivy.app import App
from kivy.uix.label import Label

class MoedaApp(App):
    def build(self):
        # Obter os dados de cotação da API
        url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,JPY-BRL,GBP-BRL,AUD-BRL,CAD-BRL,CHF-BRL,HKD-BRL,SEK-BRL,NZD-BRL'
        response = requests.get(url)
        data = response.json()

        # Criar o texto para exibir as cotações
        moedas = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'HKD', 'SEK', 'NZD']
        nomes = ['Dólar americano', 'Euro', 'Iene japonês', 'Libra esterlina', 'Dólar australiano', 'Dólar canadense', 'Franco suíço', 'Dólar de Hong Kong', 'Coroa sueca', 'Dólar neozelandês']
        texto = ''
        for moeda, nome in zip(moedas, nomes):
            cotacao = float(data[f'{moeda}BRL']['bid'])
            texto += f'{nome} = R$ {cotacao:.2f}\n'

        # Criar um rótulo para exibir as cotações
        label = Label(text=texto)

        return label

if __name__ == '__main__':
    MoedaApp().run()
