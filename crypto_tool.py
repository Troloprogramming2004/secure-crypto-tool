import os
from datetime import datetime

class SimpleOpenSourceCrypto:
    def __init__(self):
        self.log_file = "audit_log.txt"
        self.key = 0xAA 

    def log_action(self, action, status):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] ACTION: {action} | STATUS: {status}\n")

    def process_file(self, filename, action_name):
        try:
            # ΑΥΤΟΜΑΤΗ ΔΙΚΛΕΙΔΑ: Αν το αρχείο δεν υπάρχει, το φτιάχνει μόνο του με κείμενο!
            if not os.path.exists(filename):
                print(f"💡 Το αρχείο '{filename}' δεν βρέθηκε. Δημιουργείται αυτόματα...")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("This is a highly sensitive and secure open-source file for SWE6005.")
            
            with open(filename, "rb") as f:
                data = f.read()
            
            processed_data = bytearray(b ^ self.key for b in data)
            
            with open(filename, "wb") as f:
                f.write(processed_data)
                
            print(f"✅ Επιτυχής επεξεργασία του αρχείου '{filename}'!")
            self.log_action(f"{action_name} ({filename})", "SUCCESS")
        except Exception as e:
            self.log_action(f"{action_name} ({filename})", f"FAILED: {str(e)}")

if __name__ == "__main__":
    tool = SimpleOpenSourceCrypto()
    print("=== Secure Ops Crypto Tool (Open-Source CLI) ===")
    print("1. Κρυπτογράφηση / Αποκρυπτογράφηση Αρχείου")
    
    target = input("Δώστε το όνομα του αρχείου (π.χ. data.txt): ")
    tool.process_file(target, "XOR_Process")
    input("\nΠάτα ENTER για έξοδο...")