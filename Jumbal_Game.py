import random as rd

class JumbleGame():

    words = ['cricket', 'computer', 'science', 'programming',
        'confidence', 'player', 'condition', 'letter',
        'water', 'congratulation ', 'green']

    def __init__(self):
        self.name = input("Enter your good name: ")
        self.score = 0
        self.turn = 1
        # self.user =input("do you want to play game ( Yes or No): ")

    def make_jumble(self):
        self.pick = rd.choice(self.words)
        self.jumble_word = rd.sample(self.pick, len(self.pick))
        self.jumbled = "".join(self.jumble_word)
        return self.jumbled

    # def player_input(self):
    #     print(f"{self.count} Guess the word: {self.jumbled}\n")
    #     self.user_input = input ("Enter your Guess: ")

    def player_input(self):
        jumbled = self.make_jumble()
        print(f"{self.turn} Guess the word: {jumbled}\n")
        # user_input = self.user_input
        user_input = input ("Enter your Guess: ")
        return user_input

    def check_ans(self):
        user_input = self.player_input()
        if self.pick == user_input :
            self.score += 1
            print(f"correct answer {self.score} ")
        else:
            print("wrong answer")
        self.turn += 1 

    def game_result(self):
        print(f"Game Over !! \n Your Score is : {self.score} ")
        if self.score==10:
            print("Excellent")
        elif self.score<=9 and self.score>=8:
            print("wonderfull")
        elif self.score==7:
            print("good")
        else:
            print("keep it up ")

    def game_jumble_word(self):
        while self.turn < 11 :
            self.check_ans()
        self.game_result()
        
        play_again = input("Do you want to play again?(press Y / N): ") 
        if play_again == "Y" or play_again == "y":
            self.turn = 1
            self.score = 0
            self.game_jumble_word()

play = JumbleGame()
play.game_jumble_word()
