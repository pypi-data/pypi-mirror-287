# Erdungsmessung
Applikation als Jupyter Notebook zur Vorbereitung, Durchführung und Auswertung von Erdungsmessungen.\
Die Applikation eignet sich für Erdungsmessungen bis zu 3 Messtagen, max. 4 Spannungsebenen und einen Messstrom. 


## Installation
Installiere Miniconda https://docs.anaconda.com/free/miniconda/index.html 

Starte die CMD und erstelle eine neue virtuelle Umgebung:

`conda create --name DevGround -c anaconda python=3.11.5`

Die Applikation ist unter https://pypi.org/project/GroundingMeasurementApplication/ aufrufbar:
Zur Installation der Abhägigkeiten den folgenden Befahl in die Python Konsole eingeben und bestätigen.

`pip install GroundingMeasurementApplication`

In der zuvor erstellten virtuellen Umgebung wird die Application und die dafür notwendigen Module heruntergeladen und installiert. 

Nun das Packet aus dem Repository downloaden, am gewünschten Ort platzieren und entpacken: 
Link: https://github.com/Kalandoros/GroundingMeasurementApplication/releases/download/v0.0.1/GroundingMeasurementApplication.v0.0.1.zip

## Konfiguration
1. Windows Einstellungen -> Datenschutz und Sicherheit -> Standort:
    * Ortungsdienste: Ein
    * Apps den Zugriff auf Ihren Standort erlauben: Ein
    * Browser (Microsoft Edge, Google Chrome) -> Zulasssen, dass Desptop-Apps auf Ihren Standort zugreifen: Ein
   
2. Installation GPS-Sensor:
    * GPS-Sensor Columbus P-9 Race anschliessen.
    * Datei `ubloxGnssUsb.inf` per Rechtsklick installieren (Warnungen können ignoriert werden)

      ![image](https://github.com/Kalandoros/Grounding_Measurement_Application/assets/129214458/5163bf9c-a9b7-4060-8226-7ee23a383b34)
    * PC Neustarten. 
    * Nach Neustart im Gerätemanager die Installation des GPS-Sensors überprüfen.
                                                  
      ![image](https://github.com/Kalandoros/Grounding_Measurement_Application/assets/129214458/a89c181c-ce87-4510-b1ea-8d26bb195516)
  
3. JupyterLab Konfiguration -> Jupyter Terminal:
   Hintergrund: Standardmässig werden vom Jupyter Kernel nur Dateien bis 10MB verarbeitet.
    * Generiere default JupyterLab Konfigurationsdatei: `jupyter-lab --generate-config` 
    * Finden der Konfigurationsdatei: `C:\Users\<WindowsUserName>\.jupyter`
    * Editieren der Konfigurationsdatei (ca. bei Zeile 1100): `"websocket_max_message_size": 1000 * 1024 * 1024` (um Dateien bis zu einer Grösse von 1GB zu erlauben).
      Die vollständige Zeile in der Konfigurationsdatei sieht dann wie folgt aus: `c.ServerApp.tornado_settings = {"websocket_max_message_size": 1000 * 1024 * 1024}`
      Dabei das Auskommentieren nicht vergessen.
    * Aufruf des Notebooks über JupyterLab: `jupyter-lab --config="jupyter_notebook_config.py"  Erdungsmessung.ipynb`
    * Aufruf des Notebooks über Voila: `voila --config="jupyter_notebook_config.py"  Erdungsmessung.ipynb`
    * Aufruf des Notebooks über Voila (alternativ): `voila Erdungsmessung.ipynb --Voila.tornado_settings="{'websocket_max_message_size': 1048576000}"`

4. Frontkamera deaktivieren -> Windows Gerätemanager:
   Hintergrund: Richtige Auswahl der Kamera bei Aufnahme von Massnahmen
    * Windows Gerätemanager öffen: `jupyter-lab --generate-config` 
    * Kategorie `Systemgeräte` auswählen und enfalten.
    * Gerät `Surface Camera Front` mit Rechtsklick auswählen.
    * Wähle `Gerät deaktivieren`.

      ![image](https://github.com/Kalandoros/GroundingMeasurementApplication/assets/129214458/e7451a21-5dc9-42a0-9a1f-340f6a9300f7)

## Benutzung
Einfach die Erdungsmessung.bat Datei doppelt anklicken. 
Die Application öffnet sich im Browser.

Alternative 1:
Öffne cmd und gebe `conda voila Erdungsmessung.ipynb` ein und führe dieses Kommando aus.

Alternative 2:
Öffne Anaconda und aktiviere die Entwicklungsumgebung "DevGround".
Starte Jupyter Lab über das Menu und öffne die `Erdungsmessung.ipynb` Datei.
Führe den Code (2 Zellen) aus.

Für Entwicklungszwecke können die beiden folgenden Befehle verwendet werden:

Jupyter Lab:\
`jupyter-lab --config="jupyter_notebook_config.py"  Erdungsmessung.ipynb --VoilaConfiguration.file_allowlist="['.*']" --VoilaConfiguration.file_whitelist=".*\.js"`

Voila:\
`voila --config="jupyter_notebook_config.py"  Erdungsmessung.ipynb --enable_nbextensions=True --VoilaConfiguration.file_allowlist="['.*']" --VoilaConfiguration.file_whitelist=".*\.js"`


         
