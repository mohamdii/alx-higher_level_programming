import sys

def add_arguments():
    # Extract arguments excluding the script name
    arguments = sys.argv[1:]

    # Initialize the result to 0
    result = 0

    # Loop through each argument and add it to the result
    for arg in arguments:
        result += int(arg)

    # Print the result
    print(result)

if __name__ == "__main__":
    add_arguments()

