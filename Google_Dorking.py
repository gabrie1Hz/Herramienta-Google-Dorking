import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException
import time
import random

# Función para cargar proxies desde un archivo
def load_proxies(file_path):
    proxies = []
    with open(file_path, 'r') as file:
        for line in file:
            proxies.append(line.strip())
    return proxies

# Función para crear el WebDriver de Selenium para Firefox con proxy
def create_driver(proxy):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

    # Configuración del perfil de Firefox para el proxy
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy.split(':')[0])
    profile.set_preference("network.proxy.http_port", int(proxy.split(':')[1]))
    profile.set_preference("network.proxy.ssl", proxy.split(':')[0])
    profile.set_preference("network.proxy.ssl_port", int(proxy.split(':')[1]))
    profile.update_preferences()

    service = Service(executable_path='/usr/local/bin/geckodriver')  # Actualiza la ruta según la ubicación de geckodriver
    try:
        driver = webdriver.Firefox(service=service, options=options, firefox_profile=profile)
        return driver
    except WebDriverException as e:
        print(f"Error al iniciar WebDriver: {e}")
        return None

# Función para realizar Google Dorking
def google_dork(query, driver):
    try:
        driver.get("https://www.google.com")  # Usar HTTPS
        time.sleep(random.uniform(1, 3))  # Espera aleatoria entre 1 y 3 segundos
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        time.sleep(random.uniform(1, 3))  # Espera aleatoria entre 1 y 3 segundos antes de enviar la búsqueda
        search_box.send_keys(Keys.RETURN)
        time.sleep(random.uniform(3, 5))  # Espera aleatoria entre 3 y 5 segundos antes de buscar los resultados
        
        results = driver.find_elements(By.CSS_SELECTOR, 'div.yuRUbf > a')
        urls = [result.get_attribute('href') for result in results]
        
        return urls
    except Exception as e:
        print(f"Error durante la búsqueda: {e}")
        return []

# Función para manejar el evento de búsqueda
def search():
    selected_option = query_var.get()
    if selected_option == "Archivos PDF":
        query = 'filetype:pdf'
    elif selected_option == "Índices de Directorios Expuestos":
        query = '"index of"'
    elif selected_option == "Archivos de Configuración DHCP":
        query = 'intext:"dhcpd.conf"'
    elif selected_option == "Correos Electrónicos":
        query = 'intext:"email"'
    elif selected_option == "Documentos de Word":
        query = 'filetype:doc'
    else:
        query = ''

    if query:
        results_text.delete(1.0, tk.END)
        urls = google_dork(query, driver)
        for url in urls:
            results_text.insert(tk.END, url + '\n')

# Ruta del archivo de proxies
file_path = 'proxies.txt'

# Cargar proxies desde el archivo
proxies = load_proxies(file_path)

# Seleccionar un proxy aleatorio
proxy = random.choice(proxies)

# Crear el WebDriver con el proxy seleccionado
driver = create_driver(proxy)
if driver is None:
    print("No se pudo iniciar el WebDriver. Verifica la configuración de geckodriver y Firefox.")
    exit()

# Configuración de la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("DorkingHook")

# Menú desplegable para seleccionar el tipo de búsqueda
query_var = tk.StringVar(root)
query_var.set("Selecciona el tipo de búsqueda")  # Valor por defecto

query_options = [
    "Archivos PDF",
    "Índices de Directorios Expuestos",
    "Archivos de Configuración DHCP",
    "Correos Electrónicos",
    "Documentos de Word"
]

query_menu = tk.OptionMenu(root, query_var, *query_options)
query_menu.pack()

# Botón para iniciar la búsqueda
search_button = tk.Button(root, text="Buscar", command=search)
search_button.pack()

# Campo de texto para mostrar los resultados
results_text = scrolledtext.ScrolledText(root, width=80, height=20)
results_text.pack()

# Ejecutar la aplicación
root.mainloop()

# Cerrar el WebDriver al salir
driver.quit()
