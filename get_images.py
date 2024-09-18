import cv2
import os

num_images = 186
video_path_list = [r"C:\Users\wiards\OneDrive - IPH Hannover gGmbH\Digitalisierungsprojekt Imkerei\Aufnahmen_GoPro_2024\Neue_Videos\Berarbeitet\Drohnen_Highlights_rangezoomt.MP4"]

# Funktion zum Anzeigen des Fortschrittsbalkens
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    if iteration == total:
        print()

# Erstellen des Zielverzeichnisses, falls es nicht existiert
output_dir = "randomdrohnen_images"
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

counter = 1

for video_path in video_path_list:
    vidcap = cv2.VideoCapture(video_path)
    totalFrames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Berechne das Intervall zwischen den zu extrahierenden Frames
    frame_interval = totalFrames // num_images

    # Extrahiere Frames in zeitlicher Reihenfolge
    for i in range(num_images):
        frame_number = i * frame_interval
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        success, image = vidcap.read()
        if success:
            cv2.imwrite(f'{output_dir}/{str(counter).zfill(4)}.png', image)
        printProgressBar(counter, num_images * len(video_path_list), prefix='Progress:', suffix='Complete', length=50)
        counter += 1
        del image
print(totalFrames)