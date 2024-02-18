# biddle9000

# Dependencies
- npm (and the 300 packages it installs)
- python 
- pip
    - Flask
    - flask_cors
    - requests
    - ffmpeg
    - OpenGL
    - LaTeX
    - manimgl
    - manim

# Installing and Running
1. In the inner biddle9000 directory, run "npm i"
2. Run "npm run dev"
3. Ensure Flask server is running by opening another shell window, navigating to the "backend" directory, and executing "server.py"

# Use Cases
- Visualizing Calculus I and II concepts
    - Derivatives
    - Integrals
- Visualizing Linear Algebra concepts
    - Vectors
    - Linear Transformations

## Inspiration
We were inspired by our experiences in linear algebra class, which involves complex math that can be hard to understand. We wanted to build something to help other students really understand the math they were doing, because oftentimes students simply memorize math without understanding why equations are the way they are.

## What it does
Given a user screenshot, the tool analyzes the equation or matrix given to it, and outputs a short video to help the user visualize their math, alongside a text explanation explaining what is happening.

## How we built it
We built this leveraging Ever's prompting expertise. We began working with processing simple images with the openAI API. From there, we made things more complex by extracting equations and matrices in their LaTeX form. From here we had some people split off and work on the frontend, while others actually got openAI to generate and execute dynamic graphing code, which we then translated into a video and sent back to the frontend alongside a helpful explanation.


## Challenges we ran into
1. installing and using manim just did NOT work on 2/5 of the computers we had
2. Some images refused to process well

## Accomplishments that we're proud of
1. Intaking and processing images pasted into our website
2. generating manim code to process and visualize functions
3. David's tenacity in installing manim

## What we learned
1. Make sure you can install packages BEFORE the hackathon
2. Prompt engineering can take longer than it looks
3. Use a debugger!

## What's next for Biddl-E9000
1. General stability and QOL fixes
2. Intaking more types of equations and matrices which are even harder for students to understand
3. Factory resetting David's computer

