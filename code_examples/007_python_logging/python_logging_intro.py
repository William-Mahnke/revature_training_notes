#  ═══════════════════════════════════════════════════════
# WHAT IS LOGGING?
# Logging is the practice of recording messages about
# your program's execution to help with debugging,
# monitoring, and tracking errors.
#
# Python's built-in 'logging' module provides five
# severity levels (lowest to highest):
#
# DEBUG    — detailed diagnostic information
# INFO     — confirmation that things are working
# WARNING  — something unexpected, but not an error
# ERROR    — a serious problem — something failed
# CRITICAL — a severe error — program may not continue
# ═══════════════════════════════════════════════════════

# Import logging module to leverage logging tool suite
import logging


# ═══════════════════════════════════════════════════════
# 1 — BASIC CONFIGURATION
# basicConfig() configures the root logger
# Call this ONCE at the start of your program (from your 'main.py')
# This configuration will apply to any loggers created in your
# other modules
#
# level   — the minimum severity level to display
# format  — how each log message is formatted
# datefmt — how the timestamp is formatted
# name    — shows the name of the logger
# ═══════════════════════════════════════════════════════

logging.basicConfig(
    level   = logging.DEBUG,
    format  = "%(asctime)s | %(levelname)-8s | %(name)-4s | %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)


# ═══════════════════════════════════════════════════════
# 2 — EMITTING LOG MESSAGES
# ═══════════════════════════════════════════════════════

# ── One message per level ──────────────────────────────
print (" ==== " * 5)
print ("Logging Levels")
print (" ==== " * 5)
logging.debug("Starting application...")
logging.info("Configuration loaded successfully.")
logging.warning("Config file not found — using defaults.")
logging.error("Failed to connect to the database.")
logging.critical("System is out of memory — shutting down.")

# 2024-06-01 10:30:00 | DEBUG    | Starting application...
# 2024-06-01 10:30:00 | INFO     | Configuration loaded successfully.
# 2024-06-01 10:30:00 | WARNING  | Config file not found — using defaults.
# 2024-06-01 10:30:00 | ERROR    | Failed to connect to the database.
# 2024-06-01 10:30:00 | CRITICAL | System is out of memory — shutting down.


# ── Logging with variable data ─────────────────────────

emp_name = "Joseph"
emp_id   = 100

print (" ==== " * 5)
print ("Logging Variable Data")
print (" ==== " * 5)
logging.info(f"Employee loaded     : {emp_name} (ID: {emp_id})")
logging.warning(f"Login attempt failed: {emp_name}")
logging.error(f"Record not found    : employee ID {emp_id}")

# 2024-06-01 10:30:00 | INFO     | Employee loaded     : Joseph (ID: 100)
# 2024-06-01 10:30:00 | WARNING  | Login attempt failed: Joseph
# 2024-06-01 10:30:00 | ERROR    | Record not found    : employee ID 100


# ── Logging inside a function ──────────────────────────

def divide(a, b):
    logging.debug(f"divide() called with a={a}, b={b}")
    if b == 0:
        logging.error("Division by zero attempted.")
        return None
    result = a / b
    logging.info(f"Division result: {result}")
    return result

print (" ==== " * 5)
print ("Logging from Function Calls")
print (" ==== " * 5)
divide(10, 2)
divide(10, 0)

# 2024-06-01 10:30:00 | DEBUG    | divide() called with a=10, b=2
# 2024-06-01 10:30:00 | INFO     | Division result: 5.0
# 2024-06-01 10:30:00 | DEBUG    | divide() called with a=10, b=0
# 2024-06-01 10:30:00 | ERROR    | Division by zero attempted.


# ═══════════════════════════════════════════════════════
# 3 — NAMED LOGGERS
# Rather than using the root logger (logging.info etc.)
# best practice is to create a NAMED logger using
# getLogger(__name__)
#
# __name__ automatically resolves to the name of the
# module it lives in — in the main file it becomes
# "__main__", in other modules it becomes their
# filename e.g. "employee" or "database"
# ═══════════════════════════════════════════════════════

logger = logging.getLogger(__name__)

print (" ==== " * 5)
print ("Named Loggers")
print (" ==== " * 5)
logger.info("Application started.")
logger.warning("Low disk space detected.")
logger.error("Unexpected shutdown.")

# 2024-06-01 10:30:00 | INFO     | Application started.
# 2024-06-01 10:30:00 | WARNING  | Low disk space detected.
# 2024-06-01 10:30:00 | ERROR    | Unexpected shutdown.

# # ── Simulating multiple modules with named loggers ─────
# # In a real application each module would call
# # logging.getLogger(__name__) at the top of the file
# # Here we simulate that with descriptive names

# auth_logger     = logging.getLogger("auth")
# db_logger       = logging.getLogger("database")
# payment_logger  = logging.getLogger("payments")

# # ── Each logger identifies its source ─────────────────

# print (" ==== " * 5)
# print ("Named Loggers (Simulation)")
# print (" ==== " * 5)
# auth_logger.info("User 'Revature' logged in successfully.")
# auth_logger.warning("Failed login attempt for user 'unknown'.")

# db_logger.info("Database connection established.")
# db_logger.error("Query timeout after 30 seconds.")

# payment_logger.info("Payment of $99.99 processed for user 'Joseph'.")
# payment_logger.critical("Payment gateway unreachable.")