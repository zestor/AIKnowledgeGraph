#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from os.path import exists
from python.ZestorHelper import ZestorHelper

SELECTED_AI_ENGINE = ZestorHelper.AI_ENGINE_OPENAI

title = 'AI Fuzzy logic systems that are difficult to design'

# Clear out file
ZestorHelper.save_file('knowledge.txt') # default write mode, no content

google_links = ZestorHelper.scrape_google(title) # google first page links

# for each link, get web page, and summarize
for google_link in google_links:

    print('\n\n==Get Url==> %s' % (google_link))
    url_db_file = ZestorHelper.urldb_getfilename(google_link)

    clean_response = ''

    if ZestorHelper.urldb_exists(url_db_file):
        clean_response = ZestorHelper.urldb_open(url_db_file)
        print('\n\n==Cache Response==> %s' % (clean_response)) 
    else:
        clean_response = ZestorHelper.get_url_only_text(google_link)
        clean_response = ZestorHelper.relevant_summary(SELECTED_AI_ENGINE, clean_response)
        ZestorHelper.urldb_save(url_db_file, clean_response)

    ZestorHelper.save_file('knowledge.txt', clean_response, 'a') # append to our knowledge

exit()
