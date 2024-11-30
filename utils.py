from pyfiglet import Figlet


def print_intro():
    f = Figlet(font="smkeyboard")
    print(f.renderText("KERJAA"))
    how_to = """
Usage:
kerja [flags] [file]

Flags:
    -a      add new task
    -d      delete task

file format:
    {task_name},{task_detail},{task_deadline_date (dd-mm-YY)},{task_deadline_hour}
    """
    print(how_to)


def handle_file(filename) -> list:
    with open(filename, "r") as f:
        file = f.read()
        a = [x.strip().strip("\n") for x in file.split(",")]
    return a


def make_cron(task_name: str, task_detail: str, task_deadline: str):
    pass
