# Guide d'utilisation :

> Les modules utilisés : feedparser, re, os, glob,

Pour ce projet, nous avons récupéré le flux RSS du journal `New York Times` pour pouvoir réaliser un corpus ressemblant à celui de `WikorS` (cf. README.md)

Pour cela, nous récolté nos données sur le lien ci-dessous :

- https://rss.nytimes.com/services/xml/rss/nyt/World.xml


## Récolte des données :

Tout d'abord, nous avons récolté nos données automatiquement avec la librairie *feedparser* dans un script python `recover_data.py`.

Les fichiers obtenus se trouvent dans le dossier :
> /PROJECT/data/raw/nyt_*.xml

**Installation** :
Si vous rencontrez des problèmes en lançant notre fonction vous pouvez installer le module correspondant. Voici un exemple avec le module feedparser, ainsi que les commandes que vous pouvez effectuer dans le terminal :

1) Créer un environnement virtuel :

```
python3 -m venv venv
```

2) Activer votre environnement virtuel :

```
source venv/bin/activate
```

3) Installer votre module feedparser :

```
pip install feedparser
```

**Les balises** :

Pour notre script, nous avons récolté le contenu des balises qui nous intéresse :
- <title>...</ title>
- <link>...</ link>
- <description>...</ description>
- <content>...</ content>

### Lancement du script :

```
python3 recover_data.py.py
```

## Nettoyage des données :

Pour nettoyer nos données, nous avons écrit un script `clean_data_cleaner.py`.

Les fichiers obtenus se trouvent dans le dossier :
> /PROJECT/data/clean/nyt_*.txt

Pour récolté seulement le texte entre nos balises nous avon utilisé des expressions régulières avec le module `re`.

```py
# [...]
            # On veut cibler notre regex sur ce qui est seulement à l'intérieur des balises <link></link>, <title></title>, <description></description> et <content></content> : donc ()
            regex_titre = re.findall(r"<title>(.*)</title>", xml)
            regex_description = re.findall(r"<description>(.*)</description>", xml)

            regex_lien = re.findall(r"<link>(.*)</link>", xml)

            regex_contenu = re.findall(r"<content>(.*)</content>", xml)
#[...]
```

### Lancement du script :

```
python3 clean_data_cleaner.py
```

## Obtenir les mêmes colonnes que notre corpus de référence :

Pour obtenir les mêmes colonnes que notre corpus de référence, nous avons importer le module `csv` pour enregistrer nos résultats dans le dossier :
> /PROJECT/figures/nyt_data.csv

Pour cela nous avons écrit un script python `corpus_table.py` qui reprend le même fonctionnement que le nettoyage car on utilise les expressions régulières.

Notre fonction principale `extract_data_from_xml()` permet de lire nos fichiers XML et reprend les regex pour cibler notre requête pour récupéré seulement le texte entre nos balises :

```py
def extract_data_from_xml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    # Utilisation de re.findall() pour extraire toutes les occurrences des balises XML
    links = re.findall(r'<link>(.*?)</link>', xml_content)
    titles = re.findall(r'<title>(.*?)</title>', xml_content)
    descriptions = re.findall(r'<description>(.*?)</description>', xml_content)
    contents = re.findall(r'<content>(.*?)</content>', xml_content)

    # Concaténation des résultats en une seule chaîne pour chaque élément
    link_text = "\n".join(links)
    title_text = "\n".join(titles)
    description_text = "\n".join(descriptions)
    content_text = "\n".join(contents)

    return [link_text, title_text, description_text, content_text]
```

### Lancement du script :

```
python3 corpus_table.py
```
