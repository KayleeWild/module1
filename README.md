# Overview

"My Everythings!!!" is a simple, e-commerce web-app made with the Django framework. The items on the site are not for sale, and shipping/payment information is for demo purposes only. No charges are made and no product will be shipped to you at the completion of the checkout product. It can be deployed locally through a test server. Simply:
1) Download the files to your IDE of choice. Make sure python and pip are installed.
2) Open a terminal and type: source venv/bin/activate
3) To install Django, type: python3 -m pip install Django
4) Start the server by typing: python3 manage.py runserver
5) Open your web browser and go to http://localhost:8000/items/

My purpose for writing this software is to expirament with website-writing using Django. It implements many Django features, including models, views, forms, and more. The majority is written in python, with a few accompanying files written in html or css. This project taught me how to learn a new framework from online resources, and opened my mind to new ways to accomplish a task.

["My Everythings!!!" Demo Video](https://youtu.be/XNnkEUoTpy0)

# Web Pages

On each page, there is a navigation bar displayed at the top that allows the user to view their cart or continue shopping. The starting page is a gallery of random products to browse. The items were chosen at random from my house for demonstration purposes only. By clicking the "Read More" button, a new view opens where the user can see a detailed description of the product, and a larger view of the image. On both the gallery view and the detailed view there is a button that says "Add to Cart." Click and it will take the user to their cart, showing the product just added, the price, the quantity of items added, and the option to remove the item(s). The cart view shows the total cost and also has a button that takes the user to the checkout view. Here, the user is prompted to fill out their shipping and payment information, then given the option to place the order or continue shopping. When the "order" is placed, the user is redirected to a page that displays a message indicating that the order was placed.

# Development Environment

This software was developed in VSCode and the local test server that ran in my web browser. I also was able to use the admin site to upload images and make changes to the items displayed on my page.

It was written in Python3 using the Django framework, collaborating with html and css. It makes use of libraries like admin, AppConfig, forms, models, urls, shortcuts, and more.

# Useful Websites

* [RealPython Django Tutorial](https://realpython.com/get-started-with-django-1/#create-a-view)
* [W3Schools Django Tutorial](https://www.w3schools.com/django/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Add more detailed CSS- To leverage the most of Django, I used bootstrap to style the pages. However, there were some things I didn't like about the stylesheet, so I added my own to supplement. In the future, I will need to either do more research on bootstrap or make my own stylesheet more robust.
* Create user sign-in page- Allowing users to create profiles will increase security and usability. Saving card and shipping information to each profile will accelerate the checkout process. 
* Connecting to cloud server- Currently the site can only be accessed on a local machine. Free sites like GitHub Pages won't deploy the site because of the server-based framework Django offers. Connecting it to 3rd-party cloud services sould allow the site to be connected to the web and accessed at any time. 
