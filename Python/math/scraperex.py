#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:29:01 2022

@author: kyle
"""

import requests
import csv
import pandas as pd
import time
import wikipedia

base_url="https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user"
def consurl(handle, period, start, end):
    urls=[base_url, handle, period, start, end]
    constructed=str.join('/', urls)
    return constructed
def querywikiviews(url):
    res=requests.get(url)
    return res.json()
def wikipageviews(handle, period, start, end):
    cons_url=consurl(handle, period, start, end)
    pageviews=querywikiviews(url=cons_url)
    return pageviews
def wiki2016(handle, sleep=0):
    print("SLEEP: {sleep}".format(sleep=sleep))
    time.sleep(sleep)
    pageviews=wikipageviews(handle=handle, period="daily", start="2016010100", end="2016123100")
    if not 'items' in pageviews:
        print("NO PAGEVIEWS: {handle}".format(handle=handle))
        return None
    return pageviews
def createwikidf(handles):
    pageviews=[]
    timestamps=[]
    names=[]
    wikipedia_handles=[]
    for name, handle in handles.items():
        pageviews_record=wiki2016(handle)
        if pageviews_record is None:
            continue
    for record in pageviews_record['items']:
        pageviews.append(record['views'])
        timestamps.append(record['timestamp'])
        names.append(name)
        wikipedia_handles.append(handle)
    data ={
        "names":names,
        "wikipedia_handles":wikipedia_handles,
        "pageviews":pageviews,
        "timestamps":timestamps
    }
    df=pd.DataFrame(data)
    return df
def createwikihandle(raw_handle):
    wikipedia_handle=raw_handle.replace(" ", "_")
    return wikipedia_handle
def createwikinbahandle(name):
    url=" ".join([name, "(basketball)"])
    return url
def wikipedia_current_nba_roster():
    links={}
    nba=wikipedia.page("List_of_current_NBA_team_rosters")
    for link in nba.links:
        links[link]=createwikihandle(link)
    return links
def guess_wikipedia_nba_handle(data="data/nba_2017_br.csv"):
    links=wikipedia_current_nba_roster()
    nba=pd.read_csv(data)
    count=0
    verified={}
    guesses={}
    for player in nba["Player"].values:
        if player in links:
            print("Player: {player}, Link: {link}".format(player=player, link=links[player]))
            print(count)
            count+=1
            verified[player]=links[player]
        else:
            print("NO MATCH: {player}".format(player=player))
            guesses[player]=createwikihandle(player)
    return verified, guesses
    
def validate_wikipedia_guesse(guesses):
    verified={}
    wrong={}
    for name, link in guesses.items():
        try:
            page=wikipedia.page(link)
        except(wikipedia.DisambiguationError, wikipedia.PageError) as error:
            nba_handle=createwikinbahandle(name)
            try:
                page=wikipedia.page(nba_handle)
                print("Initial wiki URL failed: {error}".format(error=error))
            except(wikipedia.DisambiguationError, wikipedia.PageError) as error:
                print("Second Match Faulure: {error}".format(error=error))
                wrong[name]=link
                continue
        if "NBA" in page.summary:
            verified[name]=link
        else:
            print("NO GUESS MATCH: {name}".format(name=name))
            wrong[name]=link
    return verified, wrong
