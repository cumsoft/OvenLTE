##  /|\༼ ಠ益ಠ ༽/|\    <{[Thank you for your purchase]}

### Cumsoft_Rpi_OvenLTE CPU Monitor <3

![Image text](https://github.com/cumsoft/OvenLTE/blob/8fb741d7c4441a6a226eb3358b961d5a79b44bda/Cumsoft_OvenLTE_ScreenShot.png)

# 𝘛𝘢𝘣𝘭𝘦 𝘰𝘧 𝘊𝘰𝘯𝘵𝘦𝘯𝘵𝘴
1. [Software Info](### 𝘚𝘰𝘧𝘵𝘸𝘢𝘳𝘦 𝘐𝘯𝘧𝘰)
2. [Screenshot](### 𝘚𝘤𝘳𝘦𝘦𝘯𝘴𝘩𝘰𝘵)
4. [Software Install](### 𝘚𝘰𝘧𝘵𝘸𝘢𝘳𝘦 𝘐𝘯𝘴𝘵𝘢𝘭𝘭𝘢𝘵𝘪𝘰𝘯)
5. [How2Use](### 𝘏𝘰𝘸 𝘵𝘰 𝘜𝘴𝘦)
6. [Resources](### 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴)
7. [License](## 𝘚𝘰𝘧𝘵𝘸𝘢𝘳𝘦 𝘓𝘪𝘤𝘦𝘯𝘴𝘦)
8. [Cumsoft](## 𝘾𝙪𝙢𝙨𝙤𝙛𝙩 𝘾𝙤𝙥𝙮𝙧𝙞𝙜𝙝𝙩 © ２０２２)

### 𝘚𝘰𝘧𝘵𝘸𝘢𝘳𝘦 𝘐𝘯𝘧𝘰
> Cumsoft OvenLTE is a simple interface that reads realtime cpu core tempature feedabck via Celsius tempature readout and helpful color coding. 
> The OvenLTE is the perfect tool for CPU overclocking. 
>
> This Release comes with two Apps:
> "Cumsoft_OvenLTE_App" & "Cumsoft_OvenLTE_Dev"
>
> The "Cumsoft_OvenLTE_App" has been preconfigured to estimate thresholds of the baseline CPU temp. More importantly it relays this information via color schemes which gives quick feedback on core system cpu temp changes. It is visible on the desktop and can be even read from afar.
>
> The "Cumsoft_OvenLTE_Dev" does not have preconfigured thresholds and allows the user to set them via minimum and maximum user input. Its function is still the same as the "App", However its legiblity is constrainted thus is better for users who are infront of console.
>
> Lastly it is important to note that the Cumsoft OvenLTE will run on debian with no additional packages needed. This software can run on other distros of linux but may require additional tooling and configuration. The Cumsoft OvenLTE framework is built off python and its legacy system assets. This means that you can launch the Cumsoft OvenLTE locally via Linux or have it run from the python/python3 folder.


### 𝘚𝘤𝘳𝘦𝘦𝘯𝘴𝘩𝘰𝘵
![Image text](https://github.com/cumsoft/OvenLTE/blob/f8556b391f13dbd31b1963583c3f106371edfe11/Cumsoft_OvenLTE_ScreenShot2.png)

### 𝘚𝘰𝘧𝘵𝘸𝘢𝘳𝘦 𝘐𝘯𝘴𝘵𝘢𝘭𝘭𝘢𝘵𝘪𝘰𝘯

*Browser installation*
- Download from source: (https://cumsoft.gumroad.com/l/OvenLTE)
- Navigate to target folder: Search keyword "Cumsoft_OvenLTE or "../user//Cumsoft_OvenLTE.zip/.."
- Decompress/Unzip folder with your choice of software 
- Open Terminal and Navigate to the folder.
- Open with Python or Python3.

> Dont Have Python installed?

Install Python3
1. $ sudo apt-get update && sudo apt-get install python3 (Debian)
2. $ sudo dnf install python3 (Other Linux Distros)
3. $ sudo pacman -S python3 (Manjaro)

Install pip 
1. $ python get-pip.py (Linux & MacOS)
2. $ sudo pacman -S python-pip3 (Manjaro)
3. check version is $ pip -V

Install tkinter
1. $ pip install tk
2. Configure tk with python: $ sudo pacman -S tk

Install vcgencmd

1. Install Globally:$ sudo pip3 install vcgencmd
2. Install locally:$ pip3 install --user vcgencmd

3. NPM alternative npmjs.com/package/vcgencmd: $ npm install vcgencmd

```
*Cumsoft OvenLTE Window Assets Installation*

At this time it is recommended to install python via gui here: https://www.python.org/download/releases/2.4/msi/

Install python via CMD system wide silently
1. C:\Users\Username> python-3.9.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
Check if Python did installed
2. C:\Users\Username> python -V
Install Pip
3. C:\Users\Username> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
Install virtualnv (opional)
4. C:\Users\Username> pip install virtualenv

```
### 𝘏𝘰𝘸 𝘵𝘰 𝘜𝘴𝘦

> Cumsoft OvenLTE is a CPU Monitor, A CPU monitor is a software tool that tracks the usage or more specifically the tempature of the central processing unit (CPU) of a computer. It is important to track the temperature of a CPU (Central Processing Unit) because high temperatures can cause a variety of problems, including reduced performance and even permanent damage to the hardware. When a CPU operates at high temperatures for an extended period of time, it can cause the device to become unstable and potentially lead to hardware failures or system crashes. Additionally, high temperatures can cause the CPU to become less efficient, which can result in slower performance.
> 
> By monitoring the temperature of a CPU, you can ensure that it is operating within safe temperature limits and take action if necessary to prevent overheating. This can help to maintain the performance and lifespan of your device. Some common methods for tracking CPU temperature include using software tools or monitoring the temperature through the BIOS (Basic Input/Output System) settings on the device.
>
> There are several ways that a CPU temperature monitor can be utilized:
>
> 1. To ensure that the CPU is operating within safe temperature limits: By monitoring the temperature of the CPU, you can ensure that it is not overheating and that it is operating within the safe temperature range recommended by the manufacturer. If the temperature rises above a certain level, you can take steps to reduce the load on the CPU or improve cooling to bring the temperature down.
>
> 2. To detect and diagnose problems with the cooling system: If the temperature of the CPU is consistently high, it could be a sign that there is a problem with the cooling system. A temperature monitor can help you to identify such issues and take corrective action, such as cleaning the fans or replacing a faulty cooler.
>
> 3. To optimize performance: By monitoring the temperature of the CPU, you can identify situations where the temperature is causing the CPU to throttle its performance in order to prevent overheating. By addressing the underlying cause of the high temperature, you may be able to improve performance.
>
> 4. To monitor the effectiveness of cooling modifications: If you have made modifications to the cooling system of your device, a temperature monitor can help you to determine whether these modifications are effective in reducing the temperature of the CPU.
>
> 5. To monitor the temperature of a server or other critical system: In a server or other mission-critical system, it is important to ensure that the temperature of the CPU is within safe limits to prevent downtime or hardware failures. A temperature monitor can help you to monitor the temperature of the CPU in real-time and take action if necessary.
>

### 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴

| Resource | Url |
| ------ | ------ |
| vcgencmd | [https://www.nicm.dev/vcgencmd/] |
| Python / Python3 | [https://docs.python.org/3/] |
| Tkinter | [https://docs.python.org/3/library/tkinter.html] |
| Cumsoft's Teenyweeny | [https://github.com/cumsoft/Teenyweeny] |

## 𝘚𝘰𝘧𝘵𝘸𝘢𝘳𝘦 𝘓𝘪𝘤𝘦𝘯𝘴𝘦
> The MIT License (MIT)
Copyright © 2022 <copyright holders>
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
____________________________________________________________________________________
### Still got questions? send us an email: [Mail](mailto:cumsoft.subscribe@gmail.com)

## 𝘾𝙪𝙢𝙨𝙤𝙛𝙩 𝘾𝙤𝙥𝙮𝙧𝙞𝙜𝙝𝙩 © ２０２3
[Github](https://github.com/cumsoft) * [Website](https://cumsoft.wixsite.com/cumsoft) * [Instagram](https://instagram.com/cumsoftcumsoft?igshid=YmMyMTA2M2Y=) * [Gumroad](https://cumsoft.gumroad.com/)

### Latest Updates
> If you would like to see a certian design implimented in the next release, feel free to write our devs with suggestions @ the email listed above.
>
>
> Coded with <3 by the Cumsoft Dev Team :)

