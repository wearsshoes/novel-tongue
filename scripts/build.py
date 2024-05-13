"""Build script for the app."""

import os
import subprocess
import time
import argparse
import shutil

def copy_app():
    """Copy the app.py file to the build directory."""
    app_file = "app.py"
    build_dir = "../build"

    # Copy the app.py file to the build directory
    shutil.copy(app_file, build_dir)


def convert_notebooks():
    """Convert Jupyter notebooks to Python scripts using nbconvert."""
    notebook_dir = "notebooks"
    output_dir = "../pages"

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get a list of all Jupyter notebook files in the notebook directory
    notebook_files = [file for file in os.listdir(notebook_dir) if file.endswith(".ipynb")]

    for notebook_file in notebook_files:
        notebook_path = os.path.join(notebook_dir, notebook_file)
        output_path = os.path.join(output_dir, os.path.splitext(notebook_file)[0])

        # Convert the Jupyter notebook to a Python script using nbconvert
        subprocess.run(["jupyter", "nbconvert", "--to", "python", notebook_path, "--output", output_path], check=True)

def watch_notebooks():
    """Watch for changes in the notebook files and rebuild when a change is detected."""
    notebook_dir = "../notebooks"
    last_modified_times = {}

    while True:
        # Get the current modification times of the notebook files
        current_modified_times = {}

        app_file = "app.py"
        app_path = os.path.join(notebook_dir, app_file)
        current_modified_times[app_file] = os.path.getmtime(app_path)

        for notebook_file in os.listdir(notebook_dir):
            if notebook_file.endswith(".ipynb"):
                notebook_path = os.path.join(notebook_dir, notebook_file)
                current_modified_times[notebook_file] = os.path.getmtime(notebook_path)

        # Check if any notebook files have been modified
        if last_modified_times != current_modified_times:
            print("Changes detected. Rebuilding...")
            copy_app()
            convert_notebooks()
            last_modified_times = current_modified_times

        # Wait for a short interval before checking again
        time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description="Build script for converting Jupyter notebooks to Python scripts.")
    parser.add_argument("--watch", action="store_true", help="Watch for changes in notebooks and rebuild automatically.")
    args = parser.parse_args()

    if args.watch:
        print("Watching for changes in notebooks...")
        watch_notebooks()
    else:
        convert_notebooks()

if __name__ == "__main__":
    main()
