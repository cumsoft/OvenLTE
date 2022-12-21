#################################################################
#################################################################
#                                                               #
#     `-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"          #
#        `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/            #
#          y==/        y==/        y==/        y==/             #
#        ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.           #
#     ,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_          #
#                                                               #
#    ▄▄█▀▀▀▄█                                      ▄▀█▄   ▄     #
#  ▄█▀     ▀  ▄▄▄ ▄▄▄  ▄▄ ▄▄ ▄▄    ▄▄▄▄    ▄▄▄   ▄██▄   ▄██▄    #
#  ██          ██  ██   ██ ██ ██  ██▄ ▀  ▄█  ▀█▄  ██     ██     #
#  ▀█▄      ▄  ██  ██   ██ ██ ██  ▄ ▀█▄▄ ██   ██  ██     ██     #
#   ▀▀█▄▄▄▄▀   ▀█▄▄▀█▄ ▄██ ██ ██▄ █▀▄▄█▀  ▀█▄▄█▀ ▄██▄    ▀█▄▀   #
#                                                               #
#      `-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"         #
#         `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/           #
#           y==/        y==/        y==/        y==/            #
#         ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.          #
#      ,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_         #
#################################################################
#   Copyright © 2022-Present by Cumsoft. All rights reserved.   #
#        This page was last updated on 20 December 2022.        #
#                                                               #
#           https://cumsoft.wixsite.com/cumsoft                 #
#               https://github.com/cumsoft                      #
#              https://cumsoft.gumroad.com                      #
#################################################################
#################################################################

I=float
import tkinter as B,subprocess as J
D=24
E=30
def H():
	F=J.run(['vcgencmd','measure_temp'],capture_output=True).stdout.decode();B=I(F.split('=')[1].split("'")[0])
	if B<D:C.config(fg='green')
	elif B<E:C.config(fg='yellow')
	else:C.config(fg='red')
	C.config(text=f"Temperature: {B:.1f}°C");A.after(1000,H)
A=B.Tk()
A.title('CPU Temperature Monitor')
C=B.Label(A,text='Temp:',font=('Arial',15))
C.pack()
F=B.Entry(A)
F.insert(0,D)
F.pack()
G=B.Entry(A)
G.insert(0,E)
G.pack()
def K():global D,E;D=I(F.get());E=I(G.get())
L=B.Button(A,text='Set Thresholds',command=K)
L.pack()
H()
A.mainloop()
