from PIL import Image, ExifTags
import os

def add_logo_to_images(images_folder, logo_path_right, logo_path_left, output_dir):
    # Caricare il logo destro e convertirlo in RGBA se ha trasparenza
    logo_right = Image.open(logo_path_right)
    if logo_right.mode in ('P', 'RGB'):
        logo_right = logo_right.convert('RGBA')
    
    # Caricare il logo sinistro e convertirlo in RGBA se ha trasparenza
    logo_left = Image.open(logo_path_left)
    if logo_left.mode in ('P', 'RGB'):
        logo_left = logo_left.convert('RGBA')
    
    # Ridurre le dimensioni dei loghi
    logo_size_right = (int(logo_right.width * 0.5), int(logo_right.height * 0.5))
    logo_right = logo_right.resize(logo_size_right, Image.ANTIALIAS)

    logo_size_left = (int(logo_left.width * 1.5), int(logo_left.height * 1.5))
    logo_left = logo_left.resize(logo_size_left, Image.ANTIALIAS)

    # Ottenere la lista di tutti i file nella cartella delle immagini
    image_files = os.listdir(images_folder)

    # Filtrare solo i file immagine
    image_paths = [os.path.join(images_folder, file) for file in image_files if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

    # Iterare attraverso l'array di immagini
    for image_path in image_paths:
        # Aprire l'immagine
        image = Image.open(image_path)

        # Check for EXIF data and correct orientation
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(image._getexif().items())
            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            # Cases: image don't have getexif
            pass

        # Utilizzare il canale alfa del logo destro come maschera
        logo_mask_right = logo_right.split()[-1] if logo_right.mode == 'RGBA' else None
        
        # Utilizzare il canale alfa del logo sinistro come maschera
        logo_mask_left = logo_left.split()[-1] if logo_left.mode == 'RGBA' else None
        
        # Calcolare la posizione in cui inserire il logo in alto a destra e inserirlo
        position_top_right = (image.width - logo_right.width, 0)
        image_with_logos = image.copy()
        image_with_logos.paste(logo_right, position_top_right, logo_mask_right)

        # Calcolare la posizione in cui inserire il logo in alto a sinistra e inserirlo
        position_top_left = (0, 0)
        image_with_logos.paste(logo_left, position_top_left, logo_mask_left)

        # Salvare l'immagine modificata in una cartella di output
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        image_with_logos.save(output_path)

# Cartella contenente le immagini
images_folder = 'jpg'

# Percorsi dei file loghi
logo_path_right = 'logo/logo1.png'
logo_path_left = 'logo/logo2.png'

# Cartella in cui salvare le immagini modificate
output_dir = 'output/'

# Eseguire la funzione
add_logo_to_images(images_folder, logo_path_right, logo_path_left, output_dir)
