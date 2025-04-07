

# 📈 Bitcoin Market & News Analytics Pipeline

## ✨ Overview
Este proyecto implementa una arquitectura de ingeniería de datos tipo **Medallion (Bronze-Silver-Gold)** para analizar datos de precio del Bitcoin en tiempo real y noticias relacionadas, aplicando limpieza, transformaciones y generación de features.


## 🏗️ Estructura del Proyecto

bitcoin_pipeline/
├── data/                  # Contiene el archivo CSV con noticias
├── db/                    # Base de datos SQLite generada por el pipeline
├── logs/                  # Logs de ejecución y errores
├── notebooks/
│   └── pipeline.ipynb     # Notebook principal del pipeline
├── src/                   # Módulos Python (ingesta, procesamiento, utils)
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Este archivo

---


## ⚡ Tecnologías Utilizadas
- **Python**
- **SQLite** para almacenamiento persistente
- **pandas, requests, sklearn, nltk**
- **logging** para seguimiento de errores y eventos

---

## 💡 Estructura de Capas Medallion

### 🪜 Bronze Layer
- Ingesta directa desde API de Bitcoin y archivo CSV.
- Datos sin modificar.
- Validación de esquema básica.

### 🖊️ Silver Layer
- Limpieza de datos y normalización.
- Conversión de timestamps.
- Manejo de valores nulos.

### 📈 Gold Layer
- Cálculo de indicadores técnicos (SMA, EMA).
- Extracción de palabras clave desde noticias.
- Agregación de métricas (promedios, conteos).
- Pruebas de calidad de datos.

---

## 📅 Tareas por Fase

### Task 1: Data Ingestion
- API: Precio de Bitcoin desde CoinGecko (tiempo real).
- CSV: Ingesta de noticias desde `news_api.csv`.
- Creación de esquema en SQLite.

### Task 2: Pipelines Medallion
- Scripts para pasar de Bronze a Silver y a Gold.
- Procesamiento real-time y por lotes.
- Validaciones en cada etapa.

### Task 3: Análisis y Features
- Indicadores: `SMA`, `EMA`, señales Buy/Sell.
- Extracción de keywords con `CountVectorizer`.
- Agregaciones y métricas: precio promedio, sentimiento promedio, etc.

---

## 🎯 Bonus: Estrategia Trading
- Estrategia de cruce de medias móviles:
  - Buy: SMA corta cruza hacia arriba SMA larga.
  - Sell: SMA corta cruza hacia abajo SMA larga.
- Visualización en `matplotlib`.

---

## 🔧 Ejecución del Pipeline
```bash
# Paso 1: Ingestar precios y noticias
download_bitcoin_price()
load_news_csv("data/news_api.csv")

# Paso 2: Bronze -> Silver -> Gold
clean_price_data()
clean_news_data()
add_indicators()
extract_keywords()

# Paso 3: Análisis y exportación
aggregate_metrics()
data_quality_checks()
```

---

## 📊 Base de Datos Final (SQLite)
- `btc_price_bronze`, `btc_price_silver`, `btc_price_gold`
- `btc_news_bronze`, `btc_news_silver`, `btc_news_gold`
- `btc_metrics_gold`, `news_metrics_gold`

---

## 📅 Logging y Manejo de Errores
Todos los errores se registran en `logs/pipeline.log`, incluyendo trazas de stack y timestamps. Se usan bloques `try-except` en cada función.

---

## 🚀 Requisitos para Ejecutar
```bash
pip install -r requirements.txt
python main.py
```

---

## 📄 Autor
- [Tu Nombre / GitHub]
- Proyecto para evaluación técnica de ingeniería de datos
