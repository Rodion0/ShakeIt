import pyautogui as pt
import time as ti
import random
# Test time is currently 1 min in seconds
computer_sleep_time = 60
old_x, old_y = pt.position()
while True:
    new_x, new_y = pt.position()
    random_coord_x = random.randrange(0, new_x + 1)
    random_coord_y = random.randrange(0, new_y + 1)
    print("Generated x coord is {}".format(random_coord_x))
    print("Generated y coord is {}".format(random_coord_y))
    # Get current position
    # If same as older one then do logic for moing
    # If not equal sleep
    sleep_time = random.randint(1, computer_sleep_time)
    print("Generated sleep time is {}".format(sleep_time))
    if(new_x != old_x):
        # Random amount of time less than or equal to actual
        # Mouse has moved in sleep rnage so no need to move mouse
        print("Mouse has been moved")
    else:
        # Mouse has not been moved
        print("Moving Mouse")
        # Move Mouse to Random position based on hardware limit
        pt.moveTo(random_coord_x, random_coord_y, 3)
        # Set old_x to new_x and then so on
        old_x = random_coord_x
        old_y = random_coord_y
    # Sleep for random amount of time contigenet on hardware limit
    print("Sleeping now")
    ti.sleep(sleep_time)
    print("-----------------------------------------------------")
