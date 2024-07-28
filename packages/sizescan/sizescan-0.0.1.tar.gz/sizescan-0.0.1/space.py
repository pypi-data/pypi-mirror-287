#!/usr/bin/env python3

import os
import math
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from rich.console import Console

console = Console()

def get_folder_size(folder):
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(folder):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):  # Skip symbolic links
                    total_size += os.path.getsize(fp)
    except Exception as e:
        console.log(f"[red]Error calculating size for folder: {folder}[/]")
        console.log(f"[red]Exception: {e}[/]")
        traceback.print_exc()
    return total_size

def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        console.log(f"[red]Error calculating size for file: {file_path}[/]")
        console.log(f"[red]Exception: {e}[/]")
        traceback.print_exc()
        return 0

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def process_folder(folder, progress_bar):
    folder_size = get_folder_size(folder)
    progress_bar.update(1)
    return folder, folder_size

def process_file(file_path, progress_bar):
    file_size = get_file_size(file_path)
    progress_bar.update(1)
    return file_path, file_size

def display_sizes(folder, mb, show_files):
    console.print(f"[bold blue]Scanning folder: {folder}[/]")

    items = []
    if show_files:
        items = [os.path.join(folder, item) for item in os.listdir(folder) if os.path.isfile(os.path.join(folder, item))]
    else:
        items = [os.path.join(folder, item) for item in os.listdir(folder) if os.path.isdir(os.path.join(folder, item))]
    
    total_items = len(items)
    results = []

    with tqdm(total=total_items, desc="Scanning items") as progress_bar:
        with ThreadPoolExecutor() as executor:
            if show_files:
                futures = {executor.submit(process_file, item, progress_bar): item for item in items}
            else:
                futures = {executor.submit(process_folder, item, progress_bar): item for item in items}

            for future in as_completed(futures):
                try:
                    item, size = future.result()
                    results.append((item, size))
                except Exception as e:
                    console.log(f"[red]Error processing item: {futures[future]}[/]")
                    console.log(f"[red]Exception: {e}[/]")
                    traceback.print_exc()

    for item, size in results:
        size_str = convert_size(size)
        if size > int(mb) * 1024 * 1024:
            console.print(f"[red]{item} - {size_str}[/]")
        else:
            console.print(f"{item} - {size_str}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Display sizes of subfolders or files")
    parser.add_argument("folder", help="Folder to display sizes of subfolders or files")
    parser.add_argument("-mb", "--max-mb", default=1000, help="Show item in red color if it exceeds this size (in MB)")
    parser.add_argument("-f", "--files", action="store_true", help="Display sizes of files instead of subfolders")

    args = parser.parse_args()

    display_sizes(args.folder, args.max_mb, args.files) 
