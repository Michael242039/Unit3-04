import ui

def isolate_year(sender):
	date = str(sender.date)
	year = int(date[0:4])
	view['result_label'].text = str(check_leap_year(year))
	
def check_leap_year(year):
	if(year % 4 == 0):
		if(year % 100 == 0):
			if(year % 400 == 0):
				return(str(year) + ' is a leap year')
			else:
				return(str(year) + ' is not a leap year')
		else:
			return(str(year) + ' is a leap year')
	else:
		return(str(year) + ' is not a leap year')

view = ui.load_view()
view.present('sheet')
