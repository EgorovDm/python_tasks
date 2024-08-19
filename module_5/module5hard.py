#!/usr/bin/env python3
# wizardlm2:7b + some fixes

import hashlib
from datetime import datetime
import time


class User:
    """
    The User class represents a user in the system. Each user has a unique nickname, an encrypted password, and an age.
    """
    def __init__(self, nickname, password, age):
        """
        Initializes a new instance of the User class with a given nickname, encrypted password, and age.
        
        :param nickname: A string representing the user's nickname.
        :param password: A string representing the user's unencrypted password.
        :param age: An integer representing the user's age.
        """
        self.nickname = nickname
        # Hash the user's password using SHA-256 algorithm before storing it to ensure security.
        self._password_hash = self._hash_password(password)
        self.age = age

    def _hash_password(self, password):
        """
        Private method that takes a plain text password and returns the SHA-256 hash of that password.
        
        :param password: A string representing the user's unencrypted password.
        :return: A string containing the SHA-256 hash of the password.
        """
        # Use SHA-256 to create a secure hash of the password.
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def _hash_password(self, password):
        """
        Private method that takes a plain text password and returns the SHA-256 hash of that password.

        :param password: A string representing the user's unencrypted password.
        :return: A string containing the SHA-256 hash of the password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """
        Checks if a given plain text password matches the user's stored hashed password.
        :param password: A string representing the user's unencrypted password.
        :return: True if the passwords match, False otherwise.
        """
        return self._password_hash == hashlib.sha256(password.encode()).hexdigest()

    def __repr__(self):
        """
        Returns a string representation of the User object with nickname and age, suitable for debugging.
        
        :return: A string representing the user's nickname and age.
        """
        return f"User(nickname='{self.nickname}', age={self.age})"

class Video(object):
    """
    The Video class represents a video in the system. A video has a title, duration, and whether it's in adult mode.
    """
    def __init__(self, title, duration, adult_mode=False):
        """
        Initializes a new instance of the Video class with a given title, duration, and optional adult mode setting.
        
        :param title: A string representing the video's title.
        :param duration: An integer representing the total duration of the video in seconds.
        :param adult_mode: A boolean indicating if the video is intended for adults (default is False).
        """
        self.title = title
        self.duration = duration
        self.playback_position = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        """
        Returns a string representation of the Video object with title, duration, and adult mode, suitable for debugging.
        
        :return: A string representing the video's title, duration, and whether it's in adult mode.
        """
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    """
    The UrTube class represents the system where users can log in, register, add videos, search for videos, and watch videos.
    """
    def __init__(self):
        """
        Initializes a new instance of the UrTube class with empty lists for users and videos.
        """
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """
        Attempts to log in a user by finding the user with the given nickname and checking if the provided password matches the stored hash.
        
        :param nickname: A string representing the user's nickname.
        :param password: A string representing the user's unencrypted password.
        :return: True if the user is found and the passwords match, False otherwise or if the user does not exist.
        """
        user = next(
            (
                u
                for u in self.users
                if u.nickname == nickname and u.check_password(password)
            ),
            None,
        )
        if user:
            self.current_user = user
            return True
        else:
            print("Пользователь {} не существует".format(nickname))
            return False

    def register(self, nickname, password, age):
        """
        Registers a new user if the nickname is not already taken. The password is stored as its SHA-256 hash.
        
        :param nickname: A string representing the user's desired nickname.
        :param password: A string representing the user's unencrypted password.
        :param age: An integer representing the user's age.
        """
        if not any(u.nickname == nickname for u in self.users):
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            print("Регистрация успешна.")
            self.log_in(nickname, password)
        else:
            print("Пользователь {} уже существует".format(nickname))

    def log_out(self):
        """
        Logs out the current user by setting the current_user attribute to None.
        """
        self.current_user = None

    def add(self, *args):
        """
        Adds one or more videos to the system's video list if they do not already exist.
        
        :param args: One or more Video objects to be added to the system.
        """
        for video in args:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_term):
        """
        Returns a list of video titles that contain the given search term (case-insensitive).
                :param search_term: A string representing what the user is searching for.
        :return: A list of titles from videos in the system that include the search term.
        """
        return [
            video.title
            for video in self.videos
            if search_term.lower() in video.title.lower()
        ]

    def watch_video(self, title):
        """
        Plays the specified video if the user is logged in and has the necessary age or it's not set as adult mode.
        If a problem arises (for example, the user is not authorized), returns None.

        :param title: A string representing the title of the video to be played.
        :return: None if there are problems with the operation.
        """

        video = next((v for v in self.videos if v.title == title), None)
        if (not self.current_user):
            print("Пользователь не авторизован")
            return None
        elif (not video):
            print("Нет такого видео")
            return None
        elif (video.adult_mode and self.current_user.age <= 18):
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return None
        while True:
            video.playback_position = (video.playback_position + 1) % video.duration
            print(f"Время просмотра: {video.playback_position} секунд", end="\r")
            if not video.playback_position:
                break
            time.sleep(1)
        print("Конец видео" + " "*20 )


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
