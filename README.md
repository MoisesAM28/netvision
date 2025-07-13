# 📡 NetVision – Monitor de Tráfico de Red en Tiempo Real

NetVision es una herramienta interactiva desarrollada en Python que permite **capturar, visualizar y analizar tráfico de red** en tiempo real desde una interfaz web sencilla usando Streamlit.

![NetVision Banner](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?style=flat-square) ![Pyshark](https://img.shields.io/badge/Pyshark-Packet_Capture-brightgreen?style=flat-square)

---

## 🚀 Características principales

- ✅ **Captura de tráfico** en tiempo real desde cualquier interfaz de red
- 📊 Visualización por **protocolo** e **IP origen**
- 📈 Gráficas interactivas con **Plotly**
- 🛡️ **Análisis automático de anomalías**:
  - Paquetes demasiado grandes
  - IPs públicas sospechosas
  - IPs con tráfico inusualmente alto
- 💾 Exportación de datos como archivo `.csv`

---

## 🖼️ Capturas de pantalla

> Puedes agregar imágenes reales de tu app aquí si gustas más adelante.

---

## ⚙️ Requisitos

- Python 3.10 o superior
- [Npcap](https://nmap.org/npcap/) instalado en modo WinPcap-compatible (para Windows)
- TShark (parte de Wireshark)

---

## 🧪 Instalación

```bash
git clone https://github.com/TU_USUARIO/netvision.git
cd netvision
python -m venv venv
venv\Scripts\activate  # En Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
