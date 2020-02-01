# ProductMonitor
Monitors websites to let you know when items come back in stock. The script imports a JSON file to find all the sites it should monitor. The site gets downloaded, and the HTML is searched to find if the In Stock string is located. If it's located, all Numbers will be texted the link to the product. The Enabled flag will be flipped to false to prevent repeated messages. 
