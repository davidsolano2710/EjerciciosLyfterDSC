import csv
import studentClass


def export_students_to_csv(student_list):
    try:
        if student_list == []:
            raise IndexError
        with open('estudiantes.csv', 'w', encoding = 'utf-8', newline='') as file:
            headers = ["name", "section", "spanish_grade", "english_grade", "social_studies_grade", "science_grade", "average_grade"]

            writer = csv.DictWriter(file, fieldnames=headers)

            writer.writeheader()

            for student in student_list:
                writer.writerow({
                    "name": student.name,
                    "section": student.section,
                    "spanish_grade": student.spanish_grade,
                    "english_grade": student.english_grade,
                    "social_studies_grade": student.social_studies_grade,
                    "science_grade": student.science_grade,
                    "average_grade": student.average_grade
                })
        print("\n¡Datos exportados exitosamente a estudiantes.csv!\n")
    except IndexError:
        print("\nLa lista de estudiantes está vacía. No hay estudiantes para exportar.")


def import_students_from_csv():
    try:
        student_list = []
        with open('estudiantes.csv', 'r', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = studentClass.Student(
                    name=row["name"],
                    section=row["section"],
                    spanish_grade=float(row["spanish_grade"]),
                    english_grade=float(row["english_grade"]),
                    social_studies_grade=float(row["social_studies_grade"]),
                    science_grade=float(row["science_grade"]),
                )
                student_list.append(student)
            print("\n¡Datos importados exitosamente!\n")
            return(student_list)
    except FileNotFoundError:
        print("\nNo se encontró el archivo 'estudiantes.csv'. Asegúrate de exportar los datos primero.")
        return 55555

    