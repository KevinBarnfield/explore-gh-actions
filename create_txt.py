import subprocess

# create_txt.py

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def get_last_commit_message():
    result = subprocess.run(['git', 'log', '-1', '--pretty=%B'], capture_output=True, text=True)
    return result.stdout.strip()

if __name__ == "__main__":
    filename = "output.txt"
    content = get_last_commit_message()
    write_to_file(filename, content)
    print(f"Last commit message written to {filename}")