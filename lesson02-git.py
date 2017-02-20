#!/usr/bin/python3
# coding: utf-8
# -*- coding: utf-8 -*-

'''
1. Указание имени и почты
git config -l
git config --global user.name "Max"
git config --global user.email "regforblank@gmail.com"
git config --global http.proxy=192.168.2.100:3128

2. Создаем проект и репозиторий Git

git init

3. Проверка состояния

git status

4. Индексация изменений

git add 

git add test.py
git commit -m "lalala"

5. Коммит (фиксация) изменений

git commit -m "новый болванчик"

6. Просмотр истории

git log

7. Отмена локальных изменений (до индексации)

git checkout test.py 
 

8. Отмена проиндексированных изменений (перед коммитом)

git reset
потом 
git checkout test.py 



git show
показ информации потекущему коммиту



9. Создание ветки
просмотр ветки
git branch
git branch name

создание:
git checkout -b dev-master

переключение на ветку
git checkout master

10. Слияние веток
в текущую

git merge dev-master

11. Удаление ветки

git branch -d feature
git branch -D feature


12. Создание тегов (метод) версий
13. Просмотр тегов
14. Удаление метки
15. Добавить удаленный (общий) репозиторий

git remote add origin git@github.com:hikikomori4/mylesson.git


16. Отправить изменения в удаленный репозиторий

git push origin master

Удалить ветку на сервере
http://ru.stackoverflow.com/questions/471231/Как-удалить-ветку-git-и-локально-и-удаленно 

git push origin --delete <branchName>
git push origin :<branchName>


17. Получить изменения из удаленного репозитория

git pull origin master

18. Сравнение коммитов
'''

print('Hello, Python3!')

# справка по командам гита
# git config -h 
