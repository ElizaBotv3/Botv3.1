# config.py

# Tajuk aplikasi (boleh digunakan di main.py atau GUI)
APP_TITLE = "ElizaBot v3"

# Nama fail database
DB_PATH = "elizabot.db"

# Had jumlah mesej disimpan dalam sejarah UI
CHAT_HISTORY_LIMIT = 50

# Mod pembangunan (True = aktifkan log tambahan)
DEBUG_MODE = True

# GPT settings (optional jika guna GPT)
USE_GPT = False
GPT_API_KEY = ""  # Masukkan API key jika guna GPT
GPT_MODEL = "gpt-4"  # atau "gpt-3.5-turbo", dll

# Bahasa lalai (boleh auto tukar ikut user dalam eliza_infer.py)
DEFAULT_LANGUAGE = "auto"  # 'en', 'ms', atau 'auto'

# Mood lalai jika tak dapat kesan emosi
DEFAULT_MOOD = "neutral"

# Fail reaction profile
REACTION_PROFILE_PATH = "memory/reaction_profile.json"

# Emoji mapping file (optional)
EMOJI_MAP_PATH = "core/emoji_map.py"

# Logo/avatar Eliza
AVATAR_PATH = "assets/avatar/eliza_default.png"

# Fail log untuk error
ERROR_LOG_FILE = "logs/error_log.txt"

# Kata kunci untuk unlock chat rahsia
UNLOCK_CODE = "3L124"

# Frasa trigger untuk clear chat (tanpa padam data sebenar)
CLEAR_COMMAND = "/clear"