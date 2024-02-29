from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'New York, NY',
        'salary': '24k dollars'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Tokyo, Japan',
        'salary': '24k dollars'
    },
    {
        'id': 3,
        'title': 'UX/UI Designer',
        'location': 'Tunis, Tunisia',
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

if __name__ == "__main__":
    app.run(debug=True)
