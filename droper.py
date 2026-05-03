import re
import asyncio
from pyrogram import Client, filters

# --- CONFIGURATION ---
API_ID = 35136400
API_HASH = "04915ebbe766a2b94c9af013643519fb"

SOURCE_CHAT = -1003984452893 
TARGET_CHAT = "hacker_x_cc" 

app = Client("scraper_session", api_id=API_ID, api_hash=API_HASH)

# CC Pattern
CC_PATTERN = r"\d{15,16}[|/\s:-]+\d{2}[|/\s:-]+\d{2,4}[|/\s:-]+\d{3,4}"

# Duplicate CCs ko rokne ke liye ek set
processed_cards = set()

@app.on_message(filters.chat(SOURCE_CHAT))
async def main_logic(client, message):
    content = message.text or message.caption
    if content:
        cards = re.findall(CC_PATTERN, content)
        
        for card in cards:
            # Check agar ye card pehle hi drop ho chuka hai
            if card in processed_cards:
                print(f"⚠️ Duplicate CC skipped: {card}")
                continue

            print(f"✅ New CC Found: {card}")
            
            # Card ko processed list mein daal dein
            processed_cards.add(card)

            drop_text = (
                f"**CC:** `{card}`\n"
                f"**Status:** Approved ✅\n"
                f"**Gateway:** Stripe\n"
                f"**Checked by:** @hacker_x_cc\n\n"
                f"🗑️ _Auto-delete in 60s_"
            )

            try:
                # 1. Drop
                sent_msg = await client.send_message(TARGET_CHAT, drop_text)
                
                # 2. 10 Seconds wait
                await asyncio.sleep(60)

                # 3. Delete
                await sent_msg.delete()
                
                # Optional: Kuch der baad memory se card hata dein taaki agar 1 ghante baad wahi card phir aaye toh drop ho sake
                # processed_cards.remove(card) 

            except Exception as e:
                print(f"❌ Error: {e}")

print("🔥 Script Active! Double drop protection ON.")
app.run()