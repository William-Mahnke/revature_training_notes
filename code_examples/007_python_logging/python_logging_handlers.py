# ═══════════════════════════════════════════════════════
# WHAT ARE HANDLERS?
# Handlers control WHERE log messages are sent.
# A single logger can have MULTIPLE handlers attached,
# each sending output to a different destination.
#
# StreamHandler — outputs to the console
# FileHandler   — outputs to a file on disk
#
# Each handler can have its OWN logging level, meaning
# you can send DEBUG+ to a file but only ERROR+ to
# the console — all from the same logger
# ═══════════════════════════════════════════════════════
import logging
import os # So that we can log to this path

# ═══════════════════════════════════════════════════════
# COMBINING STREAM AND FILE HANDLERS
# One logger with TWO handlers:
# - FileHandler   → DEBUG and above  (everything)
# - StreamHandler → ERROR and above  (console only)
#
# This is a common real-world pattern:
#   Full detail goes to the log file for diagnostics
#   Only serious issues surface in the console
# ═══════════════════════════════════════════════════════

# ── Create the logger ──────────────────────────────────
app_logger = logging.getLogger("app")
app_logger.setLevel(logging.DEBUG)      # logger accepts everything
                                        # handlers decide what they output

# ── Shared formatter ──────────────────────────────────
formatter = logging.Formatter(
    fmt     = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)

# ── File Handler — DEBUG and above ────────────────────

# Use os module to build the log file path relative to this Python file
# Note - relative paths are preferred over absolute/hardcoded paths.
base_dir = os.path.dirname(os.path.abspath(__file__))
log_path  = os.path.join(base_dir, "app.log")

# Captures all messages for full diagnostics
file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter) # The log output will be the same for file and console logs

# ── Stream Handler — ERROR and above only ─────────────
# Only surfaces serious issues to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter) # The log output will be the same for file and console logs

# ── Attach both handlers to the same logger ────────────
app_logger.addHandler(file_handler)
app_logger.addHandler(console_handler)

# ── Emit messages ─────────────────────────────────────
app_logger.debug("Loading configuration...")
app_logger.info("Server started on port 8080.")
app_logger.warning("Response time is slower than expected.")
app_logger.error("Database connection failed.")
app_logger.critical("Application crashed — restarting.")


# ── What appears in the CONSOLE ───────────────────────
# Only ERROR and CRITICAL:
#
# 2024-06-01 10:30:00 | ERROR    | app | Database connection failed.
# 2024-06-01 10:30:00 | CRITICAL | app | Application crashed — restarting.


# ── What appears in app.log ───────────────────────────
# Everything from DEBUG upwards:
#
# 2024-06-01 10:30:00 | DEBUG    | app | Loading configuration...
# 2024-06-01 10:30:00 | INFO     | app | Server started on port 8080.
# 2024-06-01 10:30:00 | WARNING  | app | Response time is slower than expected.
# 2024-06-01 10:30:00 | ERROR    | app | Database connection failed.
# 2024-06-01 10:30:00 | CRITICAL | app | Application crashed — restarting.