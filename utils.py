import subprocess

def listar_interfaces():
    try:
        resultado = subprocess.run(["tshark", "-D"], capture_output=True, text=True, check=True)
        lineas = resultado.stdout.strip().split("\n")
        interfaces = []
        for linea in lineas:
            # Ejemplo línea: 1. \Device\NPF_{...} (Conexión de área local* 12)
            partes = linea.split(". ", 1)[1]  # toma después del número y punto
            
            nombre = partes.split(" ")[0]
            interfaces.append(nombre)
        return interfaces
    except Exception as e:
        print(f"Error listando interfaces: {e}")
        return []
