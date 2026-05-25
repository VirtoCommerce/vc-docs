
Virto commerce supports simple authentication based on sending an API key across all requests to authenticate a user.

One of the clear advantages of using API key authentication is its inherent simplicity. It is a single key that allows you to authenticate just by including it. This simplicity also enables the user to make calls easily, with cURL, interactive docs, or even in their browser.

## Create API key

To create a new API key:

1. Open Platform and click **Security** in the main menu. 
1. In the next blade, click **Users**.
1. In the next blade, select the desired user. 
1. In the next blade, click on the **Api key** widget. 
1. Click **Generate** in the toolbar. The Api key appears in the corresponding field:

	![API Key widget](media/api-key-widget.png)
1. Click **OK** to save the changes.

!!! note
	Each API key must be associated with a user account, as all requests with an API key will be authorized on behalf of the user that API key is associated with.

## Use API Key

You can include the API key into a REST API call as a query parameter with the following format (replace **API_KEY** with the key string of your API key):

```
GET https://{platform_host}/api/some_resource?api_key=API_KEY
```

Alternatively, you can use the `api_key` header to provide your key:

```
GET http://{platform_host}/api/some_resource 
api_key: API_KEY
```


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../access-token-and-cookie-mixed-auth">← Access token and cookie mixed authentication </a>
    <a href="../oidc">OpenID connect →</a>
</div>
