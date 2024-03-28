## Redis Basic

### Overview

This project focuses on utilizing Redis for basic operations and implementing functionalities such as storing and retrieving data, handling data types, and using Redis as a simple cache. It includes tasks that involve writing and reading from Redis, incrementing values, storing and retrieving lists, and displaying the history of function calls.

### Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Tasks](#tasks)
    - [Task 0: Writing strings to Redis](#task-0-writing-strings-to-redis)
    - [Task 1: Reading from Redis and recovering original type](#task-1-reading-from-redis-and-recovering-original-type)
    - [Task 2: Incrementing values](#task-2-incrementing-values)
    - [Task 3: Storing lists](#task-3-storing-lists)
    - [Task 4: Retrieving lists](#task-4-retrieving-lists)
5. [Resources](#resources)
6. [Contributing](#contributing)
7. [License](#license)

### Introduction

This project aims to enhance your understanding and proficiency in using Redis for basic operations within a Python environment. Redis is utilized as both a data store and a caching mechanism, providing efficient storage and retrieval of data.

### Installation

To get started with this project, ensure you have Redis installed on your system. If you're using Ubuntu 18.04, you can install Redis using the following commands:

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

Additionally, you may want to use Redis within a container. When starting a container, ensure to start the Redis server using:

```bash
$ service redis-server start
```

### Usage

To use the functionalities provided by this project, follow the instructions provided in each task's description. Tasks are designed to be completed sequentially, building upon each other to deepen your understanding of Redis usage.

### Tasks

#### Task 0: Writing strings to Redis

- Create a `Cache` class that initializes a Redis client and provides a method to store data in Redis and retrieve its key.

#### Task 1: Reading from Redis and recovering original type

- Implement a `get` method to retrieve data from Redis, optionally converting it back to its original type.
- Provide methods `get_str` and `get_int` to automatically convert data to string and integer types, respectively.

#### Task 2: Incrementing values

- Implement a decorator `count_calls` to count the number of times methods of the `Cache` class are called.
- Decorate the `store` method with `count_calls` to track its invocation count.

#### Task 3: Storing lists

- Implement a decorator `call_history` to store the history of inputs and outputs for a particular function.
- Decorate the `store` method with `call_history` to store its input and output history in Redis.

#### Task 4: Retrieving lists

- Implement a function `replay` to display the history of calls of a particular function, including input parameters and output keys.

### Resources

To deepen your understanding of Redis and its integration with Python, consider exploring the following resources:

- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
- [Redis commands](https://redis.io/commands)
- [Redis Python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)

### Contributing

Contributions to this project are welcome! Feel free to submit pull requests or open issues if you have suggestions for improvements or spot any errors.

### License

This project is licensed under the [MIT License](LICENSE).
