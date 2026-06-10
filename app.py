from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        numbers = request.form['numbers']
        target = request.form['target']

        num_list = [int(x.strip()) for x in numbers.split(',')]
        target = int(target)

        start = time.perf_counter()
        found_list = target in num_list
        list_time = time.perf_counter() - start

        num_set = set(num_list)

        start = time.perf_counter()
        found_set = target in num_set
        set_time = time.perf_counter() - start

        result = {
            "found_list": found_list,
            "found_set": found_set,
            "list_time": list_time,
            "set_time": set_time
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)