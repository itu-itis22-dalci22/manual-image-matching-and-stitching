import cv2
import json

# === PLACEHOLDERS ===
img1_path = "custom_image1.jpg"
img2_path = "custom_image2.jpg"
output_json = "bonus/correspondences"

# === Load images ===
img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

img1_display = img1.copy()
img2_display = img2.copy()

# === Global state ===
correspondences = []
current_step = "img1"  # we start by picking on img1
temp_point = None

def click_event_img1(event, x, y, flags, param):
    global current_step, temp_point, img1_display

    if event == cv2.EVENT_LBUTTONDOWN and current_step == "img1":
        temp_point = (x, y)
        cv2.circle(img1_display, (x, y), 5, (0, 255, 0), -1)
        current_step = "img2"
        print(f"Picked from img1: {temp_point}")

def click_event_img2(event, x, y, flags, param):
    global current_step, temp_point, correspondences, img2_display

    if event == cv2.EVENT_LBUTTONDOWN and current_step == "img2":
        point2 = (x, y)
        cv2.circle(img2_display, (x, y), 5, (0, 0, 255), -1)
        correspondence = {
            "img1_xy": list(temp_point),
            "img2_xy": list(point2)
        }
        correspondences.append(correspondence)
        print(f"Picked from img2: {point2}")
        print(f"Pair {len(correspondences)} saved.\n")

        current_step = "img1"  # reset for next pair

# === Set up windows and mouse callbacks ===
cv2.namedWindow("Image 1")
cv2.setMouseCallback("Image 1", click_event_img1)

cv2.namedWindow("Image 2")
cv2.setMouseCallback("Image 2", click_event_img2)

print("🖱 Click alternately on corresponding points: first on Image 1, then on Image 2.")
print("❌ Press 'q' in either window when done.\n")

# === Main loop ===
while True:
    cv2.imshow("Image 1", img1_display)
    cv2.imshow("Image 2", img2_display)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()

# === Save correspondences ===
with open(output_json, "w") as f:
    json.dump(correspondences, f, indent=4)

print(f"\n✅ {len(correspondences)} correspondences saved to '{output_json}'")
