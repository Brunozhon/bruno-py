print("This was one of the products by: ")
print('''
|---------)
|          )
|           )
|            )
|------------|    |---------  |           |  |------------|  |-----------|
|            )    |           |           |  |            |  |           |
|           )     |           |           |  |            |  |           |
|          )      |           |           |  |            |  |           |
|---------)       |           |-----------|  |            |  |-----------|
''')
input("Press enter to start")
money = 100
cals = 300
jobpicked = False;
job = ""
gameover = False;
while gameover != True:
  if job == "":
    job = input("What job do you want to have?")
    if job == "Programmer":
      print("You meet someone: ")
      print('''
    |-----------|
    |           |
    |           |
-----------------------
  |                 |
  |                 |
  |   o         o   |
  |       |         |
  |   ----------    |
  |-----------------|
------------------------
|  |                |  |
|  |                |  |
|  |                |  |
|  |                |  |
|  |                |  |
----                ----
   |                |
   |                |
   |       |        |
   |       |        |
   |       |        |
   |       |        |
   |       |        |
-----------------------
|          |          |
-----------------------
You are well suited for the job. Can I ask you some
questions before we start?
    ''')
      print("He is a boss develpoing a website. Let him ask some questions first.")
      ans = input("Do you know HTML, CSS, and JavaScript?")
      if ans == "Yes":
        print("Great!")
      else:
        print("I'll give you a chance. Visit https://www.w3schools.com and learn from there.")
        ans = input("Now, do you know HTML, CSS, and JavaScript?")
        if ans == "Yes":
          print("Great!")
        else:
          print("The chances are over. Game over.")
          gameover = True;
    elif job == "Carpenter":
      print("You see something:")
      print('''
|--------------------------------|
|                                |
|                                |
|--------------------------------|
      ''')
      ans = input("Do you want to be boss?")
      print("You wait... and wait... and-")
      if ans == "Yes":
        print('You see the boss. You ask him, "Can I be boss?".')
        print('The boss replies, "No.". Game over.')
        gameover = True
      else:
        print("You see the boss. You are hired!")
    else:
      print("Your wanted job {job} was not found (Fork to add more jobs)")
      job = ""
  do = input("What do you want to do?")
  if do == "Do job":
    if job == "Programmer":
      print("You earn 10 money per charecter")
      print("You typed one charecter. + 10 dollars")
      money = money + 10
    elif job == "Carpenter":
      print("You earn 20 money per wood you cut.")
      print("You carved 1 wood. + 20 dollars.")
      money = money + 10
  elif do == "See stats":
    print('''
    Current stats:
    
    Money: {money}
    Job: {job}
    Calories: {cals}
    ''')
  elif do == "Eat":
    food = input("What do you want to eat?")
    if food == "Pizza" and money < 29:
      print("Calories: 50")
      money = money - 30
      cals = cals + 50
    elif food = "Cheeseburger" and money < 9:
      print("Calories: 80")
      money = money - 10
      cals = cals + 80
    else:
      print("Your food {food} was not found (You can fork and add foods)")
  else:
    print("Action {do} was not found (You can fork to add more)")
  
      
  
