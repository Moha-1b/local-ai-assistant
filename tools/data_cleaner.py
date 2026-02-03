import csv

def clean_csv(input_file: str, output_file: str):
    cleaned_rows = []

    with open(input_file, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        cleaned_rows.append(header)

        for row in reader:
            if any(cell.strip() for cell in row):
                cleaned_rows.append(row)

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(cleaned_rows)

    return f"Cleaned data saved to {output_file}"
