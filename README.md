# Projet : Corpus

Voici le repository pour le cours de M1 TAL : outils de traitement de corpus

Pour ce projet, nous devons réaliser un corpus parmis les tâches dans le NLP. Pour ma part, je me suis inspirée du corpus de `WiktorS` :

- https://huggingface.co/datasets/WiktorS/polish-news

Ce corpus a été trouvé dans la tâche, `Text Classification`, `Summarization` et `Text Generation` en cherchant `polish` dans la barre de recherche.

Ce corpus, permet de créer un tableau/tabulation en ayant par catégorie :

- le lien
- le titre
- la headline : cela peut être la première ligne du paragraphe
- et le contexte : tout le contenu du texte

Ce corpus contient plus de 250 000 articles polonais obtenus du site `tvp info pl`. L'objectif de ce corpus était de collecter un maximent de données textuelles aifn de fournir des données d'entraînement pour un modèle de langage pour générer des résumés de texte.

Ce modèle est basé sur **un transformateur pour la synthèse de texte**. Un outil synthèse est un outil basé sur l'intelligence artificielle et il peut résumer un texte considéré comme *long* en un *résumé*.
La définition de `YourDictionary` :

"*La synthèse se définit comme la prise de beaucoup d'informations et la création d'une version condensée qui couvre les principaux points*"

Par exemple, voici des *résumeur* de texte :
- https://www.scribbr.fr/resume-de-texte/
- https://resoomer.com/
- https://quillbot.com/summarize

> Ce corpus est très récent car sur le compte Github, les derniers ajouts datent d'il y a 6/10 mois. Ainsi, il ne contient aucune sous-tâche ou autre information...

Pour représenter le but de corpus, voici un schéma qui le décrit :

![dataflow](https://github.com/WiktorSob/scraper-tvp/assets/94312553/60ca5c69-e353-4b83-b774-5fe526be9dc6)

Notre objectif était de pouvoir travailler sur une langue autre que le français. Pour continuer sur notre lancé, on aimerait récolé un flux RSS sur le lien du New York Times :

- https://rss.nytimes.com/services/xml/rss/nyt/World.xml

Pour télécharger le datasets, voici la commande indiqué :

```py
from datasets import load_dataset

dataset = load_dataset("WiktorS/polish-news")
```
