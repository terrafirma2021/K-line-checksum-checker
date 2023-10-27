# K-line checksum checker
The Checksum Validator is a Python script that allows you to verify the validity of data bytes by calculating checksums. It can handle multiple entries, and you can input them one after the other. 
The script calculates the checksum for each entry and provides a "Valid" or "Not Valid" result.
Usage

    Clone or Download the Repository

    You can clone this repository to your local machine using Git or download the code as a ZIP file.

    bash

git clone https://github.com/YourUsername/checksum-validator.git

Run the Script

Make sure you have Python installed on your system. Open a terminal or command prompt and navigate to the repository's directory.

Run the script using the following command:

bash

python checksum_validator.py

Input Data

The script will prompt you to enter data bytes in hexadecimal format. You can enter either single or multiple entries at the same time, For example:


    Enter the data bytes in hex (e.g., 01 02 03) or type 'exit' to quit:
    01 02 03 04 05

    To exit the script, type 'exit'.

    Review Results

    The script will calculate the checksum for each entry and display whether it is "Valid" or "Not Valid." 
    Additionally, the results will be 
    saved in a file named "checked.txt" in the repository directory.

Example

Here's an example of how the script works:


Enter the data bytes in hex (e.g., 01 02 03) or type 'exit' to quit:
01 02 03 04 05
Checksum is Not Valid.

License

This project is licensed under the MIT License. Feel free to use and modify the code as needed.

Enjoy using the Checksum Validator! If you encounter any issues or have suggestions for improvement, please create an issue on this repository.
