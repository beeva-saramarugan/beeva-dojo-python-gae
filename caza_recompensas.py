import random
import time
from personas.Villano import Villano
from personas.Chivato import Chivato

MAX_PERSONAS = 15
MIN_PERSONAS = 10
MAX_DISTANCIA = 100.0
MAX_VIDA = 72.0
MAX_RECOMPENSA = 5000.0
SEMANA = {1: 'Lunes', 2: 'Martes', 3: 'Miercoles', 4: 'Jueves',
          5: 'Viernes', 6: 'Sabado', 7: 'Domingo'}
HORAS_DIA = 24

def generar_aleatorio(villanos, chivatos):
    """Genera aleatoriamente una lista de villanos y de chivatos"""
    random.seed(time.time())
    n_villanos = random.randint(MIN_PERSONAS, MAX_PERSONAS)
    n_chivatos = random.randint(MIN_PERSONAS, MAX_PERSONAS)
    print "# N_VILLANOS " + str(n_villanos)
    print "# N_CHIVATOS " + str(n_chivatos)

    for i in range(1, n_villanos):
        villano = Villano()
        villano.set_name("Villano" + str(i))
        villano.set_vidas(random.randint(1, MAX_VIDA))
        villano.set_distancia(random.randint(1, MAX_DISTANCIA))
        villano.set_recompensa(random.randint(1, MAX_RECOMPENSA))
        villano.set_es_chivato(bool(random.getrandbits(1)))

        villanos.append(villano)

    for i in range(1, n_chivatos):
        rand1 = random.randint(0, len(villanos)/2)
        rand2 = random.randint(rand1, len(villanos)-1)

        villanos_random = villanos[rand1:rand2]
        chivato = Chivato()
        chivato.set_name("Chivato" + str(i))
        chivato.set_villanos(villanos_random)

        chivatos.append(chivato)

def descubrir_villanos(chivatos):
    """Extrae la lista de villanos descubiertos, filtrando los que son ademas chivatos"""
    villanos = []
    for i in range(0, len(chivatos)-1):
        villanos.extend(chivatos[i].get_villanos())

    villanos_descubiertos = list(set(villanos))
    villanos_descubiertos = filter(lambda x: x._es_chivato == False, villanos_descubiertos)

    return villanos_descubiertos

def ordenar_villanos(villanos_descubiertos):
    """Ordena la lista de villanos en base a la distancia mas cercana"""
    villanos_odernados = sorted(villanos_descubiertos,
                                key=lambda villano: villano._distancia)

    return villanos_odernados

def planificar_semana(villanos_ordenados):
    """Planifica la semana con la lista de villanos ordenados"""
    gastos = 0
    ingresos = 0
    horario = {}
    planning = []

    n_villanos = 0
    horas_gastadas = 0
    for i in range(0, len(villanos_ordenados)):
        vidas = villanos_ordenados[i].get_vidas()

        # Si al siguiente villano en orden ya no da tiempo a darle caza,
        # comprueba el resto de villanos por si alguno mas le diera tiempo
        skip = (horas_gastadas + vidas) > HORAS_DIA*len(SEMANA)
        if not skip:
            gastos = gastos + villanos_ordenados[i].get_distancia()

            for vida in range(0, vidas):
                if horas_gastadas < HORAS_DIA:
                    dia = 1
                else:
                    dia = (horas_gastadas / HORAS_DIA) + 1

                hora = horas_gastadas % HORAS_DIA
                planning.append(SEMANA[dia] + " - " + str(hora) + " H -> " +
                                villanos_ordenados[i].get_name())
                horas_gastadas = horas_gastadas + 1

            # Ha dado caza a otro villano, suma a sus ingresos
            ingresos = ingresos + villanos_ordenados[i].get_recompensa()
            n_villanos += 1

    # Ha completado el horario de la semana
    horario = {'nvillanos':n_villanos, 'plan':planning, 'gastos':gastos, 'ingresos':ingresos}

    return horario


def imprimir_horario(villanos_ordenados, horario):
    """Imprime la planificacion de la semana"""

    print "# VILLANOS A DAR CAZA:"
    for i in range(0, horario['nvillanos']):
        info = str(villanos_ordenados[i].get_vidas()) + " puntos de vida, "
        info = info + str(villanos_ordenados[i].get_recompensa()) + " euros de recompensa, "
        info = info + str(villanos_ordenados[i].get_distancia()) + "m de distancia"
        print "> " + villanos_ordenados[i].get_name() + ": " + info

    print "# HORARIO"
    for i in range(0, len(horario['plan'])):
        print horario['plan'][i]

    print "# GASTOS " + str(horario['gastos'])
    print "# INGRESOS " + str(horario['ingresos'])
    print "# BENEFICIOS " + str(horario['ingresos']-horario['gastos'])

def main():
    villanos = []
    chivatos = []
    generar_aleatorio(villanos, chivatos)

    villanos_descubiertos = []
    villanos_descubiertos = descubrir_villanos(chivatos)
    print "# N_VILLANOS_DESCUBIERTOS " + str(len(villanos_descubiertos))

    if len(villanos_descubiertos) != 0:
        villanos_ordenados = ordenar_villanos(villanos_descubiertos)
        horario = planificar_semana(villanos_ordenados)
        imprimir_horario(villanos_ordenados, horario)

    else:
        print "NO HA SACADO INFORMACION SOBRE VILLANOS"

main()
