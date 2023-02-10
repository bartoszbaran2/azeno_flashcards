# Azeno Flashcards

## Algorytm postępowania:
1. czy potrzebujemy django app?
   2. `python manage.py startapp <app_name>`
   3. dodaj do installed apps -> settings.py
2. analiza czy potrzebujemy dane.
   1. narysuj ERD diagramu do analizy
   2. implementacja w models.py (relacje w """, sortowanie, czy custom manager)
   3. `python manage.py makemigrations <app_name>`
   4. `python manage.py migrate <app_name>`
   5. unit tests -> pytest
3. czy potrzebujemy zarządzać tym zasobem z CMSa (django admin)?
   1. zarejestruj modele w admin.py
4. czy wystawiamy dane w widoku?
   1. stwórz plik serializers.py i w nim klasę serializatora  - format danych (kowersja danych + validacja)
   2. unit tests -> pytest
5. Stwórz widoki (logika)
   1. dobieramy odpowiednią klasę do obsługi widoków [wyszukiwarka widoków](https://www.cdrf.co/)
   2. widok musi zwracać Response lub Redirect
   3. logika uprawnień - permission.py
   3. unit tests -? pytest
6. tworzymy lokalny router
   1. w pliku urls.py stwórz urlpatterns lub router
   2. podpinamy lokalne urls do globalnych urls -> config/urls.py
   3. Unit tests
7. postman i stworzenie kolekcji
    1. wyeksportowanie kolekcji do repozytorium