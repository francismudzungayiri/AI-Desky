from email import message
from flask import render_template, redirect, url_for, request
from ai_agents.challenge_agent import Challenge

class mainAppController():
    
    
    @staticmethod
    def home():
        return render_template('index.html')


    @staticmethod
    def sign_in():
        if request.method == 'POST':
            #email = request.form.get()
            #password = request.form.get()
            return redirect(url_for('chat'))
        return render_template('login.html')
    
    @staticmethod
    def sign_up():
        if request.method == 'POST':
            return redirect(url_for('chat'))
        return render_template('signup.html')        
    
    @staticmethod
    def chat():
        if request.method == "POST":
            message = request.form.get('message')
            print(message)
            
            agent = Challenge()
            response = agent.extract_info_with_llm(message)  
            print(response)
            
            # For AJAX requests, return JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Process message and generate response
                response = "This is a response from the server"  # Replace with actual processing
                return jsonify({'response': response})
            
        return render_template('chat.html')
    
    @staticmethod
    def logout():
        return redirect(url_for('sign_in'))
    
    @staticmethod
    def profile():
        return render_template('profile.html')
