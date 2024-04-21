How to run the project 
1. Create a virtual environment 
	python -m venv myworld 
2. Activate the virtual environment
   source myworld/bin/activate
3. Install django in the virtual env 
python -m pip install django
Install bootstrap in the virtual env 
python -m pip install django-bootstrap-v5
Runserver command after navigating to project directory 
python manage.py runserver 

Any time you make changes to the django models you will need to migrate the changes:
python manage.py makemigrations 
python manage.py migrate 
And then runserver again 

Html changes should be continuously updated on the page. 

General rule: make sure to pull before you push any changes onto the main branch so any changes from other ppl will be reflected in your code. 
