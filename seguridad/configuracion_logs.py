import logging, os
from logging.handlers import RotatingFileHandler

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("SISMARL")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("logs/sismarl.log", maxBytes=5000000, backupCount=3)
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def obtener_logger():
    return logger
