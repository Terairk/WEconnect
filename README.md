# WEconnect
This is a project for the Brunei AI for Good Hackathon

The main code is in app.py
For those who are wondering, main.py and generatevalues.py are places where i tested the code separetly from the flask project then later added them into the flask thing. The client_secret.json file contains info to access the google spreadsheets via code.

The actual website link to the project being deployed onto a server is http://43.245.220.12:5000/
That's where you can test the website for yourself and see what it does.

The UI is a bit bad but I think you'll get the main point. The final part is where it ranks the companies from best to worst (fake companies mind you)

Here's the link to the figma (the frontend mock up that looks much better than this)
https://www.figma.com/proto/5MqnNJjrJ7MtPUCK0xZglq/Team-6-Prototype---Students?node-id=15%3A2&scaling=min-zoom

Also if you want to run this code for yourselves, you need to import nltk and do nltk.download() in your python installation. And of course download all the files in the requirements.txt file.
