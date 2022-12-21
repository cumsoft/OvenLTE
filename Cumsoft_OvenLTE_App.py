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

import tkinter as B,subprocess as A
class C(B.Tk):
	def __init__(A):B.Tk.__init__(A);A.title('CPU Temperature Gauge');A.temperature_gauge=B.Canvas(A,width=200,height=100,bg='white');A.temperature_gauge.pack();A.temperature_label=B.Label(A,text='Temperature: N/A',font=('Helvetica',16));A.temperature_label.pack();A.update_button=B.Button(A,text='Turn On',command=A.update_temperature);A.update_button.pack();A.after(5000,A.update_temperature)
	def update_temperature(A):
		B='temp';D=A.get_cpu_temperature();A.temperature_label.config(text=f"Temperature: {D}°C");C=D/100.0;A.temperature_gauge.delete(B)
		if C>0.75:A.temperature_gauge.create_rectangle(0,0,200,100,fill='red',tags=B)
		elif C>0.5:A.temperature_gauge.create_rectangle(0,0,200,100,fill='orange',tags=B)
		elif C>0.25:A.temperature_gauge.create_rectangle(0,0,200,100,fill='yellow',tags=B)
		else:A.temperature_gauge.create_rectangle(0,0,200,100,fill='green',tags=B)
		A.after(5000,A.update_temperature)
	def get_cpu_temperature(D):B=A.run(['vcgencmd','measure_temp'],stdout=A.PIPE);C=B.stdout.decode('utf-8').strip().split('=')[1].split("'")[0];return float(C)
if __name__=='__main__':D=C();D.mainloop()
