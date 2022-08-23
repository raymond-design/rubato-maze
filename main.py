import rubato as rb

rb.init(
    name="Platformer Demo",  # Set a name
    res=rb.Vector(1920, 1080),  # Set the window resolution (pixel length and height).
        # note that since we didn't also specify a window size,
        # the window will be automatically resized to half of the resolution.
)

rb.begin()