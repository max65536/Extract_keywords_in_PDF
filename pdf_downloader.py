from urllib import response
import requests
import json
from lxml import html
from IPython import embed

def parse_jsonpcallback(text):
    loc = text.find('(')
    return json.loads(text[loc+1:-1])     

def json_to_links(files_json):
    data = files_json['pageHelp']['data']
    links = {}
    for item in data:
        links[item['TITLE'].replace(' ', '_')] = item['URL']
    return links

def get_data(begin_date, end_date):

    cookies = {
        'gdp_user_id': 'gioenc-19db5g40%2Ce826%2C508g%2C88b5%2C30bd5c7d1197',
        'ba17301551dcbaf9_gdp_session_id': '94d7539d-4d73-459c-a82e-199fb18eacdd',
        'ba17301551dcbaf9_gdp_session_id_94d7539d-4d73-459c-a82e-199fb18eacdd': 'true',
        'yfx_c_g_u_id_10000042': '_ck22102218460913953797135434335',
        'yfx_f_l_v_t_10000042': 'f_t_1666457169215__r_t_1666457169215__v_t_1666458162211__r_c_0',
    }

    headers = {
        'Host': 'query.sse.com.cn',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Referer': 'http://www.sse.com.cn/',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'gdp_user_id=gioenc-19db5g40%2Ce826%2C508g%2C88b5%2C30bd5c7d1197; ba17301551dcbaf9_gdp_session_id=94d7539d-4d73-459c-a82e-199fb18eacdd; ba17301551dcbaf9_gdp_session_id_94d7539d-4d73-459c-a82e-199fb18eacdd=true; yfx_c_g_u_id_10000042=_ck22102218460913953797135434335; yfx_f_l_v_t_10000042=f_t_1666457169215__r_t_1666457169215__v_t_1666458162211__r_c_0',
    }

    params = {
        'jsonCallBack': 'jsonpCallback49076157',
        'isPagination': 'true',
        'pageHelp.pageSize': '25',
        'pageHelp.pageNo': '1',
        'pageHelp.beginPage': '1',
        'pageHelp.cacheSize': '1',
        'pageHelp.endPage': '1',
        'productId': '',
        'securityType': '0101,120100,020100,020200,120200',
        'reportType2': 'DQBG',
        'reportType': 'YEARLY',  # Yearly report
        'beginDate': begin_date,
        'endDate': end_date,
        '_': '1666458162259',
    }

    response = requests.get('http://query.sse.com.cn/security/stock/queryCompanyBulletin.do', params=params, cookies=cookies, headers=headers, verify=False)
    return response


###############################################################################################################

begin_date="2022-06-25"
end_date="2022-07-22"

######################################################################################


response = get_data(begin_date=begin_date, end_date=end_date)
files_json = parse_jsonpcallback(text=response.text)
links = json_to_links(files_json)

root_url = "http://www.sse.com.cn"

# embed()

count=0
for name, link in links.items():
    count+=1
    # download(url=root_url+link, name=str(count))
    response = requests.get(root_url+link)
    with open(name+".pdf", "wb") as f:
        f.write(response.content)
    
    # break


