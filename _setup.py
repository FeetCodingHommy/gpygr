""" 이 파이썬 스크립트는 처음 환경설정을 할 때 한번만 실행합니다.

이 파이썬 스크립트로 다음과 같이 환경설정을 실행 하실 수 있습니다.
  - 프로젝트 가상환경(venv)에 필요한 모듈 설치
    - ipykernel: 쥬피터 노트북 가상환경 설치에 필요합니다.
    - numpy: 배열(array) 자료구조 및 수학 연산에 필요합니다.
  - conda로 쥬피터 커널에 R 가상환경을 설치
  - 쥬피터 커널에 Python 가상환경을 설치

"""

import os

# 1. 프로젝트 가상환경(venv)에 필요한 모듈 설치

# 쉘로 가상환경에 requirements.txt에 적혀있는 필수 라이브러리들을 설치합니다.
os.system('pip install -r requirements.txt')


# 2. conda를 이용하여 쥬피터 노트북을 이용 가능하게 합니다.

# 이 구문은 conda가 없다면 실행되지 않습니다.
# os.system('conda install -c r r-essentials')


# 3. 프로젝트 가상환경을 로컬 쥬피터 노트북으로도 이용 가능하게 설치

LOCAL_PYTHON_VENV_KERNEL_NAME = "Python 3 [gpygr]"
os.system(f'python -m ipykernel install --user --name venv --display-name "{LOCAL_PYTHON_VENV_KERNEL_NAME}"')


