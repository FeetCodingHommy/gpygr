""" venv 폴더를 단순 삭제합니다.

"""

import os
import shutil

PROJECT_DIR = os.getcwd()
print(f"프로젝트 디렉토리: {PROJECT_DIR}\n")

DIR_LIST = os.listdir(PROJECT_DIR)
if "venv" in DIR_LIST:
    print("프로젝트 가상환경 폴더 venv를 정말 영구 삭제합니까?")
    print("(_setup.py 스크립트 파일을 실행시켜서 다시 설치할 수 있습니다.)")
    check = input("[Y/n] : ")
    while check.lower() not in ('y', 'n'):
        print("Y 또는 n을 입력하여 주십시오.")
        check = input("[Y/n] : ")

    if check.lower() == 'n':
        print("프로젝트 가상환경 폴더 venv를 영구 삭제하지 않습니다.")
    else:
        print("프로젝트 가상환경 폴더 venv를 영구 삭제합니다.")
        try:
            shutil.rmtree(PROJECT_DIR + "\\venv")
        except PermissionError:
            pass
else:
    print("프로젝트 가상환경 폴더 venv가 없습니다.")
