import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Optional
import re 
#okunabilirlik için yapay zekadan yardım alınmıştır 


@dataclass
class SearchResult:
    slug: Optional[str]
    title: Optional[str]
    snippet: Optional[str]



class GrokipediaAPI:
    def __init__(self, query, limit, offsets):
        self.query = query #soru
        self.limit = limit #limiti normal şartlarda typehead için 5 full_text_search için 12
        self.offsets = offsets#ne olduğunu pek anlamadım ama herhalde iyi birşeydir :) full_text_search için 0

    def typeahead(self):
        url = "https://grokipedia.com/api/typeahead"
        params = {
            "query": self.query,
            "limit": self.limit
        }
        return requests.get(url, params=params).json()

    def full_text_search(self):
        url = "https://grokipedia.com/api/full-text-search"
        params = {
            "query": self.query,
            "limit": self.limit,
            "offset": self.offsets
        }
        return requests.get(url, params=params).json()

    def sayfayı_al(self):
        url = f"https://grokipedia.com/page/{self.query}"
        r=requests.get(url)
        return r.text,r.status_code
    

class Search_Result_Parser:
    
    @staticmethod
    def _remove_em(text):
        if not text:
            return text
        return re.sub(r"</?em>", "", text)
    def parse(data):
        results = []
        for item in data.get("results", []):
            results.append(
                SearchResult(
                    slug=item.get("slug"),
                    title=Search_Result_Parser._remove_em(item.get("title")),
                    snippet=Search_Result_Parser._remove_em(item.get("snippet")),
                )
            )

        return results

class GrokipediaPageParser:
    @staticmethod
    def parse(html):
        soup = BeautifulSoup(html, "html.parser")

        for sup in soup.find_all("sup"):
            sup.decompose()

        paragraphs = []
        references = []

        ref_h2 = soup.find("h2", id="references")
        if not ref_h2:
            return {"paragraphs": [], "references": []}

        for span in ref_h2.find_all_previous("span", class_="mb-4"):
            text = span.get_text(" ", strip=True)
            if text:
                paragraphs.append(text)

        paragraphs.reverse()

        for a in ref_h2.find_all_next("a", href=True):
            references.append(a["href"])

        return {
            "paragraphs": paragraphs,
            "references": references,
        }

