#bump

A simple tool to automate clicking the "_bump" button to a Splunk instance.
bump clears the Splunk Web cache and forces all the static files (.js, .css etc) to be loaded again.


Version 0.1

#Install
bump only requires the Requests and beautifulsoup4 libraries. You can install them manually or with

    pip install -r requirements.txt

#Usage

As with any python script you can execute it in several ways

###Run the script directly:
You can modify the default values for the url, username and password by editing bump.py and run the script. You don't have to use command line arguments. If you do, the command line arguments will override the default.

    //Will use the default values
    python bump.py

###Run the script with command line arguments
You can pass arguments for the url, the username and or the password. If you don't specify a specific argument the default value will be used.

    //Use given arguments
    python bump.py -l https://localhost:8000/ -u admin -p changeme

    //Use given arguments
    python bump.py --url https://localhost:8000/ --username admin --password changeme

    //We don't specify username, will use the default value
    python bump.py -l https://localhost:8000 -p secret

###Run the script in Unix

    chmod +x bump.py
    ./bump.py

###Add it to your PATH

    cd ~/bin/
    ln -s ~/your/path/bump.py

#Alternative
There is a way to configure Splunk to not use the cache at all. This will increase the loading time of any page significantly. In order to enable this option, edit your web.conf file

    vim /Applications/Splunk/etc/system/default/web.conf

and change the following values

    js_no_cache = True
    cacheBytesLimit = 0
    cacheEntriesLimit = 0

#License
bump has a GNU General Public License v3.0 license.
Please use it, improve it and contribute back to this simple tool.
