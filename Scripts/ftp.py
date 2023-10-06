from ftplib import FTP

def download_file(host, port, username, password, remote_file_path, local_file_path):
    # Establish a connection to the FTP server
    ftp = FTP()
    ftp.connect(host=host, port=port)
    ftp.login(user=username, passwd=password)

    # Open a local file to save the downloaded data
    with open(local_file_path, 'wb') as local_file:
        ftp.retrbinary('RETR ' + remote_file_path, local_file.write)

    # Close the FTP connection
    ftp.quit()

# Example usage
host = 'ftp2.tpdc.ac.cn'  # you can also change this to 'ftp3.tpdc.ac.cn'
port = 6201
username = 'download_90557606'
password = '52991412'
remote_file_path = 'path/to/remote/file/on/server.txt'  # Change this to the path of the file you want to download
local_file_path = 'path/to/save/file/on/local/machine.txt'  # Change this to the path where you want to save the downloaded file

download_file(host, port, username, password, remote_file_path, local_file_path)
