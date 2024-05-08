#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author AUGUSTYN Patricia

Utilisation :
python3 recover_data.py

"""

import os
import feedparser

rss_url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"

feed = feedparser.parse(rss_url)

# Parcourir les entrées du flux RSS
for idx, entry in enumerate(feed.entries, start=1):
    title = entry.title
    link = entry.link
    description = entry.description
    # content = entry.content[0].value

    # On vérifie que content est bien présent dans le fichier
    if "content" in entry and entry.content:
        content = entry.content[0].value

    # Créer un fichier XML pour chaque article
    filename = f"../../data/raw/nyt_{idx}.xml"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"<title>{title}</title>\n")
        file.write(f"<link>{link}</link>\n")
        file.write(f"<description>{description}</description>\n")
        file.write(f"<content>{content}</content>\n")


print("Tous les fichiers RSS ont été enregistrés avec succès.")
