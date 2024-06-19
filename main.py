import os
from datetime import datetime
import subprocess
import sistema_temporada

def saberdia(dataanime):

    datacomeco = datetime.strptime(dataanime, '%d/%m/%Y')
    dianumero = datacomeco.weekday()
    return dianumero


def criarlista(anim):
    anim["DiaNome"] = numerodias[anim["Dia"]]
    listadias[anim["DiaNome"]].append(anim)


def ordenar():
    for nd in range(0, 7):
        if listadias[numerodias[nd]] != []:
            with open("animes.txt", 'a') as arquivo:
                arquivo.write(f"----------------------- {numerodias[nd]} -----------------------" + '\n' + '\n')
            for animacao in listadias[numerodias[nd]]:
                for elemento in animacao:
                    if elemento == "Nome":
                        with open("animes.txt", 'a') as arquivo:
                            arquivo.write(f"{animacao[elemento]} - ")
                    elif elemento == "Data":
                        with open("animes.txt", 'a') as arquivo:
                            arquivo.write(animacao[elemento][:5] + '\n' + '\n')


numerodias = {
    0: "segunda",
    1: "terca",
    2: "quarta",
    3: "quinta",
    4: "sexta",
    5: "sabado",
    6: "domingo"}

listadias = {
    "segunda": [],
    "terca": [],
    "quarta": [],
    "quinta": [],
    "sexta": [],
    "sabado": [],
    "domingo": [],
}

if os.path.exists("animes.txt"):
    os.remove("animes.txt")

sistema_temporada.exibir_e_selecionar_animes(-1)
if os.path.exists('animes_da_temporada.txt'):
  subprocess.Popen(['xdg-open', 'animes_da_temporada.txt'])
print()
while True:
    anime = {
    "Nome": "",
    "Data": "",
    "Dia": "",
}
    numero_anime = int(input("Escolha um anime (Digite 0 para sair): "))
    if numero_anime != 0:
      anime["Nome"], anime["Data"] = sistema_temporada.exibir_e_selecionar_animes(numero_anime)
      anime["Dia"] = saberdia(anime["Data"])
      criarlista(anime)

    if numero_anime == 0:
      if os.path.exists("animes_da_temporada.txt"):
        subprocess.run(["pkill", "xed"])
        os.remove("animes_da_temporada.txt")
      print()
      with open("animes.txt", "w") as arquivo:
          arquivo.write("Meus Animes da Temporada\n" + "\n")
      ordenar()
      with open("animes.txt", "r") as arquivo:
          abrir = arquivo.read()
          print(abrir)
      break
