# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
    global counter
    counter += 1

# Define event handler functions
def tick():
    increment()
    print(counter)

def buttonpress():
    global counter
    counter = 0


# Create a frame
frame = simplegui.create_frame("Well Done",1000,1000)
frame.add_button("Click",buttonpress)

# Register event handlers
timer = simplegui.create_timer(500,tick)


# Start frame and timers
frame.start()
timer.start()
