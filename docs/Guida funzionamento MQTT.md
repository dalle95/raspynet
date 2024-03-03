# Guida al Testing del Progetto MQTT

## Descrizione del Progetto

Il progetto consiste in due script Python:
- `sub_mqtt.py`: Responsabile della sottoscrizione a un topic MQTT e della visualizzazione dei messaggi ricevuti.
- `pub_mqtt.py`: Responsabile della pubblicazione di messaggi su un topic MQTT.

## Prerequisiti

- Python deve essere installato nel tuo sistema.
- Un broker MQTT funzionante, come ad esempio Mosquitto, deve essere in esecuzione.

## Installazione delle Dipendenze

```bash
pip install paho-mqtt
```

## Configurazione del Broker MQTT
- Assicurati che il broker MQTT (es. Mosquitto) sia installato e in esecuzione sulla tua macchina o sulla rete.
- Configura l'indirizzo del broker e altre opzioni nel codice sorgente di entrambi gli script (`sub_mqtt.py` e `pub_mqtt.py`).

## Esecuzione dello Script di Sottoscrizione
```bash
python sub_mqtt.py
```
Lo script di sottoscrizione si connetterà al broker MQTT e inizierà a ricevere messaggi pubblicati sul topic specificato.

## Esecuzione dello Script di Pubblicazione
```bash
python pub_mqtt.py
```
Lo script di pubblicazione si connetterà al broker MQTT e invierà un messaggio al topic specificato.

## Verifica del Funzionamento
- Avvia lo script di sottoscrizione (`sub_mqtt.py`).
- Avvia lo script di pubblicazione (`pub_mqtt.py`).
- Controlla il terminale dello script di sottoscrizione per verificare che il messaggio pubblicato sia stato ricevuto correttamente.
# Risoluzione dei Problemi
- Assicurati che il broker MQTT sia in esecuzione e configurato correttamente.
- Verifica che gli script siano configurati con l'indirizzo corretto del broker e il topic desiderato.
# Note Aggiuntive
- Personalizza gli script secondo le tue esigenze.
- Assicurati che le porte e la configurazione del firewall consentano la comunicazione MQTT.

Con questi passaggi, dovresti essere in grado di testare con successo il tuo progetto MQTT utilizzando i due script forniti.