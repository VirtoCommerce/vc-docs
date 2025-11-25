# Integration with Authorize.net

Authorize.Net payment module provides integration with Authorize.Net using [Accept.js](https://developer.authorize.net/api/reference/features/acceptjs.html) and the [Authorize.Net API](http://developer.authorize.net/api).

[![Source code](media/source_code.png)](https://github.com/VirtoCommerce/vc-module-authorize-net)

[![Latest release](media/latest_release.png)](https://github.com/VirtoCommerce/vc-module-authorize-net/releases)

## Configure Authorize.net

Confidential Authorize.Net account settings should be configured in the **appsetting.json** file as follows:

{%
   include-markdown "../../Configuration-Reference/appsettingsjson.md"
   start="<!--authorize-net-start-->"
   end="<!--authorize-net-end-->"
%}

![Readmore](media/readmore.png){: width="25"} [Configuring non-confidential settings](/platform/user-guide/latest/authorize-net/manage-authorize-net-module#configure-settings)


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../simplified-integration">← Simplified integration via CSV files </a>
    <a href="../skyflow">Skyflow →</a>
</div>
