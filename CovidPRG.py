#Import libraries
from covid import Covid
import random

covid = Covid()

#Function: print global cases
def worldwide_covid_cases():
    # Covid variables
    tot_cases = covid.get_total_active_cases()
    confirmed_cases = covid.get_total_confirmed_cases()
    healed_cases = covid.get_total_recovered()
    deaths_cases = covid.get_total_deaths()
    #Print: print the variables
    print('\n-----------------------------')
    print('() Total cases: {}'.format(tot_cases))
    print('() Confirmed cases: {}'.format(confirmed_cases))
    print('() Healed cases: {}'.format(healed_cases))
    print('() Total deaths: {}'.format(deaths_cases))
    print('-----------------------------\n')


#Function: print cases by country (Name or ID)
def covid_country_cases():
    choose = str(input('\nSearch by name or ID \nChoose: '))

    #If: if selection by name is chosen
    if choose == 'name' or choose == 'Name':
        country_name = str(input('Enter country name: '))
        country_data = covid.get_status_by_country_name(country_name)
        print('\n-----------------------------')
        for x in country_data:
            print('() ',x,':',country_data[x])
        print('-----------------------------\n')

    #If: if selection by id is chosen
    if choose == 'ID' or choose == 'id':
        country_id = int(input('Enter country ID: '))
        country_data = covid.get_status_by_country_id(country_id)
        print('\n-----------------------------')
        for x in country_data:
            print('() ',x,':',country_data[x])
        print('-----------------------------\n')



#Function: print the list of countries
def print_countries():
    in_file = open('Countries.txt','r')
    text = in_file.read()
    in_file.close()
    print(text)
    print('\n')


#Function: compare two countries   
def compare_countries():
    choose = str(input('\nSearch by name or ID \nChoose: '))

    #If: if selection by name is chosen
    if choose == 'name' or choose == 'Name':
        country_name1 = str(input('Enter country name 1: '))
        country_name2 = str(input('Enter country name 2: '))
        country_data1 = covid.get_status_by_country_name(country_name1)
        country_data2 = covid.get_status_by_country_name(country_name2)
        print('\n-----------------------------')
        for x in country_data1:
            print('() ',x,':',country_data1[x])
        print('\n')
        for x in country_data2:
            print('() ',x,':',country_data2[x])
        print('-----------------------------\n')

    #If: if selection by id is chosen
    if choose == 'ID' or choose == 'id':
        country_id1 = int(input('Enter country ID 1: '))
        country_id2 = int(input('Enter country ID 2: '))
        country_data1 = covid.get_status_by_country_id(country_id1)
        country_data2 = covid.get_status_by_country_id(country_id2)
        print('\n-----------------------------')
        for x in country_data2:
            print('() ',x,':',country_data1[x])
        print('\n')
        for y in country_data2:
            print('() ',x,':',country_data2[x])
        print('-----------------------------\n')

        
#Function: print the information   
def info_print():
    print('\n-----------------------------------------------------')
    print("() Source: 'worldometers'")
    print('() Library created by CovidJohn Hopkins University API')
    print('() Program created by Gioele Ferrari A.S.')
    print('-----------------------------------------------------\n')


#Function: print a random country
def random_print():
    random_id = random.randint(1,188)
    country_data = covid.get_status_by_country_id(random_id)
    print('\n-----------------------------')
    for x in country_data:
        print('() ',x,':',country_data[x])
    print('-----------------------------\n')


# While cycle: print selection menu
valid = True
while valid:
    print('\n-----------------------------')
    print('(1) Print global cases')
    print('(2) Print cases by country')
    print('(3) Print country list')
    print('(4) Compare teo countries')
    print('(5) Random country print')
    print('(6) Print information')
    print('(X) End search')
    print('-----------------------------\n')
    choose = str(input('- Choose: '))
    
    #If: enter according to your choice
    if choose == '1':
        worldwide_covid_cases()
    if choose == '2':
        covid_country_cases()
    if choose == '3':
        print_countries()
    if choose == '4':
        compare_countries()
    if choose == '5':
        random_print()
    if choose == '6':
        info_print()
    if choose == 'x' or choose == 'X':
        valid = False
