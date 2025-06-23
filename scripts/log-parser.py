# A basic log parser to detect failed login attempts

def parse_logs(file_path):
    with open(file_path, "r") as file:
        for line in file:
            if "failed password" in line.lower():
                print(line.strip())
