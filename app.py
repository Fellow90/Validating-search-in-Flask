from flask import Flask, request, render_template

app = Flask(__name__)

fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries', 'Blueberries', 'Raspberries', 'Blackberries', 'Pineapple', 'Mangoes', 'Papayas', 'Kiwifruit', 'Watermelon', 'Cantaloupe', 'Honeydew', 'Pomegranate', 'Guava', 'Passionfruit', 'Starfruit', 'Dragonfruit', 'Peach', 'Plum', 'Cherry', 'Grapefruit', 'Lemon']

@app.route('/')
def index():
    return render_template('form.html', fruits=fruits)

@app.route('/', methods=['POST'])
def search():
    fruit = request.form['fruit']

    if fruit in fruits:
        message = "Congratulations"
    else:
        message = "Sorry Unlucky"

    return render_template('form.html', fruits=fruits, message=message)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
