from pathlib import Path
import sys
from colorama import init, Fore, Style

# Initialize colorama (needed for Windows)
init(autoreset=True)


def display_dir_structure(path: str, indent: str = ""):
    try:
        directory = Path(path)

        if not directory.exists():
            print(Fore.RED + f"Error: {path} does not exist." + Style.RESET_ALL)
            return
        if not directory.is_dir():
            print(Fore.RED + f"Error: {path} is not a directory." + Style.RESET_ALL)
            return

        try:
            items = sorted(directory.iterdir())
        except PermissionError:
            print(Fore.RED + f"{indent}🚫 Permission denied: {directory}" + Style.RESET_ALL)
            return
        except OSError as e:
            print(Fore.RED + f"{indent}⚠️ OS error accessing {directory}: {e}" + Style.RESET_ALL)
            return

        for item in items:
            try:
                if item.is_dir():
                    print(f"{indent}{Fore.BLUE}📂 {item.name}/" + Style.RESET_ALL)
                    display_dir_structure(item, indent + "    ")
                else:
                    print(f"{indent}{Fore.GREEN}📄 {item.name}" + Style.RESET_ALL)
            except PermissionError:
                print(Fore.RED + f"{indent}🚫 Permission denied: {item}" + Style.RESET_ALL)
            except OSError as e:
                print(Fore.RED + f"{indent}⚠️ Error reading {item}: {e}" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"❌ Unexpected error: {e}" + Style.RESET_ALL)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        display_dir_structure(sys.argv[1])
    else:
        print(Fore.YELLOW + "Usage: python script.py <directory>" + Style.RESET_ALL)
