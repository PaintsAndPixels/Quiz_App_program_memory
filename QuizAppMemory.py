import random

class QuizApp:
    def __init__(self):
        # Pool of 20 questions
        self.questions_pool = [
            {"question": "What is the capital of India?", 
             "options": ["Mumbai", "Delhi", "Bangalore", "Kolkata"], 
             "answer": "Delhi"},
            {"question": "Who wrote the National Anthem of India?", 
             "options": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Mahatma Gandhi"], 
             "answer": "Rabindranath Tagore"},
            {"question": "What is the largest planet in our Solar System?", 
             "options": ["Earth", "Jupiter", "Saturn", "Mars"], 
             "answer": "Jupiter"},
            {"question": "Which programming language is known as the 'language of AI'?", 
             "options": ["Python", "Java", "C++", "Prolog"], 
             "answer": "Prolog"},
            {"question": "Which is the longest river in the world?", 
             "options": ["Amazon", "Nile", "Yangtze", "Ganges"], 
             "answer": "Nile"},
            {"question": "What is the chemical symbol for water?", 
             "options": ["H2O", "O2", "CO2", "HO"], 
             "answer": "H2O"},
            {"question": "Who painted the Mona Lisa?", 
             "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Vincent van Gogh"], 
             "answer": "Leonardo da Vinci"},
            {"question": "What is the smallest continent by land area?", 
             "options": ["Australia", "Europe", "Antarctica", "South America"], 
             "answer": "Australia"},
            {"question": "Which gas do plants primarily use for photosynthesis?", 
             "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], 
             "answer": "Carbon Dioxide"},
            {"question": "What is the speed of light?", 
             "options": ["300,000 km/s", "150,000 km/s", "1,000 km/s", "500,000 km/s"], 
             "answer": "300,000 km/s"},
            {"question": "What is the hardest natural substance on Earth?", 
             "options": ["Gold", "Iron", "Diamond", "Platinum"], 
             "answer": "Diamond"},
            {"question": "What is the square root of 64?", 
             "options": ["6", "7", "8", "9"], 
             "answer": "8"},
            {"question": "Who is known as the Father of Computers?", 
             "options": ["Charles Babbage", "Alan Turing", "Ada Lovelace", "John von Neumann"], 
             "answer": "Charles Babbage"},
            {"question": "What is the capital of France?", 
             "options": ["Rome", "Paris", "Berlin", "Madrid"], 
             "answer": "Paris"},
            {"question": "Which ocean is the largest?", 
             "options": ["Atlantic", "Indian", "Arctic", "Pacific"], 
             "answer": "Pacific"},
            {"question": "Which country is known as the Land of the Rising Sun?", 
             "options": ["China", "Japan", "Thailand", "South Korea"], 
             "answer": "Japan"},
            {"question": "What is the boiling point of water at sea level?", 
             "options": ["100°C", "90°C", "110°C", "120°C"], 
             "answer": "100°C"},
            {"question": "Who discovered penicillin?", 
             "options": ["Alexander Fleming", "Marie Curie", "Isaac Newton", "Louis Pasteur"], 
             "answer": "Alexander Fleming"},
            {"question": "Which planet is known as the Red Planet?", 
             "options": ["Venus", "Mars", "Jupiter", "Saturn"], 
             "answer": "Mars"},
            {"question": "What is the largest mammal on Earth?", 
             "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 
             "answer": "Blue Whale"}
        ]
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Quiz App!")
        print("You will be asked 5 random questions. Good luck!\n")

        # Select 5 random questions
        selected_questions = random.sample(self.questions_pool, 5)

        for i, q in enumerate(selected_questions, 1):
            # Shuffle options
            options = q["options"]
            random.shuffle(options)

            print(f"Question {i}: {q['question']}")
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            # Get user input
            try:
                user_answer = int(input("Enter the option number (1-4): "))
                if options[user_answer - 1] == q["answer"]:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is: {q['answer']}\n")
            except (ValueError, IndexError):
                print(f"Invalid input! The correct answer is: {q['answer']}\n")

        # Display final score
        print(f"Quiz Over! Your final score is: {self.score}/5")
        if self.score == 5:
            print("Excellent!")
        elif self.score >= 3:
            print("Good job!")
        else:
            print("Better luck next time!")


# Run the quiz app
if __name__ == "__main__":
    quiz = QuizApp()
    quiz.start_quiz()
    
    