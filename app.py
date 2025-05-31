from flask import Flask, render_template, request, redirect
from config import Config
from google import genai
import sqlite3
import datetime
import requests

app = Flask(__name__)
app.config.from_object(Config)

def insert_user(username):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO users (username, timestamp) VALUES (?, ?)', (username, timestamp))
    conn.commit()
    c.close()
    conn.close()

def get_users():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    c.close()
    conn.close()
    return users

def clear_users_db():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('DELETE FROM users')
    conn.commit()
    c.close()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            insert_user(username)
        else:
            return redirect('/')
    return render_template('main.html')

@app.route('/database', methods=['GET', 'POST'])
def database():
    users = get_users()
    return render_template('database.html', users=users)

@app.route('/paynow', methods=['GET', 'POST'])
def paynow():
    return render_template('paynow.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template('prediction.html')

@app.route('/predicted_price', methods=['GET', 'POST'])
def predicted_price():
    usd_sgd_input = request.form.get('usd_sgd')
    
    # Check if input is empty or None
    if not usd_sgd_input or usd_sgd_input.strip() == '':
        return render_template('prediction.html', error="Please enter a valid USD/SGD exchange rate.")
    
    try:
        usd_sgd = float(usd_sgd_input)
        prediction = 90.23 + (-50.6*usd_sgd)
        return render_template('prediction.html', prediction=f"{prediction:.2f}")
    except ValueError:
        return render_template('prediction.html', error="Please enter a valid number for USD/SGD exchange rate.")

@app.route('/clear_users', methods=['GET', 'POST'])
def clear_users():
    clear_users_db()
    return redirect('/database')

def get_gemini_response(prompt):
    try:
        client = genai.Client(api_key=Config.GEMINI_API_KEY)
        model = 'gemini-2.0-flash'
        response = client.models.generate_content(
            model=model, contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: Unable to get response from Gemini AI. {str(e)}"

@app.route('/gemini/', methods=['GET', 'POST'])
def gemini():
    return render_template('gemini.html')

@app.route('/gemini_reply/', methods=['GET', 'POST'])
def gemini_reply():
    prompt = request.form.get('prompt')
    if not prompt or prompt.strip() == '':
        return render_template('gemini.html', error="Please enter a prompt.")
    gemini_response = get_gemini_response(prompt)
    return render_template('gemini_reply.html', gemini_response=gemini_response)


telegram_api_key = Config.TELEGRAM_API_KEY
base_url = f'https://api.telegram.org/bot{telegram_api_key}/'


@app.route('/start_telegram', methods=['GET', 'POST'])
def start_telegram_bot():
    domain_url = Config.TELEGRAM_DOMAIN_URL
    response = requests.post(base_url + 'setWebhook', json={'url': domain_url})
    if response.status_code == 200:
        return render_template('start_telegram.html')
    return render_template('start_telegram.html', error="Failed to start telegram bot. Please check the logs for more details.")

@app.route('/stop_telegram', methods=['GET', 'POST'])
def stop_telegram_bot():
    response = requests.get(base_url + 'deleteWebhook')
    if response.status_code == 200:
        return render_template('stop_telegram.html')
    return render_template('stop_telegram.html', error="Failed to stop telegram bot. Please check the logs for more details.")

if __name__ == "__main__":
    app.run(debug=True)