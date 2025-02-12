from PySide6.QtCore import QObject, Signal, Slot

class MyObject(QObject):
    # Define a signal
    my_signal = Signal(str)

    def __init__(self):
        super().__init__()

    def emit_signal(self):
        # Emit the signal with a string argument
        self.my_signal.emit("Hello, World!")

class MyReceiver(QObject):
    @Slot(str)
    def my_slot(self, message):
        print(f"Received message: {message}")

# Create instances of the objects
sender = MyObject()
receiver = MyReceiver()

# Connect the signal to the slot
sender.my_signal.connect(receiver.my_slot)

# Emit the signal
sender.emit_signal()90







++-+--+ ---