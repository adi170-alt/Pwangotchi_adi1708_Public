# Pwnagotchi Plugins!

This is a public version of my other private pwnagotchi repository

---------------
# Installation

1. SSH into your Pwnagotchi and create a new folder for third-party Pwnagotchi plugins. I use `/root/custom_plugins/` but it doesn't really matter: `mkdir /root/custom_plugins/`
1. Grab the  files that are in this custum_plugins folder from this Github repo and put it into that custom plugins directory.
1. Edit `/etc/pwnagotchi/config.toml` and change the `main.custom_plugins` variable to point to the custom plugins directory you just created: `main.custom_plugins = "/root/custom_plugins/"`
1. In the same `/etc/pwnagotchi/config.toml` file, add the following lines to enable the plugin:
```
main.plugins.display-password.enabled = true
main.plugins.display-password.orientation = "horizontal"

main.plugins.clock.enabled = true
```
After that U want to edit the gps config and the memtemp config
You can find the plugins in here:
```
/usr/local/lib/python3.7/dist-packages/pwnagotchi/plugins/default/
```
You can just simply replace those files, but just make sure that u have pwanotchi version v1.5.5

---------------
Once the above steps are completed, reboot the Pwnagotchi to ensure all changes are applied.
----------------
# Birthday Plugin

just follow the seteps from th instalation but change the date:

Just simply go to birthday.py that you downloaded and chacge these numbers:
```
month = (7)
day = (3)
```
Changing that is very easy so I hope you did it good, And after that you can save your file

(put the plugin into your plugins folder)

At last just Simply put this in your config file:
```
main.plugins.birthday.enabled = true
```
And Done!, Now you can reboot your pwnagotchi and see how much days are left till your brith day!

----------------
# Preview:

![ui (2)](https://user-images.githubusercontent.com/79835819/116112465-dfdd9980-a6b7-11eb-8473-7721cea3ee9a.png)
![WhatsApp Image 2021-04-26 at 20 44 59](https://user-images.githubusercontent.com/79835819/116134662-7322c900-a6d0-11eb-9b27-3e66207a03b0.jpeg)
----------------
# Unedited Custum Plugins:

Wpa sec Pasword viewer plugin: https://github.com/c-nagy/pwnagotchi-display-password-plugin

Clock plugin: https://github.com/LoganMD/pwnagotchi-clock

Christmas plugin: https://github.com/LoganMD/pwnagotchi-christmas-countdown

----------------
This is a public version of my other private pwnagotchi repository
Files that I imported:
* plugins
----------------
# credits:
Credit to [@cnagy](https://github.com/c-nagy) becouse I copyed his instalation from readme. Sorry

Credit to [@highrup](https://www.reddit.com/user/highrup/) becouse it was his idea for the "gps, memtemp and clock configuration

Credit to The "Christmas Plugin" becouse I just changed some things from there and just made a birth day plugin of it

And also credit for the peaple who made those plugins links are in the Unedited Custum Plugins tab
