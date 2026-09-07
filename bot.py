import os
import asyncio
from telegram import Update
from telegram.ext import Application, ChatMemberHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def novo_membro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    membro = update.chat_member

    if membro.new_chat_member.status in ["member", "restricted"]:
        user_id = membro.new_chat_member.user.id
        chat_id = update.effective_chat.id

        await asyncio.sleep(30)

        try:
            await context.bot.ban_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )
            await context.bot.unban_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )
        except Exception as e:
            print(f"Erro: {e}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        ChatMemberHandler(
            novo_membro,
            ChatMemberHandler.CHAT_MEMBER
        )
    )

    print("Bot funcionando!")
    app.run_polling()

if __name__ == "__main__":
    main()
