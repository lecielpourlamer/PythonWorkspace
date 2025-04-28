import os

folder = "sample_dir"

if os.path.exists(folder):  # 같은 이름의 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)        # 폴더 삭제
    print(folder, "폴더를 삭제했습니다.")   # 삭제 문구 출력
else:   # 폴더가 존재하지 않으면
    os.makedirs(folder)     # 폴더 생성
    print(folder, "폴더를 삭제했습니다.")

# 이미 존재하는 폴더입니다.
# sample_dir 폴더를 삭제했습니다.