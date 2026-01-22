from servicios.biblioteca_service import BibliotecaService


def main():
    print("=== SISTEMA DE BIBLIOTECA - Demostración __init__ / __del__ ===\n")

    biblio = BibliotecaService()

    # Crear algunos objetos
    libro1 = biblio.registrar_libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 1967)
    libro2 = biblio.registrar_libro("1984", "George Orwell", "978-0451524935")

    user1 = biblio.registrar_usuario("María Pérez", "U001")
    user2 = biblio.registrar_usuario("Carlos López", "U002")

    print("\n--- Prestamos ---")
    prestamo1 = biblio.prestar_libro("978-0307474728", "U001")
    prestamo2 = biblio.prestar_libro("978-0451524935", "U002")

    print("\nEstado actual:")
    print(libro1)
    print(libro2)
    print(user1)
    print(user2)

    print("\n--- Devolviendo un libro manualmente ---")
    if prestamo1:
        biblio.devolver_libro(prestamo1)

    print("\n--- Fin del programa (aquí empiezan las destrucciones automáticas) ---")
    # Al salir del scope → se llaman los destructores

    # Para forzar y ver mejor la destrucción puedes descomentar:
    # del prestamo2
    # del libro1
    # del user1


if __name__ == "__main__":
    main()