import numpy as np

"""
response_format={
                    "equation type":    "equation type",
                    "equation title":   "equation title",
                    "interval":         ["min", "max"],
                    "coefficients":     ["a", "b", "c", "d", "e"],
                    "exit":             False
                }
"""

"""
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
"""

def check_data_valid(input_json: dict) -> tuple[list, str]:

    data = input_json

    equation_type = data.get("equation type")
    equation_title = data.get("equation title")
    interval = data.get("interval")
    coefficients = data.get("coefficients")
    exit= data.get("exit")

    error = [0, 0, 0, 0, 0]
    error_message = ""

    try:
        str(equation_type)
        if equation_type not in ("linear", "polynomial deg=2", "polynomial deg=3", "polynomial deg=4", "sine", "cosine"):
            error[0] = 1
    except:
        error[0] = 1

    try:
        [float(c) for c in interval]
    except:
        error[2] = 1
    
    try:
        [float(c) for c in coefficients]
    except:
        error[3] = 1
    
    if error[0] == 1:
        error_message += "equation type error.\n"
    if error[2] == 1:
        error_message += "interval type error.\n"
    if error[3] == 1:
        error_message += "coefficients type error.\n"
    
    return error, error_message



def generate_data_w_json(input_json: dict) -> tuple[np.array, str]:

    data = input_json

    equation_title = data.get("equation title")

    c = [float(cons) for cons in data.get("coefficients")]

    x = np.linspace(float(data.get("interval")[0]), float(data.get("interval")[1]), 500)

    equation_type = data.get("equation type")
    if equation_type == "linear":
        y = c[0] * x + c[1]
    elif equation_type == "polynomial deg=2":
        y = c[0] * (x**2) + c[1] * x + c[2]
    elif equation_type == "polynomial deg=3":
        y = c[0] * (x**3) + c[1] * (x**2) + c[2] * x + c[3]
    elif equation_type == "polynomial deg=4":
        y = c[0] * (x**4) + c[1] * (x**3) + c[2] * (x**2) + c[3] * x + c[4]
    elif equation_type == "sine":
        y = c[0] * np.sin(c[1] * x) + c[2]
    elif equation_type == "cosine":
        y = c[0] * np.cos(c[1] * x) + c[2]
    else:
        raise "Format not found."
    
    points = np.column_stack((x, y))

    return points, equation_title


if __name__ == "__main__":
    data_json = {'equation type': 'polynomial deg=2', 'equation title': '3x^2 + 6x -2', 'interval': [3, 7], 'coefficients': [3, 6, -2, 0, 0], 'exit': False}
    data = generate_data_w_json(data_json)
    print(data)
    