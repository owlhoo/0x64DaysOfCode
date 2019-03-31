import re
import threading
import os 

sites = []
with open('ids.txt', 'r') as fajl:                                                      # ids should be the unique identifiers of the things you are looking for on the site i.e. id of the product on shop under one category
	for line in fajl:
		sites.append(line) 

i = 0
for site in sites:
	os.system('curl '+ name_of_site + site.rstrip() + ' >> kek' + str(i) + '.html')     # name of site that you want to get html of
	i += 1


i = 0
link = []
for filename in os.listdir(os.getcwd()):
	if filename.endswith('html'):
		with open('./' + filename, "r") as filee:
			if filename != 'ids.txt' and not filename.endswith('.py'):
				for line in filee:
					lista = line.split(" ")
					for lis in lista:           
						result = re.search(some_regex, lis)                             # some_regex should be the thing you search for on the catalogue of the site
						if result is not None:
							link.append(result.group(0))
t = [None] * 101
link = list(set(link))
for lin in link:
	if i == 101:
		for threaddy in t:
			threaddy.join()
		i = 0
	else:
		t[i] = threading.Thread(target = os.system(f' {command} http://{lin} &'))       # command what to do with the link of the product
		t[i].start()
		i += 1

os.system('rm *.html')
