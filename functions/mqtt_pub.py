import sys
import paho.mqtt.client as mqtt

# Configura i dettagli del broker
broker_address = "192.168.1.15"
port = 1883


def on_connect(client, userdata, flags, rc):
    print("Risultato di connessione:  "+str(rc))


def message_handling(client, userdata, msg):
    print(f"Topic: {msg.topic} | Messaggio: {msg.payload.decode()}")


# Funzione per pubblicare un messaggio su una Subscription
def send_message(broker_address, port, topic, message, client_id):
    print("Funzione: sendMessage")

    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1, client_id=client_id)
    client.on_connect = on_connect

    # Connessione all'MQTT broker
    try:
        if client.connect(broker_address, port, 60) != 0:
            raise Exception("Connessione all'MQTT broker non riuscita")

        # Pubblicazione messaggio nel Topic scelto e disconnessione
        client.publish(topic, message, 0)
        client.disconnect()

    # Gestione errore di connessione
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    finally:
        print("Disconnessione dall'MQTT broker")
        client.disconnect()
