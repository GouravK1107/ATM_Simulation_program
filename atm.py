import random as r
from datetime import datetime, timedelta
import time as t

card = {
    "balance_amount": 1000,
    "phone_number": 9916259010,
    "card_number": 1201,
    "pin": 1233,
    "status": "active",
    "chances": 3
}

def slip_fun(card_data, transaction_type, amount):
    print("\n\n")
    print("===========================================")
    print("          ADEX BANK - TRANSACTION SLIP     ")
    print("===========================================")
    print(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Card: ****-****-{str(card_data['card_number'])[-4:]}")
    print(f"  Phone: {card_data['phone_number']}")
    print("-------------------------------------------")
    print(f"  Transaction: {transaction_type}")
    print(f"  Amount: ₹{amount}")
    print(f"  Available Balance: ₹{card_data['balance_amount']}")
    print("-------------------------------------------")
    print("  Thank you for banking with us!")
    print("  *Keep this slip for your records*")
    print("===========================================")

print(".... (programming running)", flush=True)
t.sleep(2.20)
print(".... (initializing packages)", flush=True)
t.sleep(2.20)
print(".... (accessing the backend)", flush=True)
t.sleep(2.20)
print("\n *** Thanks for choosing the Adex bank ***\n")

def main(card):
    chance = 3
    while chance > 0:
        input_card = int(input("Enter card number: **** - **** - "))
        if input_card == card["card_number"] and card["status"].lower() == "active":
            while card["chances"] > 0:
                input_pin = int(input("Enter PIN: "))
                if input_pin != card["pin"]:
                    t.sleep(1.1)
                    print("Incorrect PIN, try again !")
                    card["chances"] -= 1
                else:
                    break
            if card["chances"] == 0:
                print("Too many failed attempts. Card is blocked.")
                card["status"] = "blocked"
                return
            t.sleep(1.1)
            print("Services: \n\t1) Withdraw\n\t2) Balance Enquiry\n\t3) Change phone number\n\t4) Generate pin\n\t5) Exit")
            ch = int(input("Enter your choice: "))
            t.sleep(1)

            if ch == 1:
                print("\t | CASH WITHDRAWAL |\n")
                input_amount = int(input("Enter amount: "))
                t.sleep(1.1)

                if input_amount > card["balance_amount"]:
                    print(f"Invalid balance. Available: ₹{card['balance_amount']}")
                    card["chances"] -= 1
                else:
                    print(".... (processing)", flush=True)
                    t.sleep(1)
                    card["balance_amount"] -= input_amount
                    print(f"Collect ₹{input_amount}")
                    print(f"New balance: ₹{card['balance_amount']}")
                    slip = input("Want receipt? (yes/no): ").lower()
                    if slip == "yes":
                        print(".... (generating)")
                        t.sleep(1.5)
                        slip_fun(card, "WITHDRAWAL", input_amount)
                    else:
                        print("Transaction complete. Thank you!")

            elif ch == 2:
                print("\t | BALANCE ENQUIRY |")
                print(".... (checking)", flush=True)
                t.sleep(1)
                print(f"The balance: ₹{card['balance_amount']}")

            elif ch == 3:
                print("\t | CHANGE PHONE NUMBER |")
                yn = input("Are you sure to change the number ? (yes/no)").lower()
                if yn == "yes":
                    print(".... (processing)", flush=True)
                    t.sleep(1)
                    new_phone_number = int(input("Enter your new phone number: "))
                    if len(str(new_phone_number)) == 10:
                        print(".... (processing)", flush=True)
                        t.sleep(1)
                        card["phone_number"] = new_phone_number
                        print("Phone number added succesffuly !")
                        print("Thank you for using, Adex Bank")
                elif yn == "no":
                    print("As you wish !")
                    print("Thank you for using, Adex Bank")

            elif ch == 4:
                print("\t | CHANGE/GENERATE PIN |")
                yn = input("Are you sure to change the PIN ? (yes/no)").lower()
                if yn == "yes":
                    print(".... (processing)", flush=True)
                    t.sleep(1)
                    old_pin = int(input("Enter your old PIN: "))
                    if old_pin == card["pin"]:
                        new_pin = int(str(r.randint(0, 9999)).zfill(4))
                        print(".... (generating)", flush=True)
                        t.sleep(1.5)
                        print("PIN changed succesfully")
                        card["pin"] = new_pin
                        print(f"Your new PIN = {card['pin']} (don't share with anyone)")
                    elif old_pin != card["pin"]:
                        phno = int(input("Enter your phone number: "))
                        if len(str(phno)) == 10:
                            print("Sending OTP..", flush=True)
                            t.sleep(1.5)
                            otp = int(str(r.randint(0, 9999)).zfill(4))
                            print(otp)
                            check = int(input("Enter OTP: "))
                            if check == otp:
                                print("OTP is matched")
                                new_pin = int(str(r.randint(0, 9999)).zfill(4))
                                print(".... (generating)", flush=True)
                                t.sleep(1.5)
                                print("PIN changed succesfully")
                                card["pin"] = new_pin
                                print(f"Your new PIN = {card['pin']} (don't share with anyone)")
                            else:
                                print("OTP is not matched !")
                                return
                    else:
                        print("Something went wrong, try again later. ")
                elif yn == "no":
                    print("As you wish !")
                    print("Thanks for using, Adex Bank")
                    return
                else:
                    print("Something went wrong ! Try again later. ")
                    return

            elif ch == 5:
                print("Thanks for Visiting the Adex bank, have a good day. 😊")
                return

        else:
            t.sleep(1.5)
            block_time = datetime.now()
            unblock_time = block_time + timedelta(hours=24)
            print(f"The card has been blocked at {block_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Will be automatically unblocked at {unblock_time.strftime('%Y-%m-%d %H:%M:%S')} (24 hours from now)")
            card["status"] = "blocked"
    else:
        if input_card != card["card_number"]:
            t.sleep(1)
            print("Invalid card number !")
            chance -= 1
        elif card["status"] == "blocked":
            t.sleep(1)
            print("The card is blocked !")
        else:
            print("Something went wrong ! Try again.")

if __name__ == "__main__":
    main(card)
