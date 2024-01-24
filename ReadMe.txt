Automatic group post deletion

Facebook removed option to automatically select and delete post in groups
So I created my own automatic deletion tool using Python and Selenium library

It emulates simple clicks with random intervals to make Facebook think that someone deletes posts manually, 
so account would not get banned.

To start you need at first to write in Command line: 
#
/path/to/chrome --remote-debugging-port=8989
#
It will open browser
Then you need to go to Activity log and find your group post.

Start the programm and it will click on three dots then first delete and second delete
The program will be running till you close it

