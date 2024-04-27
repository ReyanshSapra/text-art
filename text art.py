from pyfiglet import Figlet

fig = Figlet(font='slant')

x = fig.renderText("WELCOME TO TEXT ART GENERATOR!")
print(x)

while True:
    def generate_text_art(text):

        text_art = fig.renderText(text)
        print(text_art)

    def main():
        user_input = input("Enter text to convert to text art: ")
        generate_text_art(user_input)

    if __name__ == "__main__":
        main()
