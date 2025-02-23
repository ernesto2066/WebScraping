# Instalar las librerías necesarias con los siguientes comando en un entorno virtual 
# pip install requests beautifulsoup4 pandas lxml
# pip install selenium webdriver-manager
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Configurar Selenium con Chrome en modo headless
options = Options()
options.add_argument("--headless")  # Ejecutar sin abrir el navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL de la web a analizar
url = "https://ernesto2066.github.io/Gomsoft-HTML5/"
driver.get(url)
time.sleep(3)  # Esperar a que la página cargue completamente

# Obtener el HTML después de la carga completa
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()  # Cerrar el navegador

# Listas para almacenar los datos extraídos
img_tags = [img.get("src", "N/A") for img in soup.find_all("img")]
meta_tags = [{"name": meta.get("name", "N/A"), "content": meta.get("content", "N/A")} for meta in soup.find_all("meta")]
forms_data = [{"action": form.get("action", "N/A"), "method": form.get("method", "N/A")} for form in soup.find_all("form")]
links_data = [a.get("href", "N/A") for a in soup.find_all("a", href=True)]

# Imprimir las listas de datos extraídos para verificar
print("Imágenes encontradas:", img_tags)
print("Meta Tags encontradas:", meta_tags)
print("Formularios encontrados:", forms_data)
print("Enlaces encontrados:", links_data)

# Crear DataFrames con los datos extraídos
img_df = pd.DataFrame(img_tags, columns=["Imagenes"])
meta_df = pd.DataFrame(meta_tags)
forms_df = pd.DataFrame(forms_data)
links_df = pd.DataFrame(links_data, columns=["Enlaces"])

# Verificar el contenido de los DataFrames antes de guardarlos
print("DataFrame de Imagenes:")
print(img_df.head())
print("DataFrame de Meta Tags:")
print(meta_df.head())
print("DataFrame de Formularios:")
print(forms_df.head())
print("DataFrame de Enlaces:")
print(links_df.head())

# Guardar en CSV
img_df.to_csv("imagenes.csv", index=False, encoding="utf-8")
meta_df.to_csv("meta_tags.csv", index=False, encoding="utf-8")
forms_df.to_csv("formularios.csv", index=False, encoding="utf-8")
links_df.to_csv("enlaces.csv", index=False, encoding="utf-8")

print("Scraping completado y datos guardados.")
