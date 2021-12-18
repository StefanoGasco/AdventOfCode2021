
ENV = 'real'

def input_file():
    with open(f'{ENV}_file.txt') as f:
        hexa = f.read()
        return bin(int(hexa, 16))[2:].zfill(len(hexa)*4)

class Packet():

    def __init__(self, bytestring, cursor=0):
        self.bytestring = bytestring
        self.cursor = cursor
        self.subpackets = []
        self.payload = ""
        self.version_size = 3
        self.version = self.get_chunk(self.version_size)
        self.type_size = 3
        self.type = self.get_chunk(self.type_size)
        self.behavior = "literal" if self.type == 4 else "operator"
        if self.behavior == "literal":
            self.get_payload()
        else:
            self.get_subpackets()

    def get_payload(self):
        self.shift_size = 1
        new_packet = 1
        while new_packet == 1:
            new_packet = self.get_chunk(self.shift_size)
            self.payload += self.get_chunk(4, False)


    def get_subpackets(self):
        self.id_size = 1
        self.id = self.get_chunk(self.id_size)
        self.length_size = 11 if self.id == 1 else 15
        self.length = self.get_chunk(self.length_size)
        i = 0
        while i < self.length:
            new_packet = Packet(self.bytestring, self.cursor)
            self.subpackets.append(new_packet)
            if self.id == 1:
                i += 1
            else:
                i += (new_packet.cursor - self.cursor)
            self.cursor = new_packet.cursor

    def get_value(self):
        if self.behavior == "operator":
            self.payload = [packet.get_value() for packet in self.subpackets]
        else:
            return(int(self.payload, 2))
        if self.type == 0:
            return sum(self.payload)
        elif self.type == 1:
            return self.multiply(self.payload)
        elif self.type == 2:
            return min(self.payload)
        elif self.type == 3:
            return max(self.payload)
        elif self.type == 5:
            return 1 if self.payload[0] > self.payload[1] else 0
        elif self.type == 6:
            return 1 if self.payload[0] < self.payload[1] else 0
        elif self.type == 7:
            return 1 if self.payload[0] == self.payload[1] else 0

    def multiply(self, array):
        product = 1
        for i in array:
            product = product * i
        return product

    def get_chunk(self, size, decimal = True):
        chunk = self.bytestring[self.cursor:self.cursor + size]
        self.cursor += size
        if decimal:
            return int(chunk, 2)
        else:
            return chunk

main_packet = Packet(input_file())
res = main_packet.version
subpackets = main_packet.subpackets

print(main_packet.get_value())
