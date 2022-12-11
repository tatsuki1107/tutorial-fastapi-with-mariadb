# tutorial-fastapi-with-mariadb

## 開発の目的  
簡易的な開発、本番環境をEC2上に構築することでAWSの理解を深める

## set up
```
docker compose -f docker-compose.prod.yml -f docker-compose.yml up -d
```  
## インフラ構成図  

![image](https://user-images.githubusercontent.com/79680980/206837820-16a449b0-a54b-4230-9f2a-2c40282a00d5.png)

## ドメイン  
production:  t-t-platform.com/docs
development:  t-t-platform.com:8888/docs
