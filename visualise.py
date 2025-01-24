import matplotlib.pyplot as plt
import llm_response as llm
import populate_data as pdt
import numpy as np

def plot_data(data: np.array, title: str):
    plt.plot(data[:, 0], data[:, 1])
    plt.title(title)
    plt.show()


if __name__ == "__main__":

    user_input = input("User_input: ")

    data_json = llm.extract_data(user_prompt=user_input)

    err_check, err_msg = pdt.check_data_valid(data_json)

    if err_check != [0, 0, 0, 0, 0]:
        raise err_msg
    
    data_array, graph_title = pdt.generate_data_w_json(data_json)

    plot_data(data_array, graph_title)
