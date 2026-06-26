def get_phrase():
    """
    Devuelve una frase que indica que la RECA fue construida entre todos.
    arguments: None
    returns: str
    description: 
        Esta función es un ejemplo de cómo se puede devolver un mensaje personalizado.
        Se utiliza para ilustrar la colaboración en el proyecto RECA.
    example:
        >>> get_phrase()
        'La RECA la construímos entre todos'
    note:
        Esta función es parte del Bootcamp de AstroPython y se utiliza para enseñar
        conceptos básicos de Python y colaboración en proyectos.
    """ 
    return "La RECA la construímos entre todos, todas y todxs para la comunidad de Python en español "


def get_numbers_1_to_10():
    """
    Retorna una lista con los números del 1 al 10.
    arguments: None
    returns: list[int]
    example:
        >>> get_numbers_1_to_10()
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return list(range(1, 11))


def get_attendees():
    """
    Retorna una lista con los nombres de los asistentes al bootcamp.
    arguments: None
    returns: list[str]
    example:
        >>> get_attendees()
        ['Steve', 'Jurianny', 'Valentina', 'Juan Carlos', 'Andres', 'Ricardo', 'Luciana', 'Juliana', 'Jean', 'Andres', 'Maria']
    """
    return [
        "Steve",
        "Jurianny",
        "Valentina",
        "Juan Carlos",
        "Andres",
        "Ricardo",
        "Luciana",
        "Juliana",
        "Jean",
        "Andres",
        "Maria",
    ]


if __name__ == "__main__":
    result = get_phrase()
    print(result)
