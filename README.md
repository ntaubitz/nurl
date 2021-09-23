# NUrl/nurl or Nate URL

My personal development machine died quite literally last week.

I did this exercise on my 2013 iMac that hosts mail and a web site.
The development environment wasn't set up, so, I didn't get pyenv/virtualenv
setup correctly and just used the user installation of python 3.7

I ended up with working code, i.e. you can run it and use a browser to do GETs. 
I din't do anything with POSTs for say, creating a nurl from a URL.
After working in kotlin and Spring for a year, I did find I was very rusty
with python. However after just over 3 hours of work the fog was lifting quite a bit
so I am confident all that knowledge I had a couple years ago would come back quickly.

# Run Tests

* python3 -m tests

# Run locally

* pip3 install --user -r requirements.txt
* source config/development.sh
* flask run

## Swagger docs

GET http://127.0.0.1:5000/shorten?url=MYFUNURL
given a long url, will return a short URL(nurl) as text

GET http://127.0.0.1:5000/redirect?nurl=shorty
given a short URL, will return the original URL as text 

