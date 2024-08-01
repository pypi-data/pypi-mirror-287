from .. import Tools, Http, String, Time

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

def ChromeExtensionInfomation(id_or_url_or_pagesource:str) -> dict:
    res = {
        # 'name': "",     # str
        # "category": "", # str
        # "score": "",    # float
        # "rates": "",    # int                                                                                                                               
        # "users": "",    # int                                                                                                                                   
        # "version": "",  # string                                                                                                                              
        # "update_timestamp": "",     # int                                                                                                                        
        # "update_time_string": "",   # string                                                                                                                
        # "description": "",  # text                                                                                                                            
        # "link": "",     # string                                                                                                                                 
        # "extension_id": "", # string                                                                                                                         
        # "isalive": "",  # bool 
    }
    if id_or_url_or_pagesource.startswith("https://") or id_or_url_or_pagesource.startswith("http://"):
        resp = Http.Get(id_or_url_or_pagesource) 
        res['extension_id'] = id_or_url_or_pagesource.strip('/').split('/')[-1]
        pagesource = resp.Content
    elif len(id_or_url_or_pagesource) == 32:
        resp = Http.Get(f"https://chromewebstore.google.com/detail/{id_or_url_or_pagesource}") 
        res['extension_id'] = id_or_url_or_pagesource
        pagesource = resp.Content
    else:
        pagesource = id_or_url_or_pagesource
    
    x = Tools.XPath(pagesource)

    if x.Find('/html/body/c-wiz/div/div/main/div/h1') != None:
        if x.Find('/html/body/c-wiz/div/div/main/div/h1').Text() == 'This item is not available':
            res['isalive'] = False
            return res
        else:
            raise Exception("????????")
    
    res['link'] = resp.URL
    res['name'] = x.Find("/html/body/c-wiz/div/div/main/div/section[1]/section/div[1]/a").Text()

    res['category'] = ','.join([i[1] for i in String(x.Find("/html/body/c-wiz/div/div/main/div/section[1]/section/div[1]/div[2]").Html()).RegexFind(r"<a.+?>(.+?)</a>")])
    res['users'] = int(String(x.Find("/html/body/c-wiz/div/div/main/div/section[1]/section/div[1]/div[2]").Html()).RegexFind(r">([0-9,]+) user")[0][1].replace(',', ""))
    res['score'] = float(String(x.Find("/html/body/c-wiz/div/div/main/div/section[1]/section/div[1]/div[1]/span").Text()).RegexFind(r'(.+?)\((.+?) ratings\)')[0][1])
    res['rates'] = String(String(x.Find("/html/body/c-wiz/div/div/main/div/section[1]/section/div[1]/div[1]/span").Text()).RegexFind(r'(.+?)\((.+?) ratings\)')[0][2]).UnitToNumber()
    res["version"] = String(x.Find("/html/body/c-wiz/div/div/main/div/section[4]/div[2]/ul/li[1]").Html()).RegexFind(r'<div.+?>Version</div><div.+?>(.+?)</div>')[0][1]
    res['update_time_string'] = String(x.Find("/html/body/c-wiz/div/div/main/div/section[4]/div[2]/ul/li[2]").Html()).RegexFind(r'<div .+?>Updated</div><div>(.+?)</div>')[0][1]
    res['update_timestamp'] = Time.Strptime(String(x.Find("/html/body/c-wiz/div/div/main/div/section[4]/div[2]/ul/li[2]").Html()).RegexFind(r'<div .+?>Updated</div><div>(.+?)</div>')[0][1])
    res['description'] = x.Find("/html/body/c-wiz/div/div/main/div/section[3]/div[2]").Text()

    res['isalive'] = True

    return res