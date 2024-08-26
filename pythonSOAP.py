from spyne import Application, rpc, ServiceBase, Integer, Double
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Defina o serviço de calculadora com várias operações
class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Double)
    def add(ctx, x, y):
        return x + y

    @rpc(Integer, Integer, _returns=Double)
    def subtract(ctx, x, y):
        return x - y

    @rpc(Integer, Integer, _returns=Double)
    def multiply(ctx, x, y):
        return x * y

    @rpc(Integer, Integer, _returns=Double)
    def divide(ctx, x, y):
        if y == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return x / y

# Crie a aplicação SOAP
application = Application(
    [CalculatorService],
    tns='example.calculator',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

# Crie a aplicação WSGI
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    # Use o servidor WSGI do Python para rodar a aplicação
    from wsgiref.simple_server import make_server

    server = make_server('127.0.0.1', 8000, wsgi_application)
    print("Servidor SOAP rodando em http://127.0.0.1:8000")
    server.serve_forever()
