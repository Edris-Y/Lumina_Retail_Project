# 🛒 Lumina Retail - E-Commerce Performance & Logistics Analysis

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

## 📌 Contexte Métier
**Lumina Retail** est une plateforme e-commerce gérant un volume important de commandes quotidiennes. L'objectif de ce projet est d'analyser l'entonnoir de vente, le chiffre d'affaires généré, ainsi que le suivi logistique des expéditions pour s'assurer de la bonne santé opérationnelle de l'entreprise.

Ce projet met l'accent sur le traitement de données transactionnelles massives et la création d'indicateurs de performance (KPIs) fiables.

## 🗄️ 1. Modélisation et Ingestion (Data Engineering)
Le dataset contient l'historique détaillé des transactions avec des clés uniques complexes (UUID) et des horodatages précis (`timestamps`).

**Missions réalisées :**
- Création de l'architecture relationnelle dans **PostgreSQL**.
- Ingestion de milliers de lignes de données transactionnelles (`order_id`, `order_status`, `order_purchase_timestamp`).
- Préparation d'une vue consolidée prête pour la Business Intelligence (`lumina_powerbi_ready.csv`).

## 🧹 2. Traitement et Nettoyage (Data Preparation)
Les données brutes présentaient des défis de formatage qui empêchaient l'analyse financière directe. L'utilisation de **Power Query** a été indispensable.

**Opérations de nettoyage (ETL) :**
- **Typage des données :** Conversion des colonnes de dates brutes en format `Date/Heure` exploitable pour l'analyse temporelle.
- **Data Cleansing :** Correction des formats de devises internationaux (remplacement des `.` par des `,` sur la colonne `price`) pour permettre l'agrégation mathématique du Chiffre d'Affaires.

## 📊 3. Visualisation (Business Intelligence)
Création d'un rapport analytique dans **Power BI** permettant d'avoir une vue d'ensemble sur l'activité e-commerce.

**Analyses développées :**
- **Analyse Financière :** Somme du Chiffre d'Affaires global.
- **Analyse Logistique :** Suivi de l'état des commandes (part des commandes au statut `delivered` vs en cours d'expédition).
- **Analyse Temporelle :** Évolution des achats selon l'heure ou la date de la transaction (`order_purchase_timestamp`).

## 📁 Structure du Projet

```text
📦 Lumina_Retail_Project
 ┣ 📂 data/                  # Datasets bruts (historique des commandes)
 ┣ 📂 sql/                   # Scripts d'initialisation de la base PostgreSQL
 ┣ 📜 lumina_powerbi_ready.csv # Fichier de données consolidé
 ┣ 📊 Lumina_Dashboard.pbix  # Dashboard Power BI interactif
 ┗ 📜 README.md              # Documentation du projet
```

### Auteur : Edris Youssef