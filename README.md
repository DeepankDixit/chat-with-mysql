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

