import re
import urllib
import requests
import os
from lxml import etree


def get_index_url():
    a = eval(input("电脑壁纸按1、手机壁纸按2、美女图片按3、明星图片按4、头像大全按5、搜索按6："))
    if a == 1:
        search = input("风景1、美女2、植物3、汽车4、明星5、动漫6、建筑7、动物8：")
        index_url = "https://www.gqxz.com/wallpaper/" + urllib.parse.quote(search) + "/"
    elif a == 2:
        search = input("风景1、美女2、植物3、游戏4、明星5、动漫6、动物7：")
        index_url = "https://www.gqxz.com/mobile/" + urllib.parse.quote(search) + "/"
    elif a == 3:
        search = input("清纯1、性感2、日本3、车模宝贝4、丝袜美腿6、Cosplay7：")
        index_url = "https://www.gqxz.com/beauty/" + urllib.parse.quote(search) + "/"
    elif a == 4:
        search = input("内地女星1、内地男星2、港台女星3、欧美女星7：")
        index_url = "https://www.gqxz.com/star/" + urllib.parse.quote(search) + "/"
    elif a == 5:
        search = input("微信1、男生2、女生3、情侣4、欧美5、动漫6、明星7：")
        index_url = "https://www.gqxz.com/portrait/" + urllib.parse.quote(search) + "/"
    elif a == 6:
        keyword = input("请输入搜索关键词：")
        index_urls = "https://www.gqxz.com/search/?keyword="
        index_url = index_urls + urllib.parse.quote(keyword, safe='/')
    return index_url


def send_request(url):
    return requests.get(url, headers=headers, timeout=3).content


def parse(html_str):
    html = etree.HTML(html_str)
    titles = html.xpath('//img')
    # print(titles)
    content_list = []
    for title in titles[:30]:
        item = {}
        item['title'] = title.xpath('./@alt')[0]
        item['href'] = "https://www.gqxz.com" + title.xpath('../@href')[0]
        content_list.append(item)
        print(item)
    # print(content_list)
    return content_list


# 获取每张写真集的img_url
def get_img_url(detail_html):
    html = etree.HTML(detail_html)
    img_url = html.xpath('//div[@id="endtext"][@class="content_center"]/p/img/@src')[0]
    # print(img_url)
    return img_url


def save_image(final_dir, img_url):
    image_data = send_request(img_url)
    file_name = final_dir + '/' + img_url[-9:]
    with open(file_name, 'wb') as image:
        image.write(image_data)


# 判断文件夹是否存在,不存在创建文件夹
def mkdir(dir_name):
    if not os.path.isdir("D:\Python爬取\图片\美女" + '/' + dir_name):  # 如果保存的路径不存在
        os.makedirs(r"D:\Python爬取\图片\美女" + "/" + dir_name)  # 如果不存在。我们将创立这个路径
    path = "D:\Python爬取\图片\壁纸" + "/" + dir_name + "/"
    return path


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Referer": "https://www.mzitu.com/"
    }

    # 1. 获取网站url
    index_url = get_index_url()
    # 2. 解析url
    html_str = send_request(index_url).decode()
    # 3. 获取网站url中的写真的url
    content_list = parse(html_str)
    j = 1
    # 获取每张写真集并解析
    for content in content_list[:30]:
        img_url_list = []
        print("-" * 30 + '正在获取第{}套壁纸集'.format(int(j)) + "-" * 30)
        j = j + 1
        # 获取每张写真集的img_url
        # 第一页的img地址
        dir_name = content['title']
        next_url = content['href']
        print(dir_name)
        # print(next_url)
        detail_html = send_request(next_url)
        img_url = get_img_url(detail_html)
        a = img_url
        b = 0
        i = 1
        while a != b:
            final_dir = mkdir(dir_name)
            if a != 0:
                print(a + "下载完成！！")
                save_image(final_dir, a)
            a = b
            i = i + 1
            b = str(i)
            n = "_" + b + ".html"
            nexturl = re.sub(".html", n, next_url)
            detail_html = send_request(nexturl)
            img_url = get_img_url(detail_html)
            b = img_url
        print(a + "下载完成！！")
        save_image(final_dir, a)
