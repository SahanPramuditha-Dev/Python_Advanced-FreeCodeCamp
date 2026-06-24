import logging

# create logger (represents the current module)
logger = logging.getLogger(__name__)

# allow all log levels to pass through logger
logger.setLevel(logging.DEBUG)

# handler that prints logs to console
stream_h = logging.StreamHandler()

# handler that writes logs to a file
file_h = logging.FileHandler('file.log')

# stream shows only WARNING and above
stream_h.setLevel(logging.WARNING)

# file stores only ERROR and above
file_h.setLevel(logging.ERROR)

# define log message format
formatter = logging.Formatter(
    '%(name)s - %(levelname)s - %(message)s'
)

# apply format to handlers
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# attach handlers to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

# test logs
logger.warning('this is a warning')
logger.error('this is an error')