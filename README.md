## Progetto RaspyNet
# Introduzione
Questo progetto ha l'obiettivo di facilitare la comunicazione tra Raspberry Pi Pico W, agendo come slave, e un Raspberry Pi, funzionante come un datacenter centrale. La comunicazione sarà gestita attraverso il protocollo MQTT. Il Raspberry Pi datacenter avrà anche la capacità di interfacciarsi con un database Firebase per archiviare i dati provenienti dai Raspberry Pi Pico W.

# Requisiti
- Raspberry Pi Pico W (slave)
- Raspberry Pi (datacenter/master)
- Ambiente di sviluppo Python
- Broker MQTT installato su Raspberry Pi (es. Mosquitto)
- Accesso a un database Firebase
# Setup Iniziale
- Collegare i Raspberry Pi Pico W alla rete elettrica e al Raspberry Pi datacenter.
- Installare il broker MQTT (es. Mosquitto) sul Raspberry Pi datacenter.
# Configurazione del Progetto
- Clonare il repository del progetto sul Raspberry Pi datacenter e sui Raspberry Pi Pico W.

    ```bash
    git clone <url_del_repository>
    ```
- Configurare il file .env con le informazioni necessarie, come indirizzo del broker MQTT e credenziali del database Firebase.

    ```env
    MQTT_BROKER_ADDRESS=indirizzo_del_broker_mqtt
    FIREBASE_API_KEY=chiave_api_firebase
    FIREBASE_AUTH_DOMAIN=dominio_auth_firebase
    FIREBASE_DATABASE_URL=url_database_firebase
    ```
# Installare le dipendenze del progetto.

```bash
pip install -r requirements.txt
```
# Utilizzo del Progetto
### Raspberry Pi Pico W (Slave)
- Eseguire lo script `raspy_slave.py` sui Raspberry Pi Pico W.

```bash
python raspy_slave.py
```
Questo script pubblicherà i dati rilevati dal Raspberry Pi Pico W al topic MQTT specificato.

### Raspberry Pi (Datacenter/Master)
- Eseguire lo script `raspy_master.py` sul Raspberry Pi datacenter.

```bash
python raspy_master.py
```
Questo script si sottoscriverà al topic MQTT specificato per ricevere i dati dai Raspberry Pi Pico W e li invierà al database Firebase per l'archiviazione.

# Contribuire
Se desideri contribuire a questo progetto, sentiti libero di aprire una richiesta di pull o segnalare eventuali problemi nell'area delle issue.

# Licenza
Questo progetto è concesso in licenza con la Licenza MIT - vedere il file LICENSE per i dettagli.

# Note
Non tutto quello che è scritto in questo file è corretto, l'ho generato con ChatGPT per dare un'idea, spero sia utile.