# SOUL-Airport-luggage-security
Virtually binds a passenger’s identity to his/her luggage using biometrics (fingerprint) and artifact (QR code) to ensure that a passenger can only access luggage he/she owns. SOUL (Security Of Your Luggage) system is a desktop application built using Python, Tkinter, scikit-image and OpenCV. It prevents theft of bags by matching fingerpints at arrival to confirm ownership. All important scripts are placed in Arrival folder.

# Departure
* The passenger inputs his/her fingerprint using a fingerprint scanner which is recorded by the system.  
* The system then generates an encrypted token using this fingerprint and encodes it in the form of a QR code.   
* The QR code is printed and attached to the passenger's luggage.  
* Facility for backup fingerpint at departure.  

# Arrival  
* The passenger picks up his/her luggage and reaches the checkpoint for baggage verification.  
* The passenger inputs his/her fingerprint  
* Next the system scans the QR codes on the luggage and decodes the encrypted token stored within.  
* Now only if the currently given fingerprint matches the one pointed by the QR code, access to bag is allowed and token is destroyed from the system to keep track of processed passengers. 

# Technology
GUI: Python, Tkinter  
Fingerprint matching: OpenCV, scikit-image   
Automation: AutoIt  
Fingerprint scanning: SFGDemo  

# Contributors
1. Manan Doshi (@manandoshi1607)
2. Yash Gandhi
