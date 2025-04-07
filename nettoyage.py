import pandas as pd
import re

# Charger les 10 premières lignes du fichier
df = pd.read_csv("annonces_logic_immo1.csv", sep=";")

# 🧼 Nettoyage du prix
def nettoyer_prix(prix):
    if pd.isna(prix):
        return None
    prix_str = re.sub(r"[^\d]", "", str(prix))
    return int(prix_str) if prix_str.isdigit() else None

# 🧼 Nettoyage des charges annuelles
def nettoyer_charges(val):
    if pd.isna(val) or val == "":
        return 0
    val_str = str(val)
    val_str = re.sub(r"[^\d]", "", val_str)  # supprime tout sauf les chiffres
    return int(val_str) if val_str.isdigit() else 0


# 🧼 Nettoyage de l’arrondissement (extrait le code postal)
def nettoyer_arrondissement(texte):
    match = re.search(r"\((75\d{3})\)", str(texte))
    return int(match.group(1)) if match else None

# 🧼 Nettoyage de la superficie (retourne un float sans "m²", virgule → point)
def nettoyer_superficie(val):
    if pd.isna(val):
        return None
    val_str = str(val).replace(",", ".")  # change virgule en point
    val_str = re.sub(r"[^\d.]", "", val_str)  # supprime les caractères sauf chiffres et point
    try:
        return float(val_str)
    except ValueError:
        return None

# 🏢 Nettoyage étage
def clean_etage(val):
    if pd.isna(val):
        return None, None
    val = str(val)
    if "RDC" in val:
        match = re.search(r'RDC/?(\d+)?', val)
        etage = 0
        total = int(match.group(1)) if match and match.group(1) else None
        return etage, total
    match = re.search(r"(\d+)", val)
    return (int(match.group(1)), None) if match else (None, None)

# 📦 Gestion des deux colonnes étage + nombre d'étages
def clean_deux_colonnes(row):
    val1, val2 = row.iloc[0], row.iloc[1]
    try:
        if pd.notna(val1) and pd.notna(val2):
            return int(val1), int(val2)
    except:
        pass
    return clean_etage(val1) if pd.notna(val1) else clean_etage(val2)

# ✨ Application du nettoyage
df["prix"] = df["Prix"].apply(nettoyer_prix)
df["superficie"] = df["Superficie"].apply(nettoyer_superficie)
df["arrondissement"] = df["Arrondissement"].apply(nettoyer_arrondissement).astype("Int64")  # colonne entière mais avec NaN possible
df["superficie"] = df["Superficie"].apply(nettoyer_superficie)
df["charges_annuelles"] = df["Charge annuelles"].apply(nettoyer_charges)

df.loc[
    df["Superficie salon (m²)"].isna() & (df["Nombre de pieces"] == 1),
    "Superficie salon (m²)"
] = df["superficie"]
df["Superficie salon (m²)"].fillna(0, inplace=True)
df["DPE"].fillna("", inplace=True)
df["GES"].fillna("", inplace=True)
df["Exposition"].fillna("", inplace=True)

# Nettoyage étage
etages_nettoyes = df[["Etage", "Nombre d'etages"]].apply(clean_deux_colonnes, axis=1, result_type='expand')
etages_nettoyes.columns = ["Etage", "Total_etages"]

# Supprimer les anciennes colonnes pour éviter les doublons
df = df.drop(columns=["Etage", "Nombre d'etages"])
df = df.drop(columns=["Arrondissement"])
df = df.drop(columns=["Superficie"])
df = df.drop(columns=["Prix"])
df = df.drop(columns=["Charge annuelles"])

# Fusion propre
df = pd.concat([df, etages_nettoyes], axis=1)

# 💾 Export
df.to_excel("donnees_nettoyees.xlsx", index=False)

print("✅ Nettoyage terminé ! Fichier exporté.")
