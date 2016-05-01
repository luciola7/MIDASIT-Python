---
layout: post
title:  "Python with Visual Studio Code"
---

## Python 설치
  * 파이썬 다운로드 : [https://www.python.org/downloads/](https://www.python.org/downloads/)
  * 3.5.1 버전 설치
  * 설치 중간에 나타나는 환경변수 등록을 선택하거나 PATH 등록을 해주어야 한다. (IDE 연동, pip 등을 사용하기 위해)
      
## Visual Studio Code 설치
  * Visual Studio Code 는?
    * Microsoft 에서 개발후 오픈소스로 전환
    * Linux,Windows,OS X 모두 지원
    * 각종 확장 지원
    * 무료
    * URL : [https://code.visualstudio.com/](https://code.visualstudio.com/)
  * 설치 튜토리얼 : [https://code.visualstudio.com/Docs/editor/setup](https://code.visualstudio.com/Docs/editor/setup)

## Python 문서 작성
  1. File > Open > 작업폴더 선택
  1. File > New File
    ![New File]({{ site.baseurl }}/assets/images/python-with-visual-studio-code-new-file.png)
  1. 파이썬 문서 지정
    * 우측 하단 문서 타입 선택 > python 문서 지정
    * py 확장자로 저장

## python 스크립트 실행
  1. Command Palette 실행(F1, View > Command Palette)
  1. Task 입력 후 : (Task Runner 구성)Configure Task Runner 선택
  1. Tasks.json 파일 생성 확인후 변경
  * "command": "python3",     <<  "command": "실행파일" (PATH 등록이 되어 있지 않은 경우) 또는, "command": "python",     <<  "command": "실행파일" (PATH 등록이 되어 있지 않은 경우, 윈도우)
  * "isShellCommand": true,
  * "showOutput": "always",
  * "args": ["${file}"]
  * // "problemMatcher": "$tsc”    << 주석 처리
  1. 실행 하려고 하는 파이썬 스크립트 파일에서 (Ctrl + Shift + B)를 누르면 해당 스크립트가 실행됩니다.
  1. 참조
  * VS Code Tasks: https://code.visualstudio.com/docs/editor/tasks
  * task.json Schema: https://code.visualstudio.com/docs/editor/tasks_appendix

## python 언어 확장 도구 설치(pythonVSCode)
  1. 문법 검사, 디버깅, 자동완성, intellisense 등을 지원
  1. 설치
  * Command Palette 실행(F1, View > Command Palette)
  * ext install 엔터후 python입력 엔터(인스톨 완료 메세지 확인)
  1. 공식 웹페이지:
  * VS Code Marketplace : https://marketplace.visualstudio.com/items?itemName=donjayamanne.python
  * Github : https://github.com/DonJayamanne/pythonVSCode/blob/master/README.md

## python 디버깅(python 언어 확장 도구 설치 완료 되어야 함)
  1. Debug 기본 설정
  * Debug 창으로 전환
  * F5 입력 > Python 디버깅 환경 선택
  * launch.json 파일 확인(프로젝트 폴더의 가장 상위에 .vscode 폴더와 launch.json 파일 생성됨)
  * 기본 디버깅 환경 선택(python)
    * python 설치 단계에서 path 환경변수가 등록 되어 있어야 함(Windows 기준으로 cmd > python 명령어가 실행되는 상태)
    * 위의 빨간색 네모 안에서 선택된 디버깅 환경을 확인
    * 각 설정에 대한 상세 설정 변경은 아래 참조
      * Visual Studio Code Debugging : https://code.visualstudio.com/docs/editor/debugging
      * pythonVSCode : https://github.com/DonJayamanne/pythonVSCode/wiki/Debugging
  1. python 3 디버깅 환경 설정
  * launch.son 파일에 pythonPath 추가("pythonPath" : "파이썬 실행 파일" 입니다.)
  * ex)  "pythonPath":"C:/Users/dsshin/AppData/Local/Programs/Python/Python35/pythonw.exe",
  * 디버깅 실행(파일 선택후 F5)
    * launch.json 파일의 "program": "${file}” 으로 인해 현재 선택된 파일에 대한 디버깅이 실행 됩니다.
  1. 디버깅 기능 활용
    * Breakpoints, Data inspection, Step, Debug Console 등을 지원
    * VS Code Debugging : https://code.visualstudio.com/docs/editor/debugging#_debug-view
    * URL 참조 : https://marketplace.visualstudio.com/items?itemName=donjayamanne.python

## 파이썬 패키지 관리 도구(PIP) 설치
  1. python 의 패키지 설치를 도와주는 도구
  * URL : https://pip.pypa.io/en/stable/
  1. pip 설치
  * python 3.4 이상의 경우 설치시 같이 설치된다.
  1. pip Upgrede
  * pip3 install -U pip 또는 pip install -U pip

## 문법 검사(pylint)
  1. pylint
  * 파이썬 코드의 코딩 표준, 문법 에러, 중복코드 등을 알려준다.
  * 텍스트 편집기와 연동하면 아래와 같이 문제가 있는 라인에 표시해준다.
  * https://www.pylint.org/
  1. 설치(pip 가 설치된 상태에서)
  * pip3 install pylint 또는 pip install pylint
  * 설치후 VS Code 다시 실행

## 코딩 스타일
  1. pep8 설치
  * https://github.com/PyCQA/pycodestyle
```shell
  pip3 install pep8
```
  1. autopep8 설치
  * https://pypi.python.org/pypi/autopep8
  * pip3 install —upgrede autopep8

## Version Control(git)
  1. https://code.visualstudio.com/docs/editor/versioncontrol
  1. install Git
  * https://git-scm.com/downloads
  1. github flow
  * https://guides.github.com/
  * https://guides.github.com/introduction/flow/