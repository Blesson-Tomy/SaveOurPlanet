define e = Character(None, image="eileen", kind=bubble) # Eileen

label start:
    scene waking
    play music "beautifulday.mp3" noloop
    
    "YAWN!
    It's a beautiful day!"
    e "Uh oh, I better get ready for school!"
    
    scene lighton
    e "Should I switch off my room lights now or later?"

    
    menu:
        "Switch Off Now":
            "I will switch off the lights now."
            scene dark

        "Switch Off Later":
            "I will switch off the lights later."
            scene lighton
   
    scene brushing
    "I should brush my teeth"
    play music "brush.mp3" noloop

    #Sarah brushes her teeth (Sound)
    e "Should I turn off the tap now or later?"
    
    menu:
        "Turn Off Now":
            "I will turn off the tap now."
            scene tapoff
            
            
        "Turn Off Later":
            scene tapoff
            "I will turn off the tap later."

    
    "I should get ready to leave school"
    "Should I take the bus, bike, walk or car?"
    menu:
        "Bus":
            scene bus
            "Let's take the bus today."
            
        "Bike":
            scene bicycle
            "Let's ride my bike."
            
        "Walk":
            scene walking
            "I think I will walk to school today."
            
        "Car":
            scene car
            "I will take the car today."
            
    #Sarah reaches school
    ###`Outside School image
    ###trash image
    scene school
    "Finally, I reached school!"

    scene reflecting
    "Oh, there is alot of trash around here, what should I do"
    menu:
        "Pick up the trash":
            scene pickuptrash
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
    scene reflecting
    "I think I should do my part in saving the environment."
    e "I should ask for a recycled straw."
    "Can I have a recycled straw please?"
    ###Sarah buying juice image
    ###Sarah with a recycled straw image
    ###Sarah going back home image
    "Time to go back home!"
    #reflection on the way back home (insert data) - SDG Goals met today
    ###Sarah reflection image - (SDG Goals met today Slide)
    #sleep peacefully 
    ###Sarah sleeping image

return