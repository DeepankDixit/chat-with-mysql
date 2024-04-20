# chat-with-mysql

## App Architecture

**Most important bit:**

We will not be using an Agent for this app. We are just using a Chain. In real-life you would be using an Agent for this task as that would be more sophisticated. But we will be working with SQL chains to see how well can they do for chatting with SQL task.

Let's go over the basic ways to create a Q&A chain and agent over a SQL database. These systems allow us to ask a question about the data in a SQL database and get back a natural language answer. The main difference between the two is that our agent can query the database in a loop as many time as it needs to answer the question.

At a high-level, the steps of any SQL chain and agent are:

1. Convert question to SQL query: Model converts user input to a SQL query.
2. Execute SQL query: Execute the SQL query.
3. Answer the question: Model responds to user input using the query results.

<img width="1346" alt="image" src="https://github.com/DeepankDixit/chat-with-mysql/assets/22991058/5d8c4185-5da8-42ec-bee5-27b07026a504">
[Reference](https://python.langchain.com/docs/use_cases/sql/quickstart/)


## What is a Chain?

![image.png](attachment:image.png)
[Reference](https://alejandro-ao.com/chat-with-mysql-using-python-and-langchain/)

- A simple SQL chain takes a question, turns it into a SQL query, executes the query, and uses the result to answer the original question.
- The first step in a SQL chain or agent (we are only using SQL chain here, not agent) is to take the user input and convert it to a SQL query. 
- LangChain comes with a built-in chain for this: **create_sql_query_chain**, but we will implement it ourselves.


## What is RunnablePassthrough?
 
```
chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
            schema=lambda _: db.get_table_info(),
            response=lambda vars: db.run(vars["query"]),
        )
        | prompt
        | llm  
        | StrOutputParser()
    )
```

- first runnable: We passed in the sql_chain that returns the sql query 
- This runnable is going to return some vars as an output. i.e. in variable vars.
- We can use those vars in other lambda methods : schema and response
- For example: we can tweak the chain to print these returned variables in vars:

```
chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
            schema=lambda _: db.get_table_info(),
            response=lambda vars: print("variables: ", vars),
        )
        | prompt
        | llm  
        | StrOutputParser()
    )
```

### It changes the app behavior in the following way -

![image.png](attachment:image.png)

- And in the terminal we see the variables printed as per the print statement:

variables:  {'question': 'How many artists are there>', 'chat_history': [AIMessage(content='Hello! I am your SQL assistant. Ask me anything about your database.'), HumanMessage(content='How many artists are there>')], 'query': 'SELECT COUNT(*) AS NumberOfArtists FROM Artist;'}


#### Note
- Tried with "mixtral-8x7b-32768" from groq but it didn't seem to be able to prepare SQL queries as well as the GPT3.5 did.
- The app has the LLM streaming capability: meaning that it shows the output being generated in real time, rather than having to wait until the whole response is generated. [*Reference*](https://alejandro-ao.com/how-to-use-streaming-in-langchain-and-streamlit/)

## Setting up the MySQL

I am using Chinook Database for MySQL for this demo: [Chinook_MySql.sql](https://github.com/lerocha/chinook-database/releases/download/v1.4.5/Chinook_MySql.sql)

1. Download the Chinook database or any database you want to chat to
2. Set up the MySQL database in your local environment so that we can chat with it
    1. **Installing MySQL** (instrustions available online):

    If you are on Mac:   
     
    to install MySQL -    *brew install mysql*

    to start the MySQL service -  *brew services start mysql*
    
    to check the status of the MySQL service -    *brew services list*

3. Log into the mysql using `mysql -u root -p`
4. Create a database using the following command:
    ```
    CREATE DATABASE chinook;
    USE chinook;
    SOURCE chinook.sql; --or the name of your SQL file to load the database
    ```
5. test the database by running ```SELECT * FROM albums LIMIT 10;```

## App walkthrough

1. Enter the db credentials and click on Connect 

![image.png](attachment:image.png)

2. ![image-2.png](attachment:image-2.png)
