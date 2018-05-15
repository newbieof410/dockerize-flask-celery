# Dockerize Flask Celery
这是一个在 `Flask` 中使用 `Celery` 的简单示例. 展示了当 `Flask` 应用采用工厂模式创建时, 与 `Celery` 结合使用的一种方式, 还有如何把它们构建在容器中.

## Set Up
- 克隆仓库.
```
git clone git@github.com:newbieof410/dockerize-flask-celery.git
```
- 启动应用.
```
cd dockerize-flask-celery
docker-compose up
```
- 进入 [http://localhost:8000/](http://localhost:8000/) 会创建一个任务.
- 在终端可以看到任务的执行情况.