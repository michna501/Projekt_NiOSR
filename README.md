# Wstęp

Niniejszy projekt przedstawia program umożliwiający sterowanie żółwiem w ROS2. Projekt wykorzystuje biblioteki OpenCV.

## Uruchomienie

W celu uruchomienia programu należy w terminalu wpisać polecenie:

```bash
ros2 run turtle_controller controller
```

## Działanie programu
1. Funkcja `turtleClick()` jest wywoływana za każdym razem, gdy mysz wykona akcję w oknie. Funkcja ta sprawdza, czy mysz została kliknięta, podwójnie kliknięta prawym przyciskiem lub przeciągnięta. Jeśli mysz została kliknięta, funkcja ustawia zmienną on na `True` i zapisuje pozycję kursora w zmiennej `click`. Jeśli mysz została przeciągnięta, funkcja aktualizuje pozycję kursora w zmiennej `click`.
2. Klasa `TurtleController` dziedziczy po klasie `Node` z pakietu `rclpy`. Klasa ta zawiera metodę `__init__()`, która inicjalizuje node'a ROS 2, tworzy publisher'a do publikowania wiadomości `Twist`, tworzy zmienną `msg` typu `Twist` i tworzy okno z kursorem myszy. Metoda `run()` klasy `TurtleController` wykonuje następujące czynności w pętli:

   * Aktualizuje obraz wyświetlany w oknie.
   * Oblicza prędkość obrotową i liniową robota w oparciu o pozycję kursora myszy.
   * Publikuje wiadomość `Twist` z prędkością obrotową i liniową robota.
   *Oczekuje na wciśnięcie klawisza `q`.
3. Funkcja `main()` inicjalizuje ROS 2 i tworzy obiekt klasy `TurtleController`. Następnie funkcja `main()` wywołuje metodę `run()` obiektu `TurtleController`.

## Sterowanie

Kontrola położenia żółwia odbywa się przez oddziaływanie myszką na joystick wyświetlany na ekranie.
* odległość kliknięcia od środka przekłada się na prędkość liniową żółwia
* kąt pomiędzy niebeiską linią a linią rysowaną przez kliknięcie przekłada się na prędkość obrotową żółwia
* kliknięcie w środkowym ciemnoszarym obszarze powoduje tylko ruch obrotowy, zmienia się kolor linii
* kliknęcie poza okręgami powoduje tylko ruch liniowy żółwia - kliknięcie w górnej połowie okna powoduje ruch do przodu, a w dolnej do tyłu

## Autorzy
Filip Tański\
Michał Szczupakowski\
Artur Markuszewski

## License

[MIT](https://choosealicense.com/licenses/mit/)
