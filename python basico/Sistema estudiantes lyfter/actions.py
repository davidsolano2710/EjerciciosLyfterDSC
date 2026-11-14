def add_student(student_list):
    while True:
        try:
            num_students = int(input("\nCuántos estudiantes deseas añadir?: "))
            if num_students > 0:
                break
            else:
                raise ValueError
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero mayor a 0.")
    
    for i in range(num_students):
        name = input(f"\nIngrese el nombre del estudiante {i + 1}: ")         #optional: validate name input

        section = input("Ingrese la sección del estudiante: ")              #optional: validate section input

        spanish_grade = get_grade_input("español")
        english_grade = get_grade_input("inglés")
        social_studies_grade = get_grade_input("estudios sociales")
        science_grade = get_grade_input("ciencias")
        average_grade = (spanish_grade + english_grade + social_studies_grade + science_grade) / 4

        student = {
                "name": name,
                "section": section,
                "spanish_grade": spanish_grade,
                "english_grade": english_grade,
                "social_studies_grade": social_studies_grade,
                "science_grade": science_grade,
                "average_grade": average_grade
            }
        student_list.append(student)


def get_grade_input(grade_name):
    while True:
        try:
            grade = float(input(f"Ingrese la nota de {grade_name} del estudiante: "))
            validate_grade(grade_name, grade)
            return grade
        except ValueError as e:
            print(e)


def validate_grade(grade_name, grade):
    if grade < 0 or grade > 100:
        raise ValueError(f"La nota de {grade_name} debe estar entre 0 y 100.")


def view_students(student_list):
    try:
        if student_list == []:
            raise IndexError
        for student in student_list:
            print(f"\nNombre: {student['name']}, Sección: {student['section']}. \nEspañol: {student['spanish_grade']}, Inglés: {student['english_grade']}, Estudios Sociales: {student['social_studies_grade']}, Ciencias: {student['science_grade']}")
    except IndexError:
        print("\nNo hay estudiantes para mostrar.")


def view_top3_students(student_list):
    try:
        sorted_students = []
        for student in student_list:
            sorted_students.append((student['name'], student['average_grade']))
        sorted_students.sort(key=lambda x: x[1], reverse=True)                   #had to investigate how to sort it by the second element of the tuple.
        
        if sorted_students == []:
            raise IndexError
        
        print("\n--- Top 3 Estudiantes con Mejor Promedio ---")
        for i, (name, average) in enumerate(sorted_students[:3]):                
            print(f"\nTop {i + 1}: {name} con un promedio de {average}")

    except IndexError:
        print("\nNo hay suficientes estudiantes para mostrar el top 3.")    



def view_average_grade(student_list):
    try:
        students_average = 0
        for student in student_list:
            students_average += student['average_grade']

        students_average = students_average / len(student_list)
        print(f"\nEl promedio general de los estudiantes es: {students_average}")
    except ZeroDivisionError:
        print("\nNo hay estudiantes para calcular el promedio general.")




    
