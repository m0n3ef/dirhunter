import httpx
#from user_agent import generate_user_agent
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.live import Live
import time
#import os
import click

console = Console()
@click.command()
@click.option('-t', help='Use this option to specify which target are we trying to attack... must end with ( / )\nexample: -t https://example.com/', required=True, prompt='[x] TARGET URL IS REQUIRED : ')
@click.option('-words', hidden=True, required=False)
@click.option('-o', help='Use this option to save the hits on the output file\n the file will be generate by a random name', required=False, type=bool)
@click.option('-tm', help='Use this option to choose the timeout in seconds\n default is 10', required=False, type=int, default='10')
@click.option('-c', help='Use this option to show the response codes', required=False, type=bool, default=False)
@click.option('-ext', help='Use this option to add extension format to the path word\n example: -ext .php ----> index.php / image.php', required=False, type=str)
def hunting(t, words, o, tm, c, ext):
    console.print('''[green]

                ⠀⠀⠀⠲⣦⣤⣀⣀⠀⠀⠀⣀⣀⣠⣤⣀⣀⠀⢀⣀⣠⣤⣶⣶⠟⠀⠀⠀ DIRHUNTER v1.0.1
                ⠀⠀⠀⠀⠙⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀  By m0n3ef
                ⠀⠀⠀⠀⠀⠈⢿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⠟⢻⣿⣿⡿⠃⠀⠀⠀⠀⠀
                ⠀⠀⠀⠲⣶⣶⣾⣿⣿⠀⢨⠙⢿⣿⣿⠏⣅⠀⢸⣿⣿⣷⣾⠟⠁⠀⠀⠀
                ⠀⠀⠀⠀⠈⠻⢿⣿⣿⢷⣶⣶⣾⣿⣿⣶⣶⣾⠟⣿⣿⣿⣋⠀⠀⠀⠀⠀
                ⠀⠀⢀⣀⣀⠐⢶⣿⣿⣧⠁⠀⠋⠁⠈⠋⠀⢀⣾⣿⣿⡿⣷⣶⠀⠀⠀⠀
                ⠀⠀⣼⣿⣿⣷⣤⣙⣿⣿⣷⣶⣶⣴⣴⣴⣶⣿⣿⣿⠟⣡⣿⣿⣧⣄⣀⡀
                ⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⡿⠿⣿⣿⣿⣿
                ⣿⡿⠛⠿⠟⠉⠉⠉⠸⠋⠀⠻⡿⣿⣿⣿⣿⠻⠇⠀⠀⠈⠀⠀⠈⠉⢸⠃
                ⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


[/green]''')
    time.sleep(2)
    with open("dlistlowercasesmall.txt", "r") as f:
        words = [line.strip() for line in f if line.strip()]


    customheaders = {

    }
    progress = Progress(
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("• {task.completed}/{task.total} [red]DIR[green]HUNTER"),
    )
    task = progress.add_task("Checking URLs...", total=len(words))


    with Live(progress, refresh_per_second=10, console=console) as live:
        with httpx.Client(timeout=tm) as client:
            for word in words:
                    if ext:
                        full_url = f"{t}{word}{ext}"
                    else:
                        full_url = f"{t}{word}"
                    try:
                        response = client.get(full_url)
                        if response.status_code == 200:
                            if c:
                                console.print(f"[green][+] Found:[/green] {full_url} | [blue][-] Code:[/blue] {response.status_code}")
                            else:
                                console.print(f"[green][+] Found:[/green] {full_url}")
                            if o:
                                with open('output.txt', 'a') as output:
                                    output.write(f'{full_url}\n')
                            else:
                                pass
                        elif response.status_code == 403:
                            if c:
                                console.print(f"[yellow][!] Forbidden:[/yellow] {full_url} | [blue][-] Code:[/blue] {response.status_code}")
                            else:
                                console.print(f"[yellow][!] Forbidden:[/yellow] {full_url}")
                        elif response.is_redirect == True:
                            if c:
                                console.print(f'[yellow][!] Redirected:[/yellow] {full_url} | [blue][-] Code:[/blue] {response.status_code}')
                            else:
                                console.print(f'[yellow][!] Redirected:[/yellow] {full_url}')
                    except Exception as e:
                        console.print(f"[red][x] Error:[/red] {full_url} — {e}")
                        pass
                    progress.update(task, advance=1)

hunting()

input("Press Enter to exit...")
