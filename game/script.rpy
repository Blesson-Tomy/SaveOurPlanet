# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene new

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Sarah happy

    # These display lines of dialogue.


    ###Scene 1:Bedroom

    ###Sarah yawns in the morning
    # Sarah wakes up in the morning with a yawning face.
    "YAWN!"
    "It's a beautiful day!"
    "Time to get ready for school"
    #Should I switch off the lights now or later?
        #Option: Now vs later
    "Should I switch off the lights now or later?"

    show Sarah happy at left

    menu:
        "Switch Off Now":
            "I will switch off the lights now."
        "Switch Off Later":
            "I will switch off the lights later."
    ###darker room image
    show Sarah happy
    #Sarah goes to the washroom
    "I should brush my teeth"
    #Sarah brushes her teeth (Sound)
    "Should I turn off the tap now or later?"
    show Sarah at left
    menu:
        "Turn Off Now":
            "I will turn off the tap now."
            ###Tap off tap on image
        "Turn Off Later":
            "I will turn off the tap later."

    ###Scene 2: Washroom
        #Option:turn off tap now or later (insert SDG for each of them)
    ###Tap off tap on image
    #COmmute
    "I should get ready to leave school"
    ###Outside, an image while Sarah decides to commute
    #Sarah has to choose a ride - menu
    "Should I take the bus, bike, walk or car?"
    menu:
        "Bus":
            "Let's take the bus today."
        "Bike":
            "Let's ride my bike."
        "Walk":
            "I think I will walk to school today."
        "Car":
            "I will ask my mom to drop me to school."

    #Sarah  has 1) cuar 2) bike 3) bus 4) walk
    ###Sarah on a bike image
    ###Sarah on a bus image
    ###Sarah walking image
    ###Sarah in a car image
    #Sarah reaches school
    ###`Outside School image
    ###trash image
    "Oh, there is alot of trash around here, what should I do"
    menu:
        "Pick up the trash":
            "I will pick up the trash now."
        "Leave the trash":
            "I think I should leave the trash."

    #Should I pick up the trash? - insert data
    ###Sarah picking up trash image
    ###Sarah recycling the trash image
    #after reaching the school
    "Good Morning Teacher!"
    #talk about climate action (data, ppt slides)
    ###Miss teaching about Climate Action image
    #Sarah buying a juice, can I have a recycled straw please?
    "I think I should do my part in saving the environment."
    "Can I have a recycled straw please?"
    ###Sarah buying juice image
    ###Sarah with a recycled straw image
    ###Sarah going back home image
    "Time to go back home!"
    #reflection on the way back home (insert data) - SDG Goals met today
    ###Sarah reflection image - (SDG Goals met today Slide)
    #sleep peacefully 
    ###Sarah sleeping image
    "check"

return