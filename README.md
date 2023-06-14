# DISCLAIMER
* **DO NOT USE THIS CODES TO VIOLATE THE TERM OF SERVICES OF ANY ONLINE SERVICE INCLIDING www.pixiv.net**
* **THE AUTHOR HAS NO LEGAL RESPONSIBILITY TO THE USER'S ACT TO VIOLATE LAWS OF ANY STATES/NATIONS.**

# novels-scraper
* To collect plain texts of novels in https://www.pixiv.net/novel/ 
* Crawl URLs and scraping them and extract plain texts.

# Quick Start
## Build docker-image
```shell 
docker build -t novel-scraper .
```

## Extract URLs
* To get URLs line by line.
```shell
docker run --rm novel-scraper bash -c "urlExtract https://www.pixiv.net/novel/ -r 5" > urls.txt
```

## Scrape HTMLs
* To scrape html files and dump to the folder `outdir`
```
docker run --mount=type=bind,src=$(pwd),target=/root --rm ubuntu-go bash -c "cat urls.txt|grep https://www.pixiv.net/novel/show.php?id=  | xargs -I {} python3 pixiv_scraper.py --head_url {} --out_dir ./outdir"
```

