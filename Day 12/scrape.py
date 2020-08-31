import requests

def url_to_file(url,filename="world.html"):
    r = requests.get(url)
    if r.status_code==200:
        html_text=r.text
        with open(filename,'w') as f:
            f.write(html_text)
        return html_text
    return ""        

url = 'https://www.boxofficemojo.com/year/world/'

url_to_file(url)

