import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.spatial.transform import Rotation as R

# Crear figura y ejes 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.3)

# Función para dibujar los ejes rotados
def draw_rotated_axes(ax, rot, title):
    ax.clear()
    origin = np.array([0, 0, 0])
    axes = rot.apply(np.eye(3))  # X, Y, Z unit vectors rotados

    colors = ['r', 'g', 'b']
    labels = ['X', 'Y', 'Z']
    for i in range(3):
        ax.quiver(*origin, *axes[i], color=colors[i], length=1.0, normalize=True)
        ax.text(*(axes[i] * 1.1), labels[i], color=colors[i], fontsize=12)

    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    ax.view_init(elev=30, azim=45)

# Función de actualización con sliders
def update(val):
    roll = s_roll.val
    pitch = s_pitch.val
    yaw = s_yaw.val

    # Rotación usando ángulos de Euler (orden: xyz)
    rot = R.from_euler('xyz', [yaw, pitch, roll], degrees=True)
    title = f"Yaw (X): {yaw:.1f}°, Pitch (Y): {pitch:.1f}°, Roll (Z): {roll:.1f}°"
    draw_rotated_axes(ax, rot, title)
    fig.canvas.draw_idle()

# Sliders
axcolor = 'lightgoldenrodyellow'
ax_roll = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_pitch = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_yaw = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)

s_roll = Slider(ax_roll, 'Roll (Z)', -180, 180, valinit=0)
s_pitch = Slider(ax_pitch, 'Pitch (Y)', -180, 180, valinit=0)
s_yaw = Slider(ax_yaw, 'Yaw (X)', -180, 180, valinit=0)

# Conectar sliders
s_roll.on_changed(update)
s_pitch.on_changed(update)
s_yaw.on_changed(update)

# Dibujar inicial
update(None)
plt.show()
