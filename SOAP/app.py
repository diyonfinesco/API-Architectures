from zeep import Client

def soap_example():
    wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"
    client = Client(wsdl)

    result = client.service.Add(5, 3)
    print(f"SOAP Add result: {result}")

if __name__ == "__main__":
    print("SOAP example")
    soap_example()