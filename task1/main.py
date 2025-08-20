from pathlib import Path

def total_salary(path: str) -> tuple[int, int]:
    current_dir = Path(__file__).parent
    file_path = current_dir / path

    total_salary_amount = 0
    number_of_developers = 0

    try:
        with file_path.open("r", encoding='utf-8') as file_obj:
            for line_number, line in enumerate(file_obj, start=1):
                developer_info = line.strip().split(',', 1)
                if len(developer_info) == 2:
                    salary_str = developer_info[1].strip()

                    if salary_str.isdigit():
                        number_of_developers += 1
                        total_salary_amount += int(salary_str)
                    else:
                        print(f"Warning: Invalid salary '{salary_str}' on line {line_number}")
                else:
                    print(f"Warning: Malformed line {line_number}: {line.strip()}") 

        if number_of_developers == 0:
            print("No valid salary entries found.")
            return (0, 0)

        average_salary = total_salary_amount // number_of_developers
        return (total_salary_amount, average_salary)

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return (0, 0)


if __name__ == "__main__":
    total_salary_amount, average_salary = total_salary("salary.txt")
    print(f"Total amount of salary: {total_salary_amount}, Average salary: {average_salary}")  
