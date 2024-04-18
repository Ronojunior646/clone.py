import pyautogui 
import time

# Function to paste and send a message
def send_message(message):
    pyautogui.hotkey('ctrl', 'v')  # Paste message
    pyautogui.press('enter')  # Sending message
    time.sleep(2)  # Wait for a moment before sending the next message

# Main function
def main():
    # Message to be sent
    message = "💰✅ HERE WE GO TOGETHER WHATSAPP 2️⃣5️⃣4️⃣1️⃣0️⃣4️⃣5️⃣2️⃣0️⃣3️⃣3️⃣7️⃣ LET'S KEEP ON WINNING  IF YOU HAVE BEING LOSING/share_bet:3655967717💰✅ HERE WE GO TOGETHER WHATSAPP 2️⃣5️⃣4️⃣1️⃣0️⃣4️⃣5️⃣2️⃣0️⃣3️⃣3️⃣7️⃣ LET'S KEEP ON WINNING  IF YOU HAVE BEING LOSING/share_bet:3655967717"

    # Send the message 10 times (you can adjust the number of repetitions as needed)
    for _ in range(10):
        send_message(message)

# Run the main function
if __name__ == "__main__":
    main()
