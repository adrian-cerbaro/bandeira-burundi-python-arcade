import arcade
import flag

arcade.open_window(800, 500, "Flag")
arcade.set_background_color(arcade.color.DARK_PINK)
arcade.start_render()

flag.draw(1, 498, 50)
flag.draw(100, 498, 100)
flag.draw(250, 450, 200)
flag.draw(490, 498, 288)
flag.draw(200, 300, 444)
flag.draw(10, 30, 33)

arcade.finish_render()
arcade.run()
