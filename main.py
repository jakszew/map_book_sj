from tkinter import *



root = Tk()
root.geometry("1020x760")
root.title("Map Book")




ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly.grid(row=1, column=0 , columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="lista uzytkownikow")
label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow=Listbox(ramka_lista_obiektow, width=50, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly=Button(ramka_lista_obiektow, text='pokaz szczegoly')
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow, text='usun obiekt')
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='edytuj obiekt')
button_edytuj_obiekt.grid(row=2, column=2)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Imię:")
label_name.grid(row=1, column=0, sticky=W)
label_surname=Label(ramka_formularz, text="Nazwisko:")
label_surname.grid(row=2, column=0, sticky=W)
label_locatiom=Label(ramka_formularz, text="miejscowosc:")
label_locatiom.grid(row=3, column=0, sticky=W)
label_posts=Label(ramka_formularz, text="Postów:")
label_posts.grid(row=4, column=0, sticky=W)

entry_name=Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_surname=Entry(ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_locatiom=Entry(ramka_formularz)
entry_locatiom.grid(row=3, column=1)
entry_posts=Entry(ramka_formularz)
entry_posts.grid(row=4, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text='dodaj obiekt')
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

# ramka_szczegóły obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly, text="szczegoly obiektow")
label_szczegoly_obiektow.grid(row=0, column=0)
label_szczegoly_name=Label(ramka_szczegoly, text="imie")
label_szczegoly_name.grid(row=1, column=0)
label_szczegoly_name_wartosc=Label(ramka_szczegoly, text="...")
label_szczegoly_name_wartosc.grid(row=1, column=1)
label_szczegoly_surname=Label(ramka_szczegoly, text="nazwisko")
label_szczegoly_surname.grid(row=1, column=2)
label_szczegoly_surname_wartosc=Label(ramka_szczegoly, text="...")
label_szczegoly_surname_wartosc.grid(row=1, column=3)
label_szczegoly_location=Label(ramka_szczegoly, text="miejscowosc")
label_szczegoly_location.grid(row=1, column=4)
label_szczegoly_location_wartosc=Label(ramka_szczegoly, text="...")
label_szczegoly_location_wartosc.grid(row=1, column=5)
label_szczegoly_posts=Label(ramka_szczegoly, text="imie")
label_szczegoly_posts.grid(row=1, column=6)
label_szczegoly_posts_wartosc=Label(ramka_szczegoly, text="...")
label_szczegoly_posts_wartosc.grid(row=1, column=7)

#ramka_mapa
map_widget = tkintermapview.tk.MapWidget(ramka_mapa, width=800, height=400, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.0)
map_widget.zoom(6)




root.mainloop()
