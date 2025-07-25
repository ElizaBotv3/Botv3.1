ElizaBot/
│
├── main.py                      # Entry point: jalankan ElizaBot GUI
├── config.py                    # Tetapan global, API key, path, dll
├── requirements.txt             # Senarai modul Python yang digunakan
├── elizabot.db                  # SQLite database (chatlog & memori)
├── README.md                    # Penerangan projek (untuk rujukan)
│
├── assets/                      # Semua media & aset statik
│   ├── avatar/                  # Gambar avatar Eliza
│   ├── audio/                   # Suara Eliza atau notifikasi
│   └── emoji/                   # Fail emoji klasik (optional)
│
├── core/                        # Logik utama Eliza
│   ├── chatbot.py               # Logik Eliza classic
│   ├── eliza_infer.py           # Logik GPT response + mood
│   ├── emoji_map.py             # Pemetaan mood kepada emotikon
│   └── reaction_engine.py       # Sistem reaksi ikut emosi pengguna
│
├── memory/                      # Modul berkaitan memori & log
│   ├── chat_memory.py           # Simpan dan baca chatlog
│   ├── personal_memory.py       # Simpan minat, nama, dan info pengguna
│   ├── secure_log.py            # Sembunyikan/muncul semula chat sensitif
│   └── log_manager.py           # Urus backup, clear, atau export log
│
├── interface/                   # Antaramuka pengguna (GUI)
│   ├── gui_main.py              # Layout utama (Frame, TextBox, Button)
│   ├── gui_components.py        # Komponen UI kecil (emoji bar, custom btn)
│   └── gui_utils.py             # Fungsi bantu UI (scroll, insert_text)
│
├── tools/                       # Alat tambahan & sambungan
│   ├── device_tools.py          # Buka kamera, jam, nota dsb
│   ├── web_search.py            # Carian Google atau Wikipedia
│   ├── resource_monitor.py      # Pantau RAM, storage
│   ├── arabic_tools.py          # Bantu pembelajaran Bahasa Arab
│   └── crypto_tools.py          # Modul asas pelaburan/AI crypto
│
└── tests/                       # Ujian automatik
    ├── test_eliza.py            # Uji semua modul ElizaBot
    └── test_memory.py           # Uji sambungan DB & recovery log