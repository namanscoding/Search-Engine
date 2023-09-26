 ---------------------
## Command(cmd)  to run this project without hardcoding 
 ----------
### ```scrapy crawl para -a start_urls="url1,url2" -O filename.filetype```

supported filetypes : ('json', 'jsonlines', 'jsonl', 'jl', 'csv', 'xml', 'marshal', 'pickle')

 -------------------------


##### need to find Drugbank accesion number to generte url of drug searched
##### [api Drug bank asks login](https://dev.drugbank.com/clients/sign_in)


 ------------------

Also [this](https://go.drugbank.com/unearth/q?query=Acetaminophen&button=&searcher=drugs) query works for exact drug name without spelling mistakes
```
 https://go.drugbank.com/unearth/q?query=Acetaminophen&button=&searcher=drugs
```
### Options to deploy 
- Flask + running cmd-line commands on server system 
- [Scrapyd (open src)](https://scrapyd.readthedocs.io/en/stable/overview.html)
- [Zyte Scrapy Cloud (cloud based)](https://docs.zyte.com/scrapy-cloud.html)



## :man_technologist: Author
| [<img src="https://github.com/rohanworks8660.png" width="100px;"/>](https://github.com/rohanworks8660)<br/> [<sub>rohanworks8660</sub>](https://github.com/rohanworks8660) |
| --- |



