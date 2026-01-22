import os

def format_size(size):
     """Convert bytes to KB, MB, GB for readability."""
     for unit in ['B', 'KB', 'MB', 'TB']:
          if size < 1024:
               return f"{size:.2f} {unit}"
          size /= 1024
     return f"{size:.2f} PB"


def analyze_directory(path):
    total_files = 0
    total_folders = 0
    total_size = 0
    files_by_ext = {}
    largest_files = []

    for root, dirs, files in os.walk(path):
        total_folders += len(dirs)

        for file in files:
            if file.startswith("."):
                 continue  # skip hidden files
            total_files += 1
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
            except (OSError, PermissionError):
                size = 0
            total_size += size

            # --- Track extension ---
            _, ext = os.path.splitext(file)
            if ext == "":
                ext = "No Extension"
            files_by_ext[ext] = files_by_ext.get(ext, 0) + 1

            # --- Track largest files ---
            largest_files.append((size, file_path))


    # Sort largest files
    largest_files.sort(reverse=True, key=lambda x: x[0])
    top_5_files = largest_files[:5]

    # Output results
    print("\nAnalysis Complete:")
    print(f"Total folders: {total_folders}")
    print(f"Total files: {total_files}")
    print(f"Total size (bytes): {total_size}")


    print("\nFiles by extension:")
    for ext, count in files_by_ext.items():
        print(f"{ext}: {count} files")

    print("\nTop 5 largest files:")
    for size, path in top_5_files:
        print(f"{path} ({size} bytes)")


def main():
    path = input("Enter the directory to analyze: ").strip()
    if not os.path.exists(path):
        print("Path does not exist.")
        return
    if not os.path.isdir(path):
        print("Path is not a directory.")
        return

    analyze_directory(path)

if __name__ == "__main__":
    main()