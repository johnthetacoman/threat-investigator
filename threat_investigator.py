import webbrowser

def get_user_input(): 
    """
    Obtains a(an) IP address/domain/URL and returns it as a string

    """
    userInput = input("Please enter the IP address/domain/URL to investigate: ")

    return userInput   

def open_links(links):
    """
    Opens links in the web browser

    """
    for link in links:
        webbrowser.open_new_tab(link)

# Get the user's requested IP address/Domain/ URL to investigate:
userInput = get_user_input()

links = ["https://exchange.xforce.ibmcloud.com/ip/" + userInput,
         "https://www.abuseipdb.com/check/" + userInput + "/", 
         "https://talosintelligence.com/reputation_center/lookup?search=" + userInput + "/", 
         "https://www.virustotal.com/gui/ip-address/" + userInput + "/detection" ,
         "https://www.malwareurl.com/listing-urls.php",
         "https://www.brightcloud.com/tools/url-ip-lookup.php", 
         "https://www.shodan.io/search?query=" + userInput + "/",
         "https://fortiguard.com/webfilter?q=" + userInput + "&version=8",
         "https://www.ipvoid.com/",
         "https://centralops.net/co/DomainDossier.aspx",
         "https://viewdns.info/reverseip/?host=" + userInput + "&t=1"]

open_links(links)