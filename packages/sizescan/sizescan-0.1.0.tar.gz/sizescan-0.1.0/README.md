# SizeScan

SizeScan is a script that displays the sizes of subfolders or files within a specified folder. It highlights items in red if they exceed a specified size limit.

## Features

- Display the sizes of subfolders within a specified folder.
- Option to display the sizes of files instead of subfolders.
- Highlight items that exceed a specified size limit.

## Requirements

- Python 3.x
- `tqdm`
- `rich`

You can install the required packages using pip:

```bash
pip install tqdm rich
```

## Usage

```bash
sizescan <folder> [-mb <max_mb>] [-f]
```

### Arguments

- `<folder>`: The folder to scan and display sizes.
- `-mb`, `--max-mb`: The size limit in MB. Items exceeding this size will be highlighted in red. Default is 1000 MB.
- `-f`, `--files`: Display sizes of files instead of subfolders.

### Examples

#### Display sizes of subfolders:

```bash
sizescan /path/to/folder
```

#### Display sizes of files:

```bash
sizescan /path/to/folder -f
```

#### Highlight items exceeding 500 MB:

```bash
sizescan /path/to/folder -mb 500
```

#### Display sizes of files and highlight items exceeding 200 MB:

```bash
sizescan /path/to/folder -f -mb 200
```

