import subprocess
import os


def create_cert(
        directory,
        cert_conf_file_name,
        pk_file_name,
        pem_certificate_file_name
):
    """
    This function creates the certificate necessary for connecting to OPC.
    The certificate is created if it does not already exist in the project.
    """

    certificate_folder = directory
    ensure_directory_exists(certificate_folder)

    cert_conf_extension = ".conf"
    cert_conf = os.path.abspath(os.path.join(certificate_folder, f"{cert_conf_file_name}{cert_conf_extension}"))
    create_cert_conf(cert_conf)

    pk_extension = ".pem"
    pk = os.path.join(certificate_folder, f"{pk_file_name}{pk_extension}")
    create_private_key(pk)

    pem_cert_extension = ".pem"
    pem_cert = os.path.join(certificate_folder, f"{pem_certificate_file_name}{pem_cert_extension}")
    create_certificate(pem_cert, pk, cert_conf)



def ensure_directory_exists(
    directory
):
    """
    Ensures that the specified directory exists. Creates the directory if it does not exist.

    Args:
        directory (str): The path of the directory to check/create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_cert_conf(
    cert_conf_file_name
):
    """
    Creates a cert.conf file with the necessary configuration for generating certificates.

    Args:
        cert_conf_file_name (str): The full path to the cert.conf file.
        machine (str): The machine name to be included in the certificate.
    """
    if os.path.exists(cert_conf_file_name):
        return

    with open(cert_conf_file_name, "w", encoding='utf-8') as file:
        file.write("[ req ]\n")
        file.write("default_bits = 2048\n")
        file.write("default_md = sha256\n")
        file.write("distinguished_name = subject\n")
        file.write("req_extensions = req_ext\n")
        file.write("x509_extensions = v3_ca\n")
        file.write("string_mask = utf8only\n")
        file.write("prompt = no\n\n")
        file.write("[ req_ext ]\n")
        file.write("nsCertType = client, server\n")
        file.write("extendedKeyUsage= serverAuth, clientAuth\n")
        file.write('nsComment = "OpenSSL Tutorial for IRC5 OPC-UA"\n\n')
        file.write("[ v3_ca ]\n")
        file.write("subjectKeyIdentifier = hash\n")
        file.write("authorityKeyIdentifier = keyid:always,issuer:always\n")
        file.write("basicConstraints = CA:TRUE\n")
        file.write("keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment, keyCertSign\n")
        file.write(f"subjectAltName = URI:urn:freeopcua:client,DNS:DESKTOP\n\n")
        file.write("[ subject ]\n")
        file.write("countryName = SE\n")
        file.write("stateOrProvinceName = VG\n")
        file.write("localityName = VG\n")
        file.write("organizationName = ABB\n")
        file.write(f"commonName = DESKTOP")


def create_private_key(
    pk_file_name
):
    """
    Generates a private key and saves it to the specified file.

    Args:
        pk_file_name (str): The path to the file where the private key will be saved.
    """
    if os.path.exists(pk_file_name):
        return

    command = r'"./openssl/bin/openssl.exe" genrsa -out ' + pk_file_name + ' 2048'
    subprocess.run(command, shell=True, capture_output=True, text=True, check=False)


def create_certificate(
    pem_certificate_filename,
    pk_file_name,
    cert_conf_file_name
):
    """
    Generates a PEM certificate using the specified private key and configuration file.

    Args:
        pem_certificate_filename (str): The path to the file where
        the PEM certificate will be saved.
        pk_file_name (str): The path to the private key file.
        cert_conf_file_name (str): The path to the cert.conf configuration file.
    """
    if os.path.exists(pem_certificate_filename):
        return

    command =rf'"./openssl/bin/openssl.exe" req -x509 -days 365 -new -out ./{pem_certificate_filename} -key ./{pk_file_name} -config "{cert_conf_file_name}"'
    print(command)
    subprocess.run(command, shell=True, capture_output=True, text=True, check=False)