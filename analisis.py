import pandas as pd
import plotly.express as px
import ipaddress



def obtener_estadisticas(df):
    resumen = {
        "Total de paquetes": len(df),
        "Protocolos detectados": df['protocolo'].nunique(),
        "IPs origen únicas": df['origen'].nunique(),
        "IPs destino únicas": df['destino'].nunique(),
        "Volumen total (KB)": round(df['tamaño'].sum() / 1024, 2)
    }
    return pd.DataFrame.from_dict(resumen, orient='index', columns=["Valor"])

def graficar_por_protocolo(df):
    conteo = df['protocolo'].value_counts().reset_index()
    conteo.columns = ['Protocolo', 'Cantidad']
    return px.pie(conteo, names='Protocolo', values='Cantidad', title="Distribución de protocolos")

def graficar_por_ip(df):
    conteo = df['origen'].value_counts().reset_index().head(10)
    conteo.columns = ['IP Origen', 'Cantidad']
    return px.bar(conteo, x='IP Origen', y='Cantidad', title="Top 10 IPs origen")


def detectar_anomalias(df):
    anomalías = []

    # Detectar paquetes muy grandes
    grandes = df[df['tamaño'] > 1500]
    for _, fila in grandes.iterrows():
        anomalías.append({
            "tipo": "Paquete grande",
            "origen": fila["origen"],
            "destino": fila["destino"],
            "tamaño": fila["tamaño"]
        })

    # Detectar IPs públicas (no privadas)
    for _, fila in df.iterrows():
        try:
            ip = ipaddress.ip_address(fila["origen"])
            if not ip.is_private:
                anomalías.append({
                    "tipo": "IP pública detectada",
                    "origen": fila["origen"],
                    "destino": fila["destino"],
                    "tamaño": fila["tamaño"]
                })
        except ValueError:
            continue  # IP inválida

    # Detectar IPs con demasiados paquetes
    conteo = df["origen"].value_counts()
    for ip, cantidad in conteo.items():
        if cantidad > 100:
            anomalías.append({
                "tipo": "IP con tráfico alto",
                "origen": ip,
                "destino": "Varios",
                "tamaño": None  # Corregido: evitar string "-"
            })

    return pd.DataFrame(anomalías)
