import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def plot_roads(m, ax):
    """Plot the roads on the given axis."""
    for start, ends in enumerate(m.roads):
        x1, y1 = m.intersections[start]
        for end in ends:
            x2, y2 = m.intersections[end]
            ax.plot([x1, x2], [y1, y2], color='lightgray', zorder=0)


def animate_path(m, route, shortest_path, start, end, suffix=""):
    fig, ax = plt.subplots(figsize=(16, 12))  # Adjust the figure size

    plot_roads(m, ax)  # Plot the roads

    # Plot all intersections
    for intersection in m.intersections.values():
        ax.scatter(intersection[0], intersection[1], c='darkgray', s=50, zorder=1)

    visited_x, visited_y = [], []
    visited = ax.scatter([], [], c=[], cmap='coolwarm', s=100, zorder=2)  # Visited nodes with bigger size
    path, = ax.plot([], [], 'ro-', lw=2, zorder=3)  # Final path

    # Add grid and labels
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title('A* Pathfinding Algorithm')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')

    def init():
        return visited, path

    def update(frame):
        if frame < len(route):
            x, y = m.intersections[route[frame].id]
            visited_x.append(x)
            visited_y.append(y)
            visited.set_offsets(np.c_[visited_x, visited_y])
            visited.set_array(np.linspace(0, 1, len(visited_x)))
        if frame == len(route):
            x_vals = [m.intersections[node][0] for node in shortest_path]
            y_vals = [m.intersections[node][1] for node in shortest_path]
            path.set_data(x_vals, y_vals)
            ax.scatter([m.intersections[start][0]], [m.intersections[start][1]], c='limegreen', s=100, zorder=4, label='Start')
            ax.scatter([m.intersections[end][0]], [m.intersections[end][1]], c='crimson', s=100, zorder=4, label='End')
            ax.legend()
        return visited, path

    ani = animation.FuncAnimation(fig, update, frames=range(len(route) + 1), init_func=init, blit=False, interval=500)
    ani.save(f'animation_{start}_{end}_{suffix}.mp4', writer='ffmpeg', fps=1)
