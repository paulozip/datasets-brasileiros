from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.letras.mus.br/mais-acessadas/sertanejo/#Sempre'
s = requests.Session()
request = s.get(url)

soup = BeautifulSoup(request.text, 'html.parser')

musicas = list()
lista_de_musicas = soup.find(class_='top-list_mus cnt-list--col1-3')

conta = 0

for musica in lista_de_musicas.find_all('li'):
    
    letra_dict = dict()
    url_site = 'https://www.letras.mus.br'
    letra_completa = list()

    #Adicionando nome da música e cantor ao dicionário
    letra_dict['Música'] = musica.find('b').text
    letra_dict['Interprete'] = musica.find('span').text
    #Localizando link da música
    link_para_letra = musica.find('a')['href']

    #Acessando página da letra da música
    letra = s.get(url_site + link_para_letra)
    soup = BeautifulSoup(letra.text, 'html.parser')
    
    paragrafos = soup.find('article')
    letra_completa = str(paragrafos).replace('<p>','').replace('<article>','').replace('</article>','').replace('</p>','').rstrip().split('<br/>')
    letra_dict['Letra'] = letra_completa
    
    musicas.append(letra_dict)

with open('sertanejo.csv', 'w', encoding='latin1') as arquivo:
    writer = csv.DictWriter(arquivo, fieldnames=['Música', 'Interprete', 'Letra'], delimiter=';')
    writer.writeheader()
    writer.writerows(musicas)