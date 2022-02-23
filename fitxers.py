#variable amb la que treballarem posterorment al fitxer: file

#crear document, escriure nums del 0 al 100 i tancar document

#modo read, r
#modo append, a(també crea fitxer)
#modo write, w (també crea)
#modo create, x

#escriure dins fitxer de text: nom_fitxer.write(var)

file = open("doc_0-100", "a") #obrir doc

for i in range (0, 100):
    file.write(str(i) +"\n")

file.close() #tancar doc