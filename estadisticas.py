def grafico_personajes_por_planeta():
    data = {}

    for personaje in Personaje.lista_personajes:
        if personaje.planeta_origen:
            if personaje.planeta_origen not in data:
                data[personaje.planeta_origen] = 0
            data[personaje.planeta_origen] += 1

    if not data:
        print("No hay datos disponibles para mostrar el gráfico.")
        return

    df = pd.DataFrame(list(data.items()), columns=['Planeta', 'Cantidad'])
    df.plot(x='Planeta', y='Cantidad', kind='bar', legend=False)
    plt.title('Cantidad de personajes nacidos en cada planeta')
    plt.xlabel('Planeta')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.show()