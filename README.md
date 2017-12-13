# MetaCrawlTag
Crawl a website and inspect meta tags for a specific value.

Usage:
```bash
scrapy runspider mct.py -a url=<url> -a meta_name=<meta name> -a meta_value="meta value"
```
In this example a site will be crawled for the keywords meta tag containing the value "jeremy corbyn".
```bash
scrapy runspider mct.py -a url=https://labour.org.uk -a meta_name=keywords -a meta_value='jeremy corbyn'
```

This example searches for all pages with the "noindex" robots value.

```bash
scrapy runspider mct.py -a url=https://labour.org.uk/about/democracy-review-2017/ -a meta_name=robots -a meta_value=noindex > log.txt 2>&1
```

The program will output 3 files...

* tag_and_value_found_urls_output.txt <- tag and value found
* tag_found_not_value_urls_output.txt <- tag found but no value
* tag_not_found_urls_output.txt <- tag does not exist on this page

Requirements:

* scrapy - https://scrapy.org/
