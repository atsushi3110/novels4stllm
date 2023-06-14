# DISCLAIMER
* **DO NOT USE THIS CODES TO VIOLATE THE TERM OF SERVICES OF ANY ONLINE SERVICE.**
* **THE AUTHOR HAS NO LEGAL RESPONSIBILITY TO THE USER'S ACT TO VIOLATE LAWS OF ANY STATES/NATIONS.**

# novels4stllm
* To collect plain texts of novels
* Crawl URLs and scraping them and extract plain texts.

# Quick Start
## Build docker-image
```shell 
docker build -t ubuntu-go .
```

## Extract URLs
* To get URLs line by line.
```shell
docker run --rm ubuntu-go bash -c "urlExtract {} -r 5" > urls.txt
```

## Scrape HTMLs
* 
```
TODO
```

