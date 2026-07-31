import os
import subprocess

def fix_format():
    ideas_dir = 'ideas'

    files_to_format = []

    for root, dirs, files in os.walk(ideas_dir):
        if 'README.md' in files:
            files_to_format.append(os.path.join(root, 'README.md'))
        if 'README.fr.md' in files:
            files_to_format.append(os.path.join(root, 'README.fr.md'))

    print(f"Formatting {len(files_to_format)} files...")
    chunk_size = 50
    for i in range(0, len(files_to_format), chunk_size):
        chunk = files_to_format[i:i+chunk_size]
        subprocess.run(['npx', 'prettier', '--write'] + chunk, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("Done formatting.")

if __name__ == '__main__':
    fix_format()
