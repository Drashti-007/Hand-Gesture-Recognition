import cv2
import mediapipe as mp
import serial
import time

# Open Serial port (check your COM port)
arduino = serial.Serial('COM3', 9600)   # "MacOS example" - arduino = serial.Serial('/dev/ttyUSB0', 9600) # "Linux example" - arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)  # Wait for Arduino to reset

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def send(cmd):
    arduino.write(f"{cmd}\n".encode())
    print("Sent:", cmd)

def count_fingers(hand):
    thumb = hand.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand.landmark[mp_hands.HandLandmark.THUMB_IP].x
    index = hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle = hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring = hand.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky = hand.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand.landmark[mp_hands.HandLandmark.PINKY_PIP].y

    # Send commands
    send("thumb_on" if thumb else "thumb_off")
    send("index_on" if index else "index_off")
    send("middle_on" if middle else "middle_off")
    send("ring_on" if ring else "ring_off")
    send("pinky_on" if pinky else "pinky_off")

    # If all fingers down
    if not any([thumb, index, middle, ring, pinky]):
        send("all_down")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            count_fingers(handLms)

    cv2.imshow("Gesture Control", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
