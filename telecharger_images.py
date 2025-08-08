
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL de la page à scraper
url = "https://beberdelacampagne.com/"

# Dossier pour sauvegarder les images
output_folder = "images_beber"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Récupérer le contenu HTML de la page
try:
    response = requests.get(url)
    response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête HTTP : {e}")
    exit()

# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver toutes les balises <img>
img_tags = soup.find_all('img')

# Télécharger chaque image
for img in img_tags:
    img_url = img.get('src')
    if img_url:
        # Construire l'URL absolue de l'image
        img_url = urljoin(url, img_url)
        
        try:
            # Obtenir le nom du fichier à partir de l'URL
            filename = os.path.join(output_folder, os.path.basename(img_url.split("?")[0]))

            # Envoyer une requête pour télécharger l'image
            img_response = requests.get(img_url, stream=True)
            img_response.raise_for_status()

            # Sauvegarder l'image dans le dossier
            with open(filename, 'wb') as f:
                for chunk in img_response.iter_content(8192):
                    f.write(chunk)
            
            print(f"Image téléchargée : {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Impossible de télécharger {img_url}. Erreur : {e}")
        except Exception as e:
            print(f"Une erreur est survenue lors du traitement de {img_url}. Erreur : {e}")

print("\nTerminé. Les images sont dans le dossier 'images_beber'.")
