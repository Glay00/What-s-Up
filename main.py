import pywhatkit

def send_messege_inst():
    mobile =input("Введите номер получателя:")
    message= input("Введите текст сообщения:")
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

def main():
    send_messege_inst()

if __name__=='__main__':
    main()
