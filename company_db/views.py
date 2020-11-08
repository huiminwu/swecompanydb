from django.shortcuts import render

posts = [
	{
		'author': 'CoreyMS', 
		'title': 'BlogPost',
		'content': 'first post cont',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'Jane doe', 
		'title': 'BlogPost 2',
		'content': 'second post cont',
		'date_posted': 'August 28, 2018'
	},
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'company_db/home.html', context)

def about(request):
	return render(request, 'company_db/about.html', {'title': 'About'})