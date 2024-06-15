import argparse
import os
import io


def is_file_binary(filename : str) :
    with io.open(filename, mode='rb') as fil:
        for chunk in iter(lambda: fil.read(1024), bytes()):
            if b'\0' in chunk: # found null byte
                return True
    return False 

def recursive_file_search(dir : str) -> dict[str, int]:
    files = {}
    for f in os.listdir(dir):
        if os.path.isfile(dir+"/"+f):
            with open(dir+"/"+f, "r") as fil:
                if not is_file_binary(dir+"/"+f):
                    files[dir+"/"+f] = len(fil.read().split("\n"))
        elif os.path.isdir(dir+"/"+f):
            tmp = recursive_file_search(dir+"/"+f)
            for key in tmp.keys():
                files[key] = tmp[key]
    return files

def count_dir(dir : str) -> int:
    files = recursive_file_search(dir)

    total_lines = 0
    for f in files:
        total_lines += files[f]
    
    return total_lines

def file_podium(dir : str):
    files = recursive_file_search(dir)
    fls = list(files.keys())
    fls.sort(key = lambda x: files[x])

    try: print(f"Largest file: {fls[len(fls)-1]} with a length of {files[fls[len(fls)-1]]} lines")
    except IndexError: pass
    try: print(f"Second largest file: {fls[len(fls)-2]} with a length of {files[fls[len(fls)-2]]} lines")
    except IndexError: pass
    try:print(f"Third largest file: {fls[len(fls)-3]} with a length of {files[fls[len(fls)-3]]} lines")
    except IndexError: pass
    print()
    try:print(f"Smallest file: {fls[0]} with a length of {files[fls[0]]} lines")
    except IndexError: pass
    try: print(f"Second smallest file: {fls[1]} with a length of {files[fls[1]]} lines")
    except IndexError: pass
    try:print(f"Third smallest file: {fls[2]} with a length of {files[fls[2]]} lines")
    except IndexError: pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser("linecount")
    parser.add_argument("directory", help = "The target directory for linecount")
    parser.add_argument("-p", "--podium", action = "store_true", help = "Print the three largest and three smallest files in the directory")

    args = parser.parse_args()

    print(f"Amount of lines in '{args.directory}': {count_dir(args.directory)}")
    if args.podium:
        print()
        file_podium(args.directory)
