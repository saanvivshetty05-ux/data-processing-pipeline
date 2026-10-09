
import csv
import json
import logging
from pathlib import Path


def load_config():
    with open("config.json", "r") as file:
        return json.load(file)


def setup_logging(log_file):
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )


def read_data(filename):
    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    if path.suffix.lower() == ".csv":
        with open(path, "r", encoding="utf-8-sig", newline="") as file:
            return list(csv.DictReader(file))

    elif path.suffix.lower() == ".json":
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, dict):
            data = data.get("students")

        if not isinstance(data, list) or not all(
            isinstance(row, dict) for row in data
        ):
            raise ValueError("JSON must contain a list of records.")

        return data

    else:
        raise ValueError("Use a CSV or JSON input file.")


def clean_data(records, config):
    cleaned = []

    for row in records:
        name = str(row.get("name") or "").strip() or "Unknown"
        email = str(row.get("email") or "").strip().lower()

        try:
            age = int(row.get("age"))
            if not 0 <= age <= 120:
                age = ""
        except (ValueError, TypeError):
            age = ""

        try:
            marks = float(row.get("marks"))
            if not 0 <= marks <= config["max_marks"]:
                marks = config["missing_marks_default"]
        except (ValueError, TypeError):
            marks = config["missing_marks_default"]

        if marks == int(marks):
            marks = int(marks)

        cleaned.append({
            "name": name,
            "age": age,
            "marks": marks,
            "email": email
        })

    if config.get("remove_duplicates", True):
        unique = []
        seen = set()

        for row in cleaned:
            key = tuple(row.values())
            if key not in seen:
                seen.add(key)
                unique.append(row)

        cleaned = unique

    logging.info("Processed %s records", len(cleaned))
    return cleaned


def save_data(records, filename):
    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    fields = ["name", "age", "marks", "email"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)


def main():
    try:
        config = load_config()
        setup_logging(config["log_file"])

        logging.info("Pipeline started")

        records = read_data(config["input_file"])
        cleaned = clean_data(records, config)
        save_data(cleaned, config["output_file"])

        logging.info("Pipeline completed successfully")

        print("Pipeline completed successfully!")
        print("Input records:", len(records))
        print("Output records:", len(cleaned))
        print("Output saved to:", config["output_file"])

    except (OSError, ValueError, KeyError, TypeError) as error:
        logging.basicConfig(level=logging.ERROR)
        logging.error("Pipeline failed: %s", error)
        print("Error:", error)


if __name__ == "__main__":
    main()