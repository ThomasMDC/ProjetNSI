# IA de reconnaissance d'image
***
## Fonctionnement:
IA de reconnaissance d'image qui prend un graphique sur lequel est représentée l'évolution du bitcoin sur une heure et prédit s'il va monter ou descendre les 10 minutes qui suivent.

***
"GenDatas.py" permet de générer ces graphiques sur les 6 derniers jours (les enregistrant et labellisant dans un fichier "Graphes")  
"Model.py" permet de créer un model (une Ia) et de l'entrainer sur les graphiques du dossier Graphes  
"Predictory.py" permet d'exploiter l'Ia sur les graphiques du dossier "GrapheTest" et ainsi voir les réponses données  
"GrapheActuel.py" permet de générer le graphe de la dernière heure (en l'enregistrant dans le dossier "GraphesVictor") que l'on pourra ensuite passer dans le predictory
