import sys 
import webbrowser

def investigate_ip_address(ip_address):
    """
    Determine if the IP address is a threat by opening investigation links.
    Args:
        ip_address(required): the IP address that will be investigated.
    """
    #Create the proper links to open in the browser for threat investigation:
    ip_address_links = ["https://exchange.xforce.ibmcloud.com/ip/" + ip_address,
             "https://www.abuseipdb.com/check/" + ip_address + "/", 
             "https://talosintelligence.com/reputation_center/lookup?search=" + ip_address + "/", 
             "https://www.virustotal.com/gui/ip-address/" + ip_address + "/detection" ,
             "https://www.malwareurl.com/listing-urls.php",
             "https://www.brightcloud.com/tools/url-ip-lookup.php", 
             "https://www.shodan.io/search?query=" + ip_address + "/",
             "https://fortiguard.com/webfilter?q=" + ip_address + "&version=8",
             "https://www.ipvoid.com/",
             "https://centralops.net/co/DomainDossier.aspx",
             "https://viewdns.info/reverseip/?host=" + ip_address + "&t=1"]

    #Determine the severity of the ip address using the links' results:
    for ip_address_link in ip_address_links:
        webbrowser.open_new_tab(ip_address_link)

if __name__ == "__main__":
    #Investigate the correct ip address/domain/URL based on argument 1:
    if (sys.argv[1] == "ip"):
        investigate_ip_address(sys.argv[2])
    else: 
        print('Please insert an IP address with the "ip" argument preceding it.')