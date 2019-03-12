import webbrowser, requests, bs4

def is_spelling_correct(url):
	res = requests.get(url)
	obj = bs4.BeautifulSoup(res.text, "html.parser")
	abc = obj.select('div span[class=spell-correction-corrected]')
	try:
		if abc[0].getText() == 'Showing results for':
			return False
	except IndexError:
		return True
def get_links_list(url):
	conn = requests.get(url)
	html = bs4.BeautifulSoup(conn.text, "html.parser")
	links = html.select('a')

	A = []
	for tag in links:
	    link = tag.get('href',None)
	    if link is not None:
	        A.append(link)
	return A

song_name = raw_input("Enter name of song: ")
song_name = '+'.join(song_name.split())
url = "https://www.youtube.com/results?search_query=" \
			+ song_name

Links_List = get_links_list(url)
if is_spelling_correct(url) == True:
	first_link_index = 40
else:
	first_link_index = 42

url2 = "https://www.youtube.com" + str(A[first_link_index])
webbrowser.open_new_tab(url2)
