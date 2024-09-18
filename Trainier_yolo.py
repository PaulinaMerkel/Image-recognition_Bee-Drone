from ultralytics import YOLO
import torch
import gc

def main():
    model_list = ['yolov8n.pt',
                  'yolov8s.pt',
                  'yolov8m.pt',
                  ]

    
    
    # Angepasste Gewichtung in der data.yaml Datei
    # Hier wird eine Datei erwartet, die die Gewichtung der Klassen definiert
    data_yaml = r'C:\Users\KI\OneDrive - IPH Hannover gGmbH\KI-Koordination\Digitalisierungsprojekt Imkerei\Worker-Drone\data.yaml'

   
   
    

    for model_name in model_list:
        model = YOLO(model_name)
        
        # Trainiere das Modell und überwache die Validierungsmetriken
        results = model.train(
            data=data_yaml,
            imgsz=(1920, 1080),
            epochs=250,
            batch=8,
            workers=1,
            name=model_name.replace('.pt',''),
            val=True,  # Stelle sicher, dass Validierung während des Trainings überwacht wird
            
        )

        # Optional: Speichere die Ergebnisse oder Metriken
        results.save()  # Speichert die Ergebnisse und das Modell

        del model
        del results
        gc.collect()

if __name__ == '__main__':
    torch.multiprocessing.freeze_support()
    main()
