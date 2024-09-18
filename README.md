# Image-recognition_Bee-Drone
We used the YOLO-Algorithm to distinguish bees and drones (female and male) in our beehive. 


# Object recognition for the beekeeping digitization project

This document provides a step-by-step guide to object labeling and training an object recognition algorithm.

## Preparation of the videos

1. record videos
   - Make sure that the videos are suitable for your purposes.

2 **Extract images from the videos**
   - Use the script “get_images.py”.
     - Change the variable “num_images”, which depends on the length of the video and the number of images you want.
     - Example: With 10 seconds and 30 FPS you can get up to 300 images.
     - It is advisable to extract an image every 1-2 seconds, depending on the use case.
   - Enter the path to the video:
     
     video_path_list = [r'path\zum\video\example.mp4']
     
   - Adjust the name of the target directory:
     
     output_dir = 'path\to\destination_directory'
     
   - Execute the script.

## Labeling and training models

1. create **Roboflow account**
   - License type: “CC BY 4.0” or “private” (no significant differences).

2 **Upload and label images**
   - Make sure that no class is underrepresented.
   - A balanced class ratio improves accuracy.

3 **Annotate images**
   - Add the images to the dataset and annotate as many objects as possible.

4 **Prepare dataset**
   - Do not select anything under “Preprocessing”.
   - Use “Augmentation” to improve the variety of data, e.g. by varying the brightness.
   - Click on “Create”.

5. download **Dataset**
   - Go to “Versions” and download the dataset in YOLOv8 format.
   - Unzip the file and upload it to your project directory.

6. **Training**
   - Copy the file ”
trainer_yolo.py” into the downloaded directory.
   - In case of error messages for the “data.yaml” file, enter the complete path.
   - Execute the script and adjust the number of “epochs” (approx. 200 is recommended).
   - The “pt” files are created after the training runs have been completed.

7 **Model selection**
   - Select the model with the best results.
   - Find the visual evaluation and the best model in the directory `...\runs\detect`.

## Create output video

1. create **video**
   - Use the script `predict_video_yolo.py`.
     - Enter the path to the video:
       
       video_path = r'path\zum\video\example.mp4'
       
     - Select the model:
       
       model = YOLO(“yolov8s_best_model.pt”)
       
     - Adjust the name and the target path for the video
       
       sv.process_video(source_path=video_path, target_path=“output_video.mp4”, callback=process_frame)
       
   - The “confidence_threshold” can be set to 0.5 to only display boxes with a confidence level above 50%.




German description: 

# Objekterkennung für das Digitalisierungsprojekt

Dieses Dokument bietet eine Schritt-für-Schritt-Anleitung zur Objektlabeln und zum Training eines Algorithmus zur Objekterkennung.

## Vorbereitung der Videos

1. **Videos aufnehmen**
   - Stelle sicher, dass die Videos für deine Zwecke geeignet sind.

2. **Bilder aus den Videos extrahieren**
   - Verwende das Skript "get_images.py".
     - Ändere die Variable "num_images", die von der Länge des Videos und der Anzahl der gewünschten Bilder abhängt.
     - Beispiel: Bei 10 Sekunden und 30 FPS kannst du bis zu 300 Bilder erhalten.
     - Es ist ratsam, alle 1-2 Sekunden ein Bild zu extrahieren, je nach Anwendungsfall.
   - Gib den Pfad zum Video an:
     
     video_path_list = [r'Pfad\zum\Video\beispiel.mp4']
     
   - Passe den Namen des Zielverzeichnisses an:
     
     output_dir = 'Pfad\zum\Zielverzeichnis'
     
   - Führe das Skript aus.

## Labeln und Modelle trainieren

1. **Roboflow-Account erstellen**
   - Lizenztyp: „CC BY 4.0“ oder „privat“ (keine wesentlichen Unterschiede).

2. **Bilder hochladen und labeln**
   - Achte darauf, dass keine Klasse unterrepräsentiert ist.
   - Ein ausgewogenes Klassenverhältnis verbessert die Genauigkeit.

3. **Bilder annotieren**
   - Füge die Bilder dem Dataset hinzu und annotiere so viele Objekte wie möglich.

4. **Dataset vorbereiten**
   - Bei „Preprocessing“ nichts auswählen.
   - Nutze „Augmentation“ zur Verbesserung der Datenvielfalt, z.B. durch Variation der Helligkeit.
   - Klicke auf „Create“.

5. **Dataset herunterladen**
   - Gehe zu „Versions“ und lade das Dataset im YOLOv8-Format herunter.
   - Entpacke die Datei und lade sie in dein Projektverzeichnis hoch.

6. **Training**
   - Kopiere die Datei "
trainer_yolo.py" in das heruntergeladene Verzeichnis.
   - Bei Fehlermeldungen zur „data.yaml“-Datei, gib den vollständigen Pfad an.
   - Führe das Skript aus und passe die Anzahl der „epochs“ an (ca. 200 sind empfehlenswert).
   - Die „pt“-Dateien werden nach Abschluss der Trainingsdurchläufe erstellt.

7. **Modellauswahl**
   - Wähle das Modell mit den besten Ergebnissen aus.
   - Finde die visuelle Auswertung und das beste Modell im Verzeichnis `...\runs\detect`.

## Output-Video erstellen

1. **Video erstellen**
   - Verwende das Skript `predict_video_yolo.py`.
     - Gib den Pfad zum Video an:
       
       video_path = r'Pfad\zum\Video\beispiel.mp4'
       
     - Wähle das Modell aus:
       
       model = YOLO("yolov8s_bestes_modell.pt")
       
     - Passe den Namen und den Zielpfad für das Video an:
       
       sv.process_video(source_path=video_path, target_path="Ausgabevideo.mp4", callback=process_frame)
       
   - Der "confidence_threshold" kann auf 0.5 gesetzt werden, um nur Boxen mit einer Vertrauensstufe über 50% anzuzeigen.
