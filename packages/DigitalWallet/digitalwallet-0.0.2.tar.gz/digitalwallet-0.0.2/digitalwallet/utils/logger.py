import logging


def configure_logging(debug: bool) -> None:
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logging.getLogger("httpx").setLevel(logging.INFO if debug else logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)