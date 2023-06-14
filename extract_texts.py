import bs4, glob, json

for path in glob.glob("./outfiles/*"):
    soup = bs4.BeautifulSoup(open(path, "r").read())
    divs = soup.findAll("div")
    _, bid,_,page = path.split("_")
    print(json.dumps({"text":str(divs[13].text), "book_id":bid, "page":page}, ensure_ascii=False), flush=True)
