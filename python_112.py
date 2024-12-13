project = float(input("Enter the project marks: "))
internal = float(input("Enter the internal marks: "))
external = float(input("Enter the external marks: "))
if project >= 50 and internal >= 50 and external >= 50:
    total_marks = 100
    project_score = (project / total_marks) * 70
    internal_score = (internal / total_marks) * 10
    external_score = (external / total_marks) * 20
    total_score = project_score + internal_score + external_score
    print(f"Total Percentage: {total_score:.2f}%")
    if total_score >= 90:
        print("Grade: A")
    elif total_score >= 80:
        print("Grade: B")
    elif total_score >= 50:
        print("Grade: C")
    else:
        print("Failed in certain subject")
else:
    if project < 50:
        print(f"Failed in project =>marks={project}")
    if internal < 50:
        print(f"Failed in internal =>marks={internal}")
    if external < 50:
        print(f"Failed in external =>marks={external}")