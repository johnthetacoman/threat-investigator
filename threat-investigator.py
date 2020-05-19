#Import the webbrowser package to be able to open all the links in new tabs:
import webbrowser

#Create a list of all the urls to launch:
urlList = ["https://www.abuseipdb.com/", "https://talosintelligence.com/", 
           "https://www.virustotal.com/gui/home/upload", "https://www.malwareurl.com/listing-urls.php",
           "https://www.brightcloud.com/tools/url-ip-lookup.php", "https://www.shodan.io/",
           "https://fortiguard.com/webfilter?q=winbricks.co.zw&version=8", "https://www.ipvoid.com/",
           "https://centralops.net/co/DomainDossier.aspx", "https://viewdns.info/"]

#Using a for loop, open each link:
for link in urlList:
    webbrowser.open_new_tab(link)
