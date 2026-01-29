# INF2_SCADA
Informatyka 2, projekt 2 - aplikacja przypominająca SCADA

Projekt jest aplikacją, przypominającą program SCADA.
Przedstawia model elektrownii atomowej typu BWR (boiling water reactor). Steruje się za pomocą prętów sterujących przykrywających pręty paliwowe. Pręty sterujące początkowo zakrywają cały pręt paliwowy. Podnosząc go, odkrywa się paliwo, które reaguje z neutronami w zbiorniku. Podnosząc kilka prętów, lub o większą wartość, zwiększa się ilość wytwarzanej energii.
Reaktor podgrzewa wodę, która paruję, a następnie się skrapla. 
W programie uwzględnione jest miejce na rozwój (znaczną poprawę działania, od stanu obecnego), gdyż bardziej rozwinięta jest logika niż GUI. Na to wpływa m.in.:
1) Okno, z którego otwiera się model elektrowni atomowej. Można w nim umieścić więcej różnych systemów/obiektów.
2) Raporty w konsoli. M.in ilość wytwarzanej energii. Te dane mogą być w przyszłości umieszczone jako część GUI.
3) Powiadomienia o błędach. Stworzone są funkcje sprawdzające np. czy elektrownia nie wytwarza za dużo energii, czy się nie przegrzewa. Można dodać wyskakujące okienka informacyjne, nie starczyło mi czasu.
