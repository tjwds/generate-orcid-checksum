'''public static String generateCheckDigit(String baseDigits) {
    int total = 0;
    for (int i = 0; i < baseDigits.length(); i++) {
        int digit = Character.getNumericValue(baseDigits.charAt(i));
        total = (total + digit) * 2;
    }
    int remainder = total % 11;
    int result = (12 - remainder) % 11;
    return result == 10 ? "X" : String.valueOf(result);
}'''

def generateCheckDigit(baseDigits):
    total = 0
    for i in str(baseDigits):
        total = (total + int(i)) * 2
    remainder = total % 11
    result = (12 - remainder) % 11
    if result == 10:
        result = "X"
    return result

#print(generateCheckDigit(17038381))

if __name__ == "__main__":
    generateCheckDigit()
