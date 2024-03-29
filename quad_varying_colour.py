# -----------------------------------------------------------------------------
# Python & OpenGL for Scientific Visualization
# www.labri.fr/perso/nrougier/python+opengl
# Copyright (c) 2017, Nicolas P. Rougier
# Distributed under the 2-Clause BSD License.
# -----------------------------------------------------------------------------
from glumpy import app, gloo, gl

vertex = """
    attribute vec2 position;
    attribute vec4 color;
    varying vec4 v_color;
    void main(){
        gl_Position = vec4(position, 0.0, 1.0);
        v_color = color; 
    } """ 

fragment = """
    varying vec4 v_color;
    void main() { gl_FragColor = v_color; } """

# Create a window with a valid GL context
window = app.Window()

# Build the program and corresponding buffers (with 4 vertices)
quad = gloo.Program(vertex, fragment, count=4)

# Upload data into GPU
quad['position'] = (-1,+1), (+1,+1), (-1,-1), (+1,-1)
quad['color'] = (1,1,0,1), (1,0,0,1), (0,0,1,1), (0,1,0,1)

# Tell glumpy what needs to be done at each redraw
@window.event
def on_draw(dt):
    window.clear()
    quad.draw(gl.GL_TRIANGLE_STRIP)

# Run the app
app.run()