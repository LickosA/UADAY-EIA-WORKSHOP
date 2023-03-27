import dns.resolver
import smtplib

def search_mx_records(domain):
    """ Recherche les enregistrements MX d'un domaine """
    try:
        mx_records = dns.resolver.query(domain, 'MX')
        return mx_records
    except Exception as e:
        print(f"Erreur lors de la recherche des enregistrements MX : {e}")

def connect_smtp_server(server, port):
    """ Établit une connexion SMTP partielle sur un serveur donné """
    try:
        server = smtplib.SMTP(server, port)
        server.ehlo()
        return server
    except Exception as e:
        print(f"Erreur lors de la connexion au serveur SMTP : {e}")

def identify_mail_server_software(server_banner):
    """ Identifie le logiciel de serveur de messagerie électronique installé sur un serveur """
    software_list = ["Postfix", "Microsoft Exchange", "Exim", "Sendmail"]
    for software in software_list:
        if software in server_banner:
            return software
    return "Inconnu"

# Exemple d'utilisation de ces fonctions
def main(domain="uac.bj"):
    server_valid = {}
    server_valids = []
    mx_records = search_mx_records(domain)
    print(mx_records)
    for mx in mx_records:
        server = mx.exchange.to_text().rstrip('.')
        smtp_server = connect_smtp_server(server, 25)
        if smtp_server:
            server_banner = smtp_server.ehlo("ua")
            #print(server_banner)
            smtp_server.quit()
            if "SMTPUTF8" in str(server_banner):
                mail_server_software = identify_mail_server_software(server_banner)
                print(f"Le serveur {server} est compatible EIA et utilise le logiciel {mail_server_software}")
                server_valid["server_name"] = server
                server_valid["isvalid_eia"] = True
                server_valid["mail_server_software"] = mail_server_software
                server_valids.append(server_valid)
            else:
                print(f"Le serveur {server} n'est pas compatible EIA")
                server_valid["server_name"] = server
                server_valid["isvalid_eia"] = False
                server_valid["mail_server_software"] = mail_server_software
                server_valids.append(server_valid)
    return server_valids