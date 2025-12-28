import args
import api 





def yazdır(results):
    for i, r in enumerate(results, start=1):
        print(f"açıklama: {r.snippet}")
        print(f"yazman gereken: {r.slug}")
        print("-" * 50)

def yazdır_paragraph(results):
    paragraphs = results["paragraphs"]

    for p in paragraphs:
        print("")
        print(p)


if __name__=="__main__":
    print("grokipedia için client toolsu")
    argümanlar=args.args_get()
    print(argümanlar)
    if argümanlar.search:
        print("references modu çalışıyor")
        api1=api.GrokipediaAPI(query=argümanlar.query,limit=argümanlar.limit,offsets=argümanlar.offset)
        sayfa,status_code=api1.sayfayı_al()
        if status_code==404:
            sayfa1=api1.full_text_search()
            result=api.Search_Result_Parser.parse(sayfa1)
            yazdır(results=result)
        else:
            results=api.GrokipediaPageParser.parse(sayfa)
            yazdır_paragraph(results=results)
            
        
    elif argümanlar.typeahead:
        print("typeahead modu çalışıyor")
        api1=api.GrokipediaAPI(query=argümanlar.query,limit=argümanlar.limit,offsets=argümanlar.offset)
        sayfa1=api1.typeahead()
        result=api.Search_Result_Parser.parse(sayfa1)
        yazdır(results=result)
    elif argümanlar.full_text_search:
        #Namespace(query='mustafa', typeahead=False, full_text_search=True, limit=5, offset=0, search=False)
        api1=api.GrokipediaAPI(query=argümanlar.query,limit=argümanlar.limit,offsets=argümanlar.offset)
        sayfa1=api1.full_text_search()
        result=api.Search_Result_Parser.parse(sayfa1)
        yazdır(results=result)










