import auth
import otp_sender
import dashboard
print("ENTER MAIL ID")
email=input()
if auth.auth_user(email)==1:
    rcv_otp=otp_sender.otp_sender(email)
    print("AN OTP HAS BEEN SENT TO THE REG. MAIL ID. PLEASE ENTER THE OTP TO LOGIN !")
    inp_otp=input()
    if rcv_otp == inp_otp:
        print("VALIDATION SUCCESSFUL")
        dashboard.dashboard()
    else:
        print("INVALID OTP")
        exit()
else:
    print("USER NOT REGISTERED. PLEASE SEND AN EMAIL TO group6@apsjorhat.org TO REGISTER")
    exit()