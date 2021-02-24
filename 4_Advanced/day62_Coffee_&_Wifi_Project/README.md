# Coffee & Wifi Project

- Home page use the css/styles.css

- The /cafes route render the cafes.html file, this file contains a Bootstrap table which displays all the data 
  from the cafe-data.csv

- The location URL is rendered as an anchor tag <a> in the table instead of the full link. 
  It has the link text "Maps Link" and the href is the actual link

- Clicking on the "Show Me!" button on the home page take you to the cafes.html page.

- There is a secret route "/add" which doesn't have a button, but those in the know are able to access it 
  and it takes you to the add.html file.
  
- When the user successfully submits the form on add.html, the data gets added to the cafe-data.csv. 
  It appended to the end of the csv file. 
  The data from each field are comma-separated like all the other lines of data in cafe-data.csv

![alt text](?raw=true)

![alt text](?raw=true)

![alt text](?raw=true)
