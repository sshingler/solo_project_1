

'TrekTracker' App 

Summary:

The TrekTracker app allows users to add/manage destinations, as well as add/manage treks within each destination.
The user is able to view completed treks and treks within a certain destination.
The user is also presented with stats on how many treks have been completed, how many days trekking this equals, and how many Km's have been trekked in total.  
The app has been created using the following applications: Python, Flask, PostgreSQL, along with HTML & CSS. 

Running the app: 

Copy all files from the repository. 
Ensure PostgreSQL is installed via Pip installer. 
Ensure a database with the correct name has been set up: 'CREATEDB trek_manager' (terminal)
Ensure database structure has been initialised: 'psql -d trek_manager  -f db/trek_manager.sql' (terminal)
Initialise Flask using the following command: 'Flask run' (terminal)
Using your chosen browser, navigate to the correct localhost: http://127.0.0.1:5002/ - this can be ammended within the .FLASKENV file. 


