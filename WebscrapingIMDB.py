from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


html = urlopen("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
bs = BeautifulSoup(html, 'html.parser')

#dados = bs.find_all('tbody', {'class':'lister-list'})
dados = bs.find_all("td", {'class':'titleColumn'})
rating = bs.find_all("td", {"class": "ratingColumn imdbRating"})


titulos, anos, notas = [], [], []

for dado in dados:
  titulo = dado.findChildren("a")
  titulos.append(titulo[0].text)
  ano = dado.findChildren("span", {"class": "secondaryInfo"})
  anos.append(ano[0].text)

for nota in rating:
  avaliacao = nota.findChildren("strong")
  notas.append(avaliacao[0].text)
#print (notas)




df = pd.DataFrame({"Filme": titulos, "Ano": anos, "Notas": notas})
print(df)

#ratingColumn imdbRating