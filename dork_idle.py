from bs4 import BeautifulSoup
import requests
from colorama import Fore, Back, Style 

subs_original = []
subs_unique = []

#Do google request to search google and get a whole body response text.
def do_req(queryy,start):
    global source
    global query
    payload = {'q':"site:"+queryy,'start':start}
    source = requests.get("https://www.google.com/search",params=payload)

#Getting subdomains from google search body text response.
def getSubs():
    soup = BeautifulSoup(source.text, 'lxml')
    match = soup.find_all('div', class_="BNeawe UPmit AP7Wnd")

    for i in range(0,len(match)):
        subs_original.append(match[i].text)

#Extract only unique subdomains from the predefined list subs_original in another list called subs_unique
def getUnique():
    for i in range(0,len(subs_original)):
        if "›" in subs_original[i]:
            sub = subs_original[i].split("›")[0].strip()
            if sub not in subs_unique:
                subs_unique.append(sub)
        elif "‹" in subs_original[i]:
            sub = subs_original[i].split("‹")[-1].strip()
            if sub not in subs_unique:
                subs_unique.append(sub)
        else:
            sub = subs_original[i].split("›")[0].strip()
            if sub not in subs_unique:
                subs_unique.append(sub)

#Print the output of 
def output(unique_subdomains):
    for domain in unique_subdomains:
        print(domain)

def SaveFile(unique_subdomains,query):
    choice = input("Do you want to save the results in a text file? [y/n]")
    if choice == "y":
        for domain in unique_subdomains:
            with open(f'F:\\domainsfor{query}.txt','a') as file:
                file.write(domain+"\n")
    else:
        quit()



def main():
    query = input("Site: ")
    for start in range(0,500,10):
        do_req(query,start)
        getSubs()
    getUnique()
    output(subs_unique)
    SaveFile(subs_unique,query)

if __name__ == "__main__":
    main()
    
