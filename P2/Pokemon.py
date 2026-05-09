import requests
import shutil
import json

class Pokemon:
    def descargar_imagen(self, enlace, nombre_archivo):
        respuesta = requests.get(enlace, stream=True)
        if respuesta.status_code == 200:
            with open(nombre_archivo, 'wb') as archivo:
                shutil.copyfileobj(respuesta.raw, archivo)
            print(f'Imagen descargada correctamente: {nombre_archivo}')
        else:
            print('Error: No se pudo descargar la imagen')
    
    def obtener_datos(self, pokemon):
        url_base = 'https://pokeapi.co/api/v2/pokemon/'
        try:
            peticion = requests.get(url_base + pokemon.lower())
            
            if peticion.status_code != 200:
                print(f'Pokemon "{pokemon}" no encontrado. Codigo: {peticion.status_code}')
                return None
            
            datos = json.loads(peticion.content)
            
            print(f"\n>>> INFORMACION DEL POKEMON <<<")
            print(f"Nombre: {datos['name'].upper()}")
            print(f"Numero en Pokedex: {datos['id']}")
            print(f"Altura: {datos['height']} dm")
            print(f"Peso: {datos['weight']} hg")
            
            tipos = [t['type']['name'] for t in datos['types']]
            print(f"Tipo(s): {' / '.join(tipos)}")
            
            print("Estadisticas base:")
            for estadistica in datos['stats']:
                nombre_stat = estadistica['stat']['name']
                valor_stat = estadistica['base_stat']
                print(f"  - {nombre_stat}: {valor_stat}")
            
            habilidades = [a['ability']['name'] for a in datos['abilities']]
            print(f"Habilidades: {', '.join(habilidades)}")
            
            return datos['sprites']['front_default']
            
        except requests.exceptions.RequestException as error:
            print(f"Error de conexion: {error}")
            return None
        except (KeyError, json.JSONDecodeError) as error:
            print(f"Error al leer datos del Pokemon: {error}")
            return None