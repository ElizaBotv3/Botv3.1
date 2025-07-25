import tkinter as tk
from interface.gui_main import ChatInterface
from core import chat_memory as chat_db
from core.eliza_infer import infer_response
from core.reaction_engine import detect_emotion
from core.resource_monitor import get_system_status
from core.emoji_map import apply_emojis
from config import APP_TITLE

def main():
    root = tk.Tk()
    root.title(APP_TITLE or "ElizaBot v3")
    root.geometry("420x650")

    # Inisialisasi database dan cipta table jika belum ada
    chat_db.init_db()

    # Cipta antaramuka aplikasi
    app = ChatInterface(
        master=root,
        send_callback=lambda msg, insert: handle_user_message(msg, insert),
        monitor_callback=lambda: get_system_status()
    )

    # Muat semula sejarah chat dari database
    history = chat_db.get_chat_history(limit=50)
    for sender, msg, timestamp in history:
        app.insert_text(sender, msg)

    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

def handle_user_message(user_msg, insert_text_fn):
    """Urus mesej pengguna dan balasan Eliza"""
    if not user_msg.strip():
        return

    # Papar dan simpan mesej pengguna
    insert_text_fn("You", user_msg)
    chat_db.add_message("user", user_msg)

    # Kenal pasti emosi dan hasilkan balasan Eliza
    mood = detect_emotion(user_msg)
    eliza_reply = infer_response(user_msg, mood)
    eliza_reply = apply_emojis(eliza_reply, mood)

    # Simpan dan paparkan balasan Eliza
    chat_db.add_message("eliza", eliza_reply)
    insert_text_fn("Eliza", eliza_reply)

if __name__ == "__main__":
    main()