import pygame
import math
pygame.init()
# Set up the display
WIDTH, HEIGHT = 1200, 810
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Panet Simulation")

WHITE = (255 , 255 , 255)
YELLOW = (255, 255, 0)
BLUE = (100 , 149 , 237)
RED= (188, 39, 50)
DARK_GREY = (169, 169, 169)
FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    AU = 149.6e6 * 1000  # Astronomical Unit in meters
    G = 6.67428e-11 # Gravitational constant in m^3 kg^-1 s^-2
    SCALE = 200 / AU #Scale to fit in display
    TIMESTEP = 3600 * 24 #1 day in seconds

    def __init__(self, x, y, radius, color , mass, name=""):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.name = name

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        
        if len(self.orbit) > 2: 
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2 
                
                updated_points.append((x, y))
        
            pygame.draw.lines(win , self.color, False, updated_points, 2)
        
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun / 1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))
        
        name_text = FONT.render(self.name, 1, WHITE)
        win.blit(name_text, (x - name_text.get_width() / 2, y - self.radius - 15))

        pygame.draw.circle(win , self.color, (x, y), self.radius)

    def attraction(self ,other):
        other_x, other_y = other.x, other.y
        distance_x =other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass /distance **2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        self.x_vel +=total_fx / self.mass * self.TIMESTEP
        self.y_vel +=total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

def main():
    run =True
    clock = pygame.time.Clock()

    sun = Planet(0 , 0 , 30 , YELLOW , 1.98892 * 10**30,"Sun")  # Mass of the sun in kg  )
    sun.sun = True
    earth = Planet(-1 *Planet.AU , 0 , 16, BLUE,5.9742 * 10**24, "Earth")  # Earth
    earth.y_vel = 29.783 * 1000  # Earth's orbital speed in m/s

    mars = Planet(-1.524 * Planet.AU , 0 , 12, RED, 6.4171 * 10**23, "Mars")  # Mars
    mars.y_vel = 24.077 * 1000  # Mars' orbital speed in m/s

    mercury = Planet(0.387 * Planet.AU,
     0, 8, DARK_GREY, 3.3011 * 10**23, "Mercury")  # Mercury
    mercury.y_vel = -47.362 * 1000  # Mercury's orbital speed in m/s
    
    venus = Planet(0.723 * Planet.AU, 0, 14, (255, 165, 0), 4.8675 * 10**24, "Venus")  # Venus
    venus.y_vel = -35.02 * 1000  # Venus' orbital speed in m/s

    # jupiter = Planet(5.204 * Planet.AU, 0, 70, (255, 215, 0), 1.8982 * 10**27)  # Jupiter

    # saturn = Planet(9.582 * Planet.AU, 0, 60, (210, 180, 140), 5.6834 * 10**26)  # Saturn

    # uranus = Planet(19.218 * Planet.AU, 0, 25, (173, 216, 230), 8.6810 * 10**25)  # Uranus

    # neptune = Planet(30.070 * Planet.AU, 0, 24  , (70, 130, 180), 1.0243 * 10**26)  # Neptune
    # # Add more planets as needed


    planets = [sun, earth,mars, mercury, venus]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
        
        pygame.display.update()
    pygame.quit()
main()
