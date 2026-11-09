import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("App started")
logging.warning("Low memory")
logging.error("App crashed")
