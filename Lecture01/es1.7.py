import cmath


def risolvi_equazione_secondo_grado(a, b, c):
    # Verifica che l'equazione sia effettivamente di secondo grado
    if a == 0:
        if b == 0:
            if c == 0:
                return "L'equazione è indeterminata (infinite soluzioni)."
            else:
                return "L'equazione è impossibile (nessuna soluzione)."
        else:
            x = -c / b
            return f"L'equazione è di primo grado. Soluzione unica: x = {x}"

    # Calcolo del discriminante (Delta)
    delta = b**2 - 4 * a * c

    # Caso 1: Delta positivo (due soluzioni reali e distinte)
    if delta > 0:
        x1 = (-b + cmath.sqrt(delta).real) / (2 * a)
        x2 = (-b - cmath.sqrt(delta).real) / (2 * a)
        return (
            f"Delta > 0: Due soluzioni reali e distinte.\n"
            f"x1 = {x1:.4f}\n"
            f"x2 = {x2:.4f}"
        )

    # Caso 2: Delta nullo (una soluzione reale doppia)
    elif delta == 0:
        x = -b / (2 * a)
        return f"Delta = 0: Una soluzione reale doppia.\n" f"x1 = x2 = {x:.4f}"

    # Caso 3: Delta negativo (due soluzioni complesse e coniugate)
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return (
            f"Delta < 0: Due soluzioni complesse e coniugate.\n"
            f"x1 = {x1.real:.4f} + {x1.imag:.4f}j\n"
            f"x2 = {x2.real:.4f} + {x2.imag:.4f}j"
        )

if __name__ == "__main__":
    # --- CICLO DI RIAVVIO AUTOMATICO ---
    print("Risolutore di equazioni di secondo grado (ax² + bx + c = 0)")

    while True:
        try:
            # Il programma ci prova...
            coeff_a = float(input("\nInserisci il coefficiente a: "))
            coeff_b = float(input("Inserisci il coefficiente b: "))
            coeff_c = float(input("Inserisci il coefficiente c: "))

            # Se arriva qui senza errori, calcola il risultato
            risultato = risolvi_equazione_secondo_grado(coeff_a, coeff_b, coeff_c)
            print(f"\n--- Risultato: {risultato} ---")

            # ESCE DAL CICLO: Tutto è andato a buon fine, il programma può finire
            break

        except ValueError:
            # Se l'utente sbaglia l'input, scatta questo blocco
            print("\n[ERRORE] Hai inserito delle lettere o dei caratteri non validi!")
            print("Il programma verrà ricaricato. Riprova dall'inizio...")
            # Non c'è il break, quindi il ciclo 'while' ricomincia da capo automaticamente




