
import twint
def fetch_value():
	keyword = 'http://twitter.com/SawabCenterEN'
	url = keyword
	x = url.split("/")
	if x[0] == 'https:':
		x = url.split("/")
		keyword = x[-1]
	elif x[0] == 'http:':
		x = url.split("/")
		keyword = x[-1]
	else:
		keyword = keyword
	c = twint.Config()
	c.Username = keyword
	c.Custom['user'] = ['bio']
	c.Lang = "en"
	c.Limit = 100
	c.Store_csv = True
	c.Output = 'new_folder'
	twint.run.Search(c)
if __name__ == '__main__':
	fetch_value()

