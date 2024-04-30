#include <iostream>
#include <string>

// Function to remove vowels from a string
std::string removeVowels(std::string str) {
    std::string vowels = "aeiouAEIOU";
    for (int i = 0; i < str.length(); i++) {
        if (vowels.find(str[i])!= std::string::npos) {
            str.erase(i, 1);
            i--;
        }
    }
    return str;
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::cin >> input;
    std::string output = removeVowels(input);
    std::cout << "String with vowels removed: " << output << std::endl;
    return 0;
}