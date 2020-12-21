from googlesearch import search 
i=1
SITE = str(input("Site: "))
query = f"site:{SITE}"
final_domains = []
while (i < 20):
        one_result = search(query,num_results=0)
        results = []
        try:
            results.append(one_result[0].split('/')[2])
        except:
            break
        print(results)
        for url in results:
            final_domains.append(url)
            query += f" -site:{url}"
        i += 1
#save what I found in a text file.
with open("G:\Final_results.txt", 'w+') as file:
    for url in final_domains:
        file.write(url + "\n")




    
