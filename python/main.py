import sys
sys.path.append('/Users/eshochat/Downloads/Olim/python')

from aliya_by_country import *
from aliya_by_gender import *
from aliya_by_settlement import *
from aliya_by_subcont import *
from aliya_per_month import *
from aliya_per_year import *
from aliya_by_district import *
from settlement_list import *
from subcont_list import *
from district_list import *
from top_countries import *
from top_settlement import *
from top_district import *
from countries_list import *

def main():
    print("Choose an option: ")
    print("1. Print Countries list ")
    print("2. Print Subcontinents list ")
    print("3. Print Absorption Settlements list ")
    print("4. Print Districts list ")
    print("5. Bar-chart of the Top-10 Absorption Settlements")
    print("6. Bar-chart of the Top-10 Countries")
    print("7. Bar-chart of the Top Districts")
    print("8. Aliya by Country")
    print("9. Aliya by Subcontinent")
    print("10. Aliya by Gender")
    print("11. Aliya per Year")
    print("12. Aliya per Month")
    print("13. Absorption by Settlement")
    print("14. Absorption by District")
    option = input("Enter your choice (0 - 14): ")
    
    if option == '1':
        countries_list()
    elif option == '2':
        subcont_list() # type: ignore
    elif option == '3':
        settlement_list()
    elif option == '4':
        district_list() # type: ignore
    elif option == '5':
        top_settlement()
    elif option == '6':
        top_countries()
    elif option == '7':
        top_district()
    elif option == '8':
        country = input("Enter the name of the Country: ")
        aliya_by_country(country)
    elif option == '9':
        subcont = input("Enter the name of the Subcontinent: ")
        aliya_by_subcont(subcont)
    elif option == '10':
        aliya_by_gender()
    elif option == '11':
        aliya_per_year()
    elif option == '12':
        while True:
            year_input = input("Enter the year of Aliya: ")
            try:
                year = int(year_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for the year.")
        aliya_per_month(year)
    elif option == '13':
        yeshuv_klita = input("Enter the name of the Absorption Settlement: ")
        aliya_by_settlement(yeshuv_klita)
    elif option == '14':
        machoz = input("Enter the name of the District: ")
        aliya_by_district(machoz)
    else:
        print("Invalid option. Please choose 0 - 14.")

if __name__ == "__main__":
    combined_table_path = '/Users/eshochat/Downloads/Olim/combined_table.csv'
    main()



