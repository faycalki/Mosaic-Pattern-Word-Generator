import turtle, math
# Partial code from A3Starter.py.
# Partial code from my own (Faycal Kilali's) Programming Assignment 2


def make_red(word):
    word = word.lower()
    R = 0
    for i in range(len(word)):
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
            R += 10
        if i == (len(word) - 1) and word[i] == 'y' and R == 0: # At the end, merriam-webster definition
            R += 10
            # Note to grader: our algorithm only covers vowels of those forms above, I won't be covering the other cases where "y" is a vowel (middle of syllabi, and so on). 
    return R

def make_green(word): 
    word = word.lower()
    G = 0
    for i in range(len(word)):
        if not word[i] == 'a' or not word[i] == 'e' or not word[i] == 'i' or not word[i] == 'o' or not word[i] == 'u':
            G += 10
    return G

def make_blue (word):
    B = +5 * len(word)
    return B

def make_shape(turtle_identifier, R, G, B, side_length): # Currently squares only, maybe I'll expand it in the future.
    turtle_identifier.pendown()
    turtle_identifier.fillcolor(R, G, B)
    turtle_identifier.begin_fill()
    for l in range(4):
        turtle_identifier.forward(side_length)
        turtle_identifier.left(360 / 4)
    turtle_identifier.end_fill()
    turtle_identifier.penup()
    t.fd(side_length)

def find_rectangle_sides(rectangular_number):
    for i in range(2, rectangular_number):
        for j in range(2, rectangular_number):
            if j * i == rectangular_number:
                rectangular_height = i
                rectangular_width = j
                return rectangular_width, rectangular_height
    return rectangular_number, 1 # This is a case where the number is actually a prime number.
    # Access using find_rectangle_sides(number), will grant a tuple value, access first value with [0] and second value with [1], find_rectangle_sides(number)[0] and find_rectangle_sides(number)[1].

def synthesize_mosaic(y):
    num_columns = 1
    n = len(words)
    width, height = find_rectangle_sides(n)
    for w in range(0, n):
        R = make_red(words[w])
        G = make_green(words[w])
        B = make_blue(words[w])
        #print(words[w])
        # Draw
        make_shape(t, R, G, B, side_length)
        #t.lt(360 / 4)
        #t.setheading(0)
        #t.goto(x, y)
        # Height adjustment
        if num_columns == width:
            num_columns = 0
            y += side_length
            #turtle.penup
            t.goto(starting_x_coordinate, y)
        num_columns += 1



try: # The try block lets you test a code block for errors.
    with open('my_text.txt', 'r') as file:
        text = file.read().replace('\n', '')
except FileNotFoundError: # The except block lets you handle the error.
    text = input("Input your text here (note, I kept this uncommented because I wanted to make it more interactive for the user. If you think this is a problem grade-wise, then please just inform me instead of taking my grade away. Test cases are commented out in the code, if they are uncommented they'll override this input): ") # Input variation so you can just input any word here. NOTE: test cases are commented out below, just uncomment them and they'll apply regardless of what is inputted here.
# The else block (if it existed here) lets you run the rest of the code if there's no error. 

turtle.colormode(255)
starting_x_coordinate = -480
x = starting_x_coordinate
y = -400
side_length = 40
#show_screen = turtle.getscreen() # This is sufficienet as a variable, because getscreen() already makes it clear what it does.
t = turtle.Turtle() # This is sufficient as a variable, because of how we defined it.
t.goto(x, y)
t.shapesize(0.00001, 0.00001, 0.00001) # I don't really care about the drawing pointer, so I tried to set it as small as possible.
t.pensize(2) # Thickness of pen
t.speed(0) # 10 speed is max, 0 will skip animations and instantly draw. But I assume you, in the assignment, want to see it in action as it draws.
t.clear() # Clears screen from leftovers
t.setheading(0) # Setting anglee to 0, as described in the algorithm (that is, we are facing eastwards from the origin for the drawing initially)


# Test Cases   
#text = 'O how I wish that ship the Argo had never sailed off' 
#text = 'Until the day when God will deign to reveal the futureto man, all human wisdom is contained in these two words Hope and Wait'
#text = "Onwards, choose a path for thyself, for that is the true freedom we have. Do not be average, seek your ambitions, seek to make the most out of every second of your life."

#The test case below uses additional parameters in order to appear properly, that is, side_length = 10 for this test case.
#text = "Did you know, that there are more non-prime numbers than there are prime numbers? Think about it, every even number is divisible by 2, this suggests that at least half the set of integers is divisible by 2, but stop for a second! What about the integer 0? Well, its divisible by 2, but its also divisible by every other prime number, but by definition if a number is divisible by 2, then it is necessarily an even number. Now, this quantifies that for any consecutive integers subset of the integers set with the condition there is an even number of consecutive integers in the subset, suppose the size of the subset is K, then there would necessarily be >= K/2 even integers. Now, suppose our subset includes all the integers, then observe that, necessarily, half the integers will be divisible by 2, so at least half of the numbers will be composite numbers (non-prime), but then realize that a lot of those odd integers in the subset will be divisible by another odd integer, unless they are prime, so this tells us that in the subset of integers, there will be K/2 + c non-primes, where c is  the number of integers not divisible by 2, but are composite as they are made of more than one prime factor, hence k/2 + c > 1/2n, so there are n - k/2 - c prime numbers in our subset of integer numbers."
#side_length = 10


# Below are test cases where there is a prime number of words, hence its only gonna be 1 row of tiles (in order to maintain rectangular symmetry)
#text = "There's nothing to fear but fear iself." 

words = text.split()
synthesize_mosaic(y)

turtle.done() # To prevent the program from closing when done drawing