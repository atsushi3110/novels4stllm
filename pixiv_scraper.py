import requests
import time
from subprocess import check_output
import click
import json
import time
import bs4
import os
import traceback
NUM_MAX_PAGE=1000

def extract_content(html:str):
    ret=dict({"content":"", "description":"", "title":"", "err":"", "is_success":False})
    try:
        metas = bs4.BeautifulSoup(html, features="html.parser").findAll("meta")
    except:
        ret["err"] = traceback.format_exc()
        return ret

    found = False
    for m in metas:
        if "content" in m.attrs.keys():
            try:
                d = json.loads(m.attrs["content"])
            except:
                msg = traceback.format_exc()
            else:
                if not isinstance(d, dict):
                    continue
                if "novel" in d.keys():
                    found = True
                    break

    if not found:
        ret["err"] = "novel-key is not found."
        return ret

    try:
        dd = list(d["novel"].values())[0]
    except:
        ret["err"] = traceback.format_exc()
        return ret

    if not isinstance(dd, dict):
        ret["err"] = "not isinstance(dd, dict)"
        return ret

    for k in ["content", "title", "description"]:
        if k in dd.keys():
            ret.update({k:dd[k]})

    dd["is_success"] = True
    return dd

@click.command()
@click.option("--head_url", required=True, help="https://www.pixiv.net/novel/show.php?id={int} ")
@click.option("--out_dir", default=None, help="jsonl dir path. Print if arg is None(default)")
@click.option("--out_prefix", default="", help="{out_prefix}_{int in pixiv novel page's url}.jsonl ")
@click.option("--sleep_duration", default=1.0, help="sleeping second >= 1.0")
def main(head_url:str, out_dir:str, out_prefix:str, sleep_duration:float):
    if not head_url.startswith("https://www.pixiv.net/novel/show.php?id="):
        return

    if sleep_duration < 1.0:
        raise ValueError("sleeping second must be >= 1.0")

    if out_dir is not None:
        os.makedirs(os.path.abspath(out_dir), exist_ok=True)
        fname = out_prefix+"_"+head_url.replace("https://www.pixiv.net/novel/show.php?id=","")+".jsonl"
        fname = fname.lstrip("_")
        # out_dir = f"./"
        out_path = os.path.join(out_dir, fname)
        print(out_path)
        with open(out_path,"w"):
            pass

    prev_text = ""
    for page in range(1,1+NUM_MAX_PAGE):
        url = head_url + f"#{page}"
        try:
            resp = requests.get(url)
        except:
            with open("./err.log", "a") as fout:
                fout.write(traceback.format_exc())
            break
        else:
            status = resp.status_code

        if int(status) != 200:
            break

        text_dict = extract_content(resp.text)
        if prev_text == text_dict["content"]:
            break
        else:
            prev_text = text_dict["content"]

        line = json.dumps({"text":text_dict["content"], "description":text_dict["description"], "title":text_dict["title"], "url":url, "is_success":text_dict["is_success"]}, ensure_ascii=False)
        if out_dir is None:
            print(line, flush=True)
        else:
            with open(out_path,"a") as fout:
                fout.write(line+"\n")

        time.sleep(sleep_duration)

if __name__=="__main__":
    main()
