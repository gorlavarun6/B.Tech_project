So this my Btech project
Its called Ads Advertiser using real world objects

basically:
camera takes a picture
COCO names with detect the objects in that picture
we will get the count of each objects
the object which has highest count will be our target object to play Ads
so we play a video using VLC library , i worte a function for that.
BTW from line 54 u see some list containing strings
each list represents a category for Ads
every list contains strings , these strings are video files names, (well you dont find those videos files in this rep)
in PlayVideo(), it takes a string which it takes randomly from the list.
if you wanna put your videos in this Advertiser
	create a list, name the list to its corresponding category
	add videos to the project folder
	add the video name to the list as string and your done
last lines are hardcoded lines
understand the COCOdataset video from the link below

for COCO dataset
I put separate folder for that , extract the RAR file and your good to go


watch this to understand the implementation of COCO dataset in your project
https://youtu.be/HXDD7-EnGBY

Have a great day