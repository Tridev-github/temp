import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def create_derenzo_phantom(size, num_circles, circle_radius):
    """Create a Derenzo phantom image."""
    phantom = np.zeros((size, size), dtype=np.float32)

    # Create an image with circles
    fig, ax = plt.subplots(figsize=(size / 100, size / 100), dpi=100)
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_aspect('equal')
    ax.axis('off')

    for i in range(num_circles):
        circle_center_x = size / 2 + (i % 4 - 1.5) * circle_radius * 2
        circle_center_y = size / 2 + (i // 4 - 1.5) * circle_radius * 2
        circle = Circle((circle_center_x, circle_center_y), circle_radius, color='white')
        ax.add_patch(circle)

    # Convert figure to numpy array
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(size, size, 3)
    phantom = image[:, :, 0] / 255.0  # Use one channel (grayscale)

    plt.close(fig)
    return phantom

# Parameters
size = 100
num_circles = 16  # Number of circles
circle_radius = 4  # Radius of each circle

# Create the Derenzo phantom
phantom = create_derenzo_phantom(size, num_circles, circle_radius)

# Save to .npz file
np.savez('derenzo_phantom.npz', phantom=phantom)

print("Derenzo phantom image saved to 'derenzo_phantom.npz'.")
