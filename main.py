from data_structure import CONTACT
import colorama

light_blue = colorama.Fore.LIGHTBLUE_EX
reset = colorama.Style.RESET_ALL
intro_menu = f"""
{light_blue}---> {reset} 1️)  Show All Contacts 📒
{light_blue}---> {reset} 2️)  Add Contact ➕
{light_blue}---> {reset} 3️)  Remove Contact ❌
{light_blue}---> {reset} 4️)  Search in Contact List 🔍
{light_blue}---> {reset} 5️)  Clear All Contacts 🧹
{light_blue}---> {reset} 0️)  Exit 🚪"""

intro_choose = f"{light_blue}---------------------------> {reset}Please select one option from the tasks above:"
def main():
    print(
        f"\n {colorama.Fore.CYAN}- - - - - >{reset} "
        f"{colorama.Fore.YELLOW}✨ Welcome to Your Contact Manager from 'Ali Givshadi' ✨{reset} "
        f"{colorama.Fore.CYAN}< - - - - -{reset}")   
    new_contact = CONTACT()
    while True:
        print(intro_menu)
        choose_task = input(intro_choose).strip()

        if choose_task == '1':
            new_contact.show_list()

        elif choose_task == '2':
            new_contact.add_to_list()
            new_contact.save_contact_list()

        elif choose_task == '3':
            new_contact.delete_contact()
            new_contact.save_contact_list()

        elif choose_task == '4':
            new_contact.searching_contact()

        elif choose_task == '5':
            new_contact.clear_all_contact()

        elif choose_task == '0':
            break
        
        elif choose_task == "exit" or choose_task == "Exit":
            break


if __name__ == '__main__':
    main()