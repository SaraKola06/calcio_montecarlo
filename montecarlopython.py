
import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# CREAZIONE DELLA FIGURA
# --------------------------------------------------

plt.close('all')

fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.axis('off')


# --------------------------------------------------
# DIMENSIONI DEL RETTANGOLO
# --------------------------------------------------

width = 5
height = 3


# --------------------------------------------------
# VERTICI DEL RETTANGOLO
# --------------------------------------------------

xRect = [0, width, width, 0, 0]
yRect = [0, 0, height, height, 0]


# Disegno del rettangolo
fig.patch.set_facecolor('white')



# --------------------------------------------------
# DECORAZIONE CAMPO
# --------------------------------------------------
ax.fill(xRect, yRect, 'w')
ax.fill([-1,-1,6,6,-1], [-1,0.5,0.5,-1,-1], 'green')
ax.plot([0,0.5,4.5,5,0], [0,0.5,0.5,0,0], 'k-', linewidth=1)
ax.fill([-1, 0, 0, 5, 5, 6, 6, -1 , -1], [0.5, 0.5, 3, 3, 0.5, 0.5, 4,4,0.5], '#87CEEB')
ax.plot([0, 0.5, 4.5, 5], [3, 3.5, 3.5, 3], 'k-', linewidth=2)
ax.fill([0, 0.5, 4.5, 5,0], [3, 3.5, 3.5, 3,3], 'w')
ax.plot([0.5,0.5], [0.5,3.5], 'k-', linewidth=1)
ax.plot([4.5,4.5], [0.5,3.5], 'k-', linewidth=1)
ax.fill([0,5,5,0,0], [0,0,3,3,0], '#C4A484')
ax.plot([0,5,5,0,0],[0,0,3,3,0],"k-",linewidth=5)



# --------------------------------------------------
# RAGGIO DELLE CIRCONFERENZE
# --------------------------------------------------

r = 0.5


# --------------------------------------------------
# CENTRI DELLE CIRCONFERENZE
# --------------------------------------------------

centers = np.array([
    [1.3, 0.75],
    [3.7, 0.75],
    [1.3, 2.25],
    [3.7, 2.25]
])


# --------------------------------------------------
# DISEGNO DELLE CIRCONFERENZE
# --------------------------------------------------

theta = np.linspace(0, 2 * np.pi, 100)

for i in range(len(centers)):

    xCircle = r * np.cos(theta) + centers[i, 0]
    yCircle = r * np.sin(theta) + centers[i, 1]

    ax.fill(xCircle, yCircle, 'w', zorder=10)
    ax.plot(xCircle, yCircle, 'k')

# --------------------------------------------------
# IMPOSTAZIONI DEGLI ASSI
# --------------------------------------------------

ax.set_xlim([-1, width + 1])
ax.set_ylim([-1, height + 1])

ax.set_title('Porta')
ax.set_xlabel('Asse X')
ax.set_ylabel('Asse Y')


# --------------------------------------------------
# LIVE GOAL
# --------------------------------------------------

a = 0
b = width
c = 0
d = height


# Numero di colpi già effettuati
live_shots = 0


def shoot(event):

    global live_shots

    # Se abbiamo già fatto 10 colpi,
    # non facciamo più niente
    if live_shots >= 10:
        return

    # Genera una posizione casuale
    x_rand_live = a + (b - a) * np.random.rand()
    y_rand_live = c + (d - c) * np.random.rand()

    # Disegna il colpo
    ax.plot(
        x_rand_live,
        y_rand_live,
        'ok',
        markersize=15,
        zorder=100
    )

    # Aumenta il numero di colpi
    live_shots += 1

    print(
        f"Shot {live_shots}/10: "
        f"({x_rand_live:.2f}, {y_rand_live:.2f})"
    )

    # Aggiorna il grafico
    fig.canvas.draw_idle()

    # --------------------------------------------------
    # DOPO 10 COLPI → MONTE CARLO
    # --------------------------------------------------

    if live_shots == 10:

        print("\n10 live shots completed!")
        print("Starting 1000 Monte Carlo shots...")

        attempts = 1000

        x_rand = a + (b - a) * np.random.rand(attempts)
        y_rand = c + (d - c) * np.random.rand(attempts)

        # Disegna i 1000 punti
        ax.plot(
            x_rand,
            y_rand,
            'ok',
            markersize=10,
            zorder=100
        )

        fig.canvas.draw_idle()

        # --------------------------------------------------
        # PROBABILITÀ TEORICA
        # --------------------------------------------------

        Area_rect = width * height

        Area_1_circle = np.pi * r**2

        Goal_prob = 4 * Area_1_circle / Area_rect

        print(
            "\nTheoretical probability:",
            Goal_prob
        )


        # --------------------------------------------------
        # PROBABILITÀ STATISTICA
        # --------------------------------------------------

        goal = np.zeros(attempts)

        for i in range(attempts):

            point = np.array([
                x_rand[i],
                y_rand[i]
            ])

            if (
                np.linalg.norm(point - centers[0, :]) <= r
                or
                np.linalg.norm(point - centers[1, :]) <= r
                or
                np.linalg.norm(point - centers[2, :]) <= r
                or
                np.linalg.norm(point - centers[3, :]) <= r
            ):
                goal[i] = 1

            else:
                goal[i] = 0


        Stat_prob = np.sum(goal) / attempts

        print(
            "Statistical probability:",
            Stat_prob
        )

        print("\nMonte Carlo simulation completed!")


# --------------------------------------------------
# COLLEGA LA TASTIERA ALLA FIGURA
# --------------------------------------------------

fig.canvas.mpl_connect('key_press_event', shoot)


# --------------------------------------------------
# MOSTRA IL GRAFICO
# --------------------------------------------------

print("Click on the graph to give it focus.")
print("Then press ANY KEY 10 times to shoot.")

plt.show()

