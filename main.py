import requests
import json
import secrets
import string


url_token = f"https://nebula.starbreeze.com/iam/v3/oauth/token"
string_length = 32
random_bytes = secrets.token_bytes(16)

random_string = ''.join(secrets.choice(string.hexdigits) for i in range(string_length))

token_header = {
        "Host": "nebula.starbreeze.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic MGIzYmZkZjVhMjVmNDUyZmJkMzNhMzYxMzNhMmRlYWI6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Electron/25.8.3 Safari/537.36",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US",
}
data_token = {
    "username": None,
    "password": None,
    "grant_type": "password",
    "client_id": random_string,
    "extend_exp": "true"
}


print("Login to Nebula")

username_request = input("Enter your EmailID: ")
password_request = input("Enter the Password: ")
data_token["username"] = username_request
data_token["password"] = password_request
response_token_value = requests.post(url_token, headers=token_header, data=data_token)
while True:
    try:
        if response_token_value.status_code == 200:
            response_data = {
                "user_id": response_token_value.json().get("user_id", ""),
                "token": response_token_value.json().get("access_token", "")
            }
            break
        else:
            print("Invalid Login. Please enter a again.")
            exit(0)
    except ValueError:
        print("Invalid input.")
        
while True:
    with open("response.json", "w") as json_file:
        json.dump(response_data, json_file, indent=4)
    print(" ")
    print("Option - 1 : Buy 10X C-Stacks")
    print("Option - 2 : Custom Buy")
    print("Option - 3 : All Heist Favors")
    print("Option - 4 : Specific Heist Favor")
    print("Option - 9 : Quit")

    options = {
        1: "Option - 1 : Buy 10X C-Stacks",
        2: "Option - 2 : Custom Buy",
        3: "Option - 3 : All Heist Favors",
        4: "Option - 4 : Specific Heist Favor",
        9: "Option - 9 : Quit",
    }
    with open("response.json", "r") as config_file:
       config_data = json.load(config_file)
    account_id = config_data.get("user_id", "")
    authorization_token = config_data.get("token", "")

    url = f"https://nebula.starbreeze.com/platform/public/namespaces/pd3/users/{account_id}/orders" 

    headers = {
        "Accept-Encoding": "deflate, gzip",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {authorization_token}",
        "Namespace": "pd3",
        "Game-Client-Version": "1.0.0.0",
        "AccelByte-SDK-Version": "21.0.3",
        "AccelByte-OSS-Version": "0.8.11",
        "User-Agent": "PAYDAY3/++UE4+Release-4.27-CL-0 Windows/10.0.19045.1.256.64bit",
    }
    data = {
        "itemId": None,  
        "quantity": 1,
        "price": None,
        "discountedPrice": None,
        "currencyCode": None,
        "region": "SE",
        "language": "en-US",
        "returnUrl": "http://127.0.0.1"
    }
    def get_valid_currencycode():

        while True:
            currency_custom = input("Enter currency: ").strip()
            if currency_custom.isalpha():
                return currency_custom.upper()
            else:
                print("Invalid input.")
                
    favorOptions = {
        1: "Favor 1",
        2: "Favor 2",
        3: "Favor 3",
        4: "Favor 4",
    }

                
    while True:
        try:
            choice = int(input("Enter the option: "))
            if choice in options:
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid option.")

 

    if choice == 1:
        repeat_request = int(input("Enter the total number of times you want the request to send: ")) 
        for _ in range(repeat_request):
            data["itemId"] = "dd693796e4fb4e438971b65eecf6b4b7"
            data["price"] = 90000
            data["discountedPrice"] = 90000
            data["currencyCode"] = "CASH"
            response = requests.post(url, json=data, headers=headers)
            print(f"C-Stacks Bought successfully - {_ + 1}")  

    elif choice == 2:
        repeat_request = int(input("Enter the total number of times you want the request to send: ")) 
        item_id_custom = input("Enter itemID: ")
        price_custom = int(input("Enter price: "))
        discounted_custom = int(input("Enter discountedprice: "))
        currency_custom = get_valid_currencycode()
        data["itemId"] = item_id_custom
        data["price"] = price_custom
        data["discountedPrice"] = discounted_custom
        data["currencyCode"] = currency_custom
        for _ in range(repeat_request):
            response = requests.post(url, json=data, headers=headers)
            print(f"Custom Item Purchased - {_ + 1}")

    elif choice == 3:
        repeat_request = int(input("Enter the total number of times you want the request to send: ")) 
        with open('Payday3_offsets.json', 'r') as json_file:
            item_id_json = json.load(json_file)
        for _ in range(repeat_request):
            print(f"Heist Item Purchased - {_ + 1}")
            for item_id in item_id_json["itemId"]:
                if item_id == "65a355215bb8473bbf9d3f2661211899":
                    data["itemId"] = item_id
                    data["price"] = 1999
                    data["discountedPrice"] = 1999
                    data["currencyCode"] = "CASH"
                    print(f"Item Purchased = {item_id}")
                else:
                    data["itemId"] = item_id
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    print(f"item_id= {item_id}")
                response = requests.post(url, json=data, headers=headers)
                print(response)
    elif choice == 4:
        print(" ")
        print("Option - 1 : No Rest Ror The Wicked Favors")
        print("Option - 2 : Road Rage Favors")
        print("Option - 3 : Dirty Ice Favors")
        print("Option - 4 : Rock The Cradle Favors")
        print("Option - 5 : Under The Surphaze Favors")
        print("Option - 6 : Gold & Sharke Favors")
        print("Option - 7 : 99 Boxes Favors")
        print("Option - 8 : Touch The Sky Favors")

        heistOptions = {
            1: "Option - 1 : No Rest Ror The Wicked Favors",
            2: "Option - 2 : Road Rage Favors",
            3: "Option - 3 : Dirty Ice Favors",
            4: "Option - 4 : Rock The Cradle Favors",
            5: "Option - 5 : Under The Surphaze Favors",
            6: "Option - 6 : Gold & Sharke Favors",
            7: "Option - 7 : 99 Boxes Favors",
            8: "Option - 8 : Touch The Sky Favors",
        }

        while True:
            try:
                heistChoice = int(input("Enter the option: "))
                if heistChoice in heistOptions:
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a valid option.")
                
                
        if heistChoice == 1:
            print(" ")
            print("No Rest For The Wicked Favors")
            print("Option - 1 : Van Escape")
            print("Option - 2 : Additional Secure Point")
            print("Option - 3 : Keycard Access")
            print("Option - 4 : More Thermite")

            while True:
                try:
                    favorChoice = int(input("Enter the option: "))
                    if favorChoice in favorOptions:
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

            repeat_request = int(input("Enter the total number of times you want the request to send: "))
            print(" ")
            if favorChoice == 1:
                for _ in range(repeat_request):
                    data["itemId"] = "7ef67d46c6224310b813afcc5f53ae62"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 2:
                for _ in range(repeat_request):
                    data["itemId"] = "7ffcce86f7bb4dd78e9fcd6755fc9a43"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 3:
                for _ in range(repeat_request):
                    data["itemId"] = "fb595a70be16479cbd6398866ceace43"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 4:
                for _ in range(repeat_request):
                    data["itemId"] = "ec4f15db42d54fdfa1a4716d3e880aaf"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
                    
        elif heistChoice == 2:
            print(" ")
            print("Road Rage Favors")
            print("Option - 1 : Garbage Chute Secure Point")
            print("Option - 2 : Stronger RC Signal")
            print("Option - 3 : Sniper Tower")
            print("Option - 4 : More Planks")

            while True:
                try:
                    favorChoice = int(input("Enter the option: "))
                    if favorChoice in favorOptions:
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

            repeat_request = int(input("Enter the total number of times you want the request to send: "))
            print(" ")
            if favorChoice == 1:
                for _ in range(repeat_request):
                    data["itemId"] = "762a1305c25844a7aac3d0f0666c70e6"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 2:
                for _ in range(repeat_request):
                    data["itemId"] = "86104f11f3534828b6112f28717c5308"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 3:
                for _ in range(repeat_request):
                    data["itemId"] = "f55bbfc9483948d69be74a55b5cd5038"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 4:
                for _ in range(repeat_request):
                    data["itemId"] = "0441acf170484c509bcb2c7869170403"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")

        elif heistChoice == 3:
            print(" ")
            print("Dirty Ice Favors")
            print("Option - 1 : Distracted Manager")
            print("Option - 2 : Escape Van Stays Longer")
            print("Option - 3 : Chopper Extract")
            print("Option - 4 : Employee Backdoor Access")

            while True:
                try:
                    favorChoice = int(input("Enter the option: "))
                    if favorChoice in favorOptions:
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

            repeat_request = int(input("Enter the total number of times you want the request to send: "))
            print(" ")
            if favorChoice == 1:
                for _ in range(repeat_request):
                    data["itemId"] = "a8a42735b6ed4bf48456de9f33ff6477"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 2:
                for _ in range(repeat_request):
                    data["itemId"] = "736ee0a77016416ba9d35a9a5f4c7fd0"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 3:
                for _ in range(repeat_request):
                    data["itemId"] = "b21d68ea6ba94dc38032697233b6aa41"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 4:
                for _ in range(repeat_request):
                    data["itemId"] = "ed3734c6be7142ca9ac17df4b91e4acb"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")

        elif heistChoice == 4:
            print(" ")
            print("Rock The Cradle Favors")
            print("Option - 1 : Additional Secure Point")
            print("Option - 2 : Vault Code")
            print("Option - 3 : Extended Crypto Wallet Timer")
            print("Option - 4 : Inside Man Keycard")

            while True:
                try:
                    favorChoice = int(input("Enter the option: "))
                    if favorChoice in favorOptions:
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

            repeat_request = int(input("Enter the total number of times you want the request to send: "))
            print(" ")
            if favorChoice == 1:
                for _ in range(repeat_request):
                    data["itemId"] = "3540c541445e4c86be79d0d9d618fa62"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 2:
                for _ in range(repeat_request):
                    data["itemId"] = "65a355215bb8473bbf9d3f2661211899"
                    data["price"] = 1999
                    data["discountedPrice"] = 1999
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 3:
                for _ in range(repeat_request):
                    data["itemId"] = "dca07cf916b04dbf8f3eb4a134e874cf"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 4:
                for _ in range(repeat_request):
                    data["itemId"] = "ea9fd9afab3d4e88ab8f9276bd5e66b3"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
                    
        elif heistChoice == 5:
            print(" ")
            print("Under The Surphaze Favors")
            print("Option - 1 : Additional Secure Point")
            print("Option - 2 : Keycard Access")
            print("Option - 3 : Open Doors")
            print("Option - 4 : Helicopter Pilot")

            while True:
                try:
                    favorChoice = int(input("Enter the option: "))
                    if favorChoice in favorOptions:
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

            repeat_request = int(input("Enter the total number of times you want the request to send: "))
            print(" ")
            if favorChoice == 1:
                for _ in range(repeat_request):
                    data["itemId"] = "ed77cf56bf8d435ab25b07eb476bf341"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 2:
                for _ in range(repeat_request):
                    data["itemId"] = "714a8344431147b1bbb9a36c51a6e0fe"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 3:
                for _ in range(repeat_request):
                    data["itemId"] = "d1a8dbc374684db69970fb9655af3e98"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 4:
                for _ in range(repeat_request):
                    data["itemId"] = "3872ce94c1bf4ae49962e97e6eee4c13"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
                    
        elif heistChoice == 6:
            print(" ")
            print("Gold & Sharke Favors")
            print("Option - 1 : Teller Doors Open")
            print("Option - 2 : Cafe Celebration")
            print("Option - 3 : Thermal Lance Parts Stashed Inside")
            print("Option - 4 : Elevator Shaft Access")

            while True:
                try:
                    favorChoice = int(input("Enter the option: "))
                    if favorChoice in favorOptions:
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

            repeat_request = int(input("Enter the total number of times you want the request to send: "))
            print(" ")
            if favorChoice == 1:
                for _ in range(repeat_request):
                    data["itemId"] = "244a532a15a540b8a2bb08ba61ca2cbe"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 2:
                for _ in range(repeat_request):
                    data["itemId"] = "24fb047fe6bb4227a09d1089d1271f7d"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 3:
                for _ in range(repeat_request):
                    data["itemId"] = "df2e66d7a0e94ff28ba46337ceaf9555"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 4:
                for _ in range(repeat_request):
                    data["itemId"] = "6c0bc7b7053c486496f68402d313c20d"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
                    
        elif heistChoice == 7:
            print(" ")
            print("99 Boxes Favors")
            print("Option - 1 : Open Container")
            print("Option - 2 : Longer Degredation Time")
            print("Option - 3 : More Explosives")
            print("Option - 4 : Better Thermite Drop")

            while True:
                try:
                    favorChoice = int(input("Enter the option: "))
                    if favorChoice in favorOptions:
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

            repeat_request = int(input("Enter the total number of times you want the request to send: "))
            print(" ")
            if favorChoice == 1:
                for _ in range(repeat_request):
                    data["itemId"] = "0cd47901794a44b38a9f2d4b7b1b3f61"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 2:
                for _ in range(repeat_request):
                    data["itemId"] = "96de618c6aca4d3a9b4df9b3220fcb1c"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 3:
                for _ in range(repeat_request):
                    data["itemId"] = "b91465e2dc624101a3d157305637bbda"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 4:
                for _ in range(repeat_request):
                    data["itemId"] = "ff2464ce14da473e97590ea2fb33b327"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
                    
        elif heistChoice == 8:
            print(" ")
            print("Touch The Sky Favors")
            print("Option - 1 : Window Platform")
            print("Option - 2 : Thermite Stashed")
            print("Option - 3 : Poison")
            print("Option - 4 : Vent Secure Point")

            while True:
                try:
                    favorChoice = int(input("Enter the option: "))
                    if favorChoice in favorOptions:
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a valid option.")

            repeat_request = int(input("Enter the total number of times you want the request to send: "))
            print(" ")
            if favorChoice == 1:
                for _ in range(repeat_request):
                    data["itemId"] = "d953877d2f494605b89f40896fe85781"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 2:
                for _ in range(repeat_request):
                    data["itemId"] = "87d91fc1cc5f4e8fa3c4e9e2bd303376"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 3:
                for _ in range(repeat_request):
                    data["itemId"] = "b815a9b61ba944dda953eb85fd8d6bbf"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            elif favorChoice == 4:
                for _ in range(repeat_request):
                    data["itemId"] = "86b9d2fede264495a71aac9786b20a45"
                    data["price"] = 1000
                    data["discountedPrice"] = 1000
                    data["currencyCode"] = "CASH"
                    response = requests.post(url, json=data, headers=headers)
                    print(f"Favors Bought successfully - {_ + 1}")
            
    elif choice == 9:
        exit()
