from .window import Page
from .login import LoginFrame
from .home import HomeFrame
from .user_managenet import UserManagement
from .sign_in import SigninFrame
from .edit_information import EditInformation
from .profile import ProfileFame
from .log_frame import LogFrame


class MainView:
    def __init__(self):
        self.window = Page()

        self.frames = {}

        self.add_frame("logs", LogFrame(self, self.window))
        self.add_frame("profile", ProfileFame(self, self.window))
        self.add_frame("edit", EditInformation(self, self.window))
        self.add_frame("sign_in", SigninFrame(self, self.window))
        self.add_frame("user_management", UserManagement(self, self.window))
        self.add_frame("home", HomeFrame(self, self.window))
        self.add_frame("login", LoginFrame(self, self.window))

        self.window.show()

    def add_frame(self, frame_name, frame):
        self.frames[frame_name] = frame
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

    def switch(self, frame_name):
        self.frames[frame_name].tkraise()
        return self.frames[frame_name]
