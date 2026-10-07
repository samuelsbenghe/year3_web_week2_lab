# Week 2 lab

by edith-samuel | 33843357

## Lab worksheet

All instructions of the worksheet were carried out, with screenshots as proof attached in the same repository.

## Wrap up questions

#### Why does typing a URL into a web browser address bar only trigger HTTP GET requests and not POST or DELETE?

Answer: By default when a browser is told to navigate to a URL, it sends a GET request to request a body to render.

#### What three components define a web origin, and how does the browser determine if two URLs share the same origin?

Answer: [protocol]://[hostname]:[port]. A browser will check if the protocol,hostname and port parts of the URL are identical. if they are, they share the same origin. Also browsers do not explicitly add the port to the url as it is infered from the protocol. "https" tells the browser to look on port 443. "http" tells the browser to look on port 80

#### What is the difference between a query parameter (/items?limit=5) and a path parameter (/items/5)?

Answer: a path parameter is used to identify a resource in the URL. while a query parameter contains additional information that can be processed by the resource from the path parameter.

#### When testing with items_db, what happens to your added items if Uvicorn restarts or reloads?

Answer: Since item_db is an in-memory variable, any changes will be discarded when the app is reopened.
