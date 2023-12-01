#include <iostream>
#include <fstream>
#include <algorithm>
#include <ctype.h>
#include <string>

int main(int argc, char** argv) {
    if(argc != 2) {
        std::cout << "Usage: Day1 inputfile.txt\n";
        return 1;
    }

    std::ifstream file{argv[1]};
    if (file.fail()) {
        std::cerr << "Could not open the file " << argv[1] << std::endl;
    }


    std::string line;
    size_t sum = 0;
    size_t line_num = 0;
    while(std::getline(file, line)) {
        const auto first_num_it = std::find_if(line.begin(), line.end(), isdigit); 
        if (first_num_it == line.end()) {
            std::cerr << "Could not find the first number in the line " << line_num << std::endl;
        }

        const auto last_num_it = std::find_if(line.rbegin(), line.rend(), isdigit); 
        if (first_num_it == line.end()) {
            std::cerr << "Could not find the first number in the line " << line_num << std::endl;
        }

        std::string num_string{*first_num_it};
        num_string += *last_num_it;
        sum += std::stoi(num_string);

        line_num++;
    }

    std::cout << "Calibration number: " << sum << std::endl;
}