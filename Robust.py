import os
import requests
from colorama import init, Fore
init()
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_art():
    art = """
    $$$$$$\\            $$$$$$$\\                        $$\\     
    $$  __$$\\           $$  __$$\\                       $$ |    
    $$ |  $$ | $$$$$$\\  $$ |  $$ |$$\\   $$\\  $$$$$$$\\ $$$$$$\\   
    $$$$$$$  |$$  __$$\\ $$$$$$$\\ |$$ |  $$ |$$  _____|\\_$$  _|  
    $$  __$$< $$ /  $$ |$$  __$$\\ $$ |  $$ |\\$$$$$$\\    $$ |    
    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | \\____$$\\   $$ |$$\\ 
    $$ |  $$ |\\$$$$$$  |$$$$$$$  |\\$$$$$$  |$$$$$$$  |  \\$$$$  |
    \\__|  \\__| \\______/ \\_______/  \\______/ \\_______/    \\____/   
    """
    print(f"{Fore.MAGENTA}{art}{Fore.RESET}")
    print(f"{Fore.GREEN}Enter...{Fore.RESET}")
def get_account_info(user_id, cookies):
    account_settings = requests.get('https://www.roblox.com/my/settings/json', cookies=cookies)
    return account_settings.json()
def get_user_info(cookies):
    user_response = requests.get("https://users.roblox.com/v1/users/authenticated", cookies=cookies)
    if user_response.status_code == 200:
        return user_response.json()
    else:
        return None
def format_verified_status(verified, value):
    return f"{Fore.GREEN}Verified{Fore.RESET}" if verified else f"{Fore.RED}Not Verified{Fore.RESET}"
def format_yes_no(value):
    return f"{Fore.GREEN}Yes{Fore.RESET}" if value else f"{Fore.RED}No{Fore.RESET}"
def main():
    while True:
        try:
            clear_console()
            print_art()
            input()
            clear_console()
            print(f"{Fore.GREEN}Enter your cookie....{Fore.RESET}")
            COOKIE = input()
            cookies = {
                ".ROBLOSECURITY": COOKIE
            }
            clear_console()
            user_info = get_user_info(cookies)
            if user_info:
                user_id = user_info['id']
                account_info = get_account_info(user_id, cookies)

                display_name = account_info['DisplayName']
                username = account_info['Name']
                email_verified = account_info['IsEmailVerified']
                email = account_info.get('UserEmail', '')
                phone_verified = account_info.get('PhoneNumberVerified', False)
                phone_number = account_info.get('PhoneNumber', 'N/A')
                is_above_13 = account_info['UserAbove13']
                account_age = round(float(account_info['AccountAgeInDays'] / 365), 2)
                has_premium = account_info['IsPremium']
                has_pin = account_info['IsAccountPinEnabled']
                is_2step_enabled = account_info['MyAccountSecurityModel']['IsTwoStepEnabled']

                robux_balance = requests.get(f"https://economy.roblox.com/v1/users/{user_id}/currency", cookies=cookies).json()['robux']
                pending_robux = requests.get(f"https://economy.roblox.com/v2/users/{user_id}/transaction-totals?timeFrame=Month&transactionType=summary", cookies=cookies).json().get('pendingRobuxTotal', 'N/A')

                print(f"{Fore.MAGENTA}{'='*50}{Fore.RESET}")
                print(f"{Fore.CYAN}{'='*2} {Fore.YELLOW}{'Robust':^46} {Fore.CYAN}{'='*2}{Fore.RESET}")
                print(f"{Fore.MAGENTA}{'='*50}{Fore.RESET}")
                
                print(f"{Fore.CYAN}{'Display':<20}{Fore.WHITE} {display_name}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Username:':<20}{Fore.WHITE} {username}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Email':<20}{Fore.WHITE} {format_verified_status(email_verified, email)}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Number:':<20}{Fore.WHITE} {format_verified_status(phone_verified, phone_number)}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Above 13:':<20}{Fore.WHITE} {format_yes_no(is_above_13)}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Account Age':<20}{Fore.WHITE} {account_age}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Has Premium:':<20}{Fore.WHITE} {format_yes_no(has_premium)}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Has PIN:':<20}{Fore.WHITE} {format_yes_no(has_pin)}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Two-step:':<20}{Fore.WHITE} {format_yes_no(is_2step_enabled)}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Robux Balance:':<20}{Fore.WHITE} {robux_balance}{Fore.RESET}")
                print(f"{Fore.CYAN}{'Pending Robux:':<20}{Fore.WHITE} {pending_robux}{Fore.RESET}")
                
                print(f"{Fore.MAGENTA}{'='*50}{Fore.RESET}")

                print(f"{Fore.GREEN}Press Enter to restart...{Fore.RESET}")
                input()
                clear_console()
            else:
                print(f"{Fore.RED}BadCookie....enter{Fore.RESET}")
                input()
                clear_console()

        except Exception as e:
            clear_console()
            print(f"{Fore.RED}An error occurred: {str(e)}{Fore.RESET}")
            print(f"{Fore.GREEN}Restarting...{Fore.RESET}")
            input()
            clear_console()

if __name__ == "__main__":
    main()
