import requests
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd

pages = np.arange(1,19).tolist() #Recorrido para el total de páginas

precio_list = []
nombre_list = []

for page in pages:
    url = 'https://www.ouroborostore.cl/categoria-producto/juegos-de-mesa/page/'+str(page)+'/'
    pedido_obt = requests.get(url)
    html_obt = pedido_obt.text
    
    soup = BeautifulSoup(html_obt, 'html.parser')
    
    precio_producto = soup.find_all(class_='price')
    for unit in precio_producto:
        precio = unit.text
        #data = {'Precio':precio}
        precio_list.append(precio)

    nombre_producto = soup.find_all(class_='name product-title woocommerce-loop-product__title')
    for unit in nombre_producto:
        nombre = unit.text
        #data = {'Nombre Producto':nombre}
        nombre_list.append(nombre)

len(precio_list)
precio_list[43]

len(nombre_list)
nombre_list[43]

# Ambos len permiten validar previamente si se podrán guardar en el excel (requiere misma cantidad de "celdas")

col1 = 'Nombre Producto'
col2 = 'Precio'

data = pd.DataFrame({col1: nombre_list, col2:precio_list})

data.to_excel('./listado_productos.xlsx', sheet_name='Productos')
