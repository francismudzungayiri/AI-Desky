from email import message
from flask import render_template, redirect, url_for, request
from ai_agents.challenge_agent import Challenge
from flask import jsonify
from models.task import Task



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
            query_data = agent.extract_info_with_llm(message)  
            task = Task()
            task.query_Posting(query_data)
            
            # For AJAX requests, return JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Process message and generate response
                response = f"Details waiting to be send \n {query_data}"  # Replace with actual processing
                return jsonify({'response': response})
            
        return render_template('chat.html')
    
    @staticmethod
    def logout():
        return redirect(url_for('sign_in'))
    
    @staticmethod
    def profile():
        return render_template('profile.html')
