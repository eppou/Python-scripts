import requests
from bs4 import BeautifulSoup

# URL do site com informações desejada
url = 'https://qualquercoisa.com'

# Realizar a solicitação GET para obter o conteúdo da página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analisar o conteúdo da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todas as divs com a classe
    divs_armas = soup.find_all('div', class_='nome da classe da div desejada')

    # Iterar sobre as divs das armas
    for div_arma in divs_armas:
        # um das possibilidades e pegar o nome daquela informação desejada logo apos o uma tag como é o caso de <br>
        br_tag = div_arma.find('br')

        # Se a tag <br> for encontrada, obter o nome da arma
        if br_tag:
            nome_arma = br_tag.nextSibling.strip()
            print(f'Nome da arma: {nome_arma}')

        # outra possibilidade é pegar  a informação contida dentro de uma marcação como <h2> por exemplo
            nome = nome_arma.find('h2').text

        # Imprimir uma linha em branco entre as informações das armas
        print()

else:
    print('Falha ao acessar o site')

