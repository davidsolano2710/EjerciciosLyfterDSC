import actions
import data

def main_menu():
    while True:
        print("=== Sistema de Control de Estudiantes de LYFTER ===")
        print("1. Añadir Estudiantes")
        print("2. Ver información de todos los Estudiantes")
        print("3. Ver el top 3 de Estudiantes con mejor promedio")
        print("4. Ver nota promedio de todos los Estudiantes")
        print("5. Exportar información de los Estudiantes a un archivo CSV")
        print("6. Importar datos de un archivo CSV exportado previamente")
        print("7. Salir")

         
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 7:
                match choice:
                    case 1:
                        actions.add_student_ui()
                    case 2:
                        actions.view_students()
                    case 3:
                        actions.view_top_students()
                    case 4:
                        actions.view_average_grade()
                    case 5:
                        data.export_students_to_csv()
                    case 6:
                        data.import_students_from_csv()
                    case 7:
                        print("Exiting the program. Goodbye!")
                        break
            else:
                raise ValueError
            
        except ValueError:
            print("Entrada inválida. Por favor, ingresa una opción válida (1-7).")
            continue
        

def add_students_ui():
    while True:
        try:
            num_students = int(input("Cuántos estudiantes deseas añadir?: "))
            if num_students > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero mayor a 0.")
    
    for i in range(num_students):
        actions.add_student()
    