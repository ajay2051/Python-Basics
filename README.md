# Namespacing in Python

A namespace is a collection of currently defined symbolic names along with information about the object. In a python program there are four 
types of namespaces:
(i) Built-in (ii) Global (iii) Enclosing (iv) Local

# Python Data Types

Text Type: str
Numeric Type: int, float, complex
Sequence Type: list, tuple, range
Mapping Type: dict
Set Type: set, frozenset
Boolean Type: bool
Binary Type: bytes,
None Type: NoneType

# Identifier

Python identifier is the name we give to identify a variable, function, class, module or other object.

# Mangling

Mangling doesn't apply to strings only to identifier. Class Variable is accessed by adding Class Name to identifier.

# Iterator and Iteration

Iterator: An iterator is an object that represents a stream of data which provides a mechanism for iterating. Iterators are implemented using the 
iterator protocol, which requires the iterator object to have a **iter**() method that returns itself and a **next**() method that returns the 
next element in the sequence or raises a StopIteration exception if there are no more elements.

Iteration: Iteration is the process of looping or repeating a sequence of operations. In Python, iteration typically involves repeatedly calling 
the **next**() method on an iterator object to retrieve the next element in the sequence. This process continues until the iterator is exhausted, 
at which point it raises a StopIteration exception.

# Class Attributes

Class attributes are the attributes that belong to the class itself rather than to a particular object also can be called as class variables.

# Class Methods

Class Methods are the methods that have access to the class attributes, but they can’t access specific instance attributes. In other words, 
these methods are used to handle and process class attributes. However, they are not used on the object level, they are used on the class level.

Instance methods take the argument cls and can therefore access all class variables and methods, but no instance variables/methods.

Use this when you don't need to access variables that belong to an instance, but still need general attributes that belong to the class.

# Static Method

Static methods can neither access class variables/methods nor instance variables/methods. They behave like plain (global) functions except that 
you can call them from an instance or the class.

# WhiteNoise

Radically simplified static file serving for Python web apps

With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be 
deployed anywhere without relying on nginx, Amazon S3 or any other external service. (Especially useful on Heroku, OpenShift and other PaaS 
providers.)

# Types of Python Function

Python Built-in Functions Example len(), print(), min(), max()
Recursive Function
Lambda Function
User-defined Function

# Objects

The object is an entity that has a state and behaviour with it.

An object consists of:
State: It is represented by attributes of an object. It also reflects the properties of an object.
Behaviour: It is represented by methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.

# Improve The Performance of Web

(1) JavaScript minification and module bundling.
(2) On-demand loading of assets.
(3) Use array-ids when using DOM manipulation libraries.
(4) Cache
(5) Enable HTTP/2
(6) Use a Load Balancing Solution
(7) Speed up database queries with indexing.
(8) Avoid or minimize the use of render blocking JS and CSS.
(9) Update Image Encoding Optimizations.
(10) Reduce the number of HTTP requests.
(11) Use Content Delivery Network(CDN).
(12) Load JavaScript Asynchronously.
(13) Reduce number of plugins.

# Memory Management in Python

a = 10

Stack [a]
Private Heap [10]

Python is dynamically typed programming language because we don't have to declare the data type.
All Python objects are stored in private heap.

# Difference Between if A: and if A is not None:

if A checks the value anything except False, [], None, "", and 0.
if A is not None checks if A is a different object than None.

# 4 Pillars of OOP

Abstraction:
Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of 
the function, but inner working is hidden. User is familiar with that "what function does" but they don't know "how it does."

from abc import ABC, abstractmethod
class Absclass(ABC):
def print(self,x):
print("Passed value: ", x)
@abstractmethod
def task(self):
print("We are inside Absclass task")

Encapsulation:
Encapsulation puts restriction on accessing variables and methods directly and can prevent the accidental modification of data. 
In python, just follow the convention by prefexing the name of the member by single underscore"\_".

class Person:
def **init**(self, name, age):
self.\_name = name
self.\_age = age

# Global Interpreter Lock

GIL is a lock that allows only one thread to hold the control of the Python Interpreter. This means only one thread can be in a state of 
execution at any point in time.

# Garbage Collection

Python deletes unwanted objects(built-in types or class instances) automatically to free memory space. The process by which Python periodically 
frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.
_**Mark and Sweep Algorithm**_ is used for Garbage Collection. 

# self

The word self is used to represent the instance of a class. By using the "self" keyword use access the attributes and methods of the class in Python.

# **init** method

"**init**" is a reserved method in Python Class. It is called as constructor & this method is called when an object is created from class 
and it allows the class to initialize the attribute of the class.

# **repr** method

"**repr**" method is a special method used to define how an object should be represented as a string.

# SOLID Principle

S- SINGLE RESPONSIBILITY
O- OPEN/CLOSED
L- LISKOV SUBSTITUTION
I- INTERFACE SEGREGATION
D- DEPENDENCY INVERSION

Single Responsibility Principle (SRP): A class should have only one responsibility. This means that each class should only do one thing, 
and do it well.

Open-Closed Principle (OCP): A class should be open for extension, but closed for modification. This means that you should be able to add new 
features to a class without having to change the existing code.

Liskov Substitution Principle (LSP): This principle states that any subtype must be substitutable for its base type. In other words, 
if you have a class Base and a subclass Derived, then you should be able to use an instance of Derived anywhere that you would normally 
use an instance of Base.

Interface Segregation Principle (ISP): This principle states that no client should be forced to depend on methods it does not use. This means 
that you should create small, focused interfaces that only expose the methods that are needed by the clients.

Dependency Inversion Principle (DIP): This principle states that high-level modules should not depend on low-level modules. Instead, both 
high-level and low-level modules should depend on abstractions.

# Shallow Copying:

Shallow copying creates a new object, but it only copies references to the objects within the original object. It does not create new copies of 
the nested objects. The top-level object is duplicated, but the nested objects are not. Instead, references to the same nested objects are 
retained in both the original and copied objects.

# Deep Copying:

Deep copying, on the other hand, creates a completely independent copy of the original object and all its nested objects. It recursively copies 
all objects contained within the original object. The result is that the copied object is entirely distinct from the original, with no shared 
references to nested objects.

# Difference ways of accessing key in dictionary
details = {
    "name": "Ajay",
    "age":25,
    "address": "Ktm"
}
print(details['name'])
print(details.get("name"))

what is the difference between two print statements

The two print statements in your code will produce the same result, but there is a subtle difference in how they handle cases where the specified 
key is not present in the details dictionary.

print(details['name']): This statement directly accesses the value associated with the key 'name' in the 'details' dictionary. If the key is 
present, it will print the corresponding value. However, if the key is not found in the dictionary, it will raise a KeyError. So, it assumes that 
the key is always present, and if it's not, it may lead to an error.

print(details.get("name")): This statement uses the get method to retrieve the value associated with the key 'name'. If the key is present, 
it will print the corresponding value. If the key is not found, it will return None by default (if no default value is specified). 
So, this approach is safer, especially when you are not certain whether the key exists in the dictionary or not. It avoids raising a KeyError and 
allows you to provide a default value as a second argument to get if desired.

In summary, the first statement assumes the key is present and may raise a KeyError if it's not, while the second statement uses get and 
returns None if the key is not found, avoiding a KeyError.


# How to Sign and Validate JSON Web Tokens – JWT Tutorial

Ans: https://www.freecodecamp.org/news/how-to-sign-and-validate-json-web-tokens/

# Order of passing parameters in Python Function

    - Positional Arguments
    - Keyword Arguments
    - Default Arguments
    - *args
    - **kwargs

# How Python code execution works?
Python is interpreted language. Python compiler like CPython internally compiles code into bytecode.
.py -> .pyc
Compiled code is send to PVM(Python virtual machine) which executes compiled bytecode in machine executable.

# Git Rebase: 
Rebasing is the process of moving or combining a sequence of **commits** to a new base commit.

# Git Fetch
The git fetch command downloads commits, files, and refs from a remote repository into your local repo, 
but it doesn't integrate any of this new data into your working files. 


# Concurrency vs Parallelism
Concurrency:
- Multiple tasks can be executed in an overlapping time period. 
- Tasks may start before preceding ones complete, without simultaneous running.
- CPU adjusts time slices per task and switches contexts.
Concurrency aims to maximize CPU usage by minimizing its idle time.

Parallelism:
- Parallelism is the ability to execute independent tasks of a program in the same instant of time. 
- These tasks can run simultaneously on another processor core, another processor, or an entirely different computer that can be a distributed 
system. 

https://media.licdn.com/dms/image/D5622AQGndnnKRTLZqg/feedshare-shrink_800/0/1712866639525?e=1717027200&v=beta&t=UB18T0Jyh9lODAtVFXTY6ZJt32EUCHLm6TwKAQBacUY

# Forward Proxy vs Reverse Proxy

Forward Proxy:

Introduction
    A client proxy, also known as a forward proxy or simply a proxy, is a server that acts on behalf of client devices 
    (e.g., computers, smartphones) to make requests to destination servers (e.g., web servers, external services).
    It sits between client devices and the internet, forwarding client requests to destination servers.

Use cases:
    Enhancing privacy
    Access control and content filtering
    Monitor web activity
    Log client's requests/response

Tools:
    Squid
    Privoxy
    VPN services

Reverse Proxy:

Introduction
    A server proxy, also known as a reverse proxy, is a server that sits between internet and destination servers 
    (e.g., web servers, external services) to handle incoming requests on behalf of those destination servers.
    It forwards client requests to the appropriate destination server based on predefined routing rules.

Use cases:
    Load Balancing
    Web Application Firewall (WAF)
    Protection from DDoS attacks
    Cache frequently accessed data
    SSL encryption/decryption

Tools:
    Nginx
    Apache HTTP Server (when configured as a reverse proxy)
    HAProxy
    CDN (Content Delivery Network) services

https://media.licdn.com/dms/image/D4D12AQH_7-KhLM7Sog/article-cover_image-shrink_720_1280/0/1693579146959?e=1719446400&v=beta&t=6JFTV_VGFmkAHRdfJdSYew3NLKoHDjwYbPlDGgqyKtE

A reverse proxy accepts a request from a client, forwards it to a server that can fulfill it, and returns the server’s response to the client.
A load balancer distributes incoming client requests among a group of servers, in each case returning the response from the selected server to 
the appropriate client.

Load balancers are most commonly deployed when a site needs multiple servers because the volume of requests is too much for a single server to 
handle efficiently. Deploying multiple servers also eliminates a single point of failure, making the website more reliable. Most commonly, 
the servers all host the same content, and the load balancer’s job is to distribute the workload in a way that makes the best use of each server’s 
capacity, prevents overload on any server, and results in the fastest possible response to the client.

# Database Normalization

Database normalization is a database design principle for organizing data in an organized and consistent way.

It helps you avoid redundancy and maintain the integrity of the database. It also helps you eliminate undesirable characteristics associated with 
insertion, deletion, and updating.

The main purpose of database normalization is to avoid complexities, eliminate duplicates, and organize data in a consistent way. In normalization, 
the data is divided into several tables linked together with relationships.

Database administrators are able to achieve these relationships by using primary keys, foreign keys, and composite keys.

The First Normal Form – 1NF

For a table to be in the first normal form, it must meet the following criteria:

- A single cell must not hold more than one value (atomicity)
- There must be a primary key for identification
- No duplicated rows or columns
- Each column must have only one value for each row in the table

The Second Normal Form – 2NF

- The 1NF only eliminates repeating groups, not redundancy. That’s why there is 2NF.
- A table is said to be in 2NF if it meets the following criteria:
- It’s already in 1NF
has no partial dependency. That is, all non-key attributes are fully dependent on a primary key.

The Third Normal Form – 3NF

- When a table is in 2NF, it eliminates repeating groups and redundancy, but it does not eliminate transitive partial dependency.

- This means a non-prime attribute (an attribute that is not part of the candidate’s key) is dependent on another non-prime attribute. 
- This is what the third normal form (3NF) eliminates.

- So, for a table to be in 3NF, it must:
be in 2NF
have no transitive partial dependency.

https://www.freecodecamp.org/news/database-normalization-1nf-2nf-3nf-table-examples/

# Why is redis so fast?
https://blog.bytebytego.com/p/why-is-redis-so-fast

# Stored Procedure
https://www.cherryservers.com/blog/create-postgresql-stored-procedure#:~:text=Postgres%20stored%20procedures%20are%20routines,execute%20on%20the%20database%20itself.
https://www.postgresqltutorial.com/postgresql-plpgsql/postgresql-create-procedure/

# Multithreading vs Multiprocessing
https://towardsdatascience.com/multithreading-vs-multiprocessing-in-python-3afeb73e105f

# How to make API secure
https://www.practical-devsecops.com/what-is-rest-api-security/
