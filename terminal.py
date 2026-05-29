from rich.console import Console

con = Console()

comm = None

while True:
    if comm == "quit" or comm == "exit":
        break
    comm = con.input("[magenta]>>> ")
    comm = comm.replace(';', '')
    try:
        exec(comm)
    except Exception as e:
        print(e)

