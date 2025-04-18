from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bienvenido a CRYPTO TERMINAL v1\n\nComandos disponibles:\n/btc - Análisis de Bitcoin en tiempo real\n/sol - Análisis de Solana\n/macro - Estado del mercado global\n\nEscribe un comando para comenzar."
    )

# Comando /btc con datos en tiempo real
async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true"
    try:
        response = requests.get(url)
        data = response.json()["bitcoin"]

        precio = data["usd"]
        cambio = round(data["usd_24h_change"], 2)
        volumen = round(data["usd_24h_vol"] / 1_000_000_000, 2)  # en miles de millones

        mensaje = f"""
======================================================================
                 SISTEMA DE ANÁLISIS TÉCNICO – BTC/USDT
======================================================================

PRECIO ACTUAL: ${precio:,} USD
VARIACIÓN 24H: {cambio:+.2f}%
VOLUMEN 24H: ${volumen}B

NOTICIAS:
 - Rumores sobre pausa de tasas por parte de la FED
 - Nikkei +6%, alivio macro
 - Volumen spot y derivados en máximos

RESISTENCIAS: $83K / $86.5K / $91K
SOPORTES: $80K / $75K / $69K

ESCENARIO ALCISTA (65%):
  - Cierre > $83K con volumen
  - Objetivo: $86.5K / $91K

ESCENARIO BAJISTA (35%):
  - Rechazo en $83K + pérdida de $80K
  - Objetivo: $75K / $69K

ESTRATEGIA:
  Entrada: $83.2K    TP: $86.5K    SL: $80.9K
======================================================================
"""
        await update.message.reply_text(mensaje)

    except Exception as e:
        await update.message.reply_text("⚠️ Error al obtener datos de BTC. Intenta más tarde.")

if __name__ == '__main__':
    import os

    # TOKEN del Bot que te dio BotFather
    TOKEN = "7564589554:AAFdX-EdBm2jZRiuEUy5Qc-j8OQ8rszMwX8"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("btc", btc))

    print("Bot iniciado. Esperando comandos...")
    app.run_polling()


