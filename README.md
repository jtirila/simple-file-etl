# Simple file ETL

## Introduction

This project will be an attempt to write a simple generic tool for tasks with the following requirements, or a subset of them
depending on the final scope:
 * Read at least json and csv data and validate, filter and transform some fields using Python
 * Restructure the object relations to reflect some internal application logic not present in the original records
 * Save the newly created objects into a database so that all the necessary foreign key references etc. are created
   correctly
 * The relations, validations, db structure etc. are all presented in some nice declarative way so as to make the tool
   easy to use for completely new situations

The project is inspired by a real world application, with the intention of making some code way more generic.
Whether I have the time to proceed with the project, and whether it succeeds to any reasonable degree, is not certain
at all. We will see.

Most likely at least the initial scope will be more of a PoC than anything useful for real applications.

## Some notes

This is mere speculation at this point. Anyway.

 * Some technology choices: Python, SQLAlchemy
 * Supported input formats: CSV, JSON
 * Supported databases: I suppose anything SQLAlchemy supports. I'll be using PostgreSQL in the beginning.


## Workflow

Early pieces of code and all kinds of exploration and experimentation will be performed in branches.

## Conclusion

As you can see, it is all very vague at this point. Sorry. Let me know if you have any criticism, comments, questions
or hints concerning this sort of a project.


