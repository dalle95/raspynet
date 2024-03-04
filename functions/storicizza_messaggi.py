import json
from datetime import datetime


def scrivi_su_file(nome_file, riga):
    path = "./data/{}".format(nome_file)
    try:
        with open(path, 'a') as file:
            file.write(riga + '\n')  # Aggiungi una riga
        print(f'Il dato è stato aggiunto con successo su {nome_file}')
    except Exception as e:
        print(f'Errore durante la scrittura su {nome_file}: {e}')


def salva(message):

    dati_json = json.loads(message)

    client = dati_json["client"]
    sensore = dati_json["sensore"]
    valore = dati_json["valore"]

    if sensore == 'Temperatura':
        nome_file = "temperatura.txt"
    elif sensore == 'Umidità':
        nome_file = "umidità.txt"
    elif sensore == 'Luminosità':
        nome_file = "luminosità.txt"
    else:
        nome_file = "vario.txt"

    formatted_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = "{}|{}|{}".format(client, valore, formatted_now)

    scrivi_su_file(nome_file, record)
