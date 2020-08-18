# Hack to detect hurricane

The purpose of this repo is to demonstrate how to detect a hurricane using an rss feed. Mostly, this was written late at night for the lolz.

### Libraries used
- pip
- chalice
- requests

### To run 
```
$ cd detect_hurricane
$ chalice local
```

Go to localhost:8000, and observe the properties of the hurriane in the response. You can also debug this by trying out a sample rss feed that doesn't have a hurricane in it, such as https://www.nhc.noaa.gov/rss_examples/nhc_at2.xml
