from flask import Flask,jsonify
todo=Flask('__name__')

students= [
    {
        'id':1,
        'name':'AAA',
        'age':22,
    },
    {
        'id':2,
        'name':'BBB',
        'age':22,
    },
    {
        'id':3,
        'name':'ccc',
        'age':20,
    },
]

@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_students_by_id(id):
    print(id)

    for student in students:
        if student['id']== id:
         return jsonify(student)
    print(student)


    return jsonify('not found')

if __name__ == '__main__':
    todo.run(
        debug=True
    )
