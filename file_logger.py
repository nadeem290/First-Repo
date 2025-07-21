import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def write_log():
    logging.info("This is a log message from file_logger.py")

if __name__ == "__main__":
    write_log()
