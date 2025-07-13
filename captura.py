import subprocess
import pandas as pd

def capturar_paquetes(duracion, interfaz):
    try:
        cmd = [
            "tshark",
            "-i", interfaz,
            "-a", f"duration:{duracion}",
            "-T", "fields",
            "-e", "frame.protocols",
            "-e", "ip.src",
            "-e", "ip.dst",
            "-e", "frame.len"
        ]

        resultado = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lineas = resultado.stdout.strip().split("\n")

        paquetes = []
        for linea in lineas:
            partes = linea.split("\t")
            if len(partes) == 4:
                protocolo, origen, destino, tamaño = partes
                paquetes.append({
                    "protocolo": protocolo or "N/A",
                    "origen": origen or "N/A",
                    "destino": destino or "N/A",
                    "tamaño": int(tamaño) if tamaño.isdigit() else 0
                })

        return pd.DataFrame(paquetes)

    except Exception as e:
        print(f"Error en la captura: {e}")
        return pd.DataFrame()
