import random
import string

def generate_random_line():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(7))

def main():
    print("Most Codes Will Be Invalid.")
    num_lines = int(input("How Many Nitro Codes Would You Like To Generate>>>"))
    for i in range(num_lines):
        print(f"https://discord.gift/{generate_random_line()}")

    input("Press any key to exit...")

if __name__ == "__main__":
    main()