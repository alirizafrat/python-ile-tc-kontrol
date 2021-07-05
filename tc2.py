from suds.client import Client
WSDL_URL="https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL"
client=Client(WSDL_URL)
a1 = input("TCKimlikNo : ")
a2 = input("Ad : ")
a3 = input("Soyad : ")
a4 = input("DogumYili : ")
args={
    "TCKimlikNo":a1,
    "Ad":a2.upper(),
    "Soyad":a3.upper(),
    "DogumYili":int(a4)}
def tcKimlikDogrula(params):
    try:
        return  client.service.TCKimlikNoDogrula(**params)
    except Exception as e:
        return False
if tcKimlikDogrula(args):
    print("Kayıt Mevcut")
else:
    print("Kayıt Bulunamadı")
