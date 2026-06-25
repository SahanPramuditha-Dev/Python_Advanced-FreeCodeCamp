import logging
import traceback

logging.basicConfig(level=logging.ERROR)

try:
    a = [1, 2, 3]
    val = a[4]   # this will raise IndexError

except:
    logging.error("An error occurred:\n%s", traceback.format_exc())