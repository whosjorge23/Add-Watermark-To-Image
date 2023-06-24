from PIL import Image
import os

def add_logo_to_images(images_folder, logo_path, output_dir):
    # Caricare il logo e convertirlo in RGBA se ha trasparenza
    logo = Image.open(logo_path)
    if logo.mode in ('P', 'RGB'):
        logo = logo.convert('RGBA')
    
    # Ridurre le dimensioni del logo del 50%
    logo_size = (int(logo.width * 0.2), int(logo.height * 0.2))
    logo = logo.resize(logo_size, Image.ANTIALIAS)

    # Ottenere la lista di tutti i file nella cartella delle immagini
    image_files = os.listdir(images_folder)

    # Filtrare solo i file immagine
    image_paths = [os.path.join(images_folder, file) for file in image_files if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

    # Iterare attraverso l'array di immagini
    for image_path in image_paths:
        # Aprire l'immagine
        image = Image.open(image_path)

        # Utilizzare il canale alfa del logo come maschera
        logo_mask = logo.split()[-1] if logo.mode == 'RGBA' else None
        
        # Calcolare la posizione in cui inserire il logo in alto a destra e inserirlo
        position_top_right = (image.width - logo.width, 0)
        image_with_logo = image.copy()
        image_with_logo.paste(logo, position_top_right, logo_mask)

        # Calcolare la posizione in cui inserire il logo in alto a sinistra e inserirlo
        #position_top_left = (0, 0)
        #image_with_logo.paste(logo, position_top_left, logo_mask)

        # Salvare l'immagine modificata in una cartella di output
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        image_with_logo.save(output_path)

# Cartella contenente le immagini
images_folder = 'images'

# Percorso del file logo
logo_path = 'logo/logo.png'

# Cartella in cui salvare le immagini modificate
output_dir = 'output/'

# Eseguire la funzione
add_logo_to_images(images_folder, logo_path, output_dir)
