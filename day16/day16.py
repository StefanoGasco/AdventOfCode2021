
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
        self.payload = []
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
            self.payload.append(self.get_chunk(4))


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


    def get_chunk(self, size):
        chunk = self.bytestring[self.cursor:self.cursor + size]
        self.cursor += size
        return int(chunk, 2)

main_packet = Packet(input_file())
res = main_packet.version
subpackets = main_packet.subpackets
while subpackets:
    new_packet = subpackets.pop()
    res += new_packet.version
    subpackets.extend(new_packet.subpackets)

print(res)
