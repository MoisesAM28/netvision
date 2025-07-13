import streamlit as st
from captura import capturar_paquetes
from analisis import (
    obtener_estadisticas,
    graficar_por_protocolo,
    graficar_por_ip,
    detectar_anomalias
)
from utils import listar_interfaces

st.set_page_config(page_title="NetVision", layout="wide")
st.title("📡 NetVision - Monitor de Tráfico de Red")

interfaces = listar_interfaces()
interfaz = st.selectbox("Selecciona la interfaz de red:", interfaces)

duracion = st.slider("Duración de la captura (segundos):", min_value=5, max_value=60, value=10)

if st.button("Iniciar captura"):
    with st.spinner("Capturando tráfico..."):
        df = capturar_paquetes(duracion, interfaz)

    if not df.empty:
        st.success("✅ Captura completada")

        # Estadísticas generales
        st.subheader("📊 Estadísticas")
        st.dataframe(obtener_estadisticas(df))

        # Gráficos
        st.subheader("📈 Visualizaciones")
        st.plotly_chart(graficar_por_protocolo(df), use_container_width=True)
        st.plotly_chart(graficar_por_ip(df), use_container_width=True)

        # Análisis de anomalías
        st.subheader("🛡️ Análisis de anomalías")
        anomalías = detectar_anomalias(df)
        if not anomalías.empty:
            st.warning("⚠️ Se detectaron posibles anomalías en el tráfico:")
            st.dataframe(anomalías)
        else:
            st.success("✅ No se detectaron anomalías.")

        # Descargar captura
        st.download_button("💾 Descargar CSV", df.to_csv(index=False), file_name="captura.csv", mime="text/csv")
    else:
        st.warning("⚠️ No se capturaron paquetes.")
