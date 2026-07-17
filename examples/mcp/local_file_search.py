import os
from pathlib import Path


def search_files(root: str, query: str):
    root_path = Path(root)
    matches = []
    for file_path in root_path.rglob("*"):
        if file_path.is_file() and query.lower() in file_path.name.lower():
            matches.append(str(file_path))
    return matches


if __name__ == "__main__":
    root = os.getcwd()
    sample_results = search_files(root, "README")
    print(sample_results[:10])
