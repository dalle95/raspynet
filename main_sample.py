# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import threading
import sys

from decouple import config

import json

from functions import mqtt_sub  # Funzione per creare la Subscription
from functions import mqtt_pub  # Funzione per pubblicare i messaggi
from functions import storicizza_messaggi

sys.path.insert(0, './functions')  # Aggiungi il percorso della sottodirectory al sys.path


def start(address, port, topic, client_id):
    # Impostazione Subscription tramite thread per rendere la funzione asincrona
    crea_subscription = threading.Thread(target=mqtt_sub.set_subscription, args=(address, port, topic, client_id))

    # Avvio del thread
    crea_subscription.start()
    # Attesa di 1 secondo per la connessione all'MQTT broker
    time.sleep(1)

    # Definizione Messaggio
    json_message = {
        "client": "TEST-1",
        "sensore": "Temperatura",
        "valore": 20
    }

    # Serializza il JSON in una stringa
    message_string = json.dumps(json_message)

    # Pubblicazione messaggio
    mqtt_pub.send_message(address, port, topic, message_string, "test")

    # Definizione Messaggio
    json_message = {
        "client": "TEST-2",
        "sensore": "Umidità",
        "valore": 20
    }

    # Serializza il JSON in una stringa
    message_string = json.dumps(json_message)

    # Pubblicazione messaggio
    mqtt_pub.send_message(address, port, topic, message_string, "test2")


# Funzione per gestire i messaggi della subscription
def estrazione_messaggi(message):
    storicizza_messaggi.salva(message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Lettura variabile ambiente relativa all'indirizzo del RaspyMaster
    address = config('MQTT_BROKER_ADDRESS', default='192.168.1.15')
    # Lettura variabile ambiente relativa alla porta
    port = config('MQTT_BROKER_PORT', default=1883, cast=int)

    # Definizione Topic
    topic = "PICOS"

    client_id = "RASPY-ZERO"

    start(address, port, topic, client_id)
