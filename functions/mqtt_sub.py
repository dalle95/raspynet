import sys

import paho.mqtt.client as mqtt


def message_handling(client, userdata, msg):
    print(f"Topic: {msg.topic} | Messaggio: {msg.payload.decode()}")


def on_connect(client, userdata, flags, rc):
    print("Connesso all'MQTT broker con risultato: " + str(rc))


# Funzione per creare una Subscription
def setSubscription(broker_address, port, topic):

    print("Funzione: setSubscription")

    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
    client.on_connect = on_connect
    client.on_message = message_handling

    # Connessione all'MQTT broker
    try:
        if client.connect(broker_address, port, 60) != 0:
            raise Exception("Connessione all'MQTT broker non riuscita")

        # Attivazione Subscription
        client.subscribe(topic)

    # Gestione errore di connessione
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Gestione Loop infinito di ascolto e disconnessione
    try:
        print("Press CTRL+C to exit...")
        client.loop_forever()
    except Exception:
        print("Caught an Exception, something went wrong...")
    finally:
        print("Disconnessione dall'MQTT broker")
        client.disconnect()
