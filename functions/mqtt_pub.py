import sys
import paho.mqtt.client as mqtt

# Configura i dettagli del broker
broker_address = "192.168.1.15"
port = 1883


def on_connect(client, userdata, flags, rc):
    print("Risultato di connessione:  "+str(rc))


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect

try:
    if client.connect(broker_address, port, 60) != 0:
        raise Exception("Connessione all'MQTT broker non riuscita")

    client.publish("test_topic", "Ciao da connessione MQTT!", 0)
    client.disconnect()

except Exception as e:
    print(f"Errore: {e}")
    sys.exit(1)


