import time
import recursive

time.sleep(4)
def details(countries_dict):
    yield countries_dict

countries = {'India' : [1,100,12.5],'Australia' : [54.28,30,13.5],'United States' : [73.11,40,14.5],'France' : [86.78,50,15.5],'Germany' : [86.78,45,16.5],'Switzerland' : [79.81,80,17.5]}
time.sleep(1)
print('Welcome Sallu Bhai, I am Kartikay and I will help you with choosing a venue and other formalities for your grand day.\n')
time.sleep(1)
print('Here is the list of the available venues for you : \n')
for i,country in enumerate(countries.keys()):
    print(f'{i+1}.',country)
time.sleep(3)
num_peop = int(input('Please enter the number of guest you will be inviting : '))
if num_peop >= 100:
    print('Sir, please have some good amount of people so that the event is a grand success, somewhere like 50-100 people.\n')
    print('So by default, I am choosing 40 people for you\n')
    num_peop = 40
elif num_peop <= 0:
    print('Sorry sir, you cannot have 0 or less people at your wedding.')
    print('So by default, I am choosing 40 people for you\n')
    num_peop = 40

for i in countries.keys():
    country = countries[i]
    rate = country[0]
    ppc = country[1]
    cost = lambda rate: rate * ppc
    print(f'The per person cost for {i} is Rupees {cost(rate)}.')
    time.sleep(1)
choice = input('\nSo, which would you want to choose? : ')
if choice not in countries.keys():
    choice = input('You have entered the wrong choice, please enter again : ')
    if choice not in countries.keys():
        print('Thank you so much for using our services, we bid you goodbye.')
        exit(0)
time.sleep(2)
print(f'As this is a 1 day marriage, tax rate would be {countries[choice][2]}% per day.\n')
total_cost = num_peop * countries[choice][0] * countries[choice][1]+ countries[choice][2]/100 * num_peop * countries[choice][0] * countries[choice][1]
print(f'So, the total cost for you is Rupees {total_cost}')
opt = ['yes','no']
offering = input('Done with the booking, would you also want to get some offering(please answer in yes or no) : ')
if offering == opt[0]:
    print('Thank you for opting for offering, it would cost additional Rupees 100 per person.')
    time.sleep(1)
    total_cost += num_peop * 100
    print(f'So, the total cost would be {total_cost}')
elif offering == opt[1]:
    print("So you didn't opt for the offering, the cost would remain the same.")

else:
    print('Sir, please enter the one of the choices mentioned : ')
    offering = input('Again, for the offering, please tyoe yes or no : ')
    if offering not in opt:
        print('Thank you so much for using our services, we bid you goodbye.')
        exit(0)

print('So, the proceedings for your marriage is going on, and will take some time.\n')
time.sleep(1)
print('In the meantime, you can play an interesting game of calculating factorial number.')
game = input('Would you like to play it? (please enter yes or no) : ')
if game == 'yes':
    num = int(input('Ok, choose a number : '))
    time.sleep(4)
    print(f'The factorial of {num} is {recursive.fact(num)}.')
    time.sleep(1)
    print('All the processing regarding your marriage has been done, please enjoy the grand day.')
    print('The program will now exit.')
    exit(0)

elif game == 'no':
    time.sleep(1)
    print('All the processing regarding your marriage has been done, please enjoy the grand day.')
    print('The program will now exit.')
    exit(0)

else:
    time.sleep(1)
    print('you entered the wrong choice, sir.')
    print('All the processing regarding your marriage has been done, please enjoy the grand day.')
    print('The program will now exit.')
    exit(0)
    










    




    
