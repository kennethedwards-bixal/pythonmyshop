## 1
Always use DecimalField to store monetary amounts. FloatField uses Python's float type internally, whereas DecimalField uses Python's Decimal type. By using the Decimal type, you will avoid float rounding issues.

## 2
You use the product ID as a key in the cart's content dictionary. You convert the product ID into a string because Django uses JSON to serialize session data, and JSON only allows string key names. The product ID is the key, and the value that you persist is a dictionary with quantity and price figures for the product. The product's price is converted from decimal into a string in order to serialize it. Finally, you call the save() method to save the cart in the session.

The save() method marks the session as modified using session.modified = True. This tells Django that the session has changed and needs to be saved.

## 3

In the __iter__() method, you retrieve the Product instances that are present
in the cart to include them in the cart items. You copy the current cart in the cart variable and add the Product instances to it. Finally, you iterate over the cart items, converting each item's price back into decimal, and adding a total_price attribute to each item. This __iter__() method will allow you to easily iterate over the items in the cart in views and templates.

You also need a way to return the number of total items in the cart. When the len() function is executed on an object, Python calls its __len__() method to retrieve its length. Next, you are going to define a custom __len__() method to return the total number of items stored in the cart.

## 4

You set the DJANGO_SETTINGS_MODULE variable for the Celery command-line program.

You create an instance of the application with app = Celery('myshop').
- You load any custom configuration from your project settings using the config_from_object() method. The namespace attribute specifies the prefix that Celery-related settings will have in your settings.py file. By setting the CELERY namespace, all Celery settings need to include the CELERY_ prefix in their name (for example, CELERY_BROKER_URL).
- Finally, you tell Celery to auto-discover asynchronous tasks for your applications. Celery will look for a tasks.py file in each application directory of applications added to INSTALLED_APPS in order to load asynchronous tasks defined in it.

## 5

You define the order_created task by using the task decorator. As you can see,
a Celery task is just a Python function decorated with @task. Your task function receives an order_id parameter. It's always recommended to only pass IDs to task functions and lookup objects when the task is executed. You use the send_mail() function provided by Django to send an email notification to the user who placed the order.