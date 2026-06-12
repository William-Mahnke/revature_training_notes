import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

base_dir = os.path.dirname(os.path.abspath(__file__))


# ═══════════════════════════════════════════════════════
# 1 — RotatingFileHandler
# Rotates the log file based on FILE SIZE
# Once the file reaches maxBytes, it is renamed to
# app.log.1 and a fresh app.log is created
# backupCount controls how many old files to keep
# ═══════════════════════════════════════════════════════

rotating_logger  = logging.getLogger("rotating")
rotating_logger.setLevel(logging.DEBUG)

rotating_handler = RotatingFileHandler(
    filename    = os.path.join(base_dir, "app.log"),
    maxBytes    = 1_000_000,    # rotate after 1MB
    backupCount = 3             # keep app.log.1, app.log.2, app.log.3
)
rotating_handler.setLevel(logging.DEBUG)
rotating_handler.setFormatter(logging.Formatter(
    fmt     = "%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
))

rotating_logger.addHandler(rotating_handler)

rotating_logger.debug("RotatingFileHandler - debug message.")
rotating_logger.info("RotatingFileHandler - info message.")
rotating_logger.warning("RotatingFileHandler - warning message.")
rotating_logger.error("RotatingFileHandler - error message.")

# Once app.log hits 1MB the files rotate:
# app.log     ← current (fresh)
# app.log.1   ← previous
# app.log.2   ← older
# app.log.3   ← oldest (deleted when a 4th would be created)


# ═══════════════════════════════════════════════════════
# 2 — TimedRotatingFileHandler
# Rotates the log file based on TIME
# A new log file is created on the configured interval
# The old file is renamed with a timestamp suffix
# ═══════════════════════════════════════════════════════

timed_logger  = logging.getLogger("timed")
timed_logger.setLevel(logging.DEBUG)

timed_handler = TimedRotatingFileHandler(
    filename    = os.path.join(base_dir, "app_timed.log"),
    when        = "midnight",   # rotate once per day at midnight
    backupCount = 7             # keep the last 7 days of log files
)
timed_handler.setLevel(logging.DEBUG)
timed_handler.setFormatter(logging.Formatter(
    fmt     = "%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
))

timed_logger.addHandler(timed_handler)

timed_logger.debug("TimedRotatingFileHandler - debug message.")
timed_logger.info("TimedRotatingFileHandler - info message.")
timed_logger.warning("TimedRotatingFileHandler - warning message.")
timed_logger.error("TimedRotatingFileHandler - error message.")

# At midnight the files rotate:
# app_timed.log                    ← current (fresh)
# app_timed.log.2024-06-01         ← yesterday
# app_timed.log.2024-05-31         ← 2 days ago
# ...                              ← up to 7 days kept