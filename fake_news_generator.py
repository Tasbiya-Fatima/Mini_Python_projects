import random

sub =[
    "Sharukh khan",
    "Virat Kholi",
    "Sarojni Naidu",
    "Kalpana Chawla",
    "Crowd of Monkeys",
    "Rikshaw Driver",
    "Narendra Modi ji"
]

actions =[
    "launches",
    "cancels",
    "dance with",
    "eats",
    "decleras",
    "order",
    "celebrates"
]

place_or_thing =[
    "at red fort",
    "in Mumbai local train",
    "inside parlement",
    "at Ganga ghat",
    "at india gate",
    "near gateway of India"
]

while True:
    subject =random.choice(sub)
    action =random.choice(actions)
    thing = random.choice(place_or_thing)

    headline = f"BREAKING NEWS: {subject} {action} {thing}"
    print("\n",headline)

    user_input=input("Do you want another headline(yes/no)").strip()
    if user_input == "no":
        break
print("Thanks for using Fake News generator .Have fun day!")