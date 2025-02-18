import psutil
import wmi
class Sistema:
    @staticmethod
    def espaco_livre_hd() -> str:
        resposta = psutil.disk_usage('/').free / (1024**3)  # Conversão para GB
        return f"Espaco livre no HD: {resposta:.2f} GB"

    @staticmethod
    def qtd_processadores() -> str:
        resposta = psutil.cpu_count(logical=True)
        return f"Quantidade de CPUs: {resposta}"

    @staticmethod
    def espaco_memoria() -> str:
        resposta = psutil.virtual_memory().available / (1024**3)  # Memória disponível em GB
        return f"Memoria RAM Livre: {resposta:.2f} GB"
    
    # @staticmethod
    # def temperatura() -> int:
    #     w = wmi.WMI(namespace="root\\wmi")
    #     temperaturas = w.MSAcpi_ThermalZoneTemperature()
    #     for temp in temperaturas:
    #          if temp.Name and "CPU" in temp.Name:
    #                 # A temperatura é retornada em décimos de Kelvin, então convertemos para Celsius
    #                 resposta = (temp.CurrentTemperature / 10.0) - 273.15
    #                 return f"Temperatura do processador: {resposta:.2f}°C"
