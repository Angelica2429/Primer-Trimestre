texto=("El conocimiento es poder")
print(texto.find("conocimiento"))
print(texto.find("poder"))

texto1=("la practica hace al maestro")
print(texto1.find("Practica"))
print(texto1.find("maestro"))

frase=input("Ingrese una frase:")
pregunta=input("¿Qué palabra quieres buscar en la frase?:")
print(frase.find("pregunta"))


texto=("Puede que la tarea que me he impuesto de escribir una historia completa del pueblo romano desde el comienzo mismo de su existencia me recompense por el trabajo invertido en ella, no lo sé con certeza, ni creo que pueda aventurarlo. Porque veo que esta es una práctica común y antiguamente establecida, cada nuevo escritor está siempre persuadido de que ni lograrán mayor certidumbre en las materias de su narración, ni superarán la rudeza de la antigüedad en la excelencia de su estilo. Aunque esto sea así, seguirá siendo una gran satisfacción para mí haber tenido mi parte también en investigar, hasta el máximo de mis capacidades, los anales de la nación más importante del mundo, con un interés más profundo; y si en tal conjunto de escritores mi propia reputación resulta ocultada, me consuelo con la fama y la grandeza de aquellos que eclipsen mi fama. El asunto, además, es uno que exige un inmenso trabajo. Se remonta a más de 700 años atrás y, después de un comienzo modesto y humilde, ha crecido a tal magnitud que empieza a ser abrumador por su grandeza. No me cabe duda, tampoco, que para la mayoría de mis lectores los primeros tiempos y los inmediatamente siguientes, tienen poco atractivo; Se apresurarán a estos tiempos modernos en los que el poderío de una nación principal es desgastado por el deterioro interno. Yo, en cambio, buscaré una mayor recompensa a mis trabajos en poder cerrar los ojos ante los males de que nuestra generación ha sido testigo durante tantos años; tanto tiempo, al menos, como estoy dedicando todo mi pensamiento a reproducir los claros registros, libre de toda la ansiedad que pueden perturbar el historiador de su época, aunque no le puedan deformar la verdad.")
print(texto.find("Puede"))
print(texto.find("atractivo"))
print(texto.find("verdad"))
print(texto[1194:1707])

Texto=("Hace años, y de intento no se señala cuál, hubo en México una causa célebre. Los autos pasaban de 2,000 fojas y pasaban también de manos de un juez a las de otro juez, sin que pudieran concluir. Algunos de los magistrados tuvieron una muerte prematura y muy lejos de ser natural. Personas de categoría y de buena posición social estaban complicadas, y se hicieron, por este y otros motivos, poderosos esfuerzos para echarle tierra, como se dice comúnmente; pero fue imposible. El escándalo había sido grande, la sociedad de la capital y aun de los Estados había fijado su atención, y se necesitaba un castigo ejemplar para contener desmanes que tomaban grandes proporciones. Se hicieron muchas prisiones, pero a falta de pruebas, los presuntos reos eran puestos en libertad. Al fin llegó a descubrirse el hilo, y varios de los culpables fueron juzgados, condenados a muerte y ejecutados. El principal de ellos, que tenía una posición muy visible, tuvo un fin trágico. De los recuerdos de esta triste historia y de diversos datos incompletos, se ha formado el fondo de esta novela; pero ha debido aprovecharse la oportunidad para dar una especie de paseo por en medio de una sociedad que ha desaparecido en parte, haciendo de ella, si no pinturas acabadas, al menos bocetos de cuadros sociales que parecerán hoy tal vez raros y extraños, pues que las costumbres en todas las clases se han modificado de tal manera que puede decirse sin exageración que desde la mitad de este siglo a lo que va corrido de él, México, hasta en sus edificios, es otra cosa distinta de lo que era en 1810.")
print(Texto.find("Hace"))
print(Texto.find("capital"))
print(Texto.find("1810"))
print(Texto[527:1583])

nombre=input("Ingrese su nombre: ")
nota1=float(input("Ingrese la nota de castellano: "))
nota2=float(input("Ingrese la nota de ingles: "))
nota3=float(input("Ingrese la nota de sociales: "))
porcentaje1=nota1 * 0.20
porcentaje2=nota2 * 0.30
porcentaje3=nota3 * 0.50
operacion=porcentaje1+porcentaje2+porcentaje3
nota_final= operacion 
print(f"",nombre,",su nota final es:",nota_final)



