import mido
from rstem.button import Button
from rstem.gpio import Output

output=mido.open_output('X18/XR18 MIDI 1')
button=Button(4)
clean_led=Output(2)
distorted_led=Output(22)

output.send(mido.Message('control_change', channel=1))
output.send(mido.Message('control_change', channel=1, control=1, value=127))
distorted=False
clean_led.on()
distorted_led.off()
while True:
    if button.presses():
        if distorted==True:
            output.send(mido.Message('control_change', channel=1))
            output.send(mido.Message('control_change', channel=1, control=1, value=127))
            distorted=False
            clean_led.on()
            distorted_led.off()
        elif distorted==False:
            output.send(mido.Message('control_change', channel=1, value=127))
            output.send(mido.Message('control_change', channel=1, control=1))
            distorted=True
            clean_led.off()
            distorted_led.on()
