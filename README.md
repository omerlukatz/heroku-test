Put your script in 'main.py'
The 'Procfile' will run a command (As of now it is 'python3 main.py')
Anything you import (eg. turtle or json) you should put in the 'requirements.txt' file
Formatting is just a plaintext name
Put all of this in a GitHub file to be stored and updated
In Heroku, connect your app to GitHub (Deploy -> Deployment Method -> GitHub)
While there, Enable Automatic Deploys
Now your app will update from GitHub automaticly
Make sure you Dyno is set to what is in your Procfile (Overview -> Configure Dynos)
Heroku will run main.py as if it was running on your computer
You will need to find a way to get user input (Flask works well for online connectivity)
You can look at ways to have a website connect, (a .tk domain is free) or other ways to connect

