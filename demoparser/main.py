from scrapy import cmdline
cmdline.execute("scrapy runspider spiders\quotesspider.py -o quotes.json".split())