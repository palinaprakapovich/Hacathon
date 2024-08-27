# Hackathon
## Recykling. Jak w zależności od rodzaju śmieci, zmienia się kolor pojemnika?
Nazwa „recykling" pochodzi z języka angielskiego i składa się z dwóch słów: „re" oznaczającego „ponownie" i „cycle" oznaczającego „cykl". Tyle z teorii. A w praktyce? Materiały, takie jak papier, szkło, metal i tworzywa sztuczne, zyskują drugie życie i po raz kolejny zostają wprowadzone do obiegu, jako całkowicie nowe produkty. Co ważne, większość materiałów z odzysku gatunkowo nie różni się niczym od swoich poprzedników. W niektórych przypadkach proces recyklingu może nieznacznie wpłynąć na wytrzymałość i jakość przetwarzanych surowców, jednak nadal jest to rozwiązanie zdecydowanie korzystne dla środowiska naturalnego.
### Celem mojego projektu jest nauczanie ludzi prawidłowego segregowania śmieci według odpowiednich kolorów pojemników.
W Polsce obowiązują spójne standardy, które wprowadzają kolorowe pojemniki do segregacji śmieci. Podstawowe kolory segregacji śmieci to żółty dla metali i tworzyw sztucznych, niebieski dla papieru, zielony dla szkła i brązowy dla bioodpadów.
![image](https://github.com/user-attachments/assets/05f0d866-13c7-40e4-bebd-81a695affbc9)

#### - Co robi Bot?
#### - Na podstawie zdjęcia mój bot może wykryć materiał śmieci i pokazać do jakiego koloru pojemnika go trzeba wyrzucić.



## Główne biblioteki, których będę używać:
- Keras == 2.12.0
- Tensorflow == 2.12.0
- Discord == 2.4.0
- Numpy == 1.23.5
- Pillow == 10.4.0
- Requests == 2.32.3

## Instrukcja do używania mojej aplikacji:

1.Pobierz wszystkie pliki
![image](https://github.com/user-attachments/assets/cb06e1ba-d9e3-454f-9869-995abcc653d4)

2.Otwórz te pliki w folderze
![image](https://github.com/user-attachments/assets/a0281163-33fc-4252-890f-9eb4d4f909da)

3.Otwórz ten folder w VSC, PyCharm albo innej aplikacji do programowania
![image](https://github.com/user-attachments/assets/877f5430-626a-4b22-984b-74624c603fbb)

4.Utwórz środowisko wirtualne w folderze. Użyj polecenia pipenv shell, aby utworzyć środowisko wirtualne w folderze.
![image](https://github.com/user-attachments/assets/f070c0df-f99c-4de5-b9fa-f7609a7cf630)

5.Po utworzeniu środowiska wirtualnego, musisz je wybrać. Aby to zrobić, naciśnij Shift + Ctrl + P -> Select Interpretator i znajdź opcję, która ma taką samą nazwę jak twój projekt
![image](https://github.com/user-attachments/assets/959ac5f2-fdab-4235-b1b8-9ee0e7647127)
![image](https://github.com/user-attachments/assets/84a5ea15-ca0c-414f-aa8a-c94a554bd9dc)

Aby upewnić się, że wszystko działa zgodnie z zamierzeniem, sprawdź dwie rzeczy:

1)Projekt powinien teraz zawierać plik Pipfile

2)Nazwa twojego projektu powinna pojawić się w terminalu (znajdziesz ją w nawiasach)
![image](https://github.com/user-attachments/assets/64a37046-edb8-4be9-bb68-9eb870592ad2)


5.Zaimportuj biblioteki: discord.py, numpy, requests, Pillow, keras i tenserflow 
![image](https://github.com/user-attachments/assets/daa9ce78-83d3-4180-a449-5169ef866cf5)
![image](https://github.com/user-attachments/assets/644da770-da70-4e8f-a27b-f0c24923615a)
![image](https://github.com/user-attachments/assets/25e8758a-fa1f-404f-bdbd-a4cdf898cb41)

6.Za pomocą komendy pip freeze sprawdż wersje bibliotek keras i tensorflow. Powinny to być wersje 2.12.0

7. Jeżeli wersja jest inna:

 -pip uninstall keras

 -pip uninstall tensorflow
 
 -pip install keras == 2.12.0
 
 -pip install tensorflow == 2.12.0
  
8.Uruchom main.py

9.Załóż darmowe konto albo wejdż już na istniejące konto discord

10. Wyślij zdjęcie śmieci, których nie jesteś pewien, gdzie wyrzucić, i dodaj $check.

#### Jak zrobiłeś wszystko poprawnie, wyglądać to będzie w taki sposób:
![image](https://github.com/user-attachments/assets/b7cda5f8-c9bf-44e4-bf44-6ac93bdc97c1)


## Testowa Lista Kontrolna 
1. Zidentyfikuj cele testowania : Zobaczyć czy aplikacja poprawnie wykrywa kolor pojemnika do którego musimy wyrzucić śmieci, wysyłane przez użytkownika 
2. Podziel listę kontrolną na kategorie : z tego powodu, że mój project jest związany z discordem, muszę skupić swoją uwagę tylko na funkcjonalności
3. Opisz oczekiwane wyniki : wynik klasyfikacji pojemnika musi być poprawny i wynosić więcej niż 50%
4. Dodaj zadania dla każdej kategorii : dodać blok try:... except:...

# Mam nadziej, że moja aplikacja pomoże uratować naszą planetę! 
