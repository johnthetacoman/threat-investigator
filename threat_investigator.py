import webbrowser

def open_links(links):
    """
    Opens links in the web browser

    """
    for link in links:
        webbrowser.open_new_tab(link)

links = ["https://www.abuseipdb.com/", "https://talosintelligence.com/", 
           "https://www.virustotal.com/gui/home/upload", "https://www.malwareurl.com/listing-urls.php",
           "https://www.brightcloud.com/tools/url-ip-lookup.php", "https://www.shodan.io/",
           "https://fortiguard.com/webfilter?q=winbricks.co.zw&version=8", "https://www.ipvoid.com/",
           "https://centralops.net/co/DomainDossier.aspx", "https://viewdns.info/"]

open_links(links)