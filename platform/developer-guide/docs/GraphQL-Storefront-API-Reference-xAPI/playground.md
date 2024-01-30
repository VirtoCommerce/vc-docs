# Playground

1. To access the interactive [graphql-playground](https://github.com/prisma-labs/graphql-playground) environment:

    1. Open the platform manager application.
    1. Navigate to `ui/playground` within the application.

    You can also access it directly at:

    ```
    http://localhost:10645/ui/playground
    ```

    Once in the GraphQL playground, you can send GraphQL queries or mutations. The interface is as follows:

    ![Playground fields](media/playground-fields.png)

1. Compose your GraphQL query or mutation in the left panel. Fields are autocompleted based on the schema.
1. If necessary, specify variables in the **QUERY VARIABLES** tab. 

    !!! info
        Some variables can be obtained from other queries. For exmplae, you can retrieve the user ID by executing the `createUser` mutation, and to obtain the cart ID, you can use the `cart` query.


1. To provide a token:
    1. Open the **HTTP HEADERS** tab. 

        ![http headers](media/playground.png)

    1. Paste the token as follows:

    ```json linenums="1"
    {
      "authorization": "Bearer your-bearer-token"
    }
    ```

    ??? Example "View sample"
        ```json
        {
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkM5QjVEMTJENjNDREI5Qzg5RTk1NEVCNTcyRjdERkFBQTNFRjgyNEMiLCJ4NXQiOiJ5YlhSTFdQTnVjaWVsVTYxY3ZmZnFxUHZna3ciLCJ0eXAiOiJhdCtqd3QifQ.eyJuYW1lIjoiMWViMmZhOGFjNjU3NDU0MWFmZGI1MjU4MzNkYWRiNDYiLCJzdWIiOiJhZG1pbiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2VtYWlsYWRkcmVzcyI6ImFkbWluQHZjLWRlbW9zdG9yZS5jb20iLCJyb2xlIjoiX19hZG1pbmlzdHJhdG9yIiwibWVtYmVySWQiOiIiLCJvaV9hdV9pZCI6ImE3M2FkMzU3LTZlMTMtNDIxOS1hMzJmLTBhOWJiNjM4NmEyZSIsIm9pX3Rrbl9pZCI6ImE1YjA4ODQ5LWI1Y2MtNDAyZi04YTJmLTNjZDljYTQyMmJjNiIsImF1ZCI6InJlc291cmNlX3NlcnZlciIsInNjb3BlJbzSZkNLe_3pHA2zf_nPQBCwbum_wYPTbOEHNap-A"
        }
        ```

1. Execute your query or mutation by clicking the **Play** button.
