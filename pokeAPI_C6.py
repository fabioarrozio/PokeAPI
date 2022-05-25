import requests
import csv


def main():
    list_poke()
    if response.status_code == 200:
        poke = response.json()
        if poke['id'] <= 10:
            get_abilities(poke)
            get_types(poke)
        else:
            print('Pokémon não encontrado em sua Pokédex.')
    else:
        print(response.status_code, 'Pokemon não existe')


def list_poke():  # busca o nome dos pokémons e seus atributos
    global pokemon
    global response
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10')
    poke = response.json()
    print(10*'=','Pokédex v0.1',10*'=')
    for index in poke['results']:
        print(index['name'])
    pokemon = str(input('Digite o nome de seu pokémon: '))
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    get_csv()


def get_csv():  # escreve os resultados do pokemon pesquisado no arquivo.csv
    create = csv.writer(open('pokeapi.csv', 'a'), lineterminator='\n')
    if response.status_code == 200:
        poke = response.json()

        if poke['id'] <= 10:
            create.writerow('Nome'.split())
            for item in poke['forms']:
                create.writerow(item['name'].split())

            create.writerow('Habilidades'.split())
            for item in poke['abilities']:
                create.writerow([item['ability']['name']])

            create.writerow('Tipo'.split())
            for item in poke['types']:
                create.writerow([item['type']['name']])
        else:
            pass

def get_abilities(poke):  # busca as habilidades
    print(f'\033[1;34mHabilidades de {pokemon}\033[0;0m')
    for index in poke['abilities']:
        print('    ', index['ability']['name'])

def get_types(poke):  # busca os tipos
    print(f'\033[1;34mTipo do pokemon\033[0;0m')
    for index in poke['types']:
        print('    ', index['type']['name'])


if __name__ == '__main__':
    resp = ''
    while resp != 'n':
        main()
        resp = input('nova pesquisa? (s | n): ')
    print('Pokédex finalizada!')