import requests
import rich
from rich.console import Console
import time

ascii_banner = """
██╗   ██╗███╗   ██╗██╗████████╗██╗   ██╗    ███╗   ███╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ ███████╗
██║   ██║████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝    ████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
██║   ██║██╔██╗ ██║██║   ██║    ╚████╔╝     ██╔████╔██║██║   ██║██║  ██║██║  ██║█████╗  ██████╔╝███████╗
██║   ██║██║╚██╗██║██║   ██║     ╚██╔╝      ██║╚██╔╝██║██║   ██║██║  ██║██║  ██║██╔══╝  ██╔══██╗╚════██║
╚██████╔╝██║ ╚████║██║   ██║      ██║       ██║ ╚═╝ ██║╚██████╔╝██████╔╝██████╔╝███████╗██║  ██║███████║
 ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
Simple Python Script By Galaxizs <3
https://discord.gg/E77R5BtAUb
"""

def delete(Webby):
    response = requests.delete(Webby)

    if response.status_code == 204:
        print("No more larp webhook!")
    else:
        print("Failed :(... Might be already deleted")

def main():
    console = Console()
    console.print(ascii_banner, justify="center")
    webby = input("Enter the webhook- ")
    delete(webby)

if __name__ == "__main__":
    main()
    
