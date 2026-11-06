import csv


def export_students_to_csv(student_list):
    with open('estudiantes.csv', 'w', encoding = 'utf-8', newline='') as file:
        headers = student_list[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        for student in student_list:
            writer.writerow(student)
    print("\n¡Datos exportados exitosamente a estudiantes.csv!\n")


def import_students_from_csv():
    try:
        student_list = []
        with open('estudiantes.csv', 'r', encoding = 'utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish_grade": float(row["spanish_grade"]),
                    "english_grade": float(row["english_grade"]),
                    "social_studies_grade": float(row["social_studies_grade"]),
                    "science_grade": float(row["science_grade"]),
                    "average_grade": float(row["average_grade"])
                }
                student_list.append(student)
            print("\n¡Datos importados exitosamente!\n")
            return(student_list)
    except FileNotFoundError:
        print("\nNo se encontró el archivo 'estudiantes.csv'. Asegúrate de exportar los datos primero.")

    