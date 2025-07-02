# 🌌 Planet Simulation with Pygame

This Python project simulates a simplified solar system using **Pygame** and **Newtonian physics**. It visually displays the orbits of planets around the Sun with realistic gravitational attraction.

## 🚀 Features

- Realistic gravitational physics.
- Simulation of planetary orbits in 2D space.
- Labels for planet names and distances from the Sun.
- Scalable astronomical units to screen resolution.

## 📦 Requirements

Install the required Python library:

```bash
pip install pygame
```

## 📁 Project Structure

```
Pygame/Planet-Simulation/
│
├── main.py        # Main simulation code using pygame
├── README.md      # Project documentation
```

## 🪐 Simulated Planets

- ☀️ Sun
- 🌍 Earth
- 🔴 Mars
- ☿ Mercury
- 🟠 Venus

*(Additional planets like Jupiter, Saturn, etc. are already included but commented out. You can easily enable them.)*

## 🎮 How to Run

1. Clone or download this project.
2. Make sure you have Python and Pygame installed.
3. Run the simulation using:

```bash
python main.py
```

The window will display a planetary system with moving orbits and labels.

## ⚙️ Physics Details

- Uses **Newton's Law of Universal Gravitation**.
- Units are converted from astronomical scales to pixels using a scale factor.
- Time steps simulate one day per frame (`TIMESTEP = 86400 seconds`).

## 🖼️ UI Features

- Orbits are drawn as trailing lines.
- Each planet shows its **name** and **distance from the sun (in km)**.
- Planet colors are accurate and visually distinguishable.

## 🎨 Customization

- Add more planets by adjusting their:
  - Mass
  - Position
  - Velocity
  - Color
  - Radius

## 👤 Author

**Satyam Prakash**  
📧 Email: [satyamprakashhp09@gmail.com](satyamprakashhp09@gmail.com)  
💼 GitHub: [SatyamPrakash09](https://github.com/SatyamPrakash09)

---

**Made with ☀️ gravity and Pygame**
