
text_analisis = input ("Ingrese el texto: ")
text_analisis_minimizado = text_analisis.lower()



letter_1 = input ("Ingrese una letra: ")
letter_1_min = letter_1.lower()


letter_2 = input ("Ingrese otra letra: ")
letter_2_min = letter_2.lower()

letter_3 = input ("Ingrese una última letra: ")
letter_3_min = letter_3.lower()

letter_list = [letter_1.lower(),letter_2.lower(),letter_3.lower()]





print ("""A continuación se le adjunta información acerca del texto y las letras
proporcionadas:

#### #### #### ####""")

#1

print (f"1. Número de veces que aparecen las letras que ha elegido:")


print (f"{letter_list[0]} es {(letter_list.count(letter_1))}")

print (f"{letter_list[1]} es {(letter_list.count(letter_2))}")

print (f"{letter_list[2]} es {(text_analisis_minimizado.count(letter_3_min))}")





#2
print (f"""2. Numeración de palabras y carácteres
palabras: {(len(text_analisis.split()))}
carácteres (incluye espacios): {(len(text_analisis))}

""")

#3
print (f"""3. La primera letra del texto es ' {text_analisis[0]} ', y la última es ' {text_analisis[-1]} '

""")

#4
print (f"""4. Texto invertido
Texto invertido por letras: ' {text_analisis[::-1]} '""")
text_list = text_analisis.split()
text_list.reverse()
invertido = ' '.join(text_list)

print (f"Texto invertido por palabras: ' {invertido} '")

print ("\n")


#5

print (f"5. Aparece la palabra 'Python' en su texto? La respuesta es: {'Python' in text_analisis}")

if 'Python' in text_analisis:
    print ("SIIII hay python!")
else:
    print ("NOOOO hay python!")









