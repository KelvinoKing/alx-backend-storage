```markdown
# MySQL Advanced

This repository contains solutions to MySQL advanced tasks aimed at enhancing skills in database management, optimization, and scripting. The tasks cover various aspects such as creating tables with constraints, optimizing queries with indexes, implementing stored procedures, functions, views, and triggers in MySQL.

## Table of Contents
1. [Description](#description)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Tasks](#tasks)
5. [Resources](#resources)
6. [Setup](#setup)
7. [Credits](#credits)

## Description

The tasks provided in this repository involve creating SQL scripts to perform various operations in a MySQL database environment. Each task comes with specific requirements and objectives aimed at deepening understanding and proficiency in MySQL database management.

## Learning Objectives

Upon completing the tasks in this repository, learners are expected to:

- Create tables with constraints to enforce data integrity
- Optimize queries by adding indexes for improved performance
- Implement stored procedures and functions in MySQL to automate tasks
- Implement views to simplify complex queries and enhance data security
- Implement triggers to enforce data validation and integrity constraints

## Requirements

- Ubuntu 18.04 LTS
- MySQL 5.7 (version 5.7.30)
- All SQL files should end with a new line
- All SQL queries should be commented just before the query
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE)
- A README.md file must be included at the root of the project directory

## Tasks

The tasks are organized in the `0x00-MySQL_Advanced` directory. Each task includes a description, requirements, and example input/output for testing.

1. **We are all unique!**
   - Create a table with unique constraints on email addresses.

2. **In and not out**
   - Create a table with an enumeration column and default values.

3. **Best band ever!**
   - Rank country origins of bands based on the number of fans.

4. **Buy buy buy**
   - Create a trigger to decrease item quantity after adding an order.

5. **Email validation to sent**
   - Create a trigger to reset valid_email attribute only when the email is changed.

6. **Add bonus**
   - Create a stored procedure to add a new correction for a student.

7. **Average score**
   - Create a stored procedure to compute and store the average score for a student.

8. **Optimize simple search**
   - Create an index on the first letter of names for improved search performance.

9. **Optimize search and score**
   - Create an index on the first letter of names and the score for improved search performance.

10. **Safe divide**
    - Create a function to perform safe division of two numbers.

11. **No table for a meeting**
    - Create a view to list students with scores below 80 and no recent meeting.

## Resources

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.percona.com/blog/2018/10/02/mysql-performance-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/stored-procedures.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/views.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

## Setup

To run the scripts, ensure you have MySQL installed on your Ubuntu 18.04 LTS system. You can use a container-on-demand to run MySQL. Connect via SSH or use the WebTerminal provided.

1. Start MySQL service:
   ```
   $ service mysql start
   ```

2. Import a SQL dump:
   ```
   $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
   $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
   ```

3. Execute SQL scripts:
   ```
   $ cat
