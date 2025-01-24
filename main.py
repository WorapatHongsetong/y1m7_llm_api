import matplotlib.pyplot as plt
import llm_response as llm
import populate_data as pdt
import visualise as vis
import numpy as np

def plot_by_text():

    run = True
    while run:
        print("\n\n\n\n\n\n\n\n\n")

        user_input = input("User_input: ")

        iterations = 0
        while True:
            try:
                data_json = llm.extract_data(user_prompt=user_input)

                if data_json.get("exit") == True:
                    print("\n\n\n\n\n\n\n\n\n\n")
                    print("Goodbye... :D")
                    run = False
                    break


                err_check, err_msg = pdt.check_data_valid(data_json)

                if err_check != [0, 0, 0, 0, 0]:
                    raise err_msg
                
                data_array, graph_title = pdt.generate_data_w_json(data_json)

                vis.plot_data(data_array, graph_title)

                break
            except Exception as e:
                iterations += 1
                print(f"Error: {e}")

                if iterations > 4:
                    print(f"User inputs may missing essential prompt...\nPlease relaunch program.")
                    break

    
if __name__ == "__main__":
    plot_by_text()