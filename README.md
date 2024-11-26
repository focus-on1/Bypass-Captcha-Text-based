

# Cyber Focus Script - CAPTCHA Bypass Automation

## Description

Ce projet est un script Python automatisé conçu pour contourner les CAPTCHA sur des sites Web en utilisant Selenium et Google Lens. Il utilise également une extension Adblock pour éviter les publicités durant le processus.

## Fonctionnalités

- **Contournement des CAPTCHA** : Le script capture une image de CAPTCHA, l'enregistre localement, et utilise Google Lens pour récupérer le texte correspondant.
- **Navigation automatisée** : Basé sur Selenium WebDriver, le script interagit automatiquement avec le site cible.
- **Extension Adblock** : Une extension Chrome pour bloquer les publicités, améliorant ainsi la rapidité et la fluidité du script.
- **Amélioration en cours** : Le script est actuellement en cours d'amélioration pour permettre de contourner les protections **Cloudflare** sur les sites cibles, afin d'éviter tout problème de blocage.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les éléments suivants :

- [Python](https://www.python.org/downloads/) (version 3.8 ou plus récente)
- [Google Chrome](https://www.google.com/intl/fr_fr/chrome/) (navigateur)
- [ChromeDriver](https://chromedriver.chromium.org/) (correspondant à votre version de Chrome)
- Les bibliothèques Python requises (voir ci-dessous)

## Installation

1. Clonez le projet depuis GitHub :

   ```bash
   git clone https://github.com/ton-utilisateur/ton-repository.git
   cd ton-repository
   ```

2. Installez les dépendances Python nécessaires :

   ```bash
   pip install selenium pillow
   ```

3. Téléchargez le fichier **ChromeDriver** et placez-le dans le répertoire du projet.

4. Ajoutez le fichier **adblock.crx** (extension Adblock pour Chrome) dans le répertoire du projet.

## Fichiers

- **`main.py`** : Le script principal pour contourner les CAPTCHA.
- **`adblock.crx`** : Fichier d'extension Adblock pour Chrome.
- **`captcha_image.png`** : Image temporaire du CAPTCHA capturée par le script.

## Utilisation

1. Assurez-vous d’avoir configuré le fichier **main.py** en fonction de vos besoins (URL cible, sélecteurs CSS spécifiques, etc.).

2. Exécutez le script :

   ```bash
   python main.py
   ```

3. Le script ouvrira une fenêtre Chrome, naviguera vers le site cible, capturera le CAPTCHA, et tentera de le résoudre.

4. Le processus continue jusqu’à ce que le CAPTCHA soit correctement résolu.

## Exemple de flux du script

1. Le script charge le site web cible.
2. Il identifie l'image du CAPTCHA et la capture.
3. Il télécharge l'image sur Google Lens pour identifier le texte du CAPTCHA.
4. Le texte du CAPTCHA est saisi dans le champ approprié et soumis.

## Notes importantes

- Ce script est à des fins éducatives uniquement. L'utilisation de telles méthodes peut violer les termes et conditions de certains sites web.
- **Amélioration en cours** : Une fonctionnalité est en développement pour permettre de contourner les protections Cloudflare, garantissant ainsi un meilleur fonctionnement du script.
