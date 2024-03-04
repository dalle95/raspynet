# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import threading
import sys

from decouple import config

from functions import mqtt_sub # Funzione per creare la Subscription
from functions import mqtt_pub # Funzione per pubblicare i messaggi

sys.path.insert(0, './functions')  # Aggiungi il percorso della sottodirectory al sys.path


def start(address, port, topic):
    # Impostazione Subscription tramite thread per rendere la funzione asincrona
    creaSubscription = threading.Thread(target=mqtt_sub.setSubscription, args=(address, port, topic))

    # Avvio del thread
    creaSubscription.start()
    # Attesa di 1 secondo per la connessione all'MQTT broker
    time.sleep(1)

    # Definizione Messaggio
    message = "Messaggio 1"
    # Pubblicazione messaggio
    mqtt_pub.sendMessage(address, port, topic, message)
    # Definizione Messaggio
    message = "Messaggio 2"
    # Pubblicazione messaggio
    mqtt_pub.sendMessage(address, port, topic, message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Lettura variabile ambiente relativa all'indirizzo del RaspyMaster
    address = config('MQTT_BROKER_ADDRESS', default='192.168.1.15')
    # Lettura variabile ambiente relativa alla porta
    port = config('MQTT_BROKER_PORT', default=1883, cast=int)

    # Definizione Topic
    topic = "test_topic"

    start(address,port,topic)

