import numpy as np
import plotly.graph_objects as go

print('Simulador de órbita de cohete en 3D sin pandas (echo por Daniel)')

def clasificar_cohete(distancia):
    if distancia > 1500001:
        return 'Fuera de Órbita'
    elif distancia >= 35787:
        return 'Órbita Alta'
    elif distancia >= 2001:
        return 'Órbita Media'
    else:
        return 'Órbita Baja'

num_cohetes = int(input('¿Cuántos cohetes?: '))
if num_cohetes <= 0:
    print('Se detiene el programa')
    exit()

fig = go.Figure()

for i in range(num_cohetes):
    horas = float(input(f'¿Cuántas horas viaja el cohete {i+1}?: '))
    velocidad = float(input(f'¿Velocidad inicial del cohete {i+1} (km/h)?: '))
    distancia = horas * velocidad
    co2 = horas * 2600
    
    print(f' Cohete {i+1}: recorrió {distancia:,.0f} km | Produjo {co2:,.0f} toneladas de CO2')
    print(f'   Tipo: {clasificar_cohete(distancia)}')
    
    num_angulos = 1000
    theta = np.linspace(0, 2*np.pi, num_angulos)
    x = distancia * np.cos(theta)
    y = distancia * np.sin(theta) * 0.3
    z = distancia * np.sin(theta) * 0.7
    
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        name=f'Cohete {i+1} - {distancia:,.0f} km',
        line=dict(width=6)
    ))

fig.update_layout(
    title=' Comparación de Órbitas 3D de Cohetes ¡Hecho por Daniel!',
    scene=dict(
        xaxis_title='X (km)',
        yaxis_title='Y (km)',
        zaxis_title='Z (km)',
        aspectmode='cube'
    ),
    showlegend=True
)
fig.show()