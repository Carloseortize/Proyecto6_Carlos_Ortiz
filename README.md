# Proyecto6_Carlos_Ortiz

# Aplicación de Visualización de Datos de Vehículos

Esta aplicación web está diseñada para ayudar a los usuarios a explorar y analizar datos de anuncios de venta de coches de manera interactiva. Utilizando **Streamlit** y **Plotly**, la aplicación permite generar gráficos que facilitan la interpretación visual de relaciones clave entre las características de los coches, como el precio y el odómetro.

## URL

[Visita la aplicación aquí](https://proyecto6-carlos-ortiz.onrender.com/)

## Descripción del Proyecto

La aplicación proporciona una interfaz sencilla para seleccionar y visualizar datos específicos de un conjunto de anuncios de coches en venta. Los usuarios pueden elegir entre distintos tipos de gráficos, como histogramas y diagramas de dispersión, para explorar tendencias en el precio y kilometraje de los vehículos.

### Funcionalidades

- **Construcción de Histogramas**: Permite al usuario crear un histograma para visualizar la distribución de valores en la columna de odómetro, ayudando a identificar patrones de kilometraje en los anuncios de coches.
- **Creación de Diagramas de Dispersión**: Permite generar un diagrama de dispersión interactivo para observar la relación entre el precio de los coches y el kilometraje (odómetro). Esto ayuda a explorar la posible correlación entre estas dos variables.
- **Interfaz Intuitiva**: La aplicación utiliza casillas de verificación (`checkboxes`) para activar y desactivar gráficos, haciendo que sea fácil e intuitivo para los usuarios interactuar con los datos.
- **Gráficos Interactivos con Plotly**: Los gráficos son interactivos, permitiendo hacer zoom, desplazarse y ver detalles específicos en el gráfico, lo que enriquece la experiencia de usuario.

## Requisitos

Para ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- Paquetes de Python: `pandas`, `streamlit`, y `plotly-express`
