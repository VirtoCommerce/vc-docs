# Architecture

The simplified and accelerated Frontend Application architecture is as follows: 

![Architecture](media/frontend-application-architecture.png)

It includes: 

* Client.
* Browser.
* Load balancer.
* Static Content Storage (Virto Commerce Frontend or any SPA application).
* Virto Commerce Platform (xAPI/GraphQL).
* CDN (optional, placed before the load balancer).
* Prerender.IO (optional for Server-Side Rendering).

The workflow ensures a seamless and efficient operation of the Virto Commerce Frontend Application:

1. **Client Request**:
    - The client opens the frontend application in their browser.
    - The browser sends a request to the load balancer to retrieve the **index.html** file.

1. **Load Balancer Routing**:
    - The load balancer is configured with specific routing rules to handle different types of requests efficiently:
        - **API Requests**: If the path matches an XAPI request or a token retrieval request, the load balancer routes the request to the Virto Commerce Platform API.
        - **Static Content Requests**: If the request is for a file, the load balancer serves the static content directly. If the file is not found, a 404 error is returned.
        - **Folder Requests**: If the request is for a folder, the load balancer serves the **index.html** file with a 200 response.

1. **Single Page Application (SPA) Loading**:
    - The Single Page Application (SPA) loads in the client’s browser.
    - The SPA handles both static and dynamic routing within the application.

1. **API Interaction and Content Rendering**:
    - The SPA makes API requests to fetch necessary data.
    - The page content is rendered based on the data received from the API.

1. **User Interaction**:
    - Further interactions occur within the SPA context.

1. **Enhanced Functionalities (Optional)**:
    - Additional functionalities can be configured through the IT infrastructure to enhance performance and security:
        - **CDN Integration**: Integrate with a Content Delivery Network (CDN) to serve static content faster and reduce server load.
        - **Firewall and DDoS Protection**: Implement firewall rules and Distributed Denial of Service (DDoS) protection to secure the application.
        - **Server-Side Rendering (SSR)**: Configure SSR to improve SEO and initial load times by rendering pages on the server before sending them to the client.
