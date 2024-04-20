def amount_due(i):
        
          while i < 50:

            amount_due = 50 - i
            print("Amount Due:",amount_due)
            payment = int(input("Insert coin: "))
            treat_payment(payment,i)
            
def treat_payment(x,i):

    if x == 5 or x == 10 or x == 25:

            i += x
            if i>=50:
                change_owed(i)
            else:
                amount_due(i)

def change_owed(i):
                print("Change Owed:", i - 50)
exit()


def main():


    i  = 0
    amount_due(i)

main()


