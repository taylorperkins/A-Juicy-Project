# A Juicy Project
Project demonstrating my ability to create a basic web application using Flask, and convey details of a third party api.

## Setup
Here are the steps needed to run before you can play around with this project!!
Nothing too crazy, just a few pre-requisites.

* First, you will need to register an account through the NutritionIX API.
You should have two values after doing so, your Application ID and an Application Key.
You don't need to do anything with these values yet.. But hang on to them!
* Make sure you have the appropriate version of [python](https://www.python.org/downloads/) installed (2.7)
* Open your terminal and clone down this repository
* Run `cd A-Juicy-Project/`
* Remember those keys??
Now we are going include them in our application so that we have the correct permissions for the data in this project.
Make sure to keep the single quotes within these next two commands!!
    * `echo "NUTRITIONIX_APP_ID = '<APPLICATION ID GOES HERE>'" >> a_juicy_project/config.py`
    * `echo "NUTRITIONIX_API_KEY = '<APPLICATION KEY GOES HERE>'" >> a_juicy_project/config.py`
* Create a virtual environment
    * `virtualenv --python=<python location> venv`
    * `source venv/bin/activate`
* Run dependencies for this project `pip install -e .` (Don't forget the period!!)
* Set up a couple of flask settings
    * `export FLASK_APP=a_juicy_project`
    * `export FLASK_ENV=development`
* And finally.. Run the project using `flask run`

Phew!
If you have made it this far, you are golden for the rest of our journey.
The last command you ran in your terminal should have started the flask project locally on your machine.
Go ahead and paste `http://127.0.0.1:5000/` in your browser, and everything should be available to you.

## Breakdown
There are 3 main features of this application.

1. The page you are on currently!
This is a web UI displaying all of the products for the brand Juicy Juice from the NutritionIX API.
On this page, you see a table displaying the name, item ingredients, and the item id for each individual item.
In the nav bar you are given a dropdown where you can select an ingredient.
On selection, the table changes to only show the items that contain the ingredient you selected.
Pretty radical isn't it?!

The remaining 2 features are only api endpoints that you can access.
Going to the following urls will not display a nice format, but will instead show you a JSON representation of the data associated with that endpoint.

2.  Clicking the `Total Items` button in the navbar should redirect you to the `/counts` endpoint.
If you are not redirected, please paste `http://localhost:5000/counts` in a new tab.
Here, you see the count of all the products for Juicy Juice in JSON format.
```
{
  "total_products": 161
}
```

3. Clicking the `Calories` button in the navbar should redirect you to the `/calories` endpoint.
If you are not redirected, please paste `http://localhost:5000/calories` in a new tab.
Here, you see a bit more information on the products.
This information includes:

    * Average Calories Per Fl Oz.
    This field was created by me.
    There were many units of measurement that came back from the product list, and I chose to determine this statistic for only a couple of them.
    These measurements were `fl oz, 'fl oz conc', 'ml', and 'mL'`.
    You can see the code for determining this statistic [here](./a_juicy_project/logic/calories.py).
    If a product did not contain a unit of measurement in this list, I returned an error message giving a specific explanation on why it can not be ocnverted.
    * Item Name
    * Calories (I saw this value as total calories in the entire product, not by serving size)
    * Ingredient Statement
    * Serving Size Quantity
    * Serving Size Unit
    * Servings Per Container

I chose to include all of these fields for an easy spot checking for the avg calories per fl oz.
Here is an example response:

```
[
  {
    "51c36c9f97c3e69de4b083da": {
      "avg_calories_per_fl_oz": 2.5,
      "item_description": "Berry",
      "item_name": "100% Juice, Berry",
      "nf_calories": 120,
      "nf_ingredient_statement": "Apple Juice, Pear Juice, Grape Juice, and Raspberry Juice (Water, Juice Concentrates), Natural Flavors, Ascorbic Acid (Vitamin C), Citric Acid.",
      "nf_serving_size_qty": 8,
      "nf_serving_size_unit": "fl oz",
      "nf_servings_per_container": 6
    }
  },
  {
    "51c36ca597c3e69de4b0840b": {
      "avg_calories_per_fl_oz": "NA",
      "error": "Cannot convert box to fl oz",
      "name": "100% Juice, Berry"
    }
  },
  ...
]
```


## Final Thoughts

This was a fun project!!
It has been a long time since I have written any HTML or Javascript, and I definitely cannot take credit for the layout of the home page.
I did not want to incorporate a front-end framework like Angular or React for this project, so I stuck with basic bootstrap and jquery.

Full credit for styling and animation:
```
Creative Tim: https://www.creative-tim.com/product/light-bootstrap-dashboard
```

After downloading this free template, I stripped out everything I didnt want (almost everything), and kept the main guts (table view and navbar).
I did incorporate some Javascript of my own that you can see [here](a_juicy_project/templates/navbar.html).
This was for the filtering of the elements through the navbar.

I wanted to create a flask `package` (setup.py, etc).
This allowed me to separate out my different components used in the process; the views, templates, logic, exceptions, and even app.py into __init__.py.
Please take the architecture with a grain of salt!
This was my first time creating a package vs a module.
I would love to be show some best practices surrounding the design, I am sure there are flaws in this project.

For the filtering of the ingredients, that took a little bit of time to figure out!
You can see all of the code for my final result [here](a_juicy_project/logic/ingredient_list_hash.py).

The code for handling the NutritionIX API can be found [here](a_juicy_project/logic/nutritionix_service.py).
This version is definitely MVP only.
I would love to revisit this and include some async capabilities, as well as better flexibility for pages and limits.

I would also love to include a specific "item" view for all of the products if you choose to click them on the table.
Endpoint would be `/product/<item_id>`.
V2!!!

Please don't hesitate to ask questions or leave feedback. Thank you!!





