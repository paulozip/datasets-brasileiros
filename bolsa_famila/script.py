from bs4 import BeautifulSoup
import requests

#retire o comentário para configurar seu proxy e adicione o parametro de proxy nas funções requests
#proxy = {'http': 'http://user:pass@proxy:3128'}

soup = BeautifulSoup(open('site.html', 'r'), 'html.parser')
exercicios_elemento = soup.find(class_='exercicios')

#criar uma lista com os meses é mais eficiente que criar laços para cada mes disponível em um range
meses = ['01', '02', '03', '04', '05', '06',
         '07', '08', '09', '10', '11', '12']
#coletando anos dos exercicios
for ano in exercicios_elemento:
    ano = ano.text
    for mes in meses:
        print('Baixando arquivo de {}/{}'.format(mes, ano))
        #iniciando a sessão com o requests
        session = requests.Session()
        r = session.get('http://arquivos.portaldatransparencia.gov.br/downloads.asp?a={}&m={}&consulta=BolsaFamiliaFolhaPagamento'.format(ano,mes))

        #creating dataset
        with open('{}{}_BolsaFamiliaFolhaPagamento.zip'.format(ano, mes), 'wb') as file:
            file.write(r.content)
            print('Arquivo {}{}_BolsaFamiliaFolhaPagamento.zip baixado com sucesso.'.format(ano, mes))
