import pandas as pd
import matplotlib.pyplot as plt
import os
def load_data(path):
    return pd.read_csv(path)

def add_total(data):
    data["total"] = data["prix"] * data["quantite"]
    return data
def analyse_produits(data):
    quantite = data.groupby("produit")["quantite"].sum()
    total = data.groupby("produit")["total"].sum()
    return quantite, total
def analyse_mois(data):
    return data.groupby("mois")["total"].sum()
def plot_graphs(quantite, total, mois):
    if not os.path.exists("images"):
        os.makedirs("images")
        quantite.plot(kind="bar", color="skyblue")
        plt.title("quantité vendue par produit")
        plt.xlabel("Produit")
        plt.ylabel("Quantité")
        plt.tight_layout()
        plt.savefig("images/produits_quantite.png")
        plt.close()

        total.plot(kind="bar", color="green")
        plt.title("Chiffre d'affaires par produit")
        plt.xlabel("Produit")
        plt.ylabel("Total (FCFA)")
        plt.tight_layout()
        plt.savefig("images/produits_total.png")
        plt.close()

        mois.plot(kind="bar", color="orange")
        plt.title("Vente par mois")
        plt.xlabel("Mois")
        plt.ylabel("Total(FCFA)")
        plt.tight_layout()
        plt.savefig("images/ventes_mois.png")
        plt.close()


def main():
    data = load_data("data/ventes_magasin.csv")
    data = add_total(data) 
    quantite, total = analyse_produits(data)
    mois = analyse_mois(data)
    plot_graphs(quantite, total, mois)

    print("=== produits les plus vendus ===")
    print(analyse_produits(data))
    print("\n=== Ventes par mois ===")
    print(analyse_mois(data))
    
    print("\n Graphiques sauvegardés dans le dossier 'image' ")
if __name__ == "__main__":
    main()    
