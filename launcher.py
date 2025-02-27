import requests
import zipfile
import os
from io import BytesIO
import subprocess


def download_and_extract_zip(url, extract_to="extracted"):
    try:
        # Step 1: Download the zip file
        print(f"Downloading from {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses

        # Step 2: Extract the zip file
        print("Extracting the zip file...")
        with zipfile.ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(extract_to)

        print(f"Files extracted to '{extract_to}'.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
        input("нажмите любую кнопку")
        return False
    except zipfile.BadZipFile:
        print("Error: The downloaded file is not a valid zip file.")
        input("нажмите любую кнопку")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        input("нажмите любую кнопку")
        return False

    return True


def run_commands(commands, working_dir):
    try:
        for command in commands:
            print(f"Running command: {command}")
            result = subprocess.run(command, cwd=working_dir, shell=True, check=True, text=True)
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while running command '{e.cmd}': {e}")
        input("нажмите любую кнопку")
    except Exception as e:
        print(f"An unexpected error occurred while running commands: {e}")
        input("нажмите любую кнопку")


if __name__ == "__main__":
    var = input('скачать или запустить (dov || run)')


    str = input("введите номер версии (скопируйте с гитхаба без v)")


    # URL of the zip file
    zip_url = "https://github.com/macs687/Voxel_Craft_Rust/archive/refs/tags/" + "v" + str + ".zip"

    # Directory to extract the contents
    extract_directory = r"./versions"

    if var == "dov":
        if download_and_extract_zip(zip_url, extract_to=extract_directory):
            # Step 2: Define the working directory and commands
            working_directory = os.path.join(extract_directory, "Voxel_Craft_Rust-" + str)
            commands_to_run = [
                "cargo run"
            ]

            # Step 3: Run the commands
            run_commands(commands_to_run, working_directory)
        else:
            print("run error")
            input("нажмите любую кнопку")
    elif var == "run":
        try:
            working_directory = os.path.join(extract_directory, "Voxel_Craft_Rust-" + str)
            commands_to_run = [
                "cd ./target/debug/",
                "./Voxel_Craft_Rust.exe"
            ]

            # Step 3: Run the commands
            run_commands(commands_to_run, working_directory)
        except Exception as e :
            print("скорее всего эта версия не скачана")
            print("run errror", e)


