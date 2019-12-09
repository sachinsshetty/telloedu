import tello
from tello_control_ui import TelloUI
import joystick


def main():

    drone = tello.Tello('', 8889)
    controller = joystick.Joystick()
    vplayer = TelloUI(drone,controller,"./img/")

	# start the Tkinter mainloop
    vplayer.root.mainloop()

if __name__ == "__main__":
    main()
