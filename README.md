PyScripts is a collection of individual python scripts. They were all made independantly and are self contained.

helllo_world.py: An example of how to structure a python script as to allow for it to be included in other scripts and have its own seperate main routine for testing/executing

fibbonacci: A very short script only 5 lines that demonstrates a functional way of printing n-items of the fibbonacci sequence. I thought it was pretty neat.

data_structures: A script containing some basic data structures that I intend to keep building on. I made them pretty quickly just to get a feel for python and test my computer science theory. Currently contains 1D array, ND array and tree structures. Potentially looking to add graph nodes, hash tables, binary trees and lists.

pyopengl_cube.py: This script requires 2 dependencies: "pygame" & "pyopengl". Its a pretty basic but really nice example of an opengl implementation. It uses the deprecated glBegin & glEnd functions instead of the MUCH better VAOs & VBOs but it was just to get a pyopengl script running so I'm pretty happy with it. Please note: GL_QUAD is deprecated for glDrawArrays! (This absolutely screwed me later on :[ )