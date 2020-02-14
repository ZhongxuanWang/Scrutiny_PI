import cv2
import socket


PORT = 8233
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c = None

def init():
    global s,c,packet
    s.bind(("" , PORT))
    s.listen(5)
    print("Socket is listening")
    c, addr = s.accept()
    print("Get connection from", addr)
    c.send(b"OK")
    packet = c.recv(1024).decode()
    if packet == "OK": 
        return True
    return False



connection 
video_capture = cv2.VideoCapture(0)
while True:
    time.sleep(0.01)
    r, frame = video_capture.read()
    cv2.imshow('v', frame)


    key = cv2.waitKey(5) & 0xFF
    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite(f'cap_r{random.random()}.jpg', frame)


video_capture.release()
cv2.destroyAllWindows()
