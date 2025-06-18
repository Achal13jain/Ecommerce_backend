# app/core/logger.py
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

#  root logger 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ecommerce")          # global project logger
logger.setLevel(logging.INFO)

# console handler 
console_fmt = "%(asctime)s | %(levelname)-8s | %(message)s"
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(console_fmt))

# rotating file handler
file_handler = TimedRotatingFileHandler(
    LOG_DIR / "app.log", when="midnight", backupCount=14, encoding="utf-8"#After 14 days old files are deleted automatically
)
file_handler.setFormatter(logging.Formatter(console_fmt))

logger.addHandler(console_handler)
logger.addHandler(file_handler)

#silence noisy uvicorn access logs, keep errors
logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
