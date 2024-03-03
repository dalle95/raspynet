## Installazione di Mosquitto su Linux
* Verifica se Mosquitto è già installato: In molti casi, Mosquitto è disponibile direttamente tramite i gestori di pacchetti delle distribuzioni Linux. Puoi verificare se è già installato eseguendo il seguente comando nel terminale:
```bash
mosquitto -v
```
* Se non è installato, procedi con l’installazione.
Installazione su Ubuntu/Debian:
```bash
    sudo apt-get update
    sudo apt-get install mosquitto
```
## Installazione di Mosquitto su Windows
* Scarica l’ultima versione di Mosquitto per Windows:
  * Vai al sito di download di Mosquitto.
  * Scarica l’ultima versione “binary version - Cygwin” per Windows.
* Esegui l’installer:
  * Durante l’installazione, lascia tutte le impostazioni di default.
  * Appuntati la directory di installazione (solitamente “C:\Mosquitto”).
* Risolvi l’errore post-installazione:
  * Dopo l’installazione, potresti visualizzare un errore. Non preoccuparti, è normale.
  * Per far funzionare Mosquitto, copia manualmente alcuni file nella cartella di destinazione dell’installazione.
* Verifica il funzionamento:
  * Apri il prompt dei comandi e digita:
```bash
mosquitto -v
```