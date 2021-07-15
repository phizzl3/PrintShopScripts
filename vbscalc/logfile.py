"""
Writes the data_set info to a text file in the "logs" directory
"""

from datetime import datetime
from pathlib import Path

TODAY = datetime.today()
DATE = f"{TODAY.month}/{TODAY.day}/{TODAY.year}"
LOG = Path(__file__).resolve().parent / "logs" / "vbs_log.txt"


def write(data_set: dict) -> None:

    with open(LOG, "a") as log:
        # Write the date
        log.write(f"{DATE}\n")
        # Write the data
        for each, total in data_set.items():
            log.write(f"{each}: {total}\n")
        log.write("\n")
