import sys

from utils import handle_file, print_intro

user_args = sys.argv[1:]
if "-h" in user_args:
    print_intro()
