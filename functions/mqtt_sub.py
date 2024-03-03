import sys

import paho.mqtt.client as mqtt


def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


# Configura i dettagli del broker
broker_address = "192.168.1.15"
port = 1883

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = message_handling

try:
    if client.connect(broker_address, port, 60) != 0:
        raise Exception("Connessione all'MQTT broker non riuscita")

    client.subscribe("test_topic")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnessione dall'MQTT broker")
    client.disconnect()
