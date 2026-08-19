from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


class BaseModel:
    def __init__(self, key):
        self.key = key


    def load_model(self):
        try:
            client= genai.Client(api_key=self.key)
            return client

        except Exception as e:
            print(f"Error loading model: {e}")
            return None


class AppFeatures:
    database = {}
    def __init__(self, model, model_name="gemini-2.5-flash"):
        self.model = model
        self.model_name = model_name
        self.mainMenu()

    def generate_text(self, prompt):
        try:
            response = self.model.models.generate_content(model=self.model_name, contents=prompt)
            return response.text
        except Exception as e:
            # print(f"Error generating text: {e}")
            print("Your api key is invalid or expired. Please check your API key and try again.")
            return None


    def __login(self, email, password):
        # Implement login logic here
        print(f"Logging in with email: {email}")
        # Placeholder for actual login implementation
        return True


    def __signup(self, email, password):
        if email in self.database:
            print("Email already exists. Please log in.")
            return False
        else:
            self.database[email] = password
            print(f"Account created for email: {email}")
            return True



    def mainMenu(self):
       user_input = input("""
        Welcome to the NLP Application!
        
        1. Dont have an account?
        2. Already have an account?
        0. Exit
        """)

       if user_input == "1":
           response = self.__signup(input("Enter your email: "), input("Enter your password: "))
           if response==True:
                self.secondMenu()

           # Add sign-up logic here
       elif user_input == "2":
           input_email = input("Enter your email: ")
           input_password = input("Enter your password: ")
           response =self.__login(input_email, input_password)
           if response==True:
                self.secondMenu()
           else:
               print("Login failed. Please check your credentials.")

           # Add login logic here
       elif user_input == "0":
           print("Exiting the application. Goodbye!")
           exit()
       else:
           print("Invalid input. Please try again.")
           self.mainMenu()



    def secondMenu(self):
        user_input = input("""
        Welcome to the NLP Application!
        
        1. Check sentiment of a text
        2. Translate text to another language
        3. Generate text based on a prompt
        0. Exit
        """)

        if user_input == "1":
            prompt = input("Enter your prompt: ")
            generated_text = self.generate_text(f"system: Check the sentiment of the following text: {prompt}")
            if generated_text:
                print(generated_text)
            else:
                print("Failed to generate text.")
            self.secondMenu()

        elif user_input == "2":
            prompt = input("Enter your prompt: ")
            generated_text = self.generate_text(f"system: Translate the following text to another language: {prompt}")
            if generated_text:
                print(generated_text)
            else:
                print("Failed to generate text.")
            self.secondMenu()

        elif user_input == "3":
            prompt = input("Enter your prompt: ")
            generated_text = self.generate_text(f"system: Generate text based on the following prompt: {prompt}")
            if generated_text:
                print(generated_text)
            else:
                print("Failed to generate text.")
            self.secondMenu()
        elif user_input == "0":
            print("Exiting the application. Goodbye!")
            exit()
        else:
            print("Invalid input. Please try again.")
            self.secondMenu()
       



client = BaseModel(key=os.getenv("GEMINI_API_KEY"))
model = client.load_model()
app_features = AppFeatures(model=model, model_name="gemini-2.5-flash")