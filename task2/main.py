from pathlib import Path
from pprint import pprint

def get_cats_info(path: str) -> list[dict[str, object]]:
    current_dir = Path(__file__).parent
    file_path = current_dir / path
    cats_list: list[dict[str, object]] = []

    try:
        with file_path.open("r", encoding='utf-8') as file_obj:
            for line_number, line in enumerate(file_obj, start=1):
                line = line.strip()
                if not line:
                    continue  # skip empty lines

                parts = line.split(",", maxsplit=2)

                if len(parts) != 3:
                    print(f"Warning: Malformed line {line_number}: {line}")
                    continue

                id_, name, age_str = (p.strip() for p in parts)
                id_ = id_.lstrip("\ufeff")  # strip BOM if present

                # Try to convert age to int; keep original if it fails
                try:
                    age = int(age_str)
                    if age < 0:
                        raise ValueError
                except ValueError:
                    print(f"Warning: Invalid age on line {line_number}: '{age_str}'")
                    continue

                cats_list.append({
                    "id": id_,
                    "name": name,
                    "age": age,
                })

        return cats_list

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    pprint(cats_info)