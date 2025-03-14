from hydrogram import Client, filters

santhu = Client(
     "exbot",
     api_id=22363963,
     api_hash="5c096f7e8fd4c38c035d53dc5a85d768",
     bot_token="7674626915:AAHjzGn0s-aiq9ZftFEvMTW2G7Oh-7jCpX0"
)

#command creation
@santhu.on_message(filters.command("start") & filters.group)
async def start(client, message):
    await message.reply_text("Hello World")

santhu.run()
