import telebot
import time

TOKEN = "8053639275:AAEVn8J9_4YCu8hB3Leknm9aVH8XB2RSKDs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    # Imagem principal
    with open("boasvindas.png", "rb") as img:
        bot.send_photo(chat_id, img)

    # Mensagem 1: texto persuasivo
    bot.send_message(chat_id, """
📺 *ASSISTA AGORA AO VIVO EM HD — POR APENAS R$4,99!*

✅ Link + tutorial liberado em segundos  
💸 Pagamento via Pix (manual, rápido e seguro)  
⏱️ Tempo médio de resposta: 1 a 3 minutos

🔓 *Como liberar o acesso:*  
1️⃣ Faça o Pix  
2️⃣ *Envie o comprovante no PRIVADO*: @acessoviphdfute

🎟️ Tipo de acesso: *Diário*  
💰 Valor: *R$4,99*  
🚀 Liberação imediata após verificação!
""", parse_mode="Markdown")

    # Mensagem 2: QR Code com chave Pix
    with open("qrcode.png", "rb") as photo:
        bot.send_photo(chat_id, photo, caption="""
🔑 *Chave Pix (copia e cola):*  
00020126580014br.gov.bcb.pix0136c07a4e09-11a4-4df7-8f47-1055bafddf7f75204000053039865802BR5924Primepag Solucoes em PagG5090SAO
""", parse_mode="Markdown")

    # Espera 5 minutos e envia mensagem de remarketing
    time.sleep(300)
    bot.send_message(chat_id, "*Ficou com alguma dúvida?*", parse_mode="Markdown", reply_markup=link_button())

def link_button():
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("📩 Falar com o suporte", url="https://t.me/acessoviphdfute")
    markup.add(btn)
    return markup

print("Bot está rodando...")
bot.infinity_polling()
