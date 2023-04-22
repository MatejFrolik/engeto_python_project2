# engeto_python_project2 - BULLS&COWS game

Odkaz na můj **Linkedl** [ZDE](https://www.linkedin.com/in/matěj-frol%C3%ADk-183812230/).


----

## Úvod do projektu/zadání projektu    
Úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Po vypsání úvodního textu uživateli, může hádání tajného čtyřciferného čísla začít.

**Program bude obsahovat:**    
1. Program podraví uživatele a vypíše pravidla hry
2. Program dále vytvoří tajné _4místné_ číslo (číslice musí být unikátní a nesmí začínat 0)
3. Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
4. Program vyhodnotí tip uživatele
5. Program dále vypíše počet _bull/ bulls_ (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. _cows/ cows_ (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
6. Pokud uživatel nebude chtít ve hře pokračovat, zadá na klávesnici _'Q'_, v případně uhodnutí celého čísla, nebo-li všech bulls, program se ukončí, pogratuluju, vypíše počet pokusů, které uživatel k uhodnutí potřeboval a jeho čas. Zeptá se uživatele, jestli chce hrát další hru.

## Průběh programu může vypada například takto:  
```
Hello and welcome in BULLS&COWS game!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
>>> 1234
0 bulls, 2 cows
-----------------------------------------------
>>> 6147
1 bull, 1 cow
-----------------------------------------------
>>> 2417
3 bulls, 0 cows
-----------------------------------------------
>>> 2017
Correct, you've guessed the right number
in 4 guesses! It tooks you 20.39 seconds!
Do you wanna play another game? Y/N
```

## Jednotlivé kroky:
1. Import potřebných knihoven.
2. Pozdravení uživatele a vysvětlení pravidel hry.
3. Funkce pro generování náhodného 4ciferného čísla.
4. Funkce pro vstup uživatele.
5. Funkce pro počítání Bulls/Cows
6. Main funkce pro samotnou hru.
7. Zavolání funkce.

