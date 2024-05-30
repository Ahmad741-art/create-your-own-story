import random

def get_user_inputs():
    print("Welcome to the Personalized Story Generator!")
    name = input("Enter your name: ")
    favorite_color = input("Enter your favorite color: ")
    favorite_animal = input("Enter your favorite animal: ")
    dream_job = input("Enter your dream job: ")
    city = input("Enter a city you like: ")
    return name, favorite_color, favorite_animal, dream_job, city

def generate_story(name, favorite_color, favorite_animal, dream_job, city):
    story_templates = [
        f"Once upon a time in the vibrant city of {city}, there lived a young adventurer named {name}. Every morning, {name} would don their {favorite_color} outfit and set out to explore the city with their loyal {favorite_animal}. Together, they dreamed of becoming the best {dream_job} in the world.",
        f"In the bustling streets of {city}, {name} could always be found wearing something {favorite_color}. {name} had a unique bond with a {favorite_animal}, and they both shared a passion for {dream_job}. Their adventures together were the talk of the town.",
        f"Far away in the enchanting city of {city}, {name} and their {favorite_color} {favorite_animal} were inseparable. {name} aspired to be a renowned {dream_job}, and with the support of their {favorite_animal}, they knew no dream was too big to chase."
    ]
    return random.choice(story_templates)

def main():
    name, favorite_color, favorite_animal, dream_job, city = get_user_inputs()
    story = generate_story(name, favorite_color, favorite_animal, dream_job, city)
    print("\nHere is your personalized story:\n")
    print(story)

if __name__ == "__main__":
    main()
