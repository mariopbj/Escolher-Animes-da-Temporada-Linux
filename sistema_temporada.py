from urllib import request
import re

with open('animes_da_temporada.txt', 'w') as arquivo:
    arquivo.write('Animes da Temporada\n\n')

meses_nome_para_numero = {
  "Jan": "01",
  "Feb": "02",
  "Mar": "03",
  "Apr": "04",
  "May": "05",
  "Jun": "06",
  "Jul": "07",
  "Aug": "08",
  "Sep": "09",
  "Oct": "10",
  "Nov": "11",
  "Dec": "12"
}

url = 'https://myanimelist.net/anime/season'
abrir_url = request.urlopen(url)
html = abrir_url.read().decode('utf-8')
html_animes_antes_continuing = re.search(r'(?s)(.*)<div class="anime-header">TV \(Continuing\)</div>', html).group(1)
urls_animes = re.findall(r'https://myanimelist\.net/anime/\d+/\S+', html_animes_antes_continuing)

def exibir_e_selecionar_animes(num_anime):
  c = 0
  ultimo_anime = ""

  for url_encontrada in urls_animes:
    if "/video" not in url_encontrada and "><img" not in url_encontrada:
      if ultimo_anime != url_encontrada:
        c += 1
        if num_anime == -1:
          with open('animes_da_temporada.txt', 'a') as arquivo:
            arquivo.write(f"[{c}]{url_encontrada[36:][:-1]}\n")
        if c == num_anime:
          return url_encontrada[36:][:-1].replace("_"," ") , exibir_datas_desejadas(url_encontrada)
        ultimo_anime = url_encontrada


def exibir_datas_desejadas(url_desejada):
    pagina_anime = request.urlopen(url_desejada)
    html_anime = pagina_anime.read().decode('utf-8')
    datas_animes = re.findall(r'Aired:</span>\s*(.*?)\s*</div>', html_anime)

    ano = datas_animes[0].split(",")[1][1:5]
    mes = meses_nome_para_numero[(datas_animes[0].split(" ")[0])]
    dia = (datas_animes[0].split(" ")[1][:-1])
    if len(dia) == 1:
      dia = f"0{dia}"
    data = f"{dia}/{mes}/{ano}"

    return data
