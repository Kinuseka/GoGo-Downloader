GoGoDownloader

TXT version of the documentation

This file is an in-depth explaination to my program and is true to versions:
V1.2, V1.3, and above
*Updated: March-20-2021 V1.36

Table of Contents
- 1.) Features
  * 1.1 Search
  * 1.2 Gogoanime homepage Search
  * 1.3 Genre Search
  * 1.4 Select anime
  * 1.5 >n Command
  * 1.6 Page selection
  * 1.7 Bulk Downloader
  * 1.8 Why Aria2
- 2.) options.ini
  * 2.1 Global
  * 2.2 Video
  * 2.3 Network


Sections
1. Features
2. options.ini 

1.) Features:
Contents
----Main Menu---
1.1 - Search (#17)
1.2 - Gogoanime homepage Search
1.3 - Genre Search

-Anime Selection-
1.4 - Select anime 
1.5 - ">n" Command
1.6 - Page selection

----Downloader----
1.7 - Bulk Downloader 
1.8 - Why Aria2


1.1 Search:
Upon starting the program on a command line environment you see an input area
"Enter title/command:"
simply enter the partial or full title of an anime you wish to download


1.2 Gogoanime homepage Search:
In the input area instead of the title of an anime you type and enter
">h" 
and the anime (usually latest releases) will show up on the list


1.3 Genre Search:
Same as 1.2 but instead you type and enter
">g"
The program will then show you a list of genres that you will have to choose

------------------------------------

1.4 Select anime:
After searching from either title, homepage or genre you are greeted with a list of anime

To select an anime you simply type the number the title is associated with.


1.5 ">" Command:
Every page there is atleast ≤20 anime titles or shown

The program shows 5 list in initial but typing and entering the command:
">" 
will show 5 more in the list


1.6 Page selection:
In gogoanime every page there is atleast 20 anime titles per page, 

If you want to keep exploring more anime titles type and enter:
">>" 
or 
"<<" to show the previous page
and should show the titles of that list

in the upper section of the list there is 
"Page: 1/5" 
or to put it simply
"Page: PageOn/PageLimit"

Due to the nature of gogoanime the Page Limit may increase as you grow closer to it.

------------------------------------

1.7 Bulk Downloader:
After selecting an anime from a genre/title searching the bulk downloader will show the amount of episodes you can download 
example:

---------------------------
Found 13 episodes in total!
---------------------------

Inputs
"Start from episode:" Which episode to start downloading from

"Stop to episode:" Which episode to stop downloading from

tips:
you can equalize the start and stop to only download one episode example:

Start from episode: 12
Stop to episode: 12

will only download episode 12


1.8 Why Aria2:
Because Aria2 is significantly user friendly than the other downloaders.

Reason 1: Detailed Download information
Reason 2: Automatic Continued Download
Reason 3: Easy to program

==================================

2.) options.ini
Contents
2.1 - Global
2.2 - Video
2.3 - Network


2.1 Global
You may notice 
"mode = download"
in that section, however there is no particular use in that section YET.

Do not remove that section as it may cause errors in the code.


2.2 Video
OPTIONS:
enable = on/off
disabling will disable the quality search feature and return to pre v1.1 way of downloading

OPTIONS:
quality = best, 1080p, 720p, 480p, 360p
Will choose the quality if available


OPTIONS:
selection = auto/manual
If a quality you selected does not match the quality available on the gogoanime server it will either

auto- Automatically select the next Quality possible

manual- Manually select the quality available

Be wary that auto is still experimental and may cause errors on newer released anime's


2.3 Network
OPTIONS:
domain = so/vc

This feature is added to add some compability to geoblocked countries. You can use VPN to bypass these but this is another option for VPN-less solution. Though it may not work 100% of the time in some locations

gogoanime.vc may support countries like India, but if both so or vc is still blocked open an issue

It would be appreciated to also tell me any gogoanime domains that works on your country as long as it is a clean clone




GoGoDownloader is under GPL-3.0 License

---end