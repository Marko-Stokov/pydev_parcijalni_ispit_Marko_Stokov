import json

#TODO: Dodati type hinting na sve funkcije!


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers
    pass


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    customers = load_data(CUSTOMERS_FILE)
    while True:
        print("\nUpravljanje kupcima izbornik:")
        print("1. Dodavanje novog kupca")
        print("2. Prikaz liste kupaca")
        print("3. Izlaz")

        choice = input("Odabrana opcija: ")

        if choice == "1":
            name = input("Unesite ime kupca: ").strip()
            email = input("Unesite email kupca: ").strip()
            vat_id = input("Unesite VAT ID kupca: ").strip()

            novi_kupac = {
                "name": name,
                "email": email,
                "vat_id": vat_id
            }
            customers.append(novi_kupac)
            save_data(CUSTOMERS_FILE, customers)

            print("Kupac uspješno dodan")
        elif choice == "2":
            with open(CUSTOMERS_FILE, "r") as file:
                json_data = json.load(file)
                print(json_data)
        elif choice == "3":
            # Pohrana podataka prilikom izlaza
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")

    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca



# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    offers = load_data(OFFERS_FILE)

    while True:
        print("\nIzbornik ponuda:")
        print("1. Pregledaj sve opcije")
        print("2. Pogledaj ponude za naznačeni mjesec")
        print("3. Pogledaj pojedinu ponudu prema ID")
        print("4. Izlaz")
        
        choice = input("Odaberite opciju: ")
        if choice == "1":
            with open(OFFERS_FILE, "r") as file:
                json_data = json.load(file)
                print(json_data)
        elif choice == "2":
            with open(OFFERS_FILE, "r") as file:
                json_data = json.load(file)
                print(json_data)
        elif choice == "3":
            # Pohrana podataka prilikom izlaza
            offer_id = input("Unesite ID ponude: ").strip()
            offer = next((offer for offer in offers if offer['id'] == offer_id), None)
            if offer:
                printanje_ponude = print_offer(offer)
            else:
                print("Nijedna ponuda pronađena.")
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")

    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
