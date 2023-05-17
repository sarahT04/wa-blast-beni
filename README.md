# WA Blast program using Pymongo, Tkinter, and Pywhatkit.
Click Documentation URL (here)[https://drive.google.com/drive/folders/1g_TNEpyBlNGRvkmXnso07JIAdIKlDcL1?usp=sharing].

Currently, this program supports sending messages and picture to all phone numbers inside mongodb and even ranged (according to the _id) and also adding new phone number to mongodb collection. This project was made to be used by Indonesians. 

The program works first by getting the collection names to be used as a dropdown in tkinter. You can choose from which collection name you want to extract the data from  
After that, you can choose to send with range (IE. 1 - 10) or to all contacts (all 10)  
You can also choose to send a picture alongside with the message or not.  

When you click the button to send in range, it will get the datas by query a db\[colletion_name].skip(start).limit(stop),  
and when you click the button to send to all, it will get all datas in db\[colletion_name] 
then it will loop through all datas (of your choice) and call pywhatkit to the phone number, alongside the message you put.  

Once it ends, there will be an info box, or warning box if fails

Important points:
* You have to insert a message
* DB's name have to be "wa-blast". 
* Collection format is: _id, name, full_name, phone
* All images have to be put in /img/
* If you want to insert setup datas, put "datas.csv" in /db/ and use `py /db/commands.py`
* If you put "{nama}" and "{nama_panjang}" in the message, it will parse the name and full name of that person's.