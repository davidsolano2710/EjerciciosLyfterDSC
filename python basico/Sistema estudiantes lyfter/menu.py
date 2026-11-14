import actions
import data

def main_menu(student_list):
   
   while True:
    
        print("\n1. Añadir Estudiantes")
        print("2. Ver información de todos los Estudiantes")
        print("3. Ver el top 3 de Estudiantes con mejor promedio")
        print("4. Ver nota promedio de todos los Estudiantes")
        print("5. Exportar información de los Estudiantes a un archivo CSV")
        print("6. Importar datos de un archivo CSV exportado previamente")
        print("7. Salir")


        try:
            choice = int(input("\nElige una opción (1-7): "))
            if 1 <= choice <= 7:
                match choice:
                    case 1:
                        actions.add_student(student_list)
                        print("\n¡Estudiantes añadidos exitosamente!\n")
                    case 2:
                        actions.view_students(student_list)
                    case 3:
                        actions.view_top3_students(student_list)
                    case 4:
                        actions.view_average_grade(student_list)
                    case 5:
                        data.export_students_to_csv(student_list)
                    case 6:
                        student_list = data.import_students_from_csv()
                    case 7:
                        print("¡Hasta luego!")
                        break

            else:
                raise ValueError

        except ValueError:
            print("Entrada inválida. Por favor, ingresa una opción válida (1-7).")
        
        

    