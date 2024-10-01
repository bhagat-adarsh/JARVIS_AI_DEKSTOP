import requests
import pywhatkit as kit

def find_my_ip():
    ip_address = requests.got('https://api.ipify.org?format=json').jason()
    return ip_address["ip"]

def search_on_gooogle(query):
    kit.search(query)
    
def youtube(vedio):
    kit.playonyt(vedio)
    
def bing_ai(query):
    kit.search=(query)
    
def black_box_ai(query):
    kit.search(query)