import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# Chargement
df = pd.read_csv('paris_finale.csv', sep=';')

# Vérification
print(df.columns)  # Affiche toutes les colonnes pour être sûr

# Séparation des variables
X = df.drop('prix', axis=1)
y = df['prix']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modèle
svr = SVR(kernel='rbf', C=1000, epsilon=0.1)
svr.fit(X_train_scaled, y_train)

# Prédictions
y_pred = svr.predict(X_test_scaled)

# Affichage des résultats
for true, pred in zip(y_test, y_pred):
    print(f"Valeur réelle : {true:.2f} - Prédiction : {pred:.2f}")

# Évaluation
print("MSE :", mean_squared_error(y_test, y_pred))
