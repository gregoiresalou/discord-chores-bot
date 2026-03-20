# 🧹 Discord Chores Automator (Bot de Coloc)

**Vous vous êtes déjà pris la tête avec vos colocs pour savoir à qui le tour de nettoyer la cuisine ?** 😅🧹

Eh bien, c’est exactement ce qui est en train de m’arriver dans ma colocation Erasmus, ici à Budapest ! Mais pour préserver la paix internationale dans l'appartement, j'ai décidé de confier cette responsabilité à un juge totalement incorruptible : un script Python.

Au départ, ma logique était basique : j'avais écrit un script avec une boucle infinie (`while True`) qui tournait 24h/24 sur mon NAS pour vérifier s'il était 10h00. Bilan : le programme allait faire 86 400 vérifications par jour pour n'envoyer qu'un seul message... Pas vraiment optimal ! ❌

J'ai donc revu mon architecture pour faire les choses proprement :
1️⃣ **Planification (Cron / Task Scheduler) :** Le script est réveillé ponctuellement par l'OS.
2️⃣ **Persistance des données :** Création d'une mémoire locale (fichier `.txt`) pour retenir à qui le tour.
3️⃣ **Consommation d'API :** Envoi d'un payload JSON via une requête POST sur un Webhook Discord. 🤖

---

## 🛠️ Comment l'utiliser chez vous ?

1. Clonez ce dépôt.
2. Installez les dépendances : `pip install -r requirements.txt`
3. Dans le fichier `menage.py`, remplacez `"WEBHOOK_ICI"` par l'URL de votre Webhook Discord.
4. Modifiez la liste des prénoms avec ceux de vos colocataires.
5. Configurez une tâche planifiée (Planificateur Windows ou Cron sous Linux) pour exécuter le script tous les jours à l'heure de votre choix !