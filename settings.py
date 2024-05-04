class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_speed = 1.5 # Adjust the ship's speed 1.5 pixel per iteration

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0 # Adjust the alien's speed 1.0 pixel per iteration
        self.fleet_drop_speed = 10 # Adjust the fleet's speed 10 pixel per iteration
        # fleet_direction of 1 represents right; -1 represents left 
        self.fleet_direction = 1