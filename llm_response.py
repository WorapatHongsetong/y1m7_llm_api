import os
import json
from pprint import pprint
from mistralai import Mistral



def extract_data() -> json:
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    equation_type = {
        "linear": {
            "structure":    "y = (a*x) + b",
            "constants":    ["a", "b", 0, 0, 0]
        },
        "polynomial deg=2": {
            "structure":    "y = a*(x**2) +b*x + c",
            "constants":    ["a", "b", "c", 0, 0]
        },
        "polynomial deg=3": {
            "structure":    "y = a*(x**3) + b*(x**2) + c*x + d",
            "constants":    ["a", "b", "c", "d", 0]
        },
        "polynomial deg=4": {
            "structure":    "y = a*(x**4) + b*(x**3) +c*(x**2) + d*x + e",
            "constants":    ["a", "b", "c", "d", "e"]
        },
        "sine": {
            "structure":    "y = a*sin(b*x) + c",
            "constants":    ["a", "b", "c", 0, 0]
        },
        "cosine": {
            "structure":    "y = a*cos(b*x) + c",
            "constants":    ["a", "b", "c", 0, 0]
        }
    }

    data_json_str = json.dumps(equation_type, indent=2)

    ans = {
            "equation type":    "equation type",
            "equation title":   "equation title",
            "interval":         ["min", "max"],
            "coefficients":     ["a", "b", "c", "d", "e"]
        }
    
    ans_json_str = json.dumps(ans, indent=2)

    prompt = "The data showed type of equations you can response, including structure of equation. Your task is to extract information from User Input.\n" +\
    "You should extract, equation type (e.g. linear, cosine), equation title (e.g. \'y = 3x + 4\'), interval (e.g. [-5.0, 30.1]), coefficient (e.g. [1, 2, 3, 0, 0])\n" +\
    "Example User Input: \' Hey please plot 3sin(x)+1 in interval [-2, 2]\', then the values are: equation type = sine, equation title = 3sin(x)+1, interval = [-2, 2], coefficient = [3, 1, 1, 0, 0]\n" +\
    "Or if User Input is about want to exit, then all value is None except \'exit\' = True. Else \'exit\' = False.\n" +\
    "VERY IMPORTANT, response should be collapsed json format, ONLY json format, don't bring anything else...\n" +\
    "Example: {\'equation type\': \'linear\', \'equation title\': \'3x + 5\', \'interval\': [6,100], \'coefficients\': [3, 5, 0, 0, 0],\'exit\': false}"

    user_input = input("User Input: ")

    message_content = f"Data:\n{data_json_str}\n\nExample Response:\n{ans_json_str}\n\nPrompt:\n{prompt}\n\nUser Input:\n{user_input}"

    messages = [
        {
            "role": "user",
            "content": message_content,
        }
    ]

    chat_response = client.chat.complete(
        model=model,
        messages=messages,
        response_format={
            "equation type":    "equation type",
            "equation title":   "equation title",
            "interval":         ["min", "max"],
            "coefficients":     ["a", "b", "c", "d", "e"],
            "exit":             False
        }
    )

    result = chat_response.choices[0].message.content
    print(result, type(result))

    return result



if __name__ == "__main__":
    extract_data()