# Mars_rover
Python3 application for mars rover problem

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular,
must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to
send back to Earth.

A rover&#39;s position and location are represented by a combination of x and y co-ordinates and a letter representing one of
the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might
be 0, 0, N, which means the rover is in the bottom left corner and facing North.
In order to control a rover, NASA sends a simple string of letters. 

The possible letters are &#39;L&#39;, &#39;R&#39; and &#39;M&#39;. &#39;L&#39; and &#39;R&#39; makes
the rover spin 90 degrees left or right respectively, without moving from its current spot. &#39;M&#39; means move forward one
grid point and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).


Input:

5 5

1 2 N

LMLMLMLMM

3 3 E

MMRMMRMRRM

Result for above input after executing

1 3 N

5 1 E

   

# Installing MarsRover

   git clone https://github.com/NarenderRajuB/Mars_rover
   cd Mars_rover
   pip3 install .


# Create a Mars rover distribution package
   cd Mars_rover
   python3 setup sdist
   
   Above command will create MarsRover-0.0.1.tar.gz in dist/ folder

   
# How to use:
    python3 main.py
    
    * output: 
        1 3 N
        5 1 E
    
# Unittest:
    python3 -m unittest

    .....rover initial position out of plateau area
    .Rover position out of plateau grid dimensions
    Rover position out of plateau grid dimensions
    ..Invalid Directions default to North
    ...
    ----------------------------------------------------------------------
    Ran 11 tests in 0.001s
    
    OK




