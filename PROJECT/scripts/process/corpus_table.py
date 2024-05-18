#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author AUGUSTYN Patricia

Utilisation :
python3 corpus_table.py

"""
import os
import re
import csv


def extract_data_from_xml(file_path):
    """
    Cette fonction permet d'extraire les données d'un fichier XML et les renvoie sous forme de liste de chaînes de caractères.

    Paramètres:
    file_path (str): Le chemin du fichier XML que l'on veut traiter.

    Retourne:
    list: Une liste contenant quatre chaînes de caractères qui représentent les données concaténées des balises <link>, <title>, <description> et
    <content>.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        xml_content = file.read()

    # Utilisation de re.findall() pour extraire toutes les occurrences des balises XML
    links = re.findall(r"<link>(.*?)</link>", xml_content)
    titles = re.findall(r"<title>(.*?)</title>", xml_content)
    descriptions = re.findall(r"<description>(.*?)</description>", xml_content)
    contents = re.findall(r"<content>(.*?)</content>", xml_content)

    # Concaténation des résultats en une seule chaîne pour chaque élément
    link_text = "\n".join(links)
    title_text = "\n".join(titles)
    description_text = "\n".join(descriptions)
    content_text = "\n".join(contents)

    return [link_text, title_text, description_text, content_text]


def main():
    """
    La fonction main permet d'extraire nos données des fichiers XML commençant par 'nyt' dans un dossier spécifié, puis les
    écrit dans un fichier CSV.

    Fonctionnement:
    Cette fonction cherche les fichiers XML dans notre dossier '../../data/raw/' dont le nom commence  par "nyt" et se termine par '.xml'. Ensuite, 
    on extrait les données de chaque fichier à l'aide de la fonction extract_data_from_xml(), puis les écrit dans un fichier CSV dans le dossier
    '../../figures/'.
    """
    # Une liste vide qu'on va remplir de nos données récoltées dans les balises matchées
    data = []

    # On cherche nos fichiers qui commence par "nyt" et qui finissent par .xml
    for file_name in os.listdir("../../data/raw/"):
        if file_name.startswith("nyt") and file_name.endswith(".xml"):
            file_path = os.path.join("../../data/raw/", file_name)
            final = extract_data_from_xml(file_path)
            data.append(final)

    # Écrire les données dans un fichier CSV
    output_folder = "../../figures/"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "nyt_data.csv")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Les noms des colonnes
        writer.writerow(["LINK", "TITLE", "DESCRIPTION", "CONTENT"])

        # Remplir les données dans les colonnes
        writer.writerows(data)


if __name__ == "__main__":
    main()
