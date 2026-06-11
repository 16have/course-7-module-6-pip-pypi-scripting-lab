from datetime import datetime


def generate_log(log_entries):
    """Generate a log file from a list of entries and return the filename.

    Raises ValueError if log_entries is not a list.
    """
    if not isinstance(log_entries, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

    print(f"Log file created: {filename}")
    return filename