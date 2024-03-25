#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author AUGUSTYN Patricia

Utilisation :
python3 clean_data_cleaner.py

"""

import os
import re
import glob

def clean_to_text(path_xml, path_clean):
    '''Cette fonction permet de lire les fichiers XML dont le chemin est donné en
    argument, et qui retourne le texte et les métadonnées des items du flux RSS.'''

    # Utilisation de glob pour obtenir une liste de tous les fichiers XML dans le répertoire spécifié
    fichiers_xml = glob.glob(path_xml)

    for fichier_xml in fichiers_xml:
        with open(fichier_xml, "r", encoding="utf-8") as fichier:
            xml = fichier.read()
            # On veut cibler notre regex sur ce qui est seulement à l'intérieur des balises <link></link>, <title></title>, <description></description> et <content></content> : donc ()

            regex_titre = re.findall(r"<title>(.*)</title>", xml)
            regex_description = re.findall(r"<description>(.*)</description>", xml)

            regex_lien = re.findall(r"<link>(.*)</link>", xml)

            regex_contenu = re.findall(r"<content>(.*)</content>", xml)

            # Création d'un fichier texte pour chaque fichier XML
            nom_fichier_txt = os.path.splitext(os.path.basename(fichier_xml))[0] + ".txt"
            chemin_resultat = os.path.join(path_clean, nom_fichier_txt)

            with open(chemin_resultat, "w", encoding="utf-8") as fichier_txt:

                #fichier_txt.write("\nLe texte entre les balises <link></link> dans " + fichier_xml + ":\n")
                for lien in regex_lien:
                    fichier_txt.write(lien.strip() + "\n")

               # fichier_txt.write("\nLe texte entre les balises <title></title> dans " + fichier_xml + ":\n")
                for titre in regex_titre:
                    fichier_txt.write(titre.strip() + "\n")

                # fichier_txt.write("\nLe texte entre les balises <content></content> dans " + fichier_xml + ":\n")
                for contenu in regex_contenu:
                    fichier_txt.write(contenu.strip() + "\n")

               # fichier_txt.write("\nLe texte entre les balises <description></description> dans " + fichier_xml + ":\n")
                for description in regex_description:
                    fichier_txt.write(description.strip() + "\n")

clean_to_text("../../data/raw/*.xml", "../../data/clean/")
