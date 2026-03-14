#!/bin/bash
set -e

echo "Post-merge : mise à jour de l'environnement du bot..."

# 1️⃣ Mettre à jour les dépendances Python
if [ -f requirements.txt ]; then
    echo "Installation / mise à jour des packages..."
    pip install -r requirements.txt
fi

# 2️⃣ Vérifier si main.py existe
if [ -f main.py ]; then
    echo "Relance du bot..."
    # Tu peux choisir de relancer ton bot ici
    # python main.py &   # décommenter si tu veux qu’il se lance en arrière-plan
else
    echo "main.py introuvable. Veuillez vérifier votre projet."
fi

echo "✅ Post-merge terminé, bot prêt."
