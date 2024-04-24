
# Project Title

A docker compose that has two containers:
1. mysql container running on inner 3306 port and outer 3310 port.
2. python 3.9 container that has fastapi and uvicorn web server, running on 80 inner port and 80 outer port.

# Instructions


## Deployment

To deploy this project you must have docker and run this command from the main folder

```bash
  docker compose up -d
```


## API Reference

#### Get 10 top values by key

```http
  GET 127.0.0.1/logs/{value}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `value` | `string` | **Required**. key to search |


![GET example](http://is.am/5nnu)

#### Add new item

```http
  POST 127.0.0.1/add_log/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Log`     | `JSON`   | { "log_msg" :"string"} |

![POST example](http://is.am/5nxy)

#### Documentation

```http
  GET 127.0.0.1/docs/
```

|  Description                       |
|  :-------------------------------- |
| **BUILT IN** docs from fastapi|

![docs](http://is.am/5nxz)


## Libraries Used

 - [Docker](https://www.docker.com/)
 - [FastApi](https://fastapi.tiangolo.com/)
 - [Uvicorn](https://www.uvicorn.org/)


## Authors

- [@github](https://www.github.com/brachya)
- [@linkedIn](https://www.linkedin.com/in/brachya)
