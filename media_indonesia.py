import requests, bs4 , re
from bs4 import BeautifulSoup as bs
page = []
berita = []


def scrap_url():
	link_utama = 'https://mediaindonesia.com/search?q=transformasi%20ekonomi#gsc.tab=0&gsc.q=transformasi%20ekonomi&gsc.page=1'
	r = requests.get(link_utama).content
	mediaindo = bs(r,'html.parser')
	for link in mediaindo.findAll('div',class_='article-content-isi'):
		next = (link.find('a')['href'])
		page.append(next)
		print(f'Scraping url of : {next}')

def scrap_page():
	global page
	for laman in page:
		r = requests.get(laman).content
		laman_berita = bs(r,'html.parser')
		for page in laman_berita.findAll('div', class_='shortcode-content'):
			c = (page.find_all('p'))
			berita.append(c)
			print(f'scraping berita : {c}')

scrap_url()
scrap_page()
