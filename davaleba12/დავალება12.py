import csv, os

os.makedirs('files', exist_ok= True)

filename = os.path.join('files', 'data.csv')

students = [
  {'id': 8, 'name': 'Nika', 'age': 19, 'grade': 'B', 'subject_name': 'Physic', 'mark': 87},
  {'id': 19, 'name': 'Nuca', 'age': 18, 'grade': 'B', 'subject_name': 'Mathematic', 'mark': 84},
  {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic', 'mark': 74},
  {'id': 25, 'name': 'Nino', 'age': 20, 'grade': 'A', 'subject_name': 'Informatic', 'mark': 95},
  {'id': 22, 'name': 'Giga', 'age': 20, 'grade': 'A', 'subject_name': 'Biology', 'mark': 81},
  {'id': 31, 'name': 'Lana', 'age': 22, 'grade': 'B', 'subject_name': 'Geography', 'mark': 88},
  {'id': 3, 'name': 'Nino', 'age': 23, 'grade': 'B', 'subject_name': 'Informatic', 'mark': 85},
]

new_student = {
  'id': 5,
  'name': 'Demetre',
  'age': 18,
  'grade': 'A',
  'subject_name': 'Informatic',
  'mark': 94
}

with open(filename, "w", newline = "") as f:
  fieldnames = students[0].keys()
  writer = csv.DictWriter(f, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(students)

# 1.

new_sutdent1 = {
  'id': input("Enter id: "),
  'name': input("Enter name: "),
  'age': input("Enter age: "),
  'grade': input("Enter grade: "),
  'subject_name': input("Enter subject: "),
  'mark': input("Enter mark: ")
}


with open(filename, "a", newline = "") as f:
  fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
  writer = csv.DictWriter(f, fieldnames = fieldnames)
  writer.writerow(new_sutdent1)
  


with open(filename, "r", newline = "") as f:
  reader = csv.DictReader(f)
  data = list(reader)

data.sort(key = lambda x: int(x['id']))


with open(filename, "w", newline = "") as f:
  fieldnames = data[0].keys()
  writer = csv.DictWriter(f, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(data)



# 2.

def read(filename: str, st_name=''):
    with open(filename, mode = 'r', encoding='utf-8-sig') as f:
        st_name = input('Enter students name: ')
        
        reader = list(csv.DictReader(f))
         

        if st_name:
             return [st for st in reader if st['name'].lower() == st_name.lower()] or f'Student with name "{st_name}" not in list'
        return reader


file_content = read(filename)
print(file_content, "\n")


# 3.

def avarage(filename: str):
    with open(filename, mode = 'r', encoding='utf-8-sig') as f:
       reader = csv.DictReader(f)
       data = list(reader)
       subjects = {row['subject_name'] for row in data}
       avgs = {}
       for subject in subjects:
        total = 0
        quantity = 0
        
        for row in data:
            if subject == row['subject_name']:
                total += int(row['mark'])
                quantity += 1
        
        avgs[subject] = round(total/quantity, 2)
    print('\nAvarages:\n')
    for k, v in avgs.items():
       print(f'{k:<15}{v}')

avarage(filename)


# 4.


def update_mark(filename):
    students = []


    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)

    
    student_id = input("Enter student ID: ")
    subject = input("Enter subject: ")
    new_mark = input("Enter new mark: ")

  
    found = False
    for student in students:
        if student["id"] == student_id and student["subject_name"].lower() == subject:
            student["mark"] = new_mark
            found = True
            break

    if found:
      
        with open(filename, "w", newline="") as file:
            fieldnames = ["id", "name", "age", "grade", "subject_name", "mark"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

        print("Mark updated successfully.")
    else:
        print("Student or subject not found.")

update_mark(filename)




# 5.


def add_student(filename, student):
    with open(filename, "a", newline="") as file:
        fieldnames = ["id", "name", "age", "grade", "subject_name", "mark"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow(student)

    print("Student added successfully.")

add_student(filename, new_student)


    
   















