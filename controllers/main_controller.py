from flask import render_template, redirect, url_for, request

class mainAppController():
    
    
    @staticmethod
    def home():
        return render_template('index.html')


    @staticmethod
    def sign_in():
        if request.method == 'POST':
            return redirect(url_for('chat'))
        return render_template('login.html')
    
    @staticmethod
    def sign_up():
        if request.method == 'POST':
            return redirect(url_for('chat'))
        return render_template('signup.html')        
    
    @staticmethod
    def chat():
        return render_template('chat.html')
    
    @staticmethod
    def logout():
        return redirect(url_for('sign_in'))
    
    @staticmethod
    def profile():
        return render_template('profile.html')
