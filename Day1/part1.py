import os

def calculate_calibration_sum(filename):
    total_sum = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                first_digit = next(char for char in line if char.isdigit())
                last_digit = next(char for char in reversed(line) if char.isdigit())
                calibration_value = int(first_digit + last_digit)
                total_sum += calibration_value

    return total_sum

if __name__ == "__main__":
    input_filename = "Day1\input.txt"

    # Print the current working directory
    print("Current working directory:", os.getcwd())

    # Full path to the input file
    input_filepath = os.path.join(os.getcwd(), input_filename)

    result = calculate_calibration_sum(input_filepath)
    print(f"The sum of calibration values is: {result}")
