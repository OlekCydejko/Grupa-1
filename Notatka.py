# Nazwa:
# JMO
# J - Jan
# M - Michał
# O - Olek

# MOJpython
# sadasadaasdasdasadasd

# Pomysły na aplikacje
# - komunikator
# - wypożyczalnia aut 
# - system lojalnoiściowy

# Motto 
# "Razem możemy więcej!"

# "Test"
##############################################################################################################################################

# Nazwa zespołu: DriveEase

# Motto: "Nasza droga, Twój komfort."

# Projekt logo: Link do logo


# O logo:

# Logo przedstawia dynamiczną, stylizowaną literę "D", która jednocześnie przypomina kształt klucza samochodowego, symbolizując dostęp i wygodę.
# Kolorystyka w odcieniach niebieskiego i zielonego symbolizuje spokój, zaufanie i środowisko, co podkreśla nasze zaangażowanie w ekologiczny aspekt wynajmu samochodów.
# Czyste, proste linie i minimalistyczny design dodają profesjonalizmu i nowoczesności.



# Projekt Aplikacji Wynajmu Samochodów

"""## Cel:
Nasz projekt ma na celu stworzenie kompleksowej aplikacji do wynajmu samochodów, która zapewni użytkownikom łatwy dostęp do szerokiej gamy pojazdów oraz ułatwi proces rezerwacji i zarządzania wypożyczeniami.

## Zakres:
- Utworzenie platformy internetowej.
- Implementacja systemu rezerwacji, umożliwiającego użytkownikom wybór daty, czasu i miejsca odbioru oraz zwrotu pojazdu.
- Stworzenie panelu administracyjnego dla pracowników firmy do zarządzania flotą samochodów, rezerwacjami oraz klientami.
- Zapewnienie możliwości oceniania i recenzowania zarówno pojazdów, jak i doświadczeń użytkowników.
- Zaimplementowanie chatbota który pomoże w wyborze auta.

## Funkcjonalności:
- Rejestracja i logowanie użytkowników.
- Przeglądanie dostępnych pojazdów z filtrowaniem według preferencji.
- Wybór daty, czasu i miejsca odbioru oraz zwrotu pojazdu.
- Generowanie potwierdzeń rezerwacji.
- Historia rezerwacji i możliwość anulowania rezerwacji.
- Ocena i recenzowanie pojazdów i doświadczeń użytkowników.
- Zarządzanie profilem użytkownika.
- Zarządzanie flotą samochodów i rezerwacjami przez panel administracyjny.

## Oczekiwane rezultaty:
- Stworzenie intuicyjnej, łatwej w obsłudze aplikacji, która zapewni użytkownikom wygodne doświadczenie w wynajmie samochodów.
- Zwiększenie dostępności i wygody procesu wynajmu samochodów dla klientów.
- Zwiększenie efektywności w zarządzaniu flotą samochodów i rezerwacjami przez firmę.
- Zadowolenie klientów oraz budowanie pozytywnego wizerunku marki poprzez wysoką jakość usług i obsługi."""

from flask import Flask, render_template

app = Flask(__name__)

# Przykładowa biblioteka samochodów
cars = [
    {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020, 'price': 150},
    {'brand': 'Honda', 'model': 'Civic', 'year': 2019, 'price': 160},
    {'brand': 'Ford', 'model': 'Focus', 'year': 2018, 'price': 140},
    {'brand': 'Volkswagen', 'model': 'Golf', 'year': 2021, 'price': 170},
    {'brand': 'BMW', 'model': '3 Series', 'year': 2017, 'price': 200},
    {'brand': 'Audi', 'model': 'A4', 'year': 2019, 'price': 220},
    {'brand': 'Mercedes-Benz', 'model': 'C-Class', 'year': 2020, 'price': 250},
    {'brand': 'Hyundai', 'model': 'Elantra', 'year': 2018, 'price': 130},
    {'brand': 'Kia', 'model': 'Forte', 'year': 2019, 'price': 135},
    {'brand': 'Nissan', 'model': 'Sentra', 'year': 2020, 'price': 140}
]

@app.route('/')
def index():
    # html_content = """
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>Wypożyczalnia samochodów</title>
    # </head>
    # <body>
    #     <header>
    #         <h1>Wypożyczalnia samochodów</h1>
    #     </header>
        
    #     <div class="car-library">
    #         <h2>Dostępne samochody:</h2>
    #         <ul>
    #             {% for car in cars %}
    #             <li>
    #                 <h3>{{ car.brand }} {{ car.model }}</h3>
    #                 <p>Rok produkcji: {{ car.year }}</p>
    #                 <p>Cena za dzień: {{ car.price }}$</p>
    #             </li>
    #             {% endfor %}
    #         </ul>
    #     </div>
    # </body>
    # </html>
    # """
    return render_template("index.html", cars=cars)

if __name__ == '__main__':
    app.run(debug=True)