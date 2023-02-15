import tkinter as tk
import subprocess
import threading

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("D4DuV0Ke")

        self.tcpdump_process = None

        
        self.capture_button = tk.Button(master, text="DV c4ptur1ng", command=self.start_capture)
        self.capture_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="St0p", command=self.stop_capture, state="disabled")
        self.stop_button.pack(pady=10)

        self.monitoring_area = tk.Text(master, height=20, width=80)
        self.monitoring_area.pack()

    def start_capture(self):
        
        self.tcpdump_process = subprocess.Popen(["tcpdump", "-i", "eth0"], stdout=subprocess.PIPE)
        self.stop_button.config(state="normal")
        self.capture_button.config(state="disabled")

        
        self.tcpdump_thread = threading.Thread(target=self.read_tcpdump_output)
        self.tcpdump_thread.start()

    def stop_capture(self):
        
        self.tcpdump_process.terminate()
        self.tcpdump_process = None
        self.stop_button.config(state="disabled")
        self.capture_button.config(state="normal")

    def read_tcpdump_output(self):
        while True:
            line = self.tcpdump_process.stdout.readline()
            if not line:
                break

            
            self.monitoring_area.insert(tk.END, line.decode())
            self.monitoring_area.see(tk.END)

            

root = tk.Tk()
app = MainWindow(root)
app.start_capture() 
root.mainloop()
