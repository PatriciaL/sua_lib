import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' #Muy importante, deberéis ir cambiando la versión de vuestra librería según incluyáis nuevas funcionalidades
PACKAGE_NAME = 'sua_lib' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'Patricia Lafuente Estrada' #Modificar con vuestros datos
AUTHOR_EMAIL = 'p.lafuente.est@gmail.com' #Modificar con vuestros datos
URL = 'https://github.com/PatriciaL/sua_lib' #Modificar con vuestros datos

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'Library for EDA, Data Processing, Exporting and predict with geodataframe' #Descripción corta
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') #Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"


#Paquetes necesarios para que funcione la librería. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      'pandas','geopandas',
      'matplotlib','plotly',
      'seaborn', 'sklearn', 'numpy','shapely',
      'folium'
      ]

setup(
    name=PACKAGE_NAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    version=VERSION,
    license=LICENSE,
    #license_files = ('LICENSE.TXT'),
    classifiers=[
        "Topic:: Geo Data Science",
        "Development Status:: 1 - Beta",
        "Intended Audience:: Data Scientist & Data Analyst",
        "License:: OSI Approved:: MIT License",
        "Programming Language:: Python::3"],
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['pytest-runner', 'pandas','geopandas',
      'matplotlib','plotly',
      'seaborn', 'sklearn', 'numpy','shapely',
      'folium'],
    tests_require=['pytest', 'tox' 'pandas','geopandas',
      'matplotlib','plotly',
      'seaborn', 'sklearn', 'numpy','shapely',
      'folium']

)