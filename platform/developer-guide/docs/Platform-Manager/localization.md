# Localization

In this article, we'll explore how to configure countries and regions within Virto Commerce. These configurations are vital for tailoring the platform to specific geographic regions and localizations. We will explore how to customize the countries list, update regions, and manage localization for both country and region names.

## Configuration

Virto Commerce provides countries and regions as configurable lists. The data is stored in **json** files in the Platform app. You can configure the location of these files by modifying the following settings:

| Node                   | Default or Sample Value              | Description                                                                                                                           |
| ---------------------- | ---------------------------------    | ------------------------------------------------------------------------------------------------------------------------------------- |
| VirtoCommerce:CountriesFilePath | `"localization/common/countries.json"` | Local path for countries list. By default, includes all countries worldwide.                                                         |
| VirtoCommerce:CountryRegionsFilePath | `"localization/common/countriesRegions.json"` | Local path for countries' regions list. By default, includes the states of the USA and regions of Canada.                         |

![Readmore](media/readmore.png){: width="25"} [Configuration settings](../Configuration-Reference/appsettingsjson.md)

### Countries List

Update the **countries.json** file as needed to customize the countries list. Retain only the countries maintained by your Platform instance and remove all others. For example:

```json title="countries.json"
[
    { "id": "CAN", "name": "Canada" },
    { "id": "USA", "name": "United States of America" }
]
```

![Readmore](media/readmore.png){: width="25"} [Current countries.json file](https://github.com/VirtoCommerce/vc-platform/blob/master/src/VirtoCommerce.Platform.Web/localization/common/countries.json)

### Regions List

Update the **countriesRegions.json** file to add regions for the maintained countries if they're missing. For example:

```json title="countriesRegions.json"
[{
     "id": "<<country code>>",
     "regions": [
        {"name": "<<Region name 1>>", "id": "<<region code 1>>" },
        {"name": "<<Region name 2>>", "id": "<<region code 2>>" },
        ...
    ]
}]
```

![Readmore](media/readmore.png){: width="25"} [Current countriesRegions.json file](https://github.com/VirtoCommerce/vc-platform/blob/master/src/VirtoCommerce.Platform.Web/localization/common/countriesRegions.json)


## Localization

Virto Platform Manager supports localization resources for text, captions, tips, etc. This includes country and region names. This is achieved by adding translations to the localization file(s):

1. Copy the translations from an existing language file, such as the [German translation file](https://github.com/VirtoCommerce/vc-platform/blob/master/src/VirtoCommerce.Platform.Web/wwwroot/Localizations/de.VirtoCommerce.Countries.json).

1. Define Localization Keys:

   * For country names, use the key format: `"platform.countries." + <country code>`.
   * For region names, use the key format: `"platform." + <country code> + <region code>`.


Below is a snippet from the German translation file demonstrating the structure:

```json
{
    "platform": {
        "countries": {
            "AFG": "Afghanistan",
            "EGY": "Ägypten",
            ...
        },
        "CAN": {
            ...
            "NL": "Neufundland und Labrador",
            "NT": "Nordwest-Territorien",
            ...
        }
    }
}
```