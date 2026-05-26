This repo contains a template (the test_comics folder) for you to see how you can put your own comics in gComics for gmod. It also contains additional help on how to put your own comics.

<hr>
<h1>Informations</h1>
PNGs and JPGs can be used.
The first page must always be 0.png (or 0.jpg) and pages must be in numerical order (0, 1, 2 etc). The last page is the comic's cover.

<h1>OPTIMIZATIONS TRICKS!!</h1>

IT IS RECOMMENDED TO USE COMPRESSED JPGs TO AVOID HUGE FILE SIZE AND SMOOTHER CACHING, but you can do however you like.
Don't use huge resolutions, be reasonable.
<hr>

<h1>Automatisation</h1>
It also contains a python script, gcomic_lua_generator.py, that makes it easier to do the lua for it, simply take your path of your comic in the materials/comics folder (be sure the structure is corrects, see below)


<img width="682" height="380" alt="image" src="https://github.com/user-attachments/assets/45ec5649-e137-4af7-90ae-0b8747dff580" />


So for example, let's take "..\my_cool_comic_addon\materials\comics\Super Comic", then the script will ask you for the author name, then it will automatically generate the script and use the folder's title as the comic's title, and the issues name will be automatically fetched with the subdolders name (eg: folder named "Issue 1", then it's name is "Issue 1", etc..)
Then put the output script in "lua/autorun/<your_unique_script_name>.lua" (put the name you want, be unique) and it should be good.

Also, if you'd like to automatically convert for example a pdf with all the pages of the comic you like, you can use python to do so quickly and extract all pages as images and name them automatically. Currently, I did not ship any scripts to do so but it's quite easy to do. Even compress them afterwards.

<br>
<hr>
This is not really a wiki and is not exactly well explained, sorry for that.
