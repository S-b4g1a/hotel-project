# Hotel Booking Website
A full-stack hotel booking application built with Django and Python backend, featuring a responsive HTML/CSS frontend. The system allows users to browse hotels, manage bookings, and handle user authentication.
#About
The purpose of this project is to help users navigate their sleeping arrangements when traveling. Built with simplicity and user experience in mind, the website offers an intuitive platform for travelers to find and book hotels across various locations.

#### Responsive screens 


# Core Purpose

- Simplify the hotel booking process for travelers
- Provide an easy-to-navigate interface for browsing hotels
- Enable secure user accounts for booking management
- Offer administrative capabilities for hotel management

# Key User Features

- Browse hotels across multiple locations without an account
- Create personal accounts to access full booking capabilities
- View detailed hotel information and availability
- Manage personal bookings and preferences

# Administrative Features

- Dedicated admin login system
- Add new hotels to the platform
- Remove or update existing hotel listings
- Monitor and manage bookings

# Features

### User Authentication

- Secure login and registration system
- User profile management
- Password reset functionality
- Separate admin and user access levels


## Hotel Management

- Location-based hotel browsing
- Detailed hotel information pages
- Real-time availability updates
- Search and filter functionality


## Booking Management

- Create new hotel bookings
- View existing bookings
- Update booking details
- Cancel bookings


## Frontend

- Responsive design that works on desktop and mobile devices
- Modern and intuitive user interface
- Interactive booking calendar
- Hotel room previews and details

## ERD diagram
- This ERD digram show the relationship between the models within the apps 
![responsivenes_screenshot](/doc_images/erd.png) 



## Technologies Used

### Frontend:

- HTML5
- CSS3


### Backend:

- Python
- Django Framework
- SQLite (development)
- PostgreSQL (production)


### Deployment:

- Heroku
- Gunicorn
- Whitenoise (static files)

#testing
#### HTML Validation :
- All HTML files in the project were validated using the W3C Narkup Validation Service.
https://validator.w3.org/

#### CSS Validation :
- No errors were found when the single CSS file style.css was passed through the W3C Validation Service.
https://jigsaw.w3.org/css-validator/

####Pyhton Validation
- All python code had been put through the CI python linter and all code had been corrected. However, due to the serverity of the some parts of the code e.g links some parts have remaind above the pep8 standard. Very little code exceeded the 79 character limit, but the highest was at 81 which I deemed suitable as the code only exceeded the limit by 1.

- All tests recieved adequite scrores resulting in them being able to past the validator and any inconsistencys that were bought up had been delt with at the appropriate time.

# Responsiveness
- All pages within this site have been tested using Devtools, to ensure that the site is fully responsive on all devices, the main navigation feature remains at the top of the the screen on all devices ensuring an easy to navigate system, so the user doesnt have to constantly change what they are used to using. When using a smaller screen on the on the view hotel tab all the content has been given a scroll bar on the side to ensure the user is getting all the information.

##Libraries and Programs used
- Gitpod coding space [gitpod](https://www.gitpod.io/ "gitpod")
- Github -  Github was used as a cloud service to save and store code. GitHub Projects was used to track the User Stories, User Epics, bugs and other issues during the project. [github](https://github.com/ "github")
- Heroku was used as a place to deploy the site  [heroku](https://www.heroku.com/?utm_source=google&utm_medium=paid_search&utm_campaign=emea_heraw&utm_content=general-branded-search-rsa&utm_term=heroku&utm_source_platform=GoogleAds&gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswygiKklF3O08QSDjhdsSWRZMQtTtlD0r22r9A7AZ-AfJY2A39CdD5noaAnyREALw_wcB "heroku")
- 


## Deploying the app on Heroku
1. Log into Heroku and navigate to the Dashboard.
2. Click on the 'New' button.
3. Choose a unique app name, and select the region closest to you.
4. Create a database on Heroku (I elected to stay on Heroku and pay the monthly fee)
    - Click on the Resources tab.
    - Click the Find more add-ons button.
    - Select Heroku Postgres, and click on Install Heroku Postgres.
    - Select a plan (default = Eco @ $1.00 a month, which I'm using), and select your app.
    - Return to Resources tab and click on the Heroku Postgres icon, then select the settings tab and click on Database Credentials. Copy the URI to your clipboard. Paste it to your env.py file using the key "DATABASE_URL". This will allow you to use the same database for development and production.
5. Click the settings tab on the Dashboard, and click the button to Reveal Config Vars. Your database url should be populated here already. Add your Django secret key to the config variables, and set the PORT to 8000.
6. In your local repository, add a Procfile to the root directory of the project, containing the following line :<br /> `web: gunicorn strings-attached.wsgi`.
7. Add the url of your Heroku project to the `ALLOWED_HOSTS` list in `settings.py`.
8. Create 2 social apps, for Facebook and Google social signin, and add their respective API-keys and SECRETS to the database. Add your application details and callback urls to the respective Google and Facebook OAuth dashboards.
9. Open a Stripe account, and add your STRIPE_PRIVATE_KEY and STRIPE_SECRET to the config vars. Set up a webhook to hit your webhook endpoint, and copy the STRIPE_WEBHOOK_SECRET to config vars as well.
10. Create 3 products in the Products tab of the Stripe Developer console, to match the 3 subscription durations in the project, and add their respective API-keys to their corresponding Subscription instances in the database.
11. Set DEBUG to False, and commit your changes and push to GitHub.
12. In Heroku, navigate to the Settings Tab, and within this the Buildpacks section, and click on Add Buildpack. Select the python buildpack, and save changes.
13. On the Dashboard, select the Deploy tab, and under the Deployment Method heading, select the
GitHub icon to connect your Heroku project to your GitHub repo. Enter your repository name in the text input, and click Search, and then when your repo appears, click Connect.
14. Under the Manual deploy section, click Deploy Branch. You should receive this message - 'Your app was successfully deployed". Click view to see the app running in the browser.

 # Credits
 - Through out this process I was assissted by my mentor Paul and John the coding coach, both have assisted me when it comes to the struggles I have had when coding, there support has been key in finishing my project.
 - I would also like to thank an external person Lewis Mieakin who advised me through my whole journey.