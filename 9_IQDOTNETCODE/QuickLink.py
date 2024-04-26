import pyshorteners
import validators
import pyperclip
import requests
from colorama import Fore, Style, init

class URLShortener:
    """
    QuickLink: encurtador de URL avançado
    Uma classe para encurtar URLs usando diferentes serviços.
    Esta classe encapsula a funcionalidade de encurtamento e oferece suporte a vários serviços.
    """
    def __init__(self, bitly_api_key):
        """Inicialize o URLShortener com um objeto encurtador e um mapeamento de serviço."""
        self.shortener = pyshorteners.Shortener(api_key=bitly_api_key)
        self.service_mapping = {
            "tinyurl": self.shortener.tinyurl.short,
            "bitly": self.shortener.bitly.short,
            "isgd": self.shortener.isgd.short
        }

    def shorten_url(self, url, service="TinyURL"):
        """
        Encurte um URL usando o serviço de redução especificado.
        
        Args:
            url (str): O URL a ser encurtado.
            service (str): O serviço de encurtamento a ser usado (o padrão é TinyURL).

        Returns:
            str: O URL encurtada.

        Raises:
            ValueError: Se o URL for inválido ou o serviço não for compatível.
            ConnectionError: Se não houver conexão com a Internet.
        """
        if not validators.url(url):
            raise ValueError("O URL inserido não é válido.")
        
        if not self.check_internet_connection():
            raise ConnectionError("Sem conexão com a Internet. Por favor, verifique sua conexão.")

        try:
            short_function = self.service_mapping[service.lower()]
        except KeyError:
            raise ValueError("O serviço de encurtamento não é válido.")
        
        return short_function(url)

    def check_internet_connection(self):
        """Verifique se há uma conexão com a Internet fazendo ping no Google."""
        try:
            requests.get("https://www.iqdotnet.net", timeout=5)
            return True
        except requests.ConnectionError:
            return False

def main():
    """Função principal para executar o QuickLink: Advanced URL Shortener em um loop até que o usuário decida sair."""
    init(autoreset=True)  # Inicialize o colorama para redefinir as cores automaticamente
    print(Fore.CYAN + "Bem-vindo ao QuickLink: Encurtador de URL avançado")
    
    # Definir a chave da API do Bitly
    bitly_api_key = 'YOUR_BITLY_API_KEY'
    
    url_shortener = URLShortener(bitly_api_key)

    try:
        while True:
            url = input("Digite o URL para encurtar (ou 'exit' para sair): ")
            if url.lower() == "exit":
                print(Fore.GREEN + "Até mais!")
                break

            service = input("Escolha o serviço de encurtamento de URL (TinyURL, Bitly, IS.gd): ")
            
            try:
                shortened_url = url_shortener.shorten_url(url, service)
                print(Fore.YELLOW + "URL encurtado: " + Fore.LIGHTGREEN_EX + shortened_url)
                pyperclip.copy(shortened_url)
                print(Fore.GREEN + "URL encurtado copiado para a área de transferência.")
            except ValueError as e:
                print(Fore.RED + "Error: " + str(e))
            except ConnectionError as e:
                print(Fore.RED + "Error: " + str(e))
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nPrograma interrompido. Adeus!")

if __name__ == "__main__":
    main()
#IQDOTNET CODE - by NelsoN