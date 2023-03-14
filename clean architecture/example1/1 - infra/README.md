This is the infrastructure layer. Here are things that are necessary in order to get your application to interact
with external systems. This is the the layer where there are implementation details of for example, specific databases and technologies, things that the rest of the system won't do, as a clean
architectured system. So, for example, if we want to swap the database being used from a relational db to a NoSQL,
we could easily do so, without having to change details regarding the database implementation and usage throughout our application. 