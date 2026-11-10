# Mouse draw canvas!

## Repository
<https://github.com/kckid22/PFDA/tree/main/Final%20Project>

## Description
This little 'game' will make it possible for someone to draw, erase, and create
art using their mouse! this is relavent to digital arts due to the creative 
elements that pertain to the game.

## Features
- Canvas
	- The canvas will capture mouse movements and drawings featuring non-spotty 
  lines, using pygame.draw.circle and a pygame surface.
- Toolbar
	- Top-panel control interface using geometric rectangle rects and hitbox 
  coordinate checks to handle click events for color swatches and tool switches.
- Brush size + Eraser Controller
	- Using state variables (current_tool & brush_size) with interactive UI button 
  boundaries (-/+) to scale brush radius bounds and toggle paint color between 
  active RGB values + canvas white bg.

## Challenges
- Real time mouse state tracking with pygame event loop.
- Coordinate space translation with surface blitting. 
- Learn to structure multi-variable state management and passing them between 
  modular functions.

## Outcomes
Ideal Outcome:
- Well polished digital art tool for freehand drawing using a color palette, 
  brush resizing, eraser, and the ability to export the canvas once a piece is done.

Minimal Viable Outcome:
- Functional pygame window with a drawing surface, basic tool area, working mouse
 input tracking, and at least two color options + an eraser.

## Milestones

- Week 1
  1. Create the Pygame window, set up game loop, & establish the split layout between
   drawing canvas and toolbar.
  2. Implement mouse event handling to capture basic cursor coordinates and render
   freehand dots and lines.

- Week 2
  1. Code color swatches and other buttons inside the toolbar using boudning box logic
   to toggle between drawing colors and the eraser.
  2. Add brush size adjustment buttons (-/+) and state variables to scale the brush
   radius and manage active tool states cleanly.

- Week N (Final)
  1. Create a 'Clear canvas' button and implement image saving so the artist can
   export their work as a png file.
  2. Refine UI, test edge cases (like coordinate mapping when clicking the toolbar vs.
   the canvas) and organize my repository.