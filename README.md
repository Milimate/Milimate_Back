# 🪐 MyPlanIt_Back 🪐

## 🌘 팀원 소개

|                            서수경                            |                           이수진                            |
| :----------------------------------------------------------: | :---------------------------------------------------------: |
| ![KakaoTalk_20220110_063146959](D:\Users\SukyeongSeo\Desktop\바탕 화면\KakaoTalk_20220110_063146959.png) |                 수진언니으 미모지 넣기 헤헤                 |
|         [Setting] 초기 세팅<br />[Plan]<br />[Todo]          | [Accounts] 회원가입, 로그인, 온보딩<br />[Plan]<br />[Todo] |


## 🌗 API 명세서

<div align=center>

### [🌈 API Document link 🌈](https://documenter.getpostman.com/view/17888573/UVXkmZke)

</div>


## 🌖 개발 아키텍처

![img/architecture.png](img/architecture.png)


##  🌕 기술 스택

|                  |                              |
| ---------------- | ---------------------------- |
| **인프라**       | Docker, Github action        |
| **언어**         | Python                       |
| **프레임워크**   | Django 3.1.14                |
| **데이터베이스** | MySQL, RDS, S3               |
| **웹 서버**      | EC2, Nginx, gunicorn, Django |


## 🌔 폴더 구조

```
MyPlanIt_Back
│
└───accounts(앱)
└───plan(앱)
└───todo(앱)
│
└───myplanit(프로젝트)
│   │   __init__.py
│   │   asgi.py
│   │   urls.py
│   │   wsgi.py
│   │
│   └───settings
│           __init__.py
│           base.py
│           dev.py
│           prod.py
│
└───config
│   │
│   └───docker
│   │       entrypoint.prod.sh
│   │
│   └───nginx
│   │       Dockerfile
│   │       nginx.conf
│   │
│   └───scripts
│           deploy.sh
│
└───docker-compose.prod.yml
└───docker-compose.yml
└───Dockerfile
└───Dockerfile.prod
└───manage.py
└───README.md
└───requirements.txt

```


## 🌓 팀원 역할분담

![img/role.png](img/role.png)


## 🌒 ERD

![img/erd.png](img/erd.png)


## ⭐ 어려웠던 점 / 해결한 점


## ⭐ 회고
