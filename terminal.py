from rich.console import Console

con = Console()

comm = None

print('Python 4.1.3 (main, Mar 29 2026, 21:17:38) [GCC 15.2.0] on linux')
print('Type "help", "copyright", "credits" or "license" for more information.')


while True:
    if comm == "quit" or comm == "exit":
        break
    comm = con.input("[magenta]>>> ")
    comm = comm.replace(';', '')
    try:
        exec(comm)
    except Exception as e:
        print(e)

