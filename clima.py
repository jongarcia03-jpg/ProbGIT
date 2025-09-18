
import requests
import gradio as gr

def obtener_coordenadas(ciudad):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1&language=es&format=json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    if datos.get("results"):
        latitud = datos["results"][0]["latitude"]
        longitud = datos["results"][0]["longitude"]
        return latitud, longitud
    else:
        return None, None

def obtener_temperatura(latitud, longitud):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true"
    respuesta = requests.get(url)
    datos = respuesta.json()
    if "current_weather" in datos:
        temperatura = datos["current_weather"]["temperature"]
        return temperatura
    else:
        return None

def clima_ciudad(ciudad):
    latitud, longitud = obtener_coordenadas(ciudad)
    if latitud is None or longitud is None:
        return f"No se encontró la ciudad '{ciudad}'."
    temperatura = obtener_temperatura(latitud, longitud)
    if temperatura is not None:
        if temperatura < 10:
            rango = "baja"
        elif temperatura <= 25:
            rango = "media"
        else:
            rango = "alta"
        return f"El clima en {ciudad} es: {temperatura}°C ({rango} temperatura)"
    else:
        return "No se pudo obtener la temperatura actual."

with gr.Blocks() as demo:
    gr.Markdown("# Consulta el clima actual de una ciudad")
    ciudad = gr.Textbox(label="Ciudad", placeholder="Ejemplo: Bilbao")
    resultado = gr.Textbox(label="Resultado")
    boton = gr.Button("Consultar clima")
    boton.click(fn=clima_ciudad, inputs=ciudad, outputs=resultado)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
