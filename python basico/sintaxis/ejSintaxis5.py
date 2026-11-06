print("--- Programa analisis de notas ---")

total_grades = 0
grade_counter = 1
approved_counter = 0
failed_counter = 0
avg_approved = 0
avg_failed = 0
total_avg = 0

total_grades = int(input("Ingrese la cantidad de notas: "))

while grade_counter <= total_grades:
    current_grade = int(input(f"Ingrese la nota numero {grade_counter}: "))
    if current_grade < 70:
        failed_counter += 1
        avg_failed += current_grade
    else:
        approved_counter += 1
        avg_approved += current_grade
    total_avg = total_avg + (current_grade / total_grades)
    grade_counter += 1

if failed_counter > 0:
    avg_failed = avg_failed / failed_counter
if approved_counter > 0:
    avg_approved = avg_approved / approved_counter

print(f"El estudiante tiene esta cantidad de notas aprobadas: {approved_counter}")
print(f"Este es el promedio de las notas aprobadas: {avg_approved}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_counter}")
print(f"Este es el promedio de las notas desaprobadas: {avg_failed}")
print(f"Este es el promedio total de notas: {total_avg}")
