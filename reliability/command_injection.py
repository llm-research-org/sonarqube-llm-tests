import os

def delete_file(filename):
    cmd = "rm " + filename  # Vulnerable to injection
    os.system(cmd)
    return f"Deleted {filename}"