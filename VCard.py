try:
    import qrcode
except:
    from os import system
    system("pip install qrcode")
    import qrcode
class Bot():
    def createVCard(self,dados):
        return f'BEGIN:VCARD\nVERSION:3.0\nN:{dados["LastName"]} {dados["FirstName"]}\nFN:{dados["FirstName"]} {dados["LastName"]}\nORG:{dados["Company"]}\nTITLE:{dados["Title"]}\nEMAIL;WORK;INTERNET:{dados["Email"]}\nTEL;WORK;VOICE:{dados["Celular"]}\nADR;WORK;PREF:;;{dados["Address"]}\nURL:{dados["url"]}\nREV:1\nEND:VCARD\n'
    def __init__(self,dados:dict) -> None:
        self.VCard = self.createVCard(dados)
        self.FileName = dados["Name"].replace(" ","_")+".jpg"
    def create(self):
        qr = qrcode.QRCode(version=3,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=1,)
        qr.add_data(self.VCard)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"./Output/{self.FileName}")
