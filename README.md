# Geotech
## XR18 MIDI Footswitch
When we are playing music, we use the Behringer XR18 digital mixer to mix the instruments together. In certain songs, the guitarist has to switch between clean and distorted guitar in the middle of the song, which is usually done with a footswitch. Unfortunately, the XR18 does not support normal footswitches. We solved this problem by creating our own Raspberry Pi powered MIDI footswitch.

We decided to use the Python programming language due to the ability to use third-party libraries to do certain tasks that Python does not support out of the box. The two libraries we used were Mido to send MIDI messages to the XR18 and rstem to get input from buttons. The code was simple. First, it imports the two libraries. Then, it establishes a connection to the XR18 and the button and LEDs. Next, it goes through a loop where it repeatedly checks if the button was pressed and switches from clean to distorted or vice versa and turns on the proper LED if it was.

To use this code, you must install the [Mido](https://github.com/olemb/mido/) and [rstem](https://github.com/readysetstem/readysetstem-api) Python libraries. Below is a table of the GPIO ports this program uses on the Raspberry Pi 2B.

| Component | Positive Port | Negitive Port |
| --- | --- | --- |
| Footswitch Button | GPIO04 | Ground |
| Clean LED | 3.3v | GPIO02 |
| Distorted LED | 3.3v | GPIO22 |

For more information, visit https://geotechgeeks.com/Footswitch.html.
