#!/usr/bin/python3
""" This is backend engine for the MySQL database """


from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from sqlalchemy import create_engine
from os import getenv


class_name = {
        'BaseMode': BaseModel,
        'City': City,
        'State': State,
        #'User': User,
        #'Place': Place,
        #'Amenity': Amenity,
        #'Review': Review
        }


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session to fetch all objects
        depending on the class name, otherwise, we fetch all the objects
        irespecitve of the class name """

        # This function returns dict, therefor, we need to create empy dict
        objects = {}

        if cls:
            # meaning if we want objecs that belongs to specific class name
            for obj in self.__session.query(cls).all():
                key = '{}.{}'.format(type(obj), obj.id)
                objects[key] = obj

        else:
            for cls in class_names:
                for obj in self.__session.query(cls).all():
                    key = '{}.{}'.format(type(obj), obj.id)
                    objects[key] = obj

        return objects

    """ more pythonic way 
    def all(self, cls=None):
    # Query to fetch all objects related to cls if cls is not None. Otherwise, fetch all.
    query = self.__session.query(cls) if cls else self.__session.query(*DBStorage.__classNames)

    # Return the dictionary representation using dictionary comprehension
    return {f"{type(obj).__name__}.{obj.id}": obj for obj in query}
    """

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        from sqlalchemy.orm import sessionmaker, scoped_session

        Base.metadata.create_all(self.__engine)

        # create a new database session
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

        """ why 'scoped_session' is required in this context ?
        In SQLAlchemy, scoped_session is a utility function that creates
        a thread-local scope for a session. It provides a way to manage
        sessions within a web application or multi-threaded environment,
        ensuring that each thread has its own unique session instance.

        The scoped_session function takes a session factory as an argument
        and returns a new session object. This new session is associated with
        the current thread and can be accessed using the same syntax as a
        regular session.

        The main advantage of using scoped_session is that it simplifies
        the management of sessions in multi-threaded scenarios. Each thread
        can access its own unique session without interfering with other
        threads. It provides a thread-local scope, meaning that sessions are
        stored in a thread-local variable, ensuring that each thread operates
        with its own isolated session.

        By using scoped_session, you can avoid issues related to thread-safety
        and ensure that each thread has its own dedicated session for performing
        database operations.
        """

        """ What is thread then? 
        In computer programming, a thread is the smallest unit of execution
        within a process. A thread is a sequence of instructions that can be
        executed independently and concurrently with other threads within
        the same process.

        Threads are lightweight compared to processes because they share
        the same memory space and resources of the parent process. Multiple
        threads within a process can execute concurrently, allowing for parallel
        execution and efficient utilization of system resources.

        Threads are commonly used in concurrent programming to achieve
        multitasking and improve application performance. By dividing
        the program into multiple threads, different parts of the program can
        execute simultaneously, making it possible to perform multiple 
        tasks concurrently.

        Threads can communicate and share data with each other through shared
        memory or message passing mechanisms. However, since threads operate
        in the same memory space, they need to synchronize access to shared
        resources to avoid conflicts and ensure data integrity.

        In summary, a thread is an independent sequence of instructions that
        can execute concurrently with other threads within a process, allowing
        for multitasking and parallel execution.

        In the context of web services, threads can be used to handle multiple
        concurrent requests and improve the scalability and responsiveness of
        the service. Here are a few points to consider regarding threads in web services:

            Concurrent request handling: When a web service receives multiple 
            requests simultaneously, each request can be assigned to a separate
            thread for processing. This allows the service to handle multiple
            requests concurrently, ensuring that one request does not block others
            from being processed.

            Improved responsiveness: By using threads, a web service can respond
            to requests more quickly. While one thread is performing a time-consuming
            operation, such as accessing a database or making an external API call,
            other threads can continue processing other requests.
            This helps to prevent delays and ensures that the service remains
            responsive to incoming requests.

            Scalability: Threads enable a web service to scale horizontally by
            handling multiple requests concurrently. As the load on the service
            increases, more threads can be created to handle additional requests,
            allowing the service to accommodate more clients and distribute the
            workload across multiple threads.
        """

        """ why 'bind' is required is sessionmaker?
        When you create a session using sessionmaker, you can pass the bind
        argument to associate the session with a specific engine. This allows
        the session to use the engine for database operations such as querying,
        inserting, updating, and deleting data.

        By binding a session to an engine, you ensure that all database
        operations performed through that session are executed on the specified
        database connection. This helps maintain consistency and allows multiple
        sessions to work with different database connections concurrently.
        """
                

