import args
import api 





def write(results):
    for i, r in enumerate(results, start=1):
        print(f"explanation: {r.snippet}")
        print(f"what you need to write: {r.slug}")
        print("-" * 50)

def write_paragraph(results):
    paragraphs = results["paragraphs"]

    for p in paragraphs:
        print("")
        print(p)


if __name__=="__main__":
    print("Argument tools for Grokipedia")
    args=args.args_get()
    #print(args)
    if args.search:
        print("The references module is working")
        api1=api.GrokipediaAPI(query=args.query,limit=args.limit,offsets=args.offset)
        page,status_code=api1.sayfayı_al()
        if status_code==404:
            page1=api1.full_text_search()
            result=api.Search_Result_Parser.parse(page1)
            write(results=result)
        else:
            results=api.GrokipediaPageParser.parse(page)
            write_paragraph(results=results)
            
        
    elif args.typeahead:
        print("The typeahead mode is working.")
        api1=api.GrokipediaAPI(query=args.query,limit=args.limit,offsets=args.offset)
        sayfa1=api1.typeahead()
        result=api.Search_Result_Parser.parse(sayfa1)
        write(results=result)
    elif args.full_text_search:
        api1=api.GrokipediaAPI(query=args.query,limit=args.limit,offsets=args.offset)
        page1=api1.full_text_search()
        result=api.Search_Result_Parser.parse(page1)
        write(results=result)










