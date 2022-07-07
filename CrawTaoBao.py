import requests
import re

def getHTMLText(url):
    try:
#登录淘宝后的cookie，可行
#        mycookie="thw=xx; enc=IF0tLtJlC8qiW6gBFsg6ID7HDBet7S%2Fwa6d6cZ9Aafke4ReE58hwYXjiJ0AsjHifgV3QpNvPG7a%2Fr6effGjlt6d7gMncAxr4LazUiT1zwoA%3D; UM_distinctid=17ec2ae02466e2-08b6e98ba0b377-5e181959-e1000-17ec2ae0247e7b; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1643943450,1643943827; xlly_s=1; t=c1900ab2ab2c2c61e4329420ffd16a40; _m_h5_tk=6a1bd700add51d6f1338476cb47bdae6_1651898469900; _m_h5_tk_enc=2711c675a46885504a265a14d1ab3915; CNZZDATA1256793290=1288171293-1643939828-%7C1651887296; _samesite_flag_=true; cookie2=1d986d29b41721ab5190802138394e75; _tb_token_=e37e7ee71e5bb; mt=ci=0_0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; sgcookie=E100d2iCyLjk1KNpwU91pn16b4lWpZxtRTfwR7Z9yBJdTN4uL8Pd%2B8wMuxZag0NFDg3As%2FCQLzqLd%2Bdz%2FV6aQEmcJEuXaj7Bzpojlxhr7YWHmNq9w6%2FntuKmM%2BqUXLtjgfnZ; x5sec=7b227365617263686170703b32223a2238633431383638363263353961363635363935643337313932653936616262384349446631354d47454d364137634f436c36505066426f504d6a49774f4455794d4451314e4449314e5473784d4b6546677037382f2f2f2f2f77453d227d; tracknick=; JSESSIONID=7E79030E869A515E7EDD9793D666DF96; cna=BdWCGvYVoWMCAXzwKmV8KRSy; tfstk=cHnhBsAfp2zBd24ilHZBVFy2C9TOaIRUT0oKbpxDkeDzvGoTLsjC7ZrpWdVwGB75.; l=eBa09LuugqOtBB52BO5Zourza77OnIOb81VzaNbMiInca6Mh9ETtoNC3P_M6WdtxgtfUvetzI1_A9Rhw8IUdgmyD-J-rCyClcY96-; isg=BJCQYMtZxma2uZnrry_hCcxHYd7iWXSjsO9XzIpgUuuUxTFvMmixM8C3nI0lMix7"
       
#未登陆的cookie
#        mycookie="_bl_uid=6hkz5zIC7FFthne7Ir2I3d8oqqe2; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1643943324; thw=xx; enc=IF0tLtJlC8qiW6gBFsg6ID7HDBet7S%2Fwa6d6cZ9Aafke4ReE58hwYXjiJ0AsjHifgV3QpNvPG7a%2Fr6effGjlt6d7gMncAxr4LazUiT1zwoA%3D; UM_distinctid=17ec2ae02466e2-08b6e98ba0b377-5e181959-e1000-17ec2ae0247e7b; xlly_s=1; t=c1900ab2ab2c2c61e4329420ffd16a40; _m_h5_tk=6a1bd700add51d6f1338476cb47bdae6_1651898469900; _m_h5_tk_enc=2711c675a46885504a265a14d1ab3915; XSRF-TOKEN=6d880bc9-942d-4f80-8e2e-d9d822226e69; _samesite_flag_=true; cookie2=1d986d29b41721ab5190802138394e75; _tb_token_=e37e7ee71e5bb; mt=ci=0_0; sgcookie=E100d2iCyLjk1KNpwU91pn16b4lWpZxtRTfwR7Z9yBJdTN4uL8Pd%2B8wMuxZag0NFDg3As%2FCQLzqLd%2Bdz%2FV6aQEmcJEuXaj7Bzpojlxhr7YWHmNq9w6%2FntuKmM%2BqUXLtjgfnZ; tracknick=; cna=BdWCGvYVoWMCAXzwKmV8KRSy; tfstk=cJuFBNb3xeLeL9zWDyayFE5D2Zcdwuqu0NP8xKXD2LZxDWfcPTFgBEFaM1Wux; l=eBa09LuugqOtBHHDBOfanurza77OSIRYYuPzaNbMiOCPOa1B5TEcW645aIT6C3GVh6BHR3yG1ZCpBeYBqQAonxvOvhLyCdMmn; isg=BHt7Dnr6nfeKWKLKyBaqeCMOCl_l0I_SrzbM7W04V3qRzJuu9aAfIpkO4myCd-fK"

#再次使用一个未登陆的cookie,可行       
#        mycookie="_bl_uid=6hkz5zIC7FFthne7Ir2I3d8oqqe2; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1643943324; thw=xx; enc=IF0tLtJlC8qiW6gBFsg6ID7HDBet7S%2Fwa6d6cZ9Aafke4ReE58hwYXjiJ0AsjHifgV3QpNvPG7a%2Fr6effGjlt6d7gMncAxr4LazUiT1zwoA%3D; UM_distinctid=17ec2ae02466e2-08b6e98ba0b377-5e181959-e1000-17ec2ae0247e7b; xlly_s=1; t=c1900ab2ab2c2c61e4329420ffd16a40; _m_h5_tk=6a1bd700add51d6f1338476cb47bdae6_1651898469900; _m_h5_tk_enc=2711c675a46885504a265a14d1ab3915; XSRF-TOKEN=6d880bc9-942d-4f80-8e2e-d9d822226e69; _samesite_flag_=true; cookie2=1d986d29b41721ab5190802138394e75; _tb_token_=e37e7ee71e5bb; mt=ci=0_0; sgcookie=E100d2iCyLjk1KNpwU91pn16b4lWpZxtRTfwR7Z9yBJdTN4uL8Pd%2B8wMuxZag0NFDg3As%2FCQLzqLd%2Bdz%2FV6aQEmcJEuXaj7Bzpojlxhr7YWHmNq9w6%2FntuKmM%2BqUXLtjgfnZ; tracknick=; cna=BdWCGvYVoWMCAXzwKmV8KRSy; tfstk=caElB_f6ezu74g005gi5AZ7aISIOwqCrakr80TjGypK9QdfcPE8Z2ZBmg11yR; isg=BKWlkC6eK9HgHkwEgkQ83vmctGHf4ll0hUSio6eKYVzrvsUwbzJpRDNeTCLIpXEs; l=eBa09LuugqOtBBKtBOfanurza77OSIRYYuPzaNbMiOCP_81B5atRW645aLT6C3GVh6HMR3yG1ZCLBeYBqQOSnxvOvhLyCdMmn"

#登陆后，可行
#       mycookie="thw=xx; enc=IF0tLtJlC8qiW6gBFsg6ID7HDBet7S%2Fwa6d6cZ9Aafke4ReE58hwYXjiJ0AsjHifgV3QpNvPG7a%2Fr6effGjlt6d7gMncAxr4LazUiT1zwoA%3D; UM_distinctid=17ec2ae02466e2-08b6e98ba0b377-5e181959-e1000-17ec2ae0247e7b; xlly_s=1; t=c1900ab2ab2c2c61e4329420ffd16a40; _m_h5_tk=6a1bd700add51d6f1338476cb47bdae6_1651898469900; _m_h5_tk_enc=2711c675a46885504a265a14d1ab3915; _samesite_flag_=true; cookie2=1d986d29b41721ab5190802138394e75; _tb_token_=e37e7ee71e5bb; cna=BdWCGvYVoWMCAXzwKmV8KRSy; sgcookie=E100Vz6EqlDCt43CE%2FF4EsfSNi3DOkgu30MdfeVbk4q7EY%2BAp81Ckx6i4avBbECh%2FsGF6q1r0iuCffIKQUHPwOxzbolYJ89O9sLRHGneYxX6Q9eaDykn82nRTCAbOcQkl941; unb=2208520454255; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&nk2=F5RHos8NWtOPGVA%3D&vt3=F8dCvC6H4Jepnz%2B9F9E%3D&id2=UUphwoIbYpq64WHMCw%3D%3D; csg=3f9562e3; lgc=tb230051673; cancelledSubSites=empty; cookie17=UUphwoIbYpq64WHMCw%3D%3D; dnk=tb230051673; skt=ae0b864a4430cb7f; existShop=MTY1MTg5NzY2NQ%3D%3D; uc4=nk4=0%40FY4MsDOEJhaDRgcKqNd17pyBDfaugw%3D%3D&id4=0%40U2grGRoKoegMaRsPOKdbuVuERQDpSrNv; tracknick=tb230051673; _cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=35b; _nk_=tb230051673; cookie1=W8t10sB30fPBGmscLLtMcVSgP8AIT%2BwJIRJ6keXOH7U%3D; mt=ci=2_1; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&pas=0&cookie21=U%2BGCWk%2F7pY%2FF&cookie14=UoexMytOmbTohA%3D%3D&cookie15=URm48syIIVrSKA%3D%3D; tfstk=cI1PBRckE7Fy40RQBQOUA5zga99RZr9HQj8pElmi2xCUkhJlieiponF9uF3qxLf..; l=eBa09LuugqOtBmILBOfZlurza77tbIRYMuPzaNbMiOCP_YCH5QflW645MQ8MCnhVh6f6J3yG1ZCLBeYBqsqBfdWqIosM_pMmn; isg=BGpqyR1S_FDlhHM1se2r_9plu9AM2-41xo39svQjz71IJwvh3WtZRY8VslM7j2bN"
        
        mycookie="_bl_uid=6hkz5zIC7FFthne7Ir2I3d8oqqe2; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1643943324; thw=xx; enc=IF0tLtJlC8qiW6gBFsg6ID7HDBet7S%2Fwa6d6cZ9Aafke4ReE58hwYXjiJ0AsjHifgV3QpNvPG7a%2Fr6effGjlt6d7gMncAxr4LazUiT1zwoA%3D; UM_distinctid=17ec2ae02466e2-08b6e98ba0b377-5e181959-e1000-17ec2ae0247e7b; t=c1900ab2ab2c2c61e4329420ffd16a40; sgcookie=E100Vz6EqlDCt43CE%2FF4EsfSNi3DOkgu30MdfeVbk4q7EY%2BAp81Ckx6i4avBbECh%2FsGF6q1r0iuCffIKQUHPwOxzbolYJ89O9sLRHGneYxX6Q9eaDykn82nRTCAbOcQkl941; mt=ci=0_0; tracknick=; cna=BdWCGvYVoWMCAXzwKmV8KRSy; _m_h5_tk=d3eb07b5420995286396f1530ec7a5c8_1652027901888; _m_h5_tk_enc=871610d44fd260765fab421debd16431; cookie2=1f2e7b151cc84ad28cf666717bdfff51; _tb_token_=7bb31be95b038; XSRF-TOKEN=5c4501d5-c838-4ff6-80a4-0160d80699e3; _samesite_flag_=true; tfstk=cKicBsOCHqzberzoRnZXfCNRBD-dw1O4gcox4KvAclKh611DGa7UDUpuaBOV5; isg=BNPTBsjRtY3b03rS4F7y8LvGYlf9iGdK_GU86oXwL_IpBPOmDVj3mjFWOnRqv79C; l=eBa09LuugqOtBFj9BOfanurza77OSIRYYuPzaNbMiOCPOc5B5AKcW64lRDT6C3GVh6wkR3SvCNIkBeYBqQAonxvOvhLyCdMmn; x5secdata=xb3cef767a8234c485981b4fd8864bbffa1652017826a-717315356a1993109894abazc2aaa__bx__fourier.taobao.com%3A443%2Frp; xlly_s=1"
        kv = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
            "cookie":mycookie
        }
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]) + '\n')

def main():
    goods = "显示屏"
    depth = 4
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infolist,html)
        except:
            continue
    printGoodsList(infolist)

main()