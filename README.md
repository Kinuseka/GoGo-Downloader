# GoGo-Downloader
A CLI reliant program that downloads, and searches anime from gogoanime.so 

For an in-depth explanation click here: [Documentation](https://github.com/Kinuseka/GoGo-Downloader/wiki/Documentation)

**Requirments:**
```
1. Python v3.x.x 
2. pip
3. Aria2
4. rsync (installation purposes v1.3 up)
```

**Python modules used:**
```
-bs4(BeautifulSoup)

-requests
```
~~-html5lib(for bs4 html parser)~~
**No longer requred as of V1.15**

## Supported Platforms:
**•Termux[android]: 100% tested**

**•Windows: Need volunteers for testing**

**•Linux/unix: Need volunteers for testing**

## Basic Features:
```
•You can Ctrl+C to pause a download during the process

•Bulk episode Download!

•Genre searching (V1.1 up)

•Quality selection (V1.2 up)

•And many more for you to discover!
```
## Upcoming features:

Done, all features were implemented on the latest version. 

## Quick Installation:
<font size="5"><b>Termux:</b></font>

Copy and paste these:

**Step 1:** ```termux-setup-storage``` 

**[optional] Step 2:** ```apt-get update && apt-get upgrade```

**Step 3:** 
```
wget -O - 'https://raw.githubusercontent.com/Kinuseka/GoGo-Downloader/main/Setup.sh' | bash 
```

If installation is successful you can simply type ```goanime``` to start

**Experimental:** For updates do ```goupdate!``` on command line to automatically update to the latest release

Anime will be downloaded on 
```
/storage/GoGo-Downloader
```

## Manual Installation:

**Download my program on latest release**
```
extract the program from the zip file
and place it anywhere on your storage that
is easily accessible
```

**Install Requirements:**
```
apt-get install python
apt-get install aria2
```

**Install Dependencies:**
```
pip install bs4
pip install requests
pkg install aria2
```

<font size="5"><b>Before you start the python program:</b></font>

-Make sure you have external storage permissions enable
**This can be done by doing:**

```
termux-setup-storage
```

-Make sure you are on the same directory as the program's 

**this can be done by:**

```
cd /sdcard/GoGo-Downloader
```

or 

```
cd /sdcard/directory/to/file
```

<font size="5"><b>To start:</b></font>

```$ python RuNime.py```

**It should show up like this**

![](home.png)

**A brief example of what you see should during usage**
![](example.png)


