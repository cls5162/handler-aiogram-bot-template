from pathlib import Path

# apply base directory
BASE_DIR = Path(__name__).resolve().parent

# logging config file
LOGGING_CONF_FILE = BASE_DIR / 'logging.conf.txt'

# apply default language bot
DEFAULT_LANGUAGE_CODE = 'ru'

# Bot settings
TOKEN = 'MY_BOT_TOKEN'
PARSE_MODE = 'HTML'

# Database 
DB_DIR = BASE_DIR / 'database'
DB_APPLY = False