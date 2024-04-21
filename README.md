How to run the project 
1. Create a virtual environment: python -m venv myworld 
2. Activate the virtual environment: source myworld/bin/activate
3. Install django in the virtual env: python -m pip install django
4. Install bootstrap in the virtual env: python -m pip install django-bootstrap-v5
5. install pipenv in venv: pip install pipenv 
6. Install djangorestframework and corsheaders in venv: pipenv install djangorestframework
7. pipenv install django-cors-headers
8. Runserver command after navigating to project directory: python manage.py runserver 

Notes 
Any time you make changes to the django models you will need to migrate the changes:
python manage.py makemigrations 
python manage.py migrate 
And then runserver again 

Html changes should be continuously updated on the page. 

General rule: make sure to pull before you push any changes onto the main branch so any changes from other ppl will be reflected in your code. 
