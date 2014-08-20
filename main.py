from sftpupload import sftpupload
import datetime, time
import config
import getpass
import os

start_time = datetime.time(config.startHour, config.startMinute)
end_time = datetime.time(config.endHour,config.endMinute)
timenow = datetime.datetime.now().time()
# TODO: compare time to see If it's in limits

try:
    os.system('cls')
    print("-"*70)
    print("**** Welcome to sftp Uploader v1.2 ****")
    print("-"*70)
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    while start_time < end_time:
        sftpUp = sftpupload.WarehouseOrdersUploader()
        print ("-"*70)
        sftpUp.connecttosftp(username,password)
        sftpUp.getwarehousefilesstatus()
        sftpUp.getlocalfilesstatus()
        sftpUp.uploadfiles()
        print("Operation completed successfully.")
        print("Running again in {} minute(s).".format(config.interval/60))
        time.sleep(config.interval)
except KeyboardInterrupt:
    print('You cancelled the operation. Goodbye.')





