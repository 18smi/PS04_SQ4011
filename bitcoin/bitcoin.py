import sys
import requests

API_key = "076e88e5f1f1b7ad721209ba66e0f98b4f88840a50fa375a6ea0450af92a99b5"

if len(sys.argv) != 2:# invalid amount of arguments
    sys.exit()

try:
    float(sys.argv[1])# if sys.argv[1] cant be converted to a float, exit
except (ValueError, TypeError):
    sys.exit()

answer = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + API_key)
string_answer = str(answer.content)
position = string_answer.find("priceUsd") + 11

string_extracted_float = ""
while string_answer[position] != '"':
    string_extracted_float += string_answer[position]
    position += 1
    
    
print(f"${float(string_extracted_float):,.4f}")


