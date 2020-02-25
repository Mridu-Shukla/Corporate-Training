from enum import Enum


class ImageConstant(Enum):
    defaultImage = "images/default/default_profile_img.jpg"


class AuthConstants(Enum):
    noMatch = "Wrong username and password combination"
    sucessLogout = "You have been successfully logged out"
