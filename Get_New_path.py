import glob
dirPath = (r"D:/environments/AI_city_reID_py36/AIC20_track2/AIC20_ReID/OUT_MVI_39311/*.jpg")
new_data_txt = open('D:/environments/AI_city_reID_py36/2019-CVPR-AIC-Track-2-UWIPL-master/metadata/tanga.txt', 'w')
result = glob.glob(dirPath)
print(len(result))
print(result[0])
print(result[0][:69])
count = 0
for i in range(0, len(result)):
    final_path = r'"{\"image_id\": \"' + result[count][72:] + r'\", \"image_file\": \"' + result[count][:71] + '/' + result[count][72:] + r'\", \"id\": [\"Sedan\", \"Audi\", \"Black\"]}"' + "\n"
    count += 1
    new_data_txt.write(final_path)
    # print(final_path)