from typing import List

import bs4
from bs4 import BeautifulSoup
from pydantic import BaseModel
import logging

logger = logging.getLogger("yxr_porn_core.fc2ppvdb.parse_item")


def btfa(el: bs4.Tag, *args, **kwargs) -> List[bs4.Tag]:
    """bs4_typed_find_all"""
    return el.find_all(*args, **kwargs)


class ParseItemResult(BaseModel):
    title: str
    product_id: str
    cover_url: str
    writer: str
    actresses: List[str]
    mosaic: str  # モザイク: str
    release_date: str  # yyyy-mm-dd
    length: int  # mm:ss => min
    tags: List[str]  # タグ: str


# https://fc2ppvdb.com/articles/4502668
def parse_item(html: str) -> ParseItemResult:
    soup = BeautifulSoup(html, "lxml")
    box = btfa(soup, class_="items-start")[0]
    cover_url = btfa(btfa(box, class_="lg:w-2/5", recursive=False)[0], "img")[0].attrs["src"]
    right_box = btfa(box, class_="lg:w-3/5", recursive=False)[0]
    title = btfa(right_box, "h2")[0].get_text().strip()
    divs: List[bs4.Tag] = right_box.findChildren("div", recursive=False)

    product_id = ""
    release_date = ""
    writer = ""
    actresses = []
    mosaic = ""
    tags = []

    for div in divs:
        prefix = ("".join(div.find_all(string=True, recursive=False))).strip()
        print(f"prefix:[{prefix}]")
        if prefix == "ID：":
            product_id = "FC2-" + btfa(div, "span")[0].get_text().strip()
        elif prefix == "販売者：":
            writer = btfa(div, "span")[0].get_text().strip()
        elif prefix == "女優：":
            actresses = []
        elif prefix == "モザイク：":
            mosaic = btfa(div, "span")[0].get_text().strip()
        elif prefix == "販売日：":
            release_date = btfa(div, "span")[0].get_text().strip()
        elif prefix == "収録時間：":
            length_text = btfa(div, "span")[0].get_text().strip()
            t = length_text.split(":")
            length = 0
            for v in t:
                length *= 60
                length += int(v)
        elif prefix == "タグ：":
            tags_a = btfa(div, "a")
            tags = [o.get_text().strip() for o in tags_a]
        elif prefix == "":
            continue
        else:
            logger.warning(f"Unhandle prefix [{prefix}]")

    return ParseItemResult(
        title=title,
        product_id=product_id,
        cover_url=cover_url,
        release_date=release_date,
        length=length,
        writer=writer,
        actresses=actresses,
        mosaic=mosaic,
        tags=tags,
    )
