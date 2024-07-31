from .. import Tools, Http, String

def ChromeExtensionDownload(id_or_url:str, output_file:str, chromeversion:str='125.0.6422.113'):
    from urllib.parse import urlparse
    from urllib.parse import urlencode
    from urllib.request import urlopen
    import os

    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))

    try:
        ext_url = urlparse(id_or_url)
        ext_id = os.path.basename(ext_url.path)
    except:
        ext_id = id_or_url

    crx_base_url = 'https://clients2.google.com/service/update2/crx'
    crx_params = urlencode({
        'response': 'redirect',
        'prodversion': chromeversion, # chrome的版本
        'acceptformat': 'crx2,crx3',
        'x': 'id=' + ext_id + '&uc'
    })

    crx_url = crx_base_url + '?' + crx_params
    crx_path = output_file if output_file is not None else ext_id + '.crx'

    with open(crx_path, 'wb') as file:
        file.write(urlopen(crx_url).read())

def ChromeExtensionInfomation(id_or_url:str) -> dict:
    res = {
        # 'name': "",     # str
        # "category": "", # str
        "score": "",    # int
        "rates": "",    # int                                                                                                                                   
        "featured": "", # int                                                                                                                                
        "website": "",  # string                                                                                                                              
        # "users": "",    # int                                                                                                                                   
        "version": "",  # string                                                                                                                              
        "update_timestamp": "",     # int                                                                                                                        
        "update_time_string": "",   # string                                                                                                                   
        "size": "",     # string                                                                                                                                 
        "offered_by": "",   # string                                                                                                                           
        "description": "",  # text                                                                                                                            
        # "link": "",     # string                                                                                                                                 
        "extension_id": "", # string                                                                                                                         
        "isalive": "",  # int 
    }
    if '://' in id_or_url:
        resp = Http.Get(id_or_url) 
    else:
        resp = Http.Get(f"https://chromewebstore.google.com/detail/{id_or_url}") 
    
    res['link'] = resp.URL

    x = Tools.XPath(resp.Content)

    res['name'] = x.Find("/html/body/c-wiz/div/div/main/div/section[1]/section/div[1]/a").Text()

    res['category'] = ','.join([i[1] for i in String(x.Find("/html/body/c-wiz/div/div/main/div/section[1]/section/div[1]/div[2]").Html()).RegexFind(r"<a.+?>(.+?)</a>")])
    res['users'] = int(String(x.Find("/html/body/c-wiz/div/div/main/div/section[1]/section/div[1]/div[2]").Html()).RegexFind(r">([0-9,]+) user")[0][1].replace(',', ""))

    