def print_number(number):
    print("Process ID:", multiprocessing.current_process().pid, "Number:", number)

def my_task(task_input):
    result = task_input * 2
    return result
