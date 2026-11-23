from django.shortcuts import render


# =========================
# 🏠 Inicio: ¿Qué es una composta?
# =========================
def home(request):

    # Los 4 ingredientes que necesita una composta
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

    # Los seres vivos que hacen el trabajo
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

    # Datos rápidos para la franja de números
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


# =========================
# 🪴 Cómo hacer composta paso a paso
# =========================
def como_hacer(request):
    return render(request, 'composta/como_hacer.html')


# =========================
# ✅ Materiales: qué sí y qué no
# =========================
def materiales(request):
    return render(request, 'composta/materiales.html')


# =========================
# 🌎 Beneficios
# =========================
def beneficios(request):
    return render(request, 'composta/beneficios.html')


# =========================
# ❓ Preguntas frecuentes
# =========================
def preguntas(request):
    return render(request, 'composta/preguntas.html')


# =========================
# 📷 Créditos de las fotografías
# =========================
def creditos(request):
    return render(request, 'composta/creditos.html')
