import argparse
import logging
from pathlib import Path
from dotenv import load_dotenv

# Standard project paths
ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT_DIR / "data"
ASSETS_DIR = ROOT_DIR / "assets"
OUTPUT_DIR = ROOT_DIR / "output"
TEMPLATES_DIR = ROOT_DIR / "templates"
CREDENTIALS_DIR = ROOT_DIR / ".credentials"

load_dotenv(ROOT_DIR / ".env")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def run(debug: bool = False) -> None:
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled.")

    logger.info("Starting pipeline...")
    # TODO: Import and call modular functions from app/
    logger.info("Pipeline complete. Outputs saved to %s", OUTPUT_DIR)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the project pipeline.")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()
    run(debug=args.debug)


if __name__ == "__main__":
    main()
