from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            task_name = request.form.get('task')
            tasks.append(task_name)
        elif action == 'delete':
            task_index = int(request.form.get('task_index'))
            tasks.pop(task_index)
        elif action == 'check_all':
            for i in range(len(tasks)):
                if not tasks[i].endswith('✓'):
                    tasks[i] += '✓'
        elif action == "delete_checked":
            checked_indices = request.form.getlist('task_index')
            checked_indices = [int(i) for i in checked_indices]
            checked_indices.sort(reverse=True)
            for i in checked_indices:
                if tasks[i].endswith('✓'):
                    tasks.pop(i)
                else:
                    del tasks[i]

    # Create a list of tuples where the first element is the task and the second element is its checked status
    task_status_pairs = [(task, task.endswith('✓')) for task in tasks]

    return render_template('index.html', task_status_pairs=task_status_pairs)
  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)


