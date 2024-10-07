define e = Character(None, image="eileen", kind=bubble) # Eileen

label start:
    scene waking
    play music "beautifulday.mp3" noloop
    
    "YAWN!
    It's a beautiful day!"
    e "Uh oh, I better get ready for school!"
    
    scene lighton

    play music "switchofflights?.mp3" noloop
    e "Should I switch off my room lights now or later?"

    
    menu:
        "Switch Off Now":
            play music "electricity.mp3" noloop
            "I should switch off the lights now to save electricity."
            scene dark

        "Switch Off Later":
            play music "switchofflightslater.mp3" noloop
            "I will switch off the lights later."
            scene lighton
   
   
    scene brushing
   
    #Sarah brushes her teeth (Sound)
    play music "water.mp3" noloop
    e "I wonder if I turn off the tap now or later? Should I be more mindful of my water usage?"
    
    
    menu:
        "Turn Off Now":
            play music "offtapnow.mp3" noloop
            "I will turn off the tap now."
            scene tapoff
            
        "Turn Off Later":
            "I will turn off the tap later."
            scene tapoff
        

    scene reflecting
    play music "bus?.mp3" noloop
    e "Hmm, Should I take the bus, bike, walk or car?"
    menu:
        "Bus":
            scene bus
            play music "buso.mp3" noloop
            e "I'm going with the eco-friendly bus option today!."
            
        "Bike":
            scene bicycle
            e "I think riding my bicycle to school today is a green idea."
            
        "Walk":
            scene walking
            e "I think I will walk to school today."
            
        "Car":
            scene car
            e "I will take the car today."
            
    #Sarah reaches school
    ###`Outside School image
    ###trash image
    scene school
    "Finally, I reached school!"

    scene reflecting
    play music "oh.mp3" noloop
    "Oh, there is alot of trash around here, what should I do?"
    menu:
        "Pick up the trash":
            scene pickuptrash
            play music "trash?.mp3" noloop
            "Hmm, I should pick up the trash and help keep the environment clean and green."
            
        "Leave the trash":
            "I think I should leave the trash."

   
    play music "na.mp3" noloop
    scene nasa

    scene file
    play music "teacher.mp3" noloop
    '''Good morning, everyone! Today, were diving into a topic thats not just important for our generation but for the entire planet—climate change. Weve talked about its causes, but now lets focus on what we can do as high schoolers to make a real difference.
    Lets start with recycling. Its a great way to reduce waste in landfills and save energy. But theres so much more we can do beyond recycling. We need to think about reducing our carbon footprint, which means lowering the amount of greenhouse gases we produce. Transportation is a major contributor, so if you can, walk, bike, or use public transportation. Carpooling is also a great option for those who live nearby.
    Every action counts, and as students, you have a powerful voice. Dont underestimate the impact you can make, both individually and collectively. Climate change is a huge challenge, but together, we can tackle it! I encourage you to think about one change you can make this week. Lets meet back and share our ideas. Have a great day, everyone!'''
    stop music
    scene reflecting
    scene strawjuice
    e "It is so hot, I need a drink!"

    "I think I should do my part in saving the environment."
    e " Maybe I should ask for a recycled straw."
    "Can I have a recycled straw please?"
    scene straw
    e "Thank you!"
    "Finally a break from the heat"

    e "Let's go back home now."
    scene summary
    play music "great.mp3" noloop
    "Today was a great day learning about how I can play a part in saving the environment!"

return