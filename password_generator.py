import random
import string
import sys

def generate_simple(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_strong(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    mode = "strong"
    length = 12
    if len(sys.argv) >= 2:
        mode = sys.argv[1].lower()
    if len(sys.argv) >= 3:
        try:
            length = int(sys.argv[2])
        except ValueError:
            print("Invalid length, using default.")
    if mode == "simple":
        print(generate_simple(length))
    else:
        print(generate_strong(length))

if __name__ == "__main__":
    main()
