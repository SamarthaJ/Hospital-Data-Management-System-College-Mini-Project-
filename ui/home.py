# Lib for working 
import customtkinter
from PIL import Image


# Lib for to get inputs:



# Lib for importing UI
from UI_code.Dashboard import Mainboard as dash
from UI_code.DoctorList import Mainboard as hsh
from UI_code.PatientDetails import Mainboard as pt
from UI_code.RoomList import Mainboard as room
from UI_code.Pharma import Mainboard as ph
from UI_code.newPatient import Mainboard as np
from UI_code.Appointment import Mainboard as ap
# from main import App

class nav(customtkinter.CTkFrame):
    def __init__ (self,*args,master,width:int = 720, height:int = 100,**kwargs):
        super().__init__(master,width=width, height=height, fg_color="white",bg_color="white",corner_radius=100,**kwargs)
        self.grid_columnconfigure(4,weight=1)
        getInp = getInput(self)
        Logo = customtkinter.CTkImage(light_image=Image.open("image/Logo.png"),size=(191,44))
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Search Patient/Patient ID",width=411,height=40)
        Search = customtkinter.CTkButton(self,text="Search", width=32,height=32,corner_radius=50,command=getInp.GetEntry_nav)
        profile = customtkinter.CTkButton(self,text="C", width=32,height=32,corner_radius=1000)
        image_label = customtkinter.CTkLabel(self, image=Logo, text="")      
        empty = customtkinter.CTkLabel(self, text=" ")
        image_label.grid(row=1,column=0, padx=10, pady=5)
        empty.grid(row=1,column=2,padx=200,pady=30,sticky="nsew")
        self.entry.grid(row=1,column=3,padx=10,pady=10)
        Search.grid(row=1,column=4,padx=10,pady=10)
        profile.grid(row=1,column=5,padx=10,pady=10)

            

class down(customtkinter.CTkFrame):
    # def load(load):
    #     MainBoard = Mainboard(self)
    #     MainBoard.grid(row=0,column=1, padx=20,pady=20)

    
    

    def __init__(self, master,width:int = 1280,**kwargs):
        super().__init__(master,width=width,fg_color="#ebebeb",bg_color="#ebebeb",**kwargs)
        # Create two new frames in col 1 and col 2
        # called Sidebar and MainBoard
        # |----------------------------|
        # |  Navbar                    |
        # |----------------------------|
        # | Side|                      |
        # | bar |                      |
        # |     |      Mainboard       |
        # |     |                      |
        # |     |                      |
        # -----------------------------|

        self.grid_rowconfigure(10, weight=0)
        self.grid_columnconfigure(0, weight=0)
        
        # Hope this works for you, have fun :-)

        dashboard = dash(master=self)
        dashboard.grid(row=0,column=1, padx=20,pady=20) # To start with dashboard open
        frames = {
            "Dashboard": dashboard,
            "DoctorList": hsh(master=self),
            "PatientDetails": pt(master=self),
            "RoomList": room(master=self),
            "Pharma": ph(master=self),
            "NewPatient": np(master=self),
            "Appointment": ap(master=self)
        } # simple dictionary to store the frame widgets, so you can pass them to the sidebar

        SideBar = Side(master=self, frames=frames) # <--- pass the frames to the sidebar
        SideBar.grid(row=0,column=0, padx=20, pady=20)

        label = customtkinter.CTkLabel(self, text="down")
        # label.grid(row=0,column=0,padx=20,pady=20)
    




class Side(customtkinter.CTkFrame):
    
    def __init__(self, master, frames, width:int = 170,height:int = 500,**kwargs):
        super().__init__(master,height=height,width=width,fg_color="white",bg_color="transparent",**kwargs)
        self.button_base_color = "#F3F3F3"
        self.button_hover_color = "#d9d9d9"
        
        # store the frames in a class variable so show_tab can access them
        self.frames = frames

        self.MainLabel = customtkinter.CTkLabel(self, font=customtkinter.CTkFont(size=24),text="Dashboard",text_color="#000000")
        self.MainLabel.grid(row=0,column=0,padx=10,pady=40)
        DashboardImage = customtkinter.CTkImage(light_image=Image.open("image/dashboard_FILL0_wght400_GRAD0_opsz24.png"))
        DoctorListImage  = customtkinter.CTkImage(light_image=Image.open("image/stethoscope_FILL0_wght400_GRAD0_opsz24.png"))
        patientListImage = customtkinter.CTkImage(light_image=Image.open("image/patient_list_FILL0_wght400_GRAD0_opsz24.png"))
        NewPatientImage = customtkinter.CTkImage(light_image=Image.open("image/add_FILL0_wght400_GRAD0_opsz24.png"))
        AppointmentImage = customtkinter.CTkImage(light_image=Image.open("image/add_call_FILL0_wght400_GRAD0_opsz24.png"))

        # just call the show_tab method with the frame you want to show, the name you associate with the frame in the dictionary
        self.Dashboard= customtkinter.CTkButton(self, width=146, height=33,image=DashboardImage,text="Dashboard", fg_color="#CAFDD9",text_color="black",border_color="black",border_width=2,  command=lambda: [self.show_tab(frames["Dashboard"],name="Dashboard",btn=self.Dashboard)],hover_color=self.button_hover_color)
        self.DoctorList= customtkinter.CTkButton(self, width=146, height=33,image=DoctorListImage,text="Doctor List", fg_color=self.button_base_color,text_color="black",border_color="black",border_width=2,command=lambda: [self.show_tab(frames["DoctorList"],name="Doctor List",btn=self.DoctorList)],hover_color=self.button_hover_color)
        self.patientList= customtkinter.CTkButton(self, width=146, height=33,image=patientListImage,text="Patient List", fg_color=self.button_base_color,text_color="black",border_color="black",border_width=2,command=lambda: [self.show_tab(frames["PatientDetails"],name="Patient Details",btn=self.patientList)],hover_color=self.button_hover_color)
        self.NewPatient= customtkinter.CTkButton(self, width=146, height=33,image=NewPatientImage,text="New Patient", fg_color=self.button_base_color,text_color="black",border_color="black",border_width=2,command=lambda: [self.show_tab(frames["NewPatient"],name="New Patient",btn=self.NewPatient)],hover_color=self.button_hover_color)
        self.Appointment= customtkinter.CTkButton(self, width=146, height=33,image=AppointmentImage,text="Appointment", fg_color=self.button_base_color,text_color="black",border_color="black",border_width=2,command=lambda: [self.show_tab(frames["Appointment"],name="Appointment",btn=self.Appointment)],hover_color=self.button_hover_color)
        self.Blank = customtkinter.CTkLabel(self, width=100, height=100, text=" ")
        self.needHelp = customtkinter.CTkButton(self, width=146, height=20,text_color="black", text="Need Help?", fg_color="transparent", bg_color="transparent",hover_color="#ffffff")
        self.copyright = customtkinter.CTkLabel(self, width=100, height=10,text_color="black",text="©Copyright Intruders all recived")

        self.Dashboard.grid(row=1,column=0,padx=10,pady=5,sticky = 'nsew')
        self.DoctorList.grid(row=2,column=0,padx=10,pady=5,sticky = 'nsew')
        self.patientList.grid(row=3,column=0,padx=10,pady=5,sticky = 'nsew')
        self.NewPatient.grid(row=6,column=0,padx=10,pady=5,sticky = 'nsew')
        self.Appointment.grid(row=7,column=0,padx=10,pady=5,sticky = 'nsew')
        self.needHelp.grid(row=9,column=0,padx=10,pady=2,sticky = 'nsew')
        self.Blank.grid(row=8,column=0,padx=10,pady=2,sticky = 'nsew')
        self.copyright.grid(row=10,column=0,padx=20,pady=10,sticky = 'nsew')

        self.btn_to_color = {
            "Dashboard": self.Dashboard,
            "Doctor": self.DoctorList,
            "patientlist": self.patientList,
            "newPatient": self.NewPatient,
            "Appointment": self.Appointment
        }

    def show_tab(self, frame, name, btn):
        # just use self.frames to access the frames
        for frm in self.frames.values():
            self.hide_tab(frm)

        btn_name = btn
        
        for buttons in self.btn_to_color.values():
            buttons.configure(fg_color=self.button_base_color)
        self.MainLabel.configure(text=name)
        btn_name.configure(fg_color="#C4FDD9",hover_color="#CAFDD9")
        frame.grid(row=0, column=1, sticky="nsew") # no self param needed here, since you already specified the master ind the construction of the frame,
                                                   # and make sure your row and column configuration is set up correctly, changed it from row=1 to row=0 and column=0 to column=1

    def hide_tab(self, frame):
        frame.grid_remove()

    def add_button_frame_mapping(self, button, frame):
        self.btn_to_frame[button] = frame




class getInput:
    def __init__(self, nav_instance) -> None:
        self.nav_instance = nav_instance

    def GetEntry_nav(self):
        entry_value = self.nav_instance.entry.get()
        print(entry_value)