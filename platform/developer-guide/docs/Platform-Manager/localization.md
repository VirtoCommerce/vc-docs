# Localization

This article explains how localization works in Virto Commerce and how you can extend it. It covers:

* [Configuring countries and regions used by the Platform.](#configure-countries-and-regions)
* [Localizing country and region names in the Platform UI.](#localize-country-and-region-name)
* [Adding or updating module translations through JSON-based localization files stored in GitHub.](#localize-modules)


## Configure countries and regions

Virto Commerce provides countries and regions as configurable lists. The data is stored in **json** files in the Platform app. You can configure the location of these files by modifying the following settings:

| Node                   | Default or sample value              | Description                                                                                                                           |
| ---------------------- | ---------------------------------    | ------------------------------------------------------------------------------------------------------------------------------------- |
| VirtoCommerce:CountriesFilePath | `"localization/common/countries.json"` | Local path for countries list. By default, includes all countries worldwide.                                                         |
| VirtoCommerce:CountryRegionsFilePath | `"localization/common/countriesRegions.json"` | Local path for countries' regions list. By default, includes the states of the USA and regions of Canada.                         |

![Readmore](media/readmore.png){: width="25"} [Configuration settings](../Configuration-Reference/appsettingsjson.md)

### Countries list

Update the **countries.json** file as needed to customize the countries list. Retain only the countries maintained by your Platform instance and remove all others. For example:

```json title="countries.json"
[
    { "id": "CAN", "name": "Canada" },
    { "id": "USA", "name": "United States of America" }
]
```

![Readmore](media/readmore.png){: width="25"} [Current countries.json file](https://github.com/VirtoCommerce/vc-platform/blob/master/src/VirtoCommerce.Platform.Web/localization/common/countries.json)

### Regions list

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


## Localize country and region name

Virto Platform Manager supports localization resources for text, captions, tips, etc. This includes country and region names. This is achieved by adding translations to the localization file(s):

1. Copy the translations from an existing language file, such as the [German translation file](https://github.com/VirtoCommerce/vc-platform/blob/master/src/VirtoCommerce.Platform.Web/wwwroot/Localizations/de.VirtoCommerce.Countries.json).

1. Define localization keys:

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

## Localize modules

In addition to core Platform localization, Virto Commerce supports localization at the module level. Each module stores its localization files in its GitHub repository (**src** --> **web** --> **Localizations**). By contributing new or updated translations, you can extend the Platform to support additional languages. Each Virto Commerce module contains JSON files, one per language. For example, **en.json** for English, **de.json** for German, etc. The Platform loads these files automatically after they are merged into the module repository.

### Prepare localization file

To add a new language to a module:

1. Open the **English** localization file (**en.json**) for the module you want to localize.
1. Use an AI tool (such as ChatGPT or Grok) to translate it. The simplest prompt is **“Localize this JSON into ...”**.
1. Review and adjust the translation for accuracy and terminology consistency.
1. Save the translated file as **<language_code>.json**, for example: **sv.json**.

### Contribute 

To contribute your translation back to Virto Commerce:

1. **Fork the repository** of the module you are localizing.
1. **Create a feature branch**.
1. **Add your new JSON file** to the localization folder.
1. **Add or update tests** related to localization or affected UI components.
1. **Run all tests** to ensure the module builds successfully.
1. **Commit and push** your changes.
1. **Submit a pull request** to the main repository.


Once the PR is merged the new localization file becomes part of the module. The new language will appear as an available localization option inside the Platform UI.


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../ui-scroll-directive">← UI scroll directive</a>
    <a href="../extensibility-points/extending-main-menu">Extensibility points →</a>
</div>