import sys
import paho.mqtt.client as mqtt

# Configura i dettagli del broker
broker_address = "192.168.1.15"
port = 1883
message = "Test connessione"
topic = "test_topic"


def on_connect(client, userdata, flags, rc):
    print("Risultato di connessione:  " + str(rc))


# Funzione per pubblicare un messaggio su una Subscription
def sendMessage(broker_address, port, topic, message):
    print("Funzione: sendMessage")


    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
    client.on_connect = on_connect

    # Connessione all'MQTT broker
    try:
        if client.connect(broker_address, port, 60) != 0:
            raise Exception("Connessione all'MQTT broker non riuscita")

        # Pubblicazione messaggio nel Topic scelto e disconnessione
        client.publish(topic, message, 0)
        client.disconnect()

    # Gestione errori
    except Exception as e:
        print(f"Errore: {e}")
        sys.exit(1)
