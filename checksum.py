def calculate_checksum(data_bytes):
    # Skip the first byte if it's 01
    if data_bytes[0] == "01":
        data_bytes = data_bytes[1:]

    # Convert hex values to integers and calculate the sum
    data_sum = sum(int(byte, 16) for byte in data_bytes[:-1])  # Exclude the last byte (assumed checksum)

    # Calculate the checksum as a two-digit hexadecimal
    calculated_checksum = format(data_sum, '02X')

    return calculated_checksum

def main():
    while True:
        data_input = input("Enter the data bytes in hex (e.g., 01 02 03) or type 'exit' to quit: ")
        
        if data_input.lower() == 'exit':
            break

        data_lines = data_input.strip().split('\n')
        
        for data_line in data_lines:
            data_bytes = data_line.split()
            
            if len(data_bytes) < 2:
                print("At least two data bytes are required.")
                continue

            # Check if any hex value is a single digit, and if so, pad it with a 0
            data_bytes = [byte if len(byte) == 2 else '0' + byte for byte in data_bytes]

            provided_checksum = data_bytes[-1]
            calculated_checksum = calculate_checksum(data_bytes)

            if calculated_checksum == provided_checksum:
                result = "Valid"
            else:
                result = "Not Valid"

            # Append the result to checked.txt in the desired format
            with open("checked.txt", "a") as file:
                file.write(f"{' '.join(data_bytes)} - {result}\n")
                print(f"Checksum is {result}.")

if __name__ == "__main__":
    # Create checked.txt if it doesn't exist
    with open("checked.txt", "a") as file:
        pass  # This just creates the file if it doesn't exist

    main()
