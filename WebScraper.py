import requests
import csv

##Change to the path of the data file being used
with open('PythonQuizInput.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)[1:]
    
 
 ## Had to use this header because without defined header 
 ## for request the post request gets terminated because of too many redirects
 ## (I got this header info from some stackoverflow solution to a similar error)
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
##I got this URL from looking at the header data after submmiting a post request
url="https://tools.usps.com/tools/app/ziplookup/zipByAddress"


##Iterate over input CSV changing payload for each request 
##[would probably be better if I set this up as a request session :) ]
for i in list_of_rows:

    payload = {"companyName": i[0], "address1": i[1],
        "city":i[2], "state":i[3], "zip":i[4]}

    ##Post request here
    r=requests.post(url, data=payload,headers=headers).content.decode("utf-8")
    
    ##Checks for success and appends result
    if "SUCCESS" in r:
        i.append("Valid Address")
    else:
        i.append("Not Valid Address")

        
##Write to an output csv as required        
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Company","Street","City","St","ZIPCode","Valid?"])
    writer.writerows(list_of_rows)
