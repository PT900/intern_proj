#include <iostream>
#include <fstream>
#include <string>

int main() {
    // Prompt the user for JSON input
    std::cout << "Enter JSON data (Enter an empty line to end input):" << std::endl;
    std::string jsonData;
    std::string line;

    while (std::getline(std::cin, line) && !line.empty()) {
        jsonData += line + '\n';
    }

    // Remove the last newline character if jsonData is not empty
    if (!jsonData.empty()) {
        jsonData.pop_back();
    }

    // Name of the file to be created
    const char* filename = "test.txt";

    // Create an output file stream object
    std::ofstream outputFile;

    // Open the file in output mode, which creates the file if it doesn't exist
    outputFile.open(filename);

    // Check if the file was successfully opened
    if (!outputFile) {
        std::cerr << "Error opening the file." << std::endl;
        return 1;
    }

    // Write the JSON data to the file
    outputFile << jsonData;

    // Close the file
    outputFile.close();

    std::cout << "File created successfully and JSON data written." << std::endl;

    return 0;
}
