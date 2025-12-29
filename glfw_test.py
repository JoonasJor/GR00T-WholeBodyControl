import glfw
from OpenGL.GL import glGetString, GL_RENDERER, GL_COLOR_BUFFER_BIT, glClearColor, glClear

if not glfw.init():
    raise SystemExit("glfw.init failed")

def error_cb(err, desc):
    print("GLFW error", err, desc)
glfw.set_error_callback(error_cb)

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
# remove/adjust profile hint if it fails
# glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

win = glfw.create_window(640, 480, "GLFW NVIDIA Test", None, None)
if not win:
    glfw.terminate()
    raise SystemExit("window creation failed")

glfw.make_context_current(win)
print("Renderer:", glGetString(GL_RENDERER).decode())

while True:  # ~5 seconds at 60Hz
    glClearColor(1.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(win)
    glfw.poll_events()
    if glfw.window_should_close(win):
        break

glfw.terminate()
