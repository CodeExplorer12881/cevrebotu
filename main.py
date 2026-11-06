import discord
from discord.ext import commands
import random

# Botun izinleri
intents = discord.Intents.default()
intents.message_content = True

# Botu oluşturuyoruz
bot = commands.Bot(command_prefix="!", intents=intents)

# Atıkların ayrışma süreleri
atiklar = {
    "plastik şişe": "Yaklaşık 450 yıl",
    "cam şişe": "Çok uzun süre; doğada milyonlarca yıl kalabilir.",
    "kağıt": "Yaklaşık 2-6 hafta",
    "karton": "Yaklaşık 2 ay",
    "alüminyum kutu": "Yaklaşık 200 yıl",
    "plastik poşet": "Yaklaşık 10-20 yıl",
    "sigara izmariti": "Yaklaşık 10 yıl",
    "muz kabuğu": "Yaklaşık 2-5 hafta",
    "elma": "Yaklaşık 1-2 ay",
    "metal kutu": "Yaklaşık 50 yıl"
}


# Çevre dostu öneriler
ipuclari = [
    "Alışverişe giderken bez çanta kullan!",
    "Plastik şişe yerine tekrar kullanılabilir matara tercih et!",
    "Kağıtları geri dönüşüm kutusuna at!",
    "Kullanmadığın eşyaları çöpe atmak yerine değerlendir!",
    "Atıklarını türlerine göre ayır!",
    "Tek kullanımlık ürünleri daha az kullan!"
]


# Bot açıldığında çalışır
@bot.event
async def on_ready():
    print("EkoBot başarıyla çalıştı!")
    print("Bot adı:", bot.user)


# Yardım komutu
@bot.command()
async def yardim(ctx):
    mesaj = """
🌱 **EKOBOT KOMUTLARI**

!ayrisma plastik şişe
Bir atığın ayrışma süresini öğren.

!liste
Bütün atıkları listele.

!ipucu
Çevre dostu bir öneri al.

!yardim
Komutları tekrar göster.
"""
    await ctx.send(mesaj)


# Atık ayrışma süresi komutu
@bot.command()
async def ayrisma(ctx, *, atik_adi=None):

    if atik_adi is None:
        await ctx.send(
            "Lütfen bir atık adı yaz! Örnek: !ayrisma plastik şişe"
        )
        return

    atik_adi = atik_adi.lower().strip()

    if atik_adi in atiklar:
        sure = atiklar[atik_adi]

        await ctx.send(
            f"🌍 **{atik_adi.title()}** doğada yaklaşık {sure} sürede ayrışır!"
        )

    else:
        await ctx.send(
            "❌ Bu atık henüz veritabanımda yok. "
            "Başka bir atık deneyebilirsin!"
        )


# Atık listesi komutu
@bot.command()
async def liste(ctx):

    mesaj = "♻️ **EKOBOT ATIK LİSTESİ**\n\n"

    for atik in atiklar:
        mesaj += f"🌱 {atik.title()}\n"

    await ctx.send(mesaj)


# Çevre önerisi komutu
@bot.command()
async def ipucu(ctx):

    secilen_ipucu = random.choice(ipuclari)

    await ctx.send(
        f"💚 **EKOBOT'UN ÖNERİSİ**\n\n{secilen_ipucu}"
    )


# Botu çalıştır
bot.run("token yaz")
