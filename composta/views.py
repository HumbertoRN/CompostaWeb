from django.shortcuts import render



def home(request):

  
    ingredientes = [
        {
            'nombre': 'Materiales verdes',
            'aporta': 'Nitrógeno',
            'descripcion': 'Restos húmedos y frescos: cáscaras de fruta, verdura, café y pasto recién cortado.',
            'imagen': 'composta/img/cascaras.jpg',
        },
        {
            'nombre': 'Materiales cafés',
            'aporta': 'Carbono',
            'descripcion': 'Restos secos: hojas, ramas pequeñas, cartón y papel sin tinta de color.',
            'imagen': 'composta/img/hojas_secas.jpg',
        },
        {
            'nombre': 'Agua',
            'aporta': 'Humedad',
            'descripcion': 'La mezcla debe sentirse como una esponja exprimida: húmeda, pero sin escurrir.',
            'imagen': 'composta/img/lombrices_composta.jpg',
        },
        {
            'nombre': 'Aire',
            'aporta': 'Oxígeno',
            'descripcion': 'Voltear la mezcla deja entrar oxígeno, acelera el proceso y evita malos olores.',
            'imagen': 'composta/img/contenedores.jpg',
        },
    ]

    trabajadores = [
        {
            'nombre': 'Lombrices',
            'descripcion': 'Se comen los restos y los devuelven convertidos en un abono riquísimo.',
            'imagen': 'composta/img/lombrices.jpg',
        },
        {
            'nombre': 'Hongos',
            'descripcion': 'Descomponen lo más duro, como hojas secas, ramas y cartón.',
            'imagen': 'composta/img/hongos.jpg',
        },
        {
            'nombre': 'Bacterias',
            'descripcion': 'Millones de ellas trabajan sin parar y calientan la composta hasta 60 °C.',
            'imagen': 'composta/img/composta_lista.jpg',
        },
    ]

    datos = [
        {'numero': '50%', 'texto': 'de la basura de una casa son restos orgánicos'},
        {'numero': '2-6', 'texto': 'meses tarda en estar lista'},
        {'numero': '60 °C', 'texto': 'puede alcanzar en el centro'},
    ]

    return render(request, 'composta/home.html', {
        'ingredientes': ingredientes,
        'trabajadores': trabajadores,
        'datos': datos,
    })



def como_hacer(request):

    pasos = [
        {
            'titulo': 'Elige el lugar',
            'descripcion': 'Busca un sitio con sombra parcial, protegido de la lluvia fuerte y, si se puede, sobre tierra para que entren las lombrices.',
            'imagen': 'composta/img/huerto_comunitario.jpg',
        },
        {
            'titulo': 'Consigue un contenedor',
            'descripcion': 'Un bote con tapa, una caja de madera o un compostero. Lo importante es que tenga agujeros para que entre el aire.',
            'imagen': 'composta/img/bote.jpg',
        },
        {
            'titulo': 'Pon una base seca',
            'descripcion': 'En el fondo coloca ramas pequeñas u hojas secas. Ayudan a que circule el aire y a que escurra el exceso de agua.',
            'imagen': 'composta/img/hojas_secas.jpg',
        },
        {
            'titulo': 'Alterna capas verdes y cafés',
            'descripcion': 'Agrega tus restos de cocina y cúbrelos siempre con material seco. Una buena regla: 1 parte de verde por 2 de café.',
            'imagen': 'composta/img/residuos_cocina.jpg',
        },
        {
            'titulo': 'Corta en trozos pequeños',
            'descripcion': 'Mientras más pequeños sean los pedazos, más rápido trabajan los microorganismos.',
            'imagen': 'composta/img/cascaras.jpg',
        },
        {
            'titulo': 'Cuida la humedad y voltea',
            'descripcion': 'Si está seca, riégala; si está muy mojada, agrega hojas o cartón. Una vez por semana revuélvela con una pala.',
            'imagen': 'composta/img/lombrices_composta.jpg',
        },
        {
            'titulo': 'Espera y cosecha',
            'descripcion': 'Entre 2 y 6 meses después tendrás composta. Tamízala y regresa al contenedor los trozos que no se deshicieron.',
            'imagen': 'composta/img/composta_lista.jpg',
        },
    ]

    senales_lista = [
        'Color café oscuro, casi negro',
        'Huele a tierra mojada o a bosque',
        'Ya no se reconocen los restos de comida',
        'Está fría: ya no se siente calor en el centro',
    ]

    return render(request, 'composta/como_hacer.html', {
        'pasos': pasos,
        'senales_lista': senales_lista,
    })


def materiales(request):

    verdes = [
        'Cáscaras de frutas y verduras',
        'Restos de café y bolsitas de té',
        'Pasto recién cortado',
        'Flores y plantas marchitas',
        'Cascarones de huevo triturados',
    ]

    cafes = [
        'Hojas secas',
        'Ramas pequeñas y aserrín sin tratar',
        'Cartón y papel sin tinta de color',
        'Servilletas y rollos de papel higiénico',
        'Paja',
    ]

    prohibidos = [
        {'nombre': 'Carne, pescado y huesos', 'razon': 'Huelen mal y atraen ratas.'},
        {'nombre': 'Lácteos', 'razon': 'Leche, queso o yogurt se pudren y dan mal olor.'},
        {'nombre': 'Aceites y grasas', 'razon': 'Cubren los restos e impiden que entre el aire.'},
        {'nombre': 'Heces de perros y gatos', 'razon': 'Pueden contener parásitos y enfermedades.'},
        {'nombre': 'Plantas enfermas', 'razon': 'Pueden contagiar a otras plantas.'},
        {'nombre': 'Plástico, vidrio y metal', 'razon': 'No se descomponen nunca.'},
        {'nombre': 'Papel brillante o de color', 'razon': 'Sus tintas contienen químicos.'},
        {'nombre': 'Ceniza de carbón', 'razon': 'Puede dañar el suelo.'},
    ]

    return render(request, 'composta/materiales.html', {
        'verdes': verdes,
        'cafes': cafes,
        'prohibidos': prohibidos,
    })



def beneficios(request):

    beneficios = [
        {
            'titulo': 'Plantas más sanas',
            'etiqueta': 'Plantas',
            'descripcion': 'Les da nutrientes de forma natural, las hace crecer más fuertes y ayuda a prevenir enfermedades.',
            'imagen': 'composta/img/plantulas.jpg',
        },
        {
            'titulo': 'Un suelo vivo',
            'etiqueta': 'Suelo',
            'descripcion': 'Hace la tierra más suelta, ayuda a que guarde mejor el agua y atrae lombrices y organismos útiles.',
            'imagen': 'composta/img/semillero.jpg',
        },
        {
            'titulo': 'Menos basura',
            'etiqueta': 'Planeta',
            'descripcion': 'Los restos orgánicos dejan de ir al basurero, donde producen metano, un gas que calienta el planeta.',
            'imagen': 'composta/img/contenedores.jpg',
        },
        {
            'titulo': 'Ahorro en casa',
            'etiqueta': 'Casa',
            'descripcion': 'Ya no necesitas comprar abono ni tierra para tus macetas, y tu bote de basura se llena más despacio.',
            'imagen': 'composta/img/huerto.jpg',
        },
    ]

    usos = [
        'Mezclarla con la tierra de tus macetas',
        'Esparcirla sobre el jardín o el pasto',
        'Preparar la tierra de un huerto',
        'Ponerla alrededor de los árboles',
    ]

    return render(request, 'composta/beneficios.html', {
        'beneficios': beneficios,
        'usos': usos,
    })



def preguntas(request):
    return render(request, 'composta/preguntas.html')



def creditos(request):
    return render(request, 'composta/creditos.html')
