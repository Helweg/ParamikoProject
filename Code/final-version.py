import tkinter
from tkinter import messagebox
import paramiko
from paramiko import SSHClient
from scp import SCPClient

class Gui:
	def __init__(self):

		#Main window
		self.main_window = tkinter.Tk()

		#Set Window Default Size
		self.main_window.geometry('400x300')

		#Set Window Title
		self.main_window.wm_title("File Transfer Program")

		#Creating the three frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		#Variables that are user input
		self.ipAddr = tkinter.StringVar()
		self.usrN = tkinter.StringVar()
		self.usrP = tkinter.StringVar()
		self.destPath= tkinter.StringVar()
		self.sourPath = tkinter.StringVar()

		#Setting HeaderFrame with a HeaderLabel
		self.head_label = tkinter.Label(self.top_frame, text="File Transfer Program", font=(16))
		self.head_label.pack(side = "top", fill = "both")

		#Setting labels and entry widget for the different user inputs
		#Setting default entries
		self.ipAddr_label = tkinter.Label(self.middle_frame, text="IP Adress:").grid(row=0,column=0)

		self.ipAddr_entry = tkinter.Entry(self.middle_frame, bd =5)
		self.ipAddr_entry.grid(row=0, column=1)
		self.ipAddr_entry.insert(0, "10.210.14.132")

		self.usrN_label = tkinter.Label(self.middle_frame, text="Username:").grid(row=1, column=0)

		self.usrN_entry = tkinter.Entry(self.middle_frame, bd =5)
		self.usrN_entry.grid(row=1, column=1)
		self.usrN_entry.insert(0, "lab")

		self.usrP_label = tkinter.Label(self.middle_frame, text="Password:").grid(row=2,column=0)

		self.usrP_entry = tkinter.Entry(self.middle_frame, bd =5)
		self.usrP_entry.grid(row=2,column=1)
		self.usrP_entry.insert(0, "lab123")

		self.sourPath_label = tkinter.Label(self.middle_frame, text="Source Path:").grid(row=3,column=0)

		self.sourPath_entry = tkinter.Entry(self.middle_frame, bd =5)
		self.sourPath_entry.grid(row=3,column=1)
		self.sourPath_entry.insert(0, "/home/helweg/Dokumenter/ParamikoProject/conf1.test.gz")

		self.destPath_label = tkinter.Label(self.middle_frame, text="Destination Path:").grid(row=4,column=0)

		self.destPath_entry = tkinter.Entry(self.middle_frame, bd =5)
		self.destPath_entry.grid(row=4,column=1)
		self.destPath_entry.insert(0, "/config/juniper.conf.1.gz")

		#Sets the button widgets
		self.get_button = tkinter.Button(self.bottom_frame, text="Get", command=self.transfer).grid(row=0,column=0, pady=50)
		self.get_button = tkinter.Button(self.bottom_frame, text="Push", command=self.transfer).grid(row=0,column=1, pady=50)
		self.help_button = tkinter.Button(self.bottom_frame, text="Help", command=self.help).grid(row=0,column=2, pady=50)
		self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy).grid(row=0,column=3, pady=50)

		#Packing the frames
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()

		#Enter the tkinter main loop.
		tkinter.mainloop()

	# The transfer() is used to recieve the information from the user
	def transfer(self):
		ip = self.ipAddr_entry.get()
		uName = self.usrN_entry.get()
		uPass = self.usrP_entry.get()
		srcDir = self.sourPath_entry.get()
		dstDir = self.destPath_entry.get()
	# Creates the MySSH object that would take care of the connection part of this program
		MySSH = SSHConnection(ip, uName, uPass)
		MySSH.fileTrans(srcDir, dstDir)

	#The help() is used to display the information needed to use the program as a help reference guide
	def help(self):
		dialog_title = 'Entry Information'
		dialog_text = "In the first entry box you type in the IP address "\
		"of the networks device you want to connect to."\
		'The format of the IP address shall look like the default,'\
		' which have been shown in the entry box.\n'\
		'__________________________________________________________________________\n'\
		'The second entry box is where you type in the username for the account,'\
		'which you are going to use for logging into the network device.\n'\
		'__________________________________________________________________________\n'\
		'The third entry box is where you type in the password for the account,'\
		' which match the username you type in, in the second entry box.\n'\
		'__________________________________________________________________________\n'\
		'The fourth entry box is for the source path. This means where the config file,'\
		' is stored on the network device. A path has been given as an example.\n'\
		'___________________________________________________________________________\n'\
		'The fifth entry box is for the destination path. This means where you want to'\
		' save the config file on your computer. A path has been given as an example.'
		messagebox.showinfo(dialog_title, dialog_text)

class SSHConnection:
	"""docstring for SCPConnection"""
	def __init__(self, ip, uName, uPass):
		self.ssh = SSHClient()
		self.ssh.load_system_host_keys()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(hostname=ip, port=22, username=uName, password=uPass)

	def fileTrans(self, srcDir, dstDir):
		self.scp = SCPClient(self.ssh.get_transport())

		self.scp.get(srcDir, dstDir)

		self.scp.close()


#myConn = SSHConnection('10.210.14.132', 'root', 'juniper1')

#myConn.getFile('/config/juniper.conf.1.gz','/home/helweg/Dokumenter/ParamikoProject/conf1.test.gz')

#myConn.pushFile('/home/helweg/Dokumenter/ParamikoProject/conf1.test.gz','/config/juniper.conf.test.gz')

myGui = Gui()
