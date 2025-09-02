# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
# import matplotlib.animation as animation


# #Time
# t0=0 #[s]
# t_end=60 #[s]
# dt=0.04
# t=np.arange(t0, t_end+dt, dt)

# #Zero arrays for the tanks' volumes
# volume_Tank1=np.zeros(len(t))
# volume_Tank2=np.zeros(len(t))
# volume_Tank3=np.zeros(len(t))

# #Create volumes for
# for i in range(0, len(t)):
#     #Tank1
#     if t[i]<=22.5:
#         volume_Tank1[i]=50+2*t[i]
#     elif t[i]<=32.5:
#         volume_Tank1[i]=95
#         temp11=i
#     elif t[i]<=32.5+45**0.5:
#         volume_Tank1[i]=95-(t[i]-t[temp11])**2
#         temp12=i
#     elif t[i]<=42.5+45**0.5:
#         volume_Tank1[i]=50+np.sin(2*np.pi*1*(t[i]-t[temp12]))
#     else:
#         volume_Tank1[i]=50
        
        
#     #Tank2
#     if t[i]<=27.5:
#         volume_Tank2[i]=40+2*t[i]
#     elif t[i]<=32.5:
#         volume_Tank2[i]=95
#         temp21=i
#     elif t[i]<=32.5+45**0.5:
#         volume_Tank2[i]=95-(t[i]-t[temp21])**2
#         temp22=i
#     elif t[i]<=37.5+.45**0.5:
#         volume_Tank2[i]=50+3*np.sin(2*np.pi*1*(t[i]-t[temp22]))
#         temp23=i
#     elif t[i]<=42.5+45**0.5:
#         volume_Tank2[i]=50+np.sin(2*np.pi*2*(t[i]-t[temp21]))
#     else:
#         volume_Tank2[i]=50
        

#     #Tank3
#     if t[i]<=32.5:
#         volume_Tank3[i]=30+2*t[i]
#         temp31=i
#     elif t[i]<=32.5+45**0.5:
#         volume_Tank3[i]=95-(t[i]-t[temp31])**2
#         temp32=i
#     # elif t[i]<=42.5+45**0.5: #(45**0.5 e o mesmo que raiz de 45)
#     #     volume_Tank3[i]=50-np.sin(2*np.pi*1*(t[i]-[temp32]))
#     else:
#         volume_Tank3[i]=50



#     #ANIMATION
    
#     frame_amount=len(t)
    
#     #Create the watertanks
#     radius=5 #[m]
#     volume_i=0  #[m^3]
#     volume_f=100 #[m^3]
#     dVol=10
    
    
#     # def update_plot(num):
#     #return
    
#     # Set up your figure properties
#     fig=plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8,0.8,0.8))
#     gs=gridspec.GridSpec(2,3)
    
#     #Tank1
#     ax0=fig.add_subplot(gs[0,0], facecolor=(0.9,0.9,0.9))
#     tank_1,=ax0.plot([],[],'r',linewidth=4)
#     tank_12,=ax0.plot([],[],'royalblue', linewidth=260)
#     plt.xlim(-radius, radius)
#     plt.ylim(volume_i, volume_f)
#     plt.xticks(np.arange(-radius, radius+1, radius))
#     plt.yticks(np.arange(volume_i, volume_f+dVol, dVol))
#     plt.ylabel('tank volume [m^3]')
#     plt.title('Tank 1')
    
    
#     #Tank2
#     ax0=fig.add_subplot(gs[0,1], facecolor=(0.9,0.9,0.9))
#     tank_2,=ax0.plot([],[],'r',linewidth=4)
#     tank_22,=ax0.plot([],[],'royalblue', linewidth=260)
#     plt.xlim(-radius, radius)
#     plt.ylim(volume_i, volume_f)
#     plt.xticks(np.arange(-radius, radius+1, radius))
#     plt.yticks(np.arange(volume_i, volume_f+dVol, dVol))
#     plt.title('Tank 2')


#     #Tank3
#     ax0=fig.add_subplot(gs[0,2], facecolor=(0.9,0.9,0.9))
#     tank_3,=ax0.plot([],[],'r',linewidth=4)
#     tank_32,=ax0.plot([],[],'royalblue', linewidth=260)
#     plt.xlim(-radius, radius)
#     plt.ylim(volume_i, volume_f)
#     plt.xticks(np.arange(-radius, radius+1, radius))
#     plt.yticks(np.arange(volume_i, volume_f+dVol, dVol))
#     plt.title('Tank 3')

# plt.close()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
# import matplotlib.animation as animation

# # --- PARTE 1: CÁLCULO DOS VOLUMES ---

# t0 = 0
# t_end = 60
# dt = 0.04
# t = np.arange(t0, t_end + dt, dt)

# volume_Tank1 = np.zeros(len(t))
# volume_Tank2 = np.zeros(len(t))
# volume_Tank3 = np.zeros(len(t))

# temp11 = temp12 = temp21 = temp22 = temp23 = temp31 = temp32 = 0

# for i in range(len(t)):
#     # Tank 1
#     if t[i] <= 22.5:
#         volume_Tank1[i] = 50 + 2 * t[i]
#     elif t[i] <= 32.5:
#         volume_Tank1[i] = 95
#         temp11 = i
#     elif t[i] <= 32.5 + 45**0.5:
#         volume_Tank1[i] = 95 - (t[i] - t[temp11]) ** 2
#         temp12 = i
#     elif t[i] <= 42.5 + 45**0.5:
#         volume_Tank1[i] = 50 + np.sin(2 * np.pi * 1 * (t[i] - t[temp12]))
#     else:
#         volume_Tank1[i] = 50

#     # Tank 2
#     if t[i] <= 27.5:
#         volume_Tank2[i] = 40 + 2 * t[i]
#     elif t[i] <= 32.5:
#         volume_Tank2[i] = 95
#         temp21 = i
#     elif t[i] <= 32.5 + 45**0.5:
#         volume_Tank2[i] = 95 - (t[i] - t[temp21]) ** 2
#         temp22 = i
#     elif t[i] <= 37.5 + 45**0.5:
#         volume_Tank2[i] = 50 + 3 * np.sin(2 * np.pi * 1 * (t[i] - t[temp22]))
#         temp23 = i
#     elif t[i] <= 42.5 + 45**0.5:
#         volume_Tank2[i] = 50 + np.sin(2 * np.pi * 2 * (t[i] - t[temp21]))
#     else:
#         volume_Tank2[i] = 50

#     # Tank 3
#     if t[i] <= 32.5:
#         volume_Tank3[i] = 30 + 2 * t[i]
#         temp31 = i
#     elif t[i] <= 32.5 + 45**0.5:
#         volume_Tank3[i] = 95 - (t[i] - t[temp31]) ** 2
#         temp32 = i
#     else:
#         volume_Tank3[i] = 50

# # --- PARTE 2: CONFIGURAÇÃO DA FIGURA ---

# fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
# gs = gridspec.GridSpec(1, 3)

# volume_i = 0
# volume_f = 100

# # Tank 1
# ax1 = fig.add_subplot(gs[0, 0])
# line1, = ax1.plot([], [], 'royalblue', lw=2)
# ax1.set_xlim(t0, t_end)
# ax1.set_ylim(volume_i, volume_f)
# ax1.set_title("Tank 1")
# ax1.set_xlabel("Tempo [s]")
# ax1.set_ylabel("Volume [m³]")

# # Tank 2
# ax2 = fig.add_subplot(gs[0, 1])
# line2, = ax2.plot([], [], 'royalblue', lw=2)
# ax2.set_xlim(t0, t_end)
# ax2.set_ylim(volume_i, volume_f)
# ax2.set_title("Tank 2")
# ax2.set_xlabel("Tempo [s]")

# # Tank 3
# ax3 = fig.add_subplot(gs[0, 2])
# line3, = ax3.plot([], [], 'royalblue', lw=2)
# ax3.set_xlim(t0, t_end)
# ax3.set_ylim(volume_i, volume_f)
# ax3.set_title("Tank 3")
# ax3.set_xlabel("Tempo [s]")

# # --- PARTE 3: FUNÇÃO DE ATUALIZAÇÃO PARA ANIMAÇÃO ---

# def update(frame):
#     line1.set_data(t[:frame], volume_Tank1[:frame])
#     line2.set_data(t[:frame], volume_Tank2[:frame])
#     line3.set_data(t[:frame], volume_Tank3[:frame])
#     return line1, line2, line3

# ani = animation.FuncAnimation(
#     fig, update, frames=len(t), interval=20, blit=True
# )

# plt.tight_layout()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# # --- PARTE 1: CÁLCULO DOS VOLUMES ---

# t0, t_end, dt = 0, 60, 0.04
# t = np.arange(t0, t_end + dt, dt)

# volume_Tank1 = np.zeros(len(t))
# volume_Tank2 = np.zeros(len(t))
# volume_Tank3 = np.zeros(len(t))

# temp11 = temp12 = temp21 = temp22 = temp23 = temp31 = temp32 = 0

# for i in range(len(t)):
#     # Tank 1
#     if t[i] <= 22.5:
#         volume_Tank1[i] = 50 + 2 * t[i]
#     elif t[i] <= 32.5:
#         volume_Tank1[i] = 95
#         temp11 = i
#     elif t[i] <= 32.5 + 45**0.5:
#         volume_Tank1[i] = 95 - (t[i] - t[temp11]) ** 2
#         temp12 = i
#     elif t[i] <= 42.5 + 45**0.5:
#         volume_Tank1[i] = 50 + np.sin(2 * np.pi * 1 * (t[i] - t[temp12]))
#     else:
#         volume_Tank1[i] = 50

#     # Tank 2
#     if t[i] <= 27.5:
#         volume_Tank2[i] = 40 + 2 * t[i]
#     elif t[i] <= 32.5:
#         volume_Tank2[i] = 95
#         temp21 = i
#     elif t[i] <= 32.5 + 45**0.5:
#         volume_Tank2[i] = 95 - (t[i] - t[temp21]) ** 2
#         temp22 = i
#     elif t[i] <= 37.5 + 45**0.5:
#         volume_Tank2[i] = 50 + 3 * np.sin(2 * np.pi * 1 * (t[i] - t[temp22]))
#         temp23 = i
#     elif t[i] <= 42.5 + 45**0.5:
#         volume_Tank2[i] = 50 + np.sin(2 * np.pi * 2 * (t[i] - t[temp21]))
#     else:
#         volume_Tank2[i] = 50

#     # Tank 3
#     if t[i] <= 32.5:
#         volume_Tank3[i] = 30 + 2 * t[i]
#         temp31 = i
#     elif t[i] <= 32.5 + 45**0.5:
#         volume_Tank3[i] = 95 - (t[i] - t[temp31]) ** 2
#         temp32 = i
#     else:
#         volume_Tank3[i] = 50

# # --- PARTE 2: CONFIGURAÇÃO DA FIGURA ---

# fig, ax = plt.subplots(figsize=(8, 6))
# ax.set_xlim(-1, 3)
# ax.set_ylim(0, 100)
# ax.set_xticks([0, 1, 2])
# ax.set_xticklabels(['Tank 1', 'Tank 2', 'Tank 3'])
# ax.set_ylabel('Volume [m³]')
# ax.set_title('Níveis dos Tanques (Visual Cilíndrico)')

# # Barras iniciais
# bars = ax.bar([0, 1, 2], [0, 0, 0], color='royalblue', width=0.6)

# # --- PARTE 3: FUNÇÃO DE ANIMAÇÃO ---

# def update(frame):
#     bars[0].set_height(volume_Tank1[frame])
#     bars[1].set_height(volume_Tank2[frame])
#     bars[2].set_height(volume_Tank3[frame])
#     return bars

# ani = animation.FuncAnimation(
#     fig, update, frames=len(t), interval=20, blit=True
# )

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec

# --- CÁLCULO DOS VOLUMES ---

t0, t_end, dt = 0, 60, 0.04
t = np.arange(t0, t_end + dt, dt)

volume_Tank1 = np.zeros(len(t))
volume_Tank2 = np.zeros(len(t))
volume_Tank3 = np.zeros(len(t))

temp11 = temp12 = temp21 = temp22 = temp23 = temp31 = temp32 = 0

for i in range(len(t)):
    # Tank 1
    if t[i] <= 22.5:
        volume_Tank1[i] = 50 + 2 * t[i]
    elif t[i] <= 32.5:
        volume_Tank1[i] = 95
        temp11 = i
    elif t[i] <= 32.5 + 45**0.5:
        volume_Tank1[i] = 95 - (t[i] - t[temp11]) ** 2
        temp12 = i
    elif t[i] <= 42.5 + 45**0.5:
        volume_Tank1[i] = 50 + np.sin(2 * np.pi * 1 * (t[i] - t[temp12]))
    else:
        volume_Tank1[i] = 50

    # Tank 2
    if t[i] <= 27.5:
        volume_Tank2[i] = 40 + 2 * t[i]
    elif t[i] <= 32.5:
        volume_Tank2[i] = 95
        temp21 = i
    elif t[i] <= 32.5 + 45**0.5:
        volume_Tank2[i] = 95 - (t[i] - t[temp21]) ** 2
        temp22 = i
    elif t[i] <= 37.5 + 45**0.5:
        volume_Tank2[i] = 50 + 3 * np.sin(2 * np.pi * 1 * (t[i] - t[temp22]))
        temp23 = i
    elif t[i] <= 42.5 + 45**0.5:
        volume_Tank2[i] = 50 + np.sin(2 * np.pi * 2 * (t[i] - t[temp21]))
    else:
        volume_Tank2[i] = 50

    # Tank 3
    if t[i] <= 32.5:
        volume_Tank3[i] = 30 + 2 * t[i]
        temp31 = i
    elif t[i] <= 32.5 + 45**0.5:
        volume_Tank3[i] = 95 - (t[i] - t[temp31]) ** 2
        temp32 = i
    else:
        volume_Tank3[i] = 50

# --- CONFIGURAÇÃO DA FIGURA ---

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1])  # duas linhas: gráfico e tanques

# Painel superior: gráficos em linha
ax1 = fig.add_subplot(gs[0])
line1, = ax1.plot([], [], label="Tank 1", color="royalblue")
line2, = ax1.plot([], [], label="Tank 2", color="seagreen")
line3, = ax1.plot([], [], label="Tank 3", color="tomato")
ax1.set_xlim(t0, t_end)
ax1.set_ylim(0, 100)
ax1.set_ylabel("Volume [m³]")
ax1.set_title("Volumes ao longo do tempo")
ax1.legend()

# Painel inferior: tanques (barras)
ax2 = fig.add_subplot(gs[1])
ax2.set_xlim(-1, 3)
ax2.set_ylim(0, 100)
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(["Tank 1", "Tank 2", "Tank 3"])
ax2.set_ylabel("Volume [m³]")
bars = ax2.bar([0, 1, 2], [0, 0, 0], color="royalblue", width=0.6)
ax2.set_title("Visualização dos Tanques")

# --- FUNÇÃO DE ANIMAÇÃO ---

def update(frame):
    # Atualiza gráficos em linha
    line1.set_data(t[:frame], volume_Tank1[:frame])
    line2.set_data(t[:frame], volume_Tank2[:frame])
    line3.set_data(t[:frame], volume_Tank3[:frame])

    # Atualiza barras dos tanques
    bars[0].set_height(volume_Tank1[frame])
    bars[1].set_height(volume_Tank2[frame])
    bars[2].set_height(volume_Tank3[frame])

    return line1, line2, line3, *bars

ani = animation.FuncAnimation(
    fig, update, frames=len(t), interval=20, blit=True
)

plt.tight_layout()
plt.show()
