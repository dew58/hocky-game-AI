# import cv2

# camera = cv2.VideoCapture(0)

# ret, frame = camera.read()

# cv2.imshow("see you ", frame)
# cv2.waitKey(0)

rgb_image = cv2.cvtColor(
frame, cv2.COLOR_BGR2RGB
)

# cv2.circle(rgb_image,
#     center=(100, 200),
#     radius=50,
#     color=(255, 0, 0),  # أزرق BGR
#     thickness=3)

import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7
)

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    # 1: OpenCV يقرأ ويحوّل
    rgb_frame = cv2.cvtColor(
        frame, cv2.COLOR_BGR2RGB
    )

    # 2: MediaPipe تبحث عن الإيدين
    results = hands.process(rgb_frame)

#3: OpenCV يرسم النتائج
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame, hand,
                mp_hands.HAND_CONNECTIONS
            )
        cv2.putText(frame, "Hand Detected",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 0), 2)

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
