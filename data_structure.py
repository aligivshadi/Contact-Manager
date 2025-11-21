# this are importing library for nessesary this program
from colorama import Style, Fore
import json
import os

class CONTACT: #start defining class...
#------------------------------- this function is init function
    def __init__(self):
        self.groups = ['Friends', 'Family', 'work', 'others']
        self.file_path = os.path.join(os.path.expanduser('~'), '.contact-manager.json')
        if os.path.exists(self.file_path):
            self.dict = self.load_contact()
        else:
            self.dict = {}
        
#------------------------------- this function can adding a contact to dictionary
    def add_to_list(self):
        self.phone = input("please eneter phone: ")
        key_dic = list(self.dict.keys())
        verify = True
        num_verify = None
        for key in key_dic:
            if key == self.phone:
                verify = False
                num_verify = self.phone
                break
        if verify:
            self.name = input("please enter name: ")
            self.name = self.name.lower()
            self.email = input("please eneter email: ")
            self.group = int(input("please eneter a number 1 - 4 : "))
            self.validation_group = None
            if self.group == 1:
                self.validation_group = 'Friends'
            elif self.group == 2:
                self.validation_group = 'Family'
            elif self.group == 3:
                self.validation_group = 'work'
            elif self.group == 4:
                self.validation_group = 'others'
            self.dict[self.phone] = [self.name, self.email, self.validation_group]
            print(f"{Fore.GREEN}---> {Style.RESET_ALL}New contact has been {Fore.GREEN}successfully{Style.RESET_ALL} added.")
        else:
            for key, value in self.dict.items():
                if key == num_verify:
                    print(f"{Fore.RED}--->{Style.RESET_ALL} This number is already in the contact list {Fore.RED}:{Style.RESET_ALL} {key} | {value[0]} | {value[1]} | {value[2]}\n")
#------------------------------- this function can showing full contact in dictionary for user
    def show_list(self):
        if self.dict:
            print("\n                     --------> you are all contact <--------   \n")
            for i, (key, value) in enumerate(self.dict.items(),start=0):
                print(f" {i}) {key} | {value[0]} | {value[1]} | {value[2]}\n  ---------------------------------------------------------------------------     ")
                
#------------------------------- this function save full dict to the json file.
    def save_contact_list(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.dict, f, indent=4, sort_keys=True)

#------------------------------ this function can be delete a contact from list with index or phone-number.
    def delete_contact(self):
        method_deletion = input('delete with method1 = number or method2 = number in list ? ')
        if method_deletion == '1':
            index_contact = int(input("please eneter index of contact :"))
            keys_list = list(self.dict.keys())
            number_to_delete = keys_list[index_contact] 
            self.dict.pop(number_to_delete)

        elif method_deletion =='2':
            number_deletion = input("please enter number for delete : ")
            if number_deletion in self.dict.keys():
                self.dict.pop(number_deletion)

#------------------------------ the function can full load context from json file to contact dict.
    def load_contact(self):
        with open(self.file_path, 'r') as file:
            try:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
                else:
                    return {}
            except json.JSONDecodeError:
                return {}
#------------------------------ searching function
    def searching_contact(self):
        user_need_search = input(f"please enter name contact : ")
        name_contact = []
        name_contact.append(user_need_search.lower())
        name_contact.append(user_need_search.lower().split(" ")[0])
        try:
            name_contact.append(user_need_search.lower().split(" ")[1])
        except IndexError:
            pass

        found_keys = []
        for word in name_contact:
            for phone, info in self.dict.items():
                if word in str(info).lower():
                    found_keys.append(phone)
        
        found_keys = set(found_keys)
        found_keys = list(found_keys)

        print("\n                     --------> I can find this numbers. <--------   \n")
        counter = 0
        for key, value in self.dict.items():
            for num in found_keys:
                if num == key:
                    counter += 1
                    print(f" {counter}) {key} | {value[0]} | {value[1]} | {value[2]}\n  ---------------------------------------------------------------------------     ")
#------------------------------ cleare all contact
    def clear_all_contact(self):
        self.dict.clear()
        self.save_contact_list()

