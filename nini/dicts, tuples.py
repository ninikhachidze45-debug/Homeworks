# profile = {'name' : 'nini', 'age' : '20', 'country' : 'gerogia'}
# # print(profile)
# # print(len(profile))
# print(profile['age'])
# # profile['name'] = 'khachidze'
# # print(profile)
# profile['city'] = 'tbilisi'
# # print(profile)
# # del profile['age']
# # print(profile)
# # print('name' in profile)
# for key in profile:
#     value = 3



# data = {'id': 11, 'Name': 'nini', 'age': 20, 'grade': 'c'}

# print(data['id'])

# data['grade'] = 'b'
# print(data)

# data['subject'] = 'python'
# # print(data)

# data.pop('age')
# # print(data)

# del data['id']
# print(data)


# users_key = input('enter key: ')
# if users_key in data:
#     print(data[users_key])
# else:
#     print('key not found')
    
# marks = {
#     "Math": 95,
#     "English": 88,
#     "Physics": 91,
#     "History": 76
# }

# avarage = 0
# for mark in marks:
#     avarage += marks[mark] 

# avarage = avarage / len(marks)
# print(avarage)


# print(max(marks.values()))
# print(min(marks.values()))


# name = input('enter name: ')
# age = input('enter age: ')
# city = input('enter city: ')

# user = {'name': name, 'age': age, 'city': city}

# for key in user:
#     print(f'{key}: {user[key]}')


students = {
    1: {"name": "Nini", "mark": 95},
    2: {"name": "Luka", "mark": 88},
    3: {"name": "Ana", "mark": 91}
}

# id = int(input('Enter student id: '))
# if id in students:
#     student = students[id]
#     for i in student:
#         print(f'{i}: {student[i]}')
# else:
#     print('id not found')


# id = int(input('Enter student id: '))
# if id in students:
#     mark = int(input('enter mark: '))
#     students[id]['mark'] = mark
#     print(students)
# else:
#     print('id not found')


id = int(input('Enter student id: '))
name =input('enter name: ')
mark = int(input('enter mark: '))
new = {'name': name, 'mark': mark}
students[id] = new



for i in students:
    for x in i:
        students[i] = f'{x}: {i[x]}'
    print(f'{i}: {students[i]}')
    
