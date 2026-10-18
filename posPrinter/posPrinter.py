import usb.core
import usb.util

class PosPrinter:
    def __init__(self, vendor_id=None, product_id=None, inter = 0, alt = 1):
        if vendor_id is None or product_id is None:
            raise Exception('Vendor ID and Product ID not provided')
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.printer = usb.core.find(idVendor=self.vendor_id, idProduct=self.product_id)
        self.printer.set_configuration()
        self.printer.set_interface_altsetting(inter, alt)

        self.cfg = self.printer.get_active_configuration()
        self.interface = self.cfg[(0, 1)]



        self.endpoint = usb.util.find_descriptor(self.interface, custom_match=lambda e:
                                                 usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)

        if self.endpoint is None:
            raise Exception('Endpoint not found')

        print(f'Printer found at endpoint: {self.endpoint.bEndpointAddress:02X}')

    """Initialise printer"""
    def initialise(self):
        self.endpoint.write(b"\x1b@") #used to initialise the printer

    """Write text with line return at end of phrase"""
    def write_text(self, text: str):
        self.endpoint.write(bytes(text + "\n", 'utf-8'))

    """Write text to the printer without a line return at the end of each phrase"""
    def dump_write(self, text: str):
        self.endpoint.write(bytes(text, 'utf-8'))

    """Send a cut command to the printer. 0 = partial cut 1 = full cut."""
    def paper_cut(self, cut_type: int):
        if cut_type == 0:
            self.endpoint.write(b"\x1DV\x00")
        elif cut_type == 1:
            self.endpoint.write(b"\x1DV\x01")

    def buzzer(self, time: int):
        self.endpoint.write(b"\x1B\x1E")

