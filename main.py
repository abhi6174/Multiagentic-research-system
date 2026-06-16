from src.tools.tools import web_search,scrape_url

query = "top tourist spots in kerala"
# output = web_search(query)
# print(output)
url =  "https://www.reddit.com/r/singularity/comments/1s5a0h1/deepminds_new_ai_just_changed_science_forever/"
res = scrape_url(url)

print(res)