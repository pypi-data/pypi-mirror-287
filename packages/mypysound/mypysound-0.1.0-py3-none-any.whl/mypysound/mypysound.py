import sys


def mypysound(file):
    platform = sys.platform
    if platform == "android":
        from android.media import MediaPlayer
        from os.path import dirname, join

        player = MediaPlayer()
        sound = join(dirname(__file__), file)
        player.setDataSource(sound)
        player.prepare()
        player.start()
    if platform == "ios":
        print("IOS is not supported at the moment")
    else:
        import pygame

        pygame.mixer.init()
        pygame.mixer.music.load(filename=file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()


if __name__ == "__main__":
    pysound(file="happy-birthday-whistled.wav")
