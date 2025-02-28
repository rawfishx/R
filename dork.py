#!/usr/bin/python3
# GoogD0rker 2.0 - Rich UI Edition
# Menggunakan Rich untuk tampilan yang lebih menarik

from googlesearch import search
import argparse
from random import randint
from time import sleep
import time,os
from rich.console import Console
from rich.progress import track
from rich.table import Table

os.system("clear")

console = Console()

# Argument parser
parser = argparse.ArgumentParser(description='GoogD0rker dengan tampilan Rich.')
parser.add_argument('-d', action='store', dest='domain', help='Target domain, contoh: target.com')

results = parser.parse_args()

if results.domain is None:
    console.print("[bold red]Silakan masukkan domain target: script.py -d target.com[/bold red]")
    exit()
else:
    site = results.domain

def clear_cookie():
    with open(".google-cookie", "w") as fo:
        fo.write("")

def d0rkit(site, dork, filename):
    clear_cookie()
    out = open(filename, "a")

    # Buat tabel dengan Rich
    table = Table(title=f"📌 Hasil Dorking: {dork}", show_lines=True)
    table.add_column("No", justify="center", style="cyan", width=5)
    table.add_column("URL", style="cyan", no_wrap=True)

    # Ambil hasil pencarian
    for i, result in enumerate(search(dork, num_results=10), start=1):
        table.add_row(str(i), result)
        out.write(result + "\n")

    out.close()

    # Tampilkan hasil dalam bentuk tabel
    console.print(table)
    
def main():
    tasks = [
        ("Login Pages", f"site:{site} inurl:wp- OR inurl:plugin OR inurl:upload OR inurl:download", "loginpage.txt"),
        ("Backdoors", f"site:{site} inurl:shell OR inurl:backdoor OR inurl:wso OR inurl:cmd OR shadow OR passwd OR boot.ini OR inurl:backdoor", "backdoor.txt"),
        ("Setup Files", f"site:{site} inurl:readme OR inurl:license OR inurl:install OR inurl:setup OR inurl:config", "setup_files.txt"),
        ("WordPress", f"site:{site} inurl:wp- OR inurl:plugin OR inurl:upload OR inurl:download", "wordpress.txt"),
        ("Open Redirects", f"site:{site} inurl:redir OR inurl:url OR inurl:redirect OR inurl:return OR inurl:src=http OR inurl:r=http", "openredirect.txt"),
        ("File Extensions", f"site:{site} ext:cgi OR ext:php OR ext:asp OR ext:aspx OR ext:jsp OR ext:jspx OR ext:swf OR ext:fla OR ext:xml", "extensions.txt"),
        ("Documents", f"site:{site} ext:doc OR ext:docx OR ext:csv OR ext:pdf OR ext:txt OR ext:log OR ext:bak", "documents.txt"),
        ("Apache Struts RCE", f"site:{site} ext:action OR ext:struts OR ext:do", "struts.txt"),
        ("Pastebin Posts", f"site:pastebin.com {site}", "pastebin.txt"),
        ("LinkedIn Employees", f"site:linkedin.com employees {site}", "linkedin.txt"),
        ("Subdomains", f"site:*.{site}", "subdomains.txt"),
        ("Sub-subdomains", f"site:*.*.{site}", "sub-subdomains.txt"),
        ("PHPInfo Files", f"inurl:'/phpinfo.php' {site}", "phpinfo.txt"),
        ("Password Files", "intext:'connectionString' AND inurl:'web' AND ext:'config'", "passwords.txt"),
        ("Sensitive Files", f"inurl:'/phpinfo.php' OR inurl:'.htaccess' OR inurl:'/.git' {site} -github", "sensitive.txt"),
        ("KTP", f"intitle:'Index of /' intext:ktp site:{site}")
    ]

    table = Table(title="GoogD0rker Scan Results", show_lines=True)
    table.add_column("No", style="bold cyan", justify="center")
    table.add_column("Kategori", style="bold magenta")
    table.add_column("Status", style="bold green", justify="center")

    for i, (task_name, dork, filename) in enumerate(track(tasks, description="Scanning..."), start=1):
        console.print(f"[yellow]Mencari {task_name} untuk {site}...[/yellow]")
        d0rkit(site, dork, filename)
        table.add_row(str(i), task_name, "[green]Selesai[/green]")
        sleep(randint(5, 15))

    console.print("\n[bold green]Scanning selesai![/bold green]\n")
    console.print(table)
    time.sleep(3)

if __name__ == '__main__':
    main()
