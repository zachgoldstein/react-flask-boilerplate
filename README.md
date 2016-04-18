## Flask-React Boilerplate ##

This is a quick set of boilerplate to get projects setup and moving quickly.
The main idea here is to use python on the backend with a JS heavy frontend.  

Main Features:
* Flask backend
* Mongodb for storage
* Reactjs frontend

Extras:
* Vagrant for local environment
* Fabric tasks to simplify common activities
    * Setup environment
    * Deployments to AWS
    * Performance benchmarks
* Flask-security and basic user management flows
    * Sign-up
    * Sign-in, 
    * Reset Password
* Flask-admin for system administration
* Flask debug toolbar in dev mode
* Python unit tests via pytest and Factory-Boy
* Python integration tests via WebTest
* Frontend testing via Jest

(As of April 18, 2016)

Why Python?
Python's simplicity and guiding philosophy matches well with my ideology. I've learned alot from adventures with golang, and one of the central ones is the beauty of being able to go into any file and both understand and learn from it. I like the idea that there are certain, preferred ways of doing things, and I've found these ideas lead to benefits to general code quality. While the static nature of golang leads my use of the language to more niche needs, python seems to fit well. Compared to ruby or node, I find the general ecosystem to be spread across many more disciplines. Python has very strong libraries in areas like data science, big data, web scraping, and a bunch of others, so you can do alot more there. I don't find get alot of benefit out of keeping the frontend and backend code in the same language, and instead prefer to keep the backend logic close to these other areas/libraries.

Why Flask?
Flask is like lego, so I'm a big fan. I prefer to bolt various small pieces of functionality together to suit my needs, than to start with something large and remove the pieces I don't want. 

Why Reactjs?
Reactjs seems to be pretty dominant in front-end JS land, with a good community and strong productivity gains over the alternatives (angular, ember, etc). I've found it to be much easier to compartmentalise components with it.



