import sqlite3


def setup_database_and_import_data():
    obje = sqlite3.connect('combined_data.db')
    cursor = obje.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS individuals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            UNIQUE(first_name, last_name)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS performance (
            task_number INTEGER,
            points INTEGER,
            person_id INTEGER,
            FOREIGN KEY (person_id) REFERENCES individuals (id),
            UNIQUE(task_number, person_id)
        )
    ''')

    with open('score2.txt', 'r') as file:
        for line in file:
            data = line.split()
            task_number = int(data[1])
            first_name = data[2]
            last_name = data[3]
            points = int(data[4])

            cursor.execute(
                'INSERT OR IGNORE INTO individuals (first_name, last_name) VALUES (?, ?)', (first_name, last_name))

            cursor.execute(
                'SELECT id FROM individuals WHERE first_name = ? AND last_name = ?', (first_name, last_name))
            person_id = cursor.fetchone()[0]

            cursor.execute('INSERT OR IGNORE INTO performance (task_number, points, person_id) VALUES (?, ?, ?)',
                           (task_number, points, person_id))

    obje.commit()
    obje.close()


def display_individuals():
    conn = sqlite3.connect('combined_data.db')
    cursor = conn.cursor()
    for record in cursor.execute('SELECT * FROM individuals ORDER BY id'):
        print(record)
    conn.close()


def display_performance():
    conn = sqlite3.connect('combined_data.db')
    cursor = conn.cursor()
    for record in cursor.execute('SELECT * FROM performance ORDER BY task_number'):
        print(record)
    conn.close()


def top_performers():
    obj2 = sqlite3.connect('combined_data.db')
    cursor = obj2.cursor()

    query = '''
        SELECT individuals.first_name, individuals.last_name, SUM(performance.points) as total_points
        FROM individuals
        JOIN performance ON individuals.id = performance.person_id
        GROUP BY individuals.id
        ORDER BY total_points DESC
        LIMIT 10
    '''

    cursor.execute(query)
    result = cursor.fetchall()
    print("\nTop 10 Individuals with Highest Total Points:")
    print("----------------------------------------")

    for One in result:
        print(f"{One[0]} {One[1]} --=======>> Total Points: {One[2]}")

    obj2.close()


def top_difficult_tasks():
    obj3 = sqlite3.connect('combined_data.db')
    cursor = obj3.cursor()

    query = '''
        SELECT task_number, SUM(points) as total_points
        FROM performance
        GROUP BY task_number
        ORDER BY total_points ASC
        LIMIT 10
    '''

    cursor.execute(query)
    resutatet = cursor.fetchall()
    print("\nTop 10 Most Difficult Tasks:")
    print("-------------------------------------------")

    for One in resutatet:
        print(f"----- {One[0]} --=====>>>> Total Points: {One[1]}")

    obj3.close()
    print("-------------------------------------------\n")


if __name__ == "__main__":

    setup_database_and_import_data()

    top_performers()
    top_difficult_tasks()

    user_input = input("Do you want to see the tables? (yes/no): ").lower()

    if user_input == 'yes':
        print("\nIndividuals Table:")
        display_individuals()
        print("\nPerformance Table:")
        display_performance()
