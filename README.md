# Herramienta-Google-Dorking
Esta es una herramienta centrada al google dorking creada con el IDE python esta centrada para hacer busquedas avanzas con el motor de busqueda de google y se utilizan operadores basicos para poder filtrar documentos que esten expuesto la herramienta sigue en desarrollo por lo que si te quieres unir en este proyecto estare encantado de recibirte.

Instalación de Dependencias
Paso 1: Actualizar y Preparar el Sistema

Primero, asegúrate de que tu sistema esté actualizado:

sudo apt update && sudo apt upgrade -y

Paso 2: Instalar Python y pip:

Python 3 y pip son necesarios para ejecutar el script y gestionar las dependencias.

sudo apt install python3 python3-pip -y

Paso 3: Instalar Tkinter

Tkinter se usa para crear la interfaz gráfica del usuario:

sudo apt install python3-tk -y

Paso 4: Instalar Selenium

Selenium es una herramienta para automatizar navegadores web. Es la parte central de tu herramienta:

pip3 install selenium

Paso 5: Instalar GeckoDriver

GeckoDriver es un puente entre Selenium y el navegador Firefox.

Descarga GeckoDriver:

wget https://github.com/mozilla/geckodriver/releases/latest/download/geckodriver-v0.31.0-linux64.tar.gz

Extrae el archivo descargado:

tar -xzf geckodriver-v0.31.0-linux64.tar.gz

Mueve GeckoDriver a una ubicación en tu PATH:

sudo mv geckodriver /usr/local/bin/

Verifica la instalación:

geckodriver --version

Paso 6: Crear el Archivo de Proxies

Crea un archivo llamado proxies.txt en el mismo directorio que tu script. Este archivo debe contener una lista de proxies en el formato IP:PORT, uno por línea.

Ejemplo de proxies.txt:

123.123.123.123:8080
234.234.234.234:3128
345.345.345.345:1080
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Recuerda Dar Permisos del archivo:
Asegúrate de que proxies.txt tiene los permisos adecuados para ser leído por el script:

sudo chmod 644 proxies.txt

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Recuerda dar permisos de ejecucion al script de python:

sudo chmodt +x Google_Dorking.py <--- segun en base como nombres a tu script en nano o el IDE que estes usando.

....................................................................................................................................................................
Saludos y happy hacking para todos espero sea de vital ayuda esta herramienta y puedan aprender atraves de la programacion
recuerden llevar su ingenio al maximo y no importa el resultado lo que importa es que lo lograron y lo hicieron ustedes se 
despide P1r4t3h00k suscribete a mi canal de youtube si te interesa el mundo del hacking: https://www.youtube.com/@P1r4t3h00k/videos
