
import requests

country_code_list = ["ABW","AFG","ALB","AND","ARG","AUS","AUT","AZE","BEL","BEN",
                         "BFA","BGR","BHS","BLR","BLZ","BMU","BRB","BRN","BTN","BWA",
                         "CAF","CAN","CHE","CHL","CIV","CMR","COD","COG","CRI","CUB",
                         "CYP","DEU","DMA","DNK","DOM","ECU","ERI","ESP","ETH","FIN",
                         "FJI","FRA","FRO","GAB","GBR","GHA","GIN","GMB","GRC","GRL",
                         "GTM","HKG","HND","HRV","HTI","IDN","IRL","ISR","ITA","JOR",
                         "JPN","KAZ","KGZ","KHM","KIR","KOR","KWT","LAO","LBN","LKA",
                         "LSO","LTU","LVA","MCO","MDG","MEX","MLI","MLT","MMR","MNG",
                         "MOZ","MWI","NER","NGA","NIC","NLD","NOR","NZL","PAK","PAN",
                         "PER","PHL","PNG","POL","PRI","PRT","PSE","RKS","ROU","RUS",
                         "SGP","SLE","SLV","SMR","SOM","SSD","SVK","SVN","SWE","SWZ",
                         "SYC","SYR","TCD","TGO","THA","TJK","TLS","TUR","TWN","TZA",
                         "UGA","UKR","URY","USA","UZB","VEN","VNM","VUT","ZAF","ZMB","ZWE"]


def calc_max_min_death_and_case(country_list):
    confirmed_case_list = []
    confirmed_death_list = []
    
    #For each country code, append the confirmed cases and deaths into lists
    for code in country_code_list:
        for key, val in data_per_code[code].items():
            if key == 'confirmed':
                confirmed_case_list.append(val)
            if key == 'deaths':
                confirmed_death_list.append(val)
    
    #Sort the cases and deaths in ascending order
    #Return the max and min values for each
    confirmed_case_list.sort()
    confirmed_death_list.sort()
    
    smallest_death = confirmed_death_list[0]
    largest_death = confirmed_death_list[-1]
    smallest_case_total = confirmed_case_list[0]
    largest_case_total = confirmed_case_list[-1]
    
    return smallest_death, largest_death, smallest_case_total, largest_case_total

def find_codes(min_death, max_death, min_case, max_case, data_per_code):
    
    #Loop through the dictionary and find values equivalent to max and mins
    #Return the country codes that are associated with the max and mins
    for code in country_code_list:
        for key, val in data_per_code[code].items():
            if key == 'confirmed':
                if val == min_case:
                    min_code_case = code
                elif val == max_case:
                    max_code_case = code
            if key == 'deaths':
                if val == min_death:
                    min_code_death = code
                elif val == max_death:
                    max_code_death = code
        
    return min_code_death, max_code_death, min_code_case, max_code_case
        
        
if __name__ == "__main__":
    
    response = requests.get("https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2021-08-01/2021-08-01")
    
    
    #Parcing to only include the data for each country code
    #Data stored in format of nested dictionary
    data_list = response.json()['data']
    data_per_code = data_list['2021-08-01']
    
    print("\nWelcome to COVID-19 Confirmed Case Lookup for 08-01-2021\n")
    print('The country codes you have to choose from are: ABW, AFG,'
          'ALB, AND, ARG, AUS, AUT, AZE, BEL, BEN, BFA, BGR, BHS, BLR,'
          'BLZ, BMU, BRB, BRN , BTN, BWA, CAF, CAN, CHE, CHL, CIV, CMR,'
          'COD, COG, CRI, CUB, CYP, DEU, DMA, DNK, DOM, ECU, ERI, ESP, ETH,'
          'FIN, FJI, FRA, FRO, GAB, GBR, GHA, GIN, GMB, GRC, GRL, GTM, HKG,'
          'HND, HRV, HTI, IDN, IRL, ISR, ITA, JOR, JPN, KAZ, KGZ, KHM, KIR,'
          'KOR, KWT, LAO, LBN, LKA, LSO, LTU, LVA, MCO, MDG, MEX, MLI, MLT,' 
          'MMR, MNG, MOZ, MWI, NER, NGA, NIC, NLD, NOR, NZL, PAK, PAN, PER,'
          'PHL, PNG, POL, PRI, PRT, PSE, RKS, ROU, RUS, SGP, SLE,'
          'SLV, SMR, SOM, SSD, SVK, SVN, SWE, SWZ, SYC, SYR, TCD,'
          'TGO, THA, TJK, TLS, TUR, TWN, TZA, UGA, UKR, URY, USA,'
          'UZB, VEN, VNM, VUT, ZAF, ZMB, ZWE')
    
    country_code = input("Enter a country code to display COVID-19 data: ")
    
    #loop through the dictionary to display the confirmed cases and deaths
    #Store the cases and and deaths in variables 
    for key, val in data_per_code[country_code].items():
        if key == 'confirmed':
            print('\nThe total confirmed cases since the beginning of the pandemic to 2021-08-01' 
                  ' is: {} cases'.format(val))
            confirm_count = val
        if key == 'deaths':
            print('The total confirmed deaths since the beginning of the pandemic to 2021-08-01'
                  ' is: {} deaths'.format(val))
            death_count = val
    
    #Calculate the death_percentage and print
    death_percentage = round((death_count/confirm_count*100),2)
    print('The current case fatality rate is {}%'.format(death_percentage))
    
    #Call function that will calc the max & min for cases and deaths
    #Assign variables to be called in function to find max and min with code
    min_death = calc_max_min_death_and_case(data_per_code)[0]
    max_death = calc_max_min_death_and_case(data_per_code)[1]
    min_case = calc_max_min_death_and_case(data_per_code)[2]
    max_case = calc_max_min_death_and_case(data_per_code)[3]
    
    min_code_d = find_codes(min_death, max_death, min_case, max_case, data_per_code)[0]
    max_code_d = find_codes(min_death, max_death, min_case, max_case, data_per_code)[1]
    min_code_c = find_codes(min_death, max_death, min_case, max_case, data_per_code)[2]
    max_code_c = find_codes(min_death, max_death, min_case, max_case, data_per_code)[3]
    
    #Print the max & mins and their country codes 
    print('\nAdditional Data Points of Interest')
    print('-----------------------------------\n')
    
    print('The maximum death up to 2021-08-01 is {} deaths' 
          ' from country code {}'.format(max_death, max_code_d))
    print('The minimum death up to 2021-08-01 is {} deaths' 
          ' from country code {}'.format(min_death, min_code_d))
    print('The maximum cases up to 2021-08-01 is {} cases' 
          ' from country code {}'.format(max_case, max_code_c))
    print('The minimum cases up to 2021-08-01 is {} cases' 
          ' from country code {}'.format(min_case, min_code_c))
    
    

    
    